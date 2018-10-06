# better-wget
Script written to make wget more efficient, which restarts `wget` when download speed is below a certain limit.

## how to use
- replace the url in the array inside `Popen` with the one you want to download.
- create file `output.txt`
- python3 download.py 


## todo
- make it generic and give control to user through CLI
- log download percentage and/or other stuff
- check and control download failures, very low speeds, etc.
