#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
#import read_sub as sub
import py_read_output as rd 
import plot_sub as p
from pylab import * 
import numpy as np 
import sys
import os

'''
usage
 e.g. python plot_output.py 
'''
 
#names = ["fiducial_agn", "cv_standard"]
#names = ["cv_standard"]
#names = ["fiducial_agn"]
names = 

try:
	f = open("cv_standard.out", "r")
	for line in f:
		data = line.split()
		if len(data) > 2:
			if data[0] == "!!Python" and data[1]=="Version":
				VERSION = data[2]
except IOError:
	print "Couldn't read version"
	VERSION=""
	


print "VERSION %s" % VERSION

for i in range(len(names)):

	name = names[i]

	pf_dict = sub.read_pf(name)						# read in pf file

	convergence = sub.read_convergence (name)		# get convergence of model

	print "Model %s" % name
	print "%.2fpc Converged" % (100.0*convergence)

	# run py_wind- only need to run this to create the files
	sub.run_py_wind(VERSION, name)

	p.make_geometry_plot(name)					# make plots of pywind quantities
	p.make_geometry_ratios(name)


	# this is the current dev spectral file
	s = sub.read_spec_file(name)

	# this is the benchmark spectral file to test against
	s_bench = sub.read_spec_file("/Users/jmatthews/Documents/quick_regression/Python_78/%s" % name)

	# just make some standard spectrum plots
	p.make_standard_plot(s, name)
	p.make_components_plot(s, name)

	p.make_residual_plot(s, s_bench, name)		# make residual plots
	p.make_comp_plot(s, s_bench, name)			# make comparison plots
	p.make_components_comp_plot(s, s_bench, name)	# make components comparison plots



	# this is the current dev spectot file
	s = sub.read_spectot_file(name)

	# this is the benchmark spectot file to test against
	s_bench = sub.read_spectot_file("/Users/jmatthews/Documents/quick_regression/Python_78/%s" % name)

	p.make_log_spec_tot_plot(s, name)
	p.make_log_spec_tot_comp_plot(s, s_bench, name)



# move all the wind data somewhere out the way
#os.system("mkdir wind_data")
os.system("mv *.dat wind_data/")
#os.system("open -a preview *.png")

print "all done"
