import os
import signal
import sys

MyList = []

for files in os.walk('/root/logs'):
	if 'openstack-log.tar.bz2' in files[2] and files[0].endswith('/probe'):
		#print files
		MyList.append(files[0])
if __name__ == "__main__":
	for path in MyList:
		command_s = 'openstack-validation-tool -i '+path+' -o /root/temp/'
		print command_s
		try:
			os.system(command_s)
		except KeyboardInterrupt:
			break

