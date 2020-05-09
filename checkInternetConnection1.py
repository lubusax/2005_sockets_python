import urllib.request
import time

def connect(host='http://google.com'):
	try:
		urllib.request.urlopen(host) #Python 3.x
		print('connected')
		return True
	except:
		print('NOT connected')
		return False
# test
duration = time.process_time()
connect()
duration = time.process_time() - duration
print('time ellapsed ', duration*1000, 'ms')