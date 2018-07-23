# This file is executed on every boot (including wake-boot from deepsleep)

import time
import sys
import uos
import _thread

Thread = [ False ]

def GetFileHash():
	return uos.stat('index.py')[8] # Get File Time
	
def thread_check():
	bak = GetFileHash()
	_thread.start_new_thread(thread_index, ())
	while(True):
		time.sleep(1)
		tmp = GetFileHash()
		if(bak != tmp):
			bak = tmp
			if(Thread[0]):
				Thread[0] = False
				while Thread[0] == False:
					time.sleep(0.5)
			_thread.start_new_thread(thread_index, ())
def thread_index():
	Thread[0] = True
	file = open('index.py', "r")
	code = file.read()
	file.close()
	try:
		exec(code, {'Thread' : Thread})
	except Exception as e:
		sys.print_exception(e)
	while Thread[0]:
		pass
	Thread[0] = True
if __name__ == "__main__":
	ThreadFileCheck = _thread.start_new_thread(thread_check, ())
