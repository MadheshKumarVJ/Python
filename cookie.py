import http.cookiejar
import  urllib


url = 'https://www.linkedin.com/feed/'

def extractCookies():
    cookie_jar = http.cookiejar.CookieJar()

    url_opener= urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
    url_opener.open(url)
    print("[")
    print("{")
    for cookie in cookie_jar:
        print("\""+cookie.name+"\""+":"+cookie.value+",")
    print("}")
    print("]")
extractCookies()