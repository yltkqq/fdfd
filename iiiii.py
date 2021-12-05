import urllib.request

url="http://49.232.124.89:8080/telecom/sign?mobile=17760490797"
req=urllib.request.Request(url)
resp=urllib.request.urlopen(req)
data=resp.read().decode('utf-8')

print(data)