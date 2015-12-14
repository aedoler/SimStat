###############
README: SimStat
###############

1. Install
==========
The simstat.py script can be obtained from github at https://github.com/fhejazi/SimStat.
Required module are:

- scipy
- numpy
- math
- sys
- argparse

All modules with the exception of scipy and numpy are part of the standard library.
scipy and numpy can be installed on Ubuntu via:

 apt-get install python-scipy

 apt-get install python-numpy

2. Running simstat.py
=====================

Simstat.py can be run as follows:

Option 1)
*********

To obtain the confidence interval for a sample, when the total number of data points, mean
and standard deviation are known, use the following syntax below. Confidence level is optional
and defaults to 0.95 (95%), if not specified.

 python simstat.py sum [num mean std] [conf]

Example:

 python simstat.py sum 10 5.4 1.2 0.99

 (4.4225415044376284, 6.3774584955623723)

Option 2)
*********

To obtain the confidence interval for a sample, when the raw sample data is available in a
csv format, use the following syntax below. Additionally, other values of interest, such as
MIN, MAX and variance are also returned.

 python simstat.py data [data_file] [conf]

Example:

 python simstat.py data data.txt 0.95

 Num: 10, Min: 99.1, Max: 933.3, Mean: 341.9220, Variance: 55918.5200

 (195.35846711874191, 488.485532881258)

