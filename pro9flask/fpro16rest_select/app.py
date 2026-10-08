from flask import Flask, request, render_template, redirect, jsonify
from db import get_connFunc

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# 전체 직원 조회
@app.get("/acorn/jikwon")
def jikwon_list():
    sql = """
        SELECT jikwonno, jikwonname, busername, jikwonjik, jikwonpay,
        YEAR(jikwonibsail) AS ibsayear
        FROM jikwon
        INNER JOIN buser ON jikwon.busernum = buser.buserno
        ORDER BY jikwonno
    """

    with get_connFunc() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()

    return jsonify({"ok": True, "data": rows})

# 직원 1명 조회
@app.get("/acorn/jikwon/<int:no>")
def jikwon_one(no):
    sql = """
        SELECT jikwonno, jikwonname, busername, jikwonjik, jikwonpay,
        year(jikwonibsail) AS ibsayear
        FROM jikwon
        INNER JOIN buser ON jikwon.busernum = buser.buserno
        where jikwonno =%s
    """

    with get_connFunc() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (no,))
            row = cur.fetchone()

    return jsonify ({"ok":True, "data":row}) 

# 전체 부서 조회
@app.get("/acorn/buser")
def buser_list():
    sql = """
        SELECT * FROM buser order BY buserno
    """

    with get_connFunc() as conn:
        with conn.cursor() as cur:
            cur.execute(sql)
            rows = cur.fetchall()

    return jsonify ({"ok":True, "data":rows}) 

#  부서별 직원 조회
@app.get("/acorn/buser/<int:no>")
def buser_jikwon_list(bno):
    sql = """
        SELECT jikwonno, jikwonname, jikwonjik, jikwonpay, YEAR(jikwonibsail) AS ibsayear
        FROM jikwon
        WHERE busernum = %s
    """

    with get_connFunc() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (bno,))
            rows = cur.fetchall()

    return jsonify({"ok": True, "data": rows})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000);