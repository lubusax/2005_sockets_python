import socket
import time

duration = time.process_time()

IPaddress=socket.gethostbyname(socket.gethostname())
# if IPaddress=="127.0.0.1":
# 		print("No internet, your localhost is "+ IPaddress)
# else:
# 		print("Connected, with the IP address: "+ IPaddress )


duration = time.process_time() - duration
print('time ellapsed ', duration*1000, 'ms')