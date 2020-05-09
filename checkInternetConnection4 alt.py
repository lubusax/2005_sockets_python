import socket
import time
import shlex
from subprocess import call, PIPE, STDOUT

def get_return_code_of_simple_cmd(cmd, stderr=STDOUT):
  """Execute a simple external command and return its exit status."""
  args = shlex.split(cmd)
  if call(args, stdout=PIPE, stderr=stderr) == 0:
    answer = True # there was an answer to the ping
  else:
    answer = False
  
  return answer

def is_network_alive():
  cmd = "ping -c 1 1.1.1.1"
  return get_return_code_of_simple_cmd(cmd)

duration = time.process_time()

result = is_network_alive()

duration = time.process_time() - duration

print('result: ', result)
print('time ellapsed ', duration*1000, 'ms')