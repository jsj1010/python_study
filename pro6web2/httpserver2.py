# CGIHTTPRequestHandler : simplehttprequesthandler의 확장 클래스
# html,css 같은 정적 파일도 서비스하면서,
#/cgi-bin 아래의 python프로그램 같은 cgi스크립트도 실행 할 수 있게 해주는 클래스,
# get, post 모두 지원 가능
# cgi(common gateway interface)
#    :웹서버와 외부 프로그램 사이에서 정보를 주고받는 방법이나 규약

from http.server import CGIHTTPRequestHandler, HTTPServer

PORT = 9999

class Handler(CGIHTTPRequestHandler):
    cgi_directories =['/cgi-bin']

def runFunc():
    serv = HTTPServer(('127.0.0.1',PORT), Handler)
    print('웹 서비스 진행 중....')

    try:
        serv.serve_forever()
    except Exception as e:
        print('서버 종료')
    finally:
        serv.server_close()

if __name__ == '__main__':
    runFunc()