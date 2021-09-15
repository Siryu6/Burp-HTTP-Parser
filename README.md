# Burp HTTPParser

Small Python class to parse "raw" (string) BurpSuite requests.

ContentType supported:
- Standart POST data
- multipart/form-data
- Json


## Usage

Using this request as exemple:
```
POST /test HTTP/1.1
Host: example.com
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Content-Type: application/x-www-form-urlencoded
Connection: close

param1=test&param2=anotherparam
```
Example script:
```python
from httpParser import HttpParser

with open("sample_req.txt", "r") as f:
    raw_req=f.read()

parsed_req=HttpParser(raw_req)
print(f"""Host: {parsed_req.host}
Path: {parsed_req.path}
Method: {parsed_req.method}
Headers: {parsed_req.headers}
Params: {parsed_req.params}
""")
```
Return:
```
Host: example.com
Path: /test
Method: POST
Headers: {'Host': 'example.com', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'en-US,en;q=0.9', 'Content-Type': 'application/x-www-form-urlencoded', 'Connection': 'close'}
Params: {'param1': 'test', 'param2': 'anotherparam'}
```

## Notes

As I only needed to parse POST requests, HttpParser doesn't work on GET Requests yet.  
Please give me sample requests when creating issues :)



