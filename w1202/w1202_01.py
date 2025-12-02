# 1XX: Informational(정보 제공)
#   임시 응답으로 현재 클라이언트의 요청까지는 처리되었으니 계속 진행하라는 의미입니다. HTTP 1.1 버전부터 추가되었습니다.
# 2XX: Success(성공)
#   클라이언트의 요청이 서버에서 성공적으로 처리되었다는 의미입니다.
# 3XX: Redirection(리다이렉션)
#   완전한 처리를 위해서 추가 동작이 필요한 경우입니다. 주로 서버의 주소 또는 요청한 URI의 웹 문서가 이동되었으니 그 주소로 다시 시도하라는 의미입니다.
# 4XX: Client Error(클라이언트 에러)
#   없는 페이지를 요청하는 등 클라이언트의 요청 메시지 내용이 잘못된 경우를 의미합니다.
# 5XX: Server Error(서버 에러)
#   서버 사정으로 메시지 처리에 문제가 발생한 경우입니다. 서버의 부하, DB 처리 과정 오류, 서버에서 익셉션이 발생하는 경우를 의미합니다.

import requests

# requests url정보를 가져옴
url = "http://www.google.com"
res = requests.get(url)

# 에러시 프로그램 종료
res.raise_for_status()

# 응답코드 성공 : 200, 실패 : 404(클라이언트),500(서버)
print("응답코드 : ",res.status_code) 

# 성공코드 출력
print(requests.codes.ok)

# print(res.text)