from flask import Flask, render_template, request
import pymysql
import pandas as pd
import numpy as np
from markupsafe import escape
import koreanize_matplotlib
import matplotlib.pyplot as plt

#문자열의 HTML 특수문자를 안전하게 바꾸는 함수,  <, > 등을 &lt;, &gt;로 바꿔서 브라우저가 코드를 실행하지 않고 글자로 표시한다

#직원 번호, 직원명, 부서명, 부서전화, 연봉, 직급 자료 읽어 출력

app = Flask(__name__)

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8mb4'
}  #원래는 env 써야함

def get_connection():
    return pymysql.connect(**config)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dbshow", methods=['GET', 'POST'])
def dbshow():
    #부서명을 입력받아 해당 부서에 근무 직원 출력 
    dept = request.args.get("dept","").strip()
    sql = """
        select j.jikwonno as 사번,j.jikwonname as 직원명,b.busername as 부서명,
        j.jikwonjik as 직급,j.jikwonpay as 연봉, year(now()) - year(j.jikwonibsail) as 근무년수, j.jikwongen as 성별
        from jikwon j inner join buser b on j.busernum=b.buserno 
    """ 
    params = []
    if dept:
        sql += " where b.busername like %s"
        params.append(f"{dept}%")
    sql += "order by j.jikwonno, j.jikwonname"

    # SQL 실행
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            rows = cur.fetchall()
            cols = [c[0] for c in cur.description] #description 칼럼등 여러 정보를 반환

    df = pd.DataFrame(rows, columns=cols)
    # print(df.to_html(index=False))

    #DataFrame을 table tag로 만들기
    if not df.empty:
        jikwondata = df[['사번','직원명', '부서명','직급','연봉','근무년수']].to_html(index=False)
    else:
        jikwondata = "직원 정보가 없어요"

    # 직급별 연봉 통계
    if not df.empty:
        stats_df = (
            df.groupby("직급")["연봉"]
            .agg(합계="sum", 평균="mean")
            .round(2)
            .reset_index()
            .sort_values(by='평균', ascending=False)
    )
        statsdata = stats_df.to_html(index=False)
    else:
        statsdata = "통계 대상 자료가 없어요"
        

    # 성별 직급별 직원 수 교차표 
    if not df.empty:
        crosst = pd.crosstab(
            index=df['성별'], columns=df['직급'], margins=True, margins_name='합계'
        )
        crossdata = crosst.to_html()
    else:
        crossdata = "교차표 대상 자료가 없어요"


    # 부서별 최고 연봉자
    if not df.empty:
        maxpay = df.groupby('부서명')['연봉'].max()      # 최댓값
        top_df = pd.merge(df, maxpay, on=['부서명', '연봉'])        # 부서명과 연봉이 둘 다 같은 직원만 남김 inner join 같은느낌
        topdata = top_df[['부서명', '직원명', '직급', '연봉']].to_html(index=False)
    else:
        topdata = "최고 연봉자 자료가 없어요"



    #부서별 직원 비율 계산 : 전체 인원 대비 각 부서 인원 비율

    if not df.empty:
        total = len(pd.read_sql("select * from jikwon", get_connection())) #전체 가져오기 len(df) 쓰면 비율 이상하게 나옴
        dept_count = df.groupby('부서명')['직원명'].count() #부서별 직원 수
        dept_ratio = (dept_count / total * 100).round(2) #부서별 직원 비율 계산
        ratiodata = dept_ratio.reset_index().to_html(index=False)
    else:
        ratiodata = "비율 대상 자료가 없어요" 
    
    return render_template("dbshow.html", jikwondata=jikwondata, statsdata=statsdata, crossdata=crossdata, topdata=topdata, ratiodata=ratiodata)



if __name__ == '__main__':
    app.run(debug=True)



