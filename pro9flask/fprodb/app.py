# pandas 문제 8)
# MariaDB에 저장된 jikwon, buser 테이블을 이용하여 아래의 문제에 답하시오.
# Django 또는 Flask 모듈을 사용하여 결과를 클라이언트 브라우저로 출력하시오.

#    1) 사번, 직원명, 부서명, 직급, 연봉, 근무년수를 DataFrame에 기억 후 출력하시오. (join)
#        : 부서번호, 직원명 순으로 오름 차순 정렬 

#    2) 부서명, 직급 자료를 이용하여  각각 연봉합, 연봉평균을 구하시오.

#    3) 부서명별 연봉합, 평균을 이용하여 세로막대 그래프를 출력하시오.

#    4) 성별, 직급별 빈도표를 출력하시오.

#    5) 부서별 최고 연봉자 출력 : 부서명별로 가장 연봉이 높은 직원 1명씩 출력 
#        출력 항목: 부서명, 직원명, 연봉
#    6) 부서별 직원 비율 계산 : 전체 인원 대비 각 부서 인원 비율(%) 
#        비율 계산 (%)은 dept_ratio = (dept_count / total * 100).round(2)
#       결과를 DataFrame으로 출력
#       예: 총 인원: 30명
#            영업부 20%
#            총무부 30%
#            전산부 5%
#            ...

from flask import Flask, render_template, request
import pymysql
import pandas as pd
from markupsafe import escape


app = Flask(__name__)

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8mb4'
}

def get_connection():
    return pymysql.connect(**config)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dbshow", methods=['GET', 'POST'])
def dbshow():
    dept = request.args.get("dept", "").strip()

    sql = """
        select j.jikwonno as 직원번호, jikwonname as 직원명, 
        b.busername as 부서명, b.busertel as 부서전화,
        j.jikwonpay as 연봉, j.jikwonjik as 직급
        from jikwon j inner join buser b
        on j.busernum=b.buserno
    """
    params = []
    if dept:
        sql += " where b.busername like %s"
        params.append(f"{dept}%")

    sql += " order by jikwonno asc"


    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, params)
            rows = cur.fetchall()
            cols = [c[0] for c in cur.description] # description: 칼람 등 여러 정보 반환

    df = pd.DataFrame(rows, columns=cols)
    # print(df.to_html(index=False))

    # DataFrame을 table tag로 만들기
    if not df.empty:
        jikwondata = df[['직원번호', '직원명', '부서명', '부서전화', '연봉']].to_html(index=False)
        # jikwondata = df.to_html(index=False)  # 전부 다 보내기
    else: 
        jikwondata = "직원 정보가 없다"

    # print(jikwondata)

    # 직급별 연봉 통계 
    if not df.empty:
        stats_df = (
            df.groupby("직급")["연봉"]
            .agg(평균="mean", 표준편차=lambda x:x.std(ddof=0)) # ddof=0(모표준편차),1(표본표준편차)
            .round(2)
            .reset_index()
            .sort_values(by='평균', ascending=False)
        )
        stats_df['표준편차'] = stats_df['표준편차'].fillna(0)
        # print(stats_df.to_html(index=False))
        statsdata = stats_df.to_html(index=False)
    else:
        statsdata = "통계 대상 자료가 없다"


    if not df.empty:
        crosst = pd.crosstab(
            index=df['부서명'],columns=df['직급'],margins=True,margins_name='합계'
        )
        crossdata =crosst.to_html()
    else:
        crossdata = "교차표 대상자료가 없어요"

    # return render_template("dbshow.html", jikwondata=df.to_html(index=False))
    return render_template("dbshow.html", \
                        jikwondata=jikwondata,
                        statsdata=statsdata,
                        crossdata=crossdata,
                        dept=escape(dept) # xss 방지)
    )


if __name__ == '__main__':
    app.run(debug=True)
