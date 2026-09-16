
import sys
sys.stdout.reconfigure(encoding='utf-8')

import MySQLdb
from dotenv import load_dotenv
import os

load_dotenv()

config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'port': int(os.getenv('DB_PORT', 3306)),
    'charset': os.getenv('DB_CHARSET', 'utf8mb4')
}


print("Content-Type: text/html; charset=utf-8")
print()
print("""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>상품 정보</title>
</head>
<body>
<h2>* 상품 정보 *</h2>
""")

conn = None
try:
    conn = MySQLdb.connect(**config)
    cursor = conn.cursor()
    cursor.execute("""
        select code, sang, su, dan from sangdata
    """)

    datas = cursor.fetchall()
    print("<table border='1'>")

    print("<tr><th>코드</th><th>품명</th><th>수량</th><th>단가</th></tr>")
    
    for data in datas:
        print("<tr>")

        print(f"<td>{data[0]}</td>")
        print(f"<td>{data[1]}</td>")
        print(f"<td>{data[2]}</td>")
        print(f"<td>{data[3]}</td>")
        print("</tr>")
        
    print("</table>")
except Exception as e:
    
    print("오류: " + e)
finally:
    if conn:
        conn.close()

print("""
</body>
</html>
""")