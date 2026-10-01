from flask import flask, render_template,request,redirect,url_for, flash
# pip install pymysql
import pymysql
import os
from flask import get_flashed_messages # 저장해둔 메세지를 꺼내는 함수
# 예: flash("에러~~") -> 메세지를 세션에 잠시 저장 후 get

app = flask(__name__);
app.secret_key = "abc1234" # 쿠키서명용 비밀키

#MariaDB 연결 정보
DB_HOST = os.getenv("DB_HOST","127.0.0.1")
DB_PORT = os.getenv("DB_PORT","3306")
DB_USER = os.getenv("DB_USER","ROOT")
DB_PASSWORD = os.getenv("DB_PASSWORD","123")
DB_NAME = os.getenv("DB_NAME","test")

def get_conn():
    return pymysql.connect(
        host = DB_HOST,
        port = DB_PORT,
        user = DB_USER,
        password = DB_PASSWORD,
        database=DB_NAME,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=False
    )
    # DictCursor : select 결과를 'dict type' 형태로 접근가능
    # 예: {'code':1, 'sang':'mouse'...} row['code'], row['sang'] 가능, 원래는 raw[0] 이런식

@app.route("/")
def index():
    pass