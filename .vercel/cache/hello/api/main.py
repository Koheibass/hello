from fastapi import FastAPI


class CustomHTTPRequestHandler(FastAPI):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write("GETメソッドを実装".encode())


server_address = ("localhost", 3000)
httpd = FastAPI(server_address, CustomHTTPRequestHandler)
httpd.serve_forever()
