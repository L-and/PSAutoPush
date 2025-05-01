n, m = map(int, input().split()) # n: 저장된 사이트주소의 수, m: 비밀번호를 찾을려는 사이트의 수

passwordDict = dict() # [주소] = 비밀번호 로 저장

for i in range(n): # 사이트와 비밀번호 입력
    url, password = map(str, input().split())
    
    passwordDict[url] = password

for i in range(m): # 찾을려는 사이트 입력
    targetURL = input()
    print(passwordDict[targetURL])
