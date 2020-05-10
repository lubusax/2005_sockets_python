import socket
import time
import shlex
from subprocess import call, PIPE, STDOUT, Popen

def getReturnCode(cmd, stderr=STDOUT, timeout=1):
  """Execute a simple shell command and return its exit status."""
  args = shlex.split(cmd)
  childProcess = Popen(args,stdout=PIPE,stderr=stderr)
  try:
    childProcess.communicate(timeout=timeout)
    returnCode = childProcess.returncode
  except:
    returnCode = -99 # timeout or other error
  return returnCode

def internetAccess():
  cmd = "ping -c 1 1.1.1.1"
  return getReturnCode(cmd) == 0

duration = time.process_time()

result = internetAccess()

duration = time.process_time() - duration

print('result: ', result)
print('time ellapsed ', duration*1000, 'ms')