import socket
import time

def is_connected():
  try:
    # connect to the host -- tells us if the host is actually
    # reachable
    socket.create_connection(("www.google.com", 80))
    return True
  except OSError:
    pass
  return False

duration = time.process_time()

is_connected()

duration = time.process_time() - duration
print('time ellapsed ', duration*1000, 'ms')