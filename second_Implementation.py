import os
import webview
import threading
import http.server
import socketserver
import time


PORT = 8080 
FILENAME = "index.html"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
URL = f"http://localhost:{PORT}/{FILENAME}"

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=BASE_DIR, **kwargs)

def start_server():
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
            print(f"Server started at {BASE_DIR}")
            httpd.serve_forever()
    except Exception as e:
        print(f"Server error: {e}")

if __name__ == "__main__":
    # 1. Sunucuyu arka planda başlat
    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()

    time.sleep(1.5)

    # 3. UI Penceresini aç
    print(f"Launching Dashboard: {URL}")
    webview.create_window(
        title="UCS Satellite Database Dashboard",
        url=URL,
        width=1920,
        height=1080,
        resizable=True
    )
    
    webview.start()