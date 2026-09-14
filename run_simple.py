"""
Skrip server alternatif tanpa perlu install library tambahan (Built-in Python).
Bisa langsung di-running di VS Code:
python run_simple.py
"""
import http.server
import socketserver
import webbrowser
import os
from threading import Timer

PORT = 8000
DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def open_browser():
    webbrowser.open_new_tab(f'http://127.0.0.1:{PORT}/index.html')

if __name__ == '__main__':
    Timer(1.2, open_browser).start()
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("=" * 60)
        print("  SISTEM PERMINTAAN MASTER MATERIAL & APPROVAL (SERVER RINGAN)")
        print(f"  Server berjalan di: http://127.0.0.1:{PORT}/index.html")
        print("  Browser akan terbuka secara otomatis...")
        print("  Tekan Ctrl+C di terminal VS Code untuk menghentikan server")
        print("=" * 60)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer dihentikan.")
