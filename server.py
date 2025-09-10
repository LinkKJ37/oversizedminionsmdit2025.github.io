# This is a simple Python web server using the built-in http.server module.
# It will serve the 'index.html' file in the same directory.
#
# To run this server:
# 1. Save this file as 'server.py'.
# 2. Save the 'index.html' file in the same folder.
# 3. Open your terminal or command prompt.
# 4. Navigate to the folder where you saved the files.
# 5. Run the command: python -m http.server
# 6. Open your web browser and go to http://localhost:8000 to see your website!

import http.server
import socketserver

# Set the port number for the server. You can change this if you want.
PORT = 8000

# Create a handler to serve files.
Handler = http.server.SimpleHTTPRequestHandler

# Start the server.
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
