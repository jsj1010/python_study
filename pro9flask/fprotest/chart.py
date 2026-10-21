import pymysql
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

config = {
    'host':'127.0.0.1',
    'user':'root',
    'password':'123',
    'database':'test',
    'port':3306,
    'charset':'utf8'
}

try:
    conn = pymysql.connect(**config)
    sql = """
    select busername 부서명, jikwonpay 연봉
    from jikwon inner join buser
    on jikwon.busernum=buser.buserno
    """
    df = pd.read_sql(sql, conn)

    buser_pay = df.groupby('부서명')['연봉'].agg(['sum', 'mean'])
    buser_pay.columns = ['연봉합', '연봉평균']
    print(buser_pay)

    # 세로 막대 그래프 
    buser_pay.plot(kind='bar', rot=0)
    plt.title('부서명별 연봉합, 평균')
    plt.xlabel('부서명')
    plt.ylabel('연봉')
    plt.tight_layout()

    fig = plt.gcf()
    plt.show()
    fig.savefig('static/image/buser_pay.png')

except Exception as e:
    print('처리 오류:', e)
finally:
    conn.close()