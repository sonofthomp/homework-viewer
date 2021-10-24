import time
import os
from datetime import datetime

while True:
	os.system("python checker.py")
	print("Just updated for " + datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
	time.sleep(1800)
