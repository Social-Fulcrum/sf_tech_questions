import pandas as pd 

"""
PYTHON TEST

Pandas is a widely used tool for analyzing tabular data structures (spreadsheets, SQL tables, etc.) in Python.
It is one of Social Fulcrum's core tools for managing and analyzing data, and is part of the majority of our work.

Reference Documentation:

Pandas Documentation: http://pandas.pydata.org/pandas-docs/version/0.18.0/
Pandas Tutorial: http://pandas.pydata.org/pandas-docs/version/0.18.1/tutorials.html
Installing Pandas (or using a web service): http://pandas.pydata.org/pandas-docs/stable/install.html

In this file, please write a main function that reads the sample_dataset.csv included in this repository
into a Pandas DataFrame object and prints answer to the questions posed in the function.

Documentation for the sample_dataset can be found in sample_dataset_documentation.md.

The function does not need to return a value.

"""

def main():

	"""
	QUESTION 1
	
	Is there a meaningful relationship between the client's CPM and major calendar
	events (such as US holidays)?

	To answer, please print the mean CPM for holidays and non-holidays.
	Feel free to change the pre-set variable names if you like.

	More information on CPM can be found here:
	https://en.wikipedia.org/wiki/Cost_per_mille
	"""

	print 'CPM by holiday/non-holiday:\n'
	print 'Holiday CPM: ' + holiday_cpm + ' Non-Holiday CPM: ' + non_holiday_cpm
	print '\n\n'

	"""
	QUESTION 2
	
	What are the most and least expensive audiences by:
		- CPM? https://en.wikipedia.org/wiki/Cost_per_mille
		- CPC? http://www.wordstream.com/cost-per-click
		- Cost per pixel_5?
		- Cost per pixel_10?

	To answer, please print the audience field for each metric.
	Feel free to change the pre-set variable names if you like.

	More information on CPM can be found here:
	https://en.wikipedia.org/wiki/Cost_per_mille
	"""	

	print 'Highest and lowest CPM:\n'
	print 'High: ' + cpm_audience_high + ' Low: ' + cpm_audience_low
	print '\n\n'

	print 'Highest and lowest CPC:\n'
	print 'High: ' + cpc_audience_high + ' Low: ' + cpc_audience_low
	print '\n\n'

	print 'Highest and lowest pixel_5:\n'
	print 'High: ' + pixel5_audience_high + ' Low: ' + pixel5_audience_low
	print '\n\n'

	print 'Highest and lowest pixel_10:\n'
	print 'High: ' + pixel10_audience_high + ' Low: ' + pixel10_audience_low
	print '\n\n'

	return None


if __name__ == '__main__':
	main()