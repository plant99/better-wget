from subprocess import Popen
import time
...
# Runs the command in another process. Doesn't block
process = Popen(['wget',
				'-c',
				'http://podoce.dinf.usherbrooke.ca/static/dataset/MIO-TCD-Classification.tar',
				'-v',
				'--output-file=output.txt'
			])

# wait a bit for first log to output.txt

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
	    if speed[-1] == 'B':
	    	process.kill()
	    	print('finished')
	    	process = Popen(['wget',
				'-c',
				'http://podoce.dinf.usherbrooke.ca/static/dataset/MIO-TCD-Classification.tar',
				'-v',
				'--output-file=output.txt'
			])
	    elif speed[-1] == 'K':
	    	if(float(speed.split('K')[0]) < 100):
	    		process.kill()
	    		print('finished')
	    		process = Popen(['wget',
					'-c',
					'http://podoce.dinf.usherbrooke.ca/static/dataset/MIO-TCD-Classification.tar',
					'-v',
					'--output-file=output.txt'
				])
	    fo.close()
	else:
	    # Has finished
	    print("finished")
	time.sleep(1)


