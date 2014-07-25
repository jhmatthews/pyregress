#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
import read_sub as sub
import plot_sub as p
from pylab import * 
import numpy as np 
import sys
import os

'''
usage
 e.g. python plot_output.py sv 
'''
 
names = ["fiducial_agn", "cv_standard"]
#names = ["cv_standard"]
#names = ["fiducial_agn"]


try:
	f = open("cv_standard.out", "r")
	for line in f:
		data = line.split()
		if len(data) > 2:
			if data[0] == "!!Python" and data[1]=="Version":
				VERSION = data[2]
except IOError:
	print "Couldn't read version"
	VERSION="78a_dev"
	


print "VERSION %s" % VERSION

for i in range(len(names)):

	name = names[i]

	pf_dict = sub.read_pf(name)

	convergence = sub.read_convergence (name)

	print "Model %s" % name
	print "%.2fpc Converged" % (100.0*convergence)

	# run py_wind- only need to runt his to create the files
	sub.run_py_wind(VERSION, name)

	s = sub.read_spec_file(name)

	p.make_standard_plot(s, name)

	p.make_components_plot(s, name)

	s_bench = sub.read_spec_file("/Users/jmatthews/Documents/quick_regression/Python_78/%s" % name)

	p.make_residual_plots(s, s_bench, name)
	p.make_comp_plots(s, s_bench, name)

	s = sub.read_spectot_file(name)

	p.make_log_spec_tot_plot(s, name)

	p.make_geometry_plot(name)


os.system("mkdir wind_data")
os.system("mv *.dat wind_data/")
os.system("open -a preview *.png")

print "all done"
