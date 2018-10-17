import sys
import download
if len(sys.argv) != 3:
	print("Usage python better-wget [url] [target location - full path]")
else:
	url = sys.argv[1]
	dest = sys.argv[2]

	download.download_url(url, dest)

