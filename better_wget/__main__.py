import sys
from .download import download_url


def maingl():
	if len(sys.argv) != 4:
		print("Usage python better-wget [url] [target location - full path] [minimum speed - in KBps]")
	else:
		url = sys.argv[1]
		dest = sys.argv[2]
		min_speed = sys.argv[3]
		download_url(url, dest, min_speed)

