from subprocess import Popen
import time
...
# Runs the command in another process. Doesn't block
process = None
def start_download(url, path_prefix):
	global process
	if process:
		process.kill()
		print('finished')
	process = Popen(['wget',
				'-c',
				url,
				'-v',
				'-P',
				path_prefix,
				'--output-file=output.txt'
			])

def download_url(url, path_prefix, min_speed):

	# wait a bit for first log to output.txt
	start_download(url, path_prefix)

	time.sleep(2)
	while(True):
		if process.poll() is None: 
		    # Still running
		    fo = open("./output.txt", "r+")
		    lines_ = fo.read()
		    lines = lines_.split('\n')
		    lastLine = lines[len(lines)-2]
		    splitLastLine = lastLine.split(' ')

		    speed = splitLastLine[len(splitLastLine)-2]
		    print(speed)
		    if not speed:
		    	continue
		    if speed[-1] == 'B':
		    	start_download(url, path_prefix)
		    elif speed[-1] == 'K':
		    	if(float(speed.split('K')[0]) < min_speed):
		    		start_download(url, path_prefix)
		    fo.close()
		else:
		    # Has finished
		    print("finished")
		time.sleep(1)


