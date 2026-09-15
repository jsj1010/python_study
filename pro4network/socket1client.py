# client
from socket import *

clientsock = socket(AF_INET, SOCK_STREAM)
clientsock.connect(('192.168.0.25',8888))
clientsock.send("안녕 서버".encode()) # 문자열을 바이트로 변환하여 서버로 보냄

clientsock.close()

# server 실행 중 - client 실행 - server가 메세지 수신 후 종료