In this project we wrote a software that detects faces and lips
in a video feed coming from an built-in webcam. The purpose of
this miniprojet is to create a software that calculate smile
ratios given bounding box coordinates, these ratios will later
be used to filter out noise in automatic lip reading.

The project contains 4 files:
	- data_acquisition.py
	- smile_ratio.py
	- smile_records.csv
	- processed_data.csv

1. data_acquisition.py
It is used to detect the smiles and save coordinates into a
csv file used for further processing. 

How to use:
- run the script
- it will open the webcam recorder
- it will automatically save points to a csv file

IMPORTANT:
Running this script will overwrite the existing smile_records.csv
file, and new points will be saved. It is recommended not to run
it before the existing points are processed.

2. smile_ratio.py
It is used to compute the smile ratios from the coordinates
in smile_records.csv. It contains 3 different versions to do this:
	- the naive version
	- the vectorized version
	- the multiprocessing version

How to use:
	- open the script
	- comment out the unused versions
	- run the script

IMPORTANT:
Given the fact that library specific functions are used, the
script can only run the naive and vectorized functions 
simultaneously, but the multiprocessing version has to be run
separately. Further instructions are given in the script.

3. smile_records.csv
It is used to save coordinates and computed ratios. It can
be opened with Microsoft Excel (recommended) or Notepad.

4. processed_data.csv
It stores computation results from all 3 versions of the
algorithm.
