Vercel python built-in http handler
---

```
Running 10s test @ https://builtin-hello-world.vercel.app/
  2 threads and 8 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   117.39ms   71.06ms   1.12s    98.34%
    Req/Sec    35.73      6.13    40.00     93.94%
  712 requests in 10.02s, 252.40KB read
Requests/sec:     71.06
Transfer/sec:     25.19KB
```
Code
---
```python
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Hello, World!\n'.encode('utf-8'))
```
