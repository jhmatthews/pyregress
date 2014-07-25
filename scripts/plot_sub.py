#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
from pylab import *
import numpy as np
import read_sub as sub

def make_standard_plot(s, name):

	fig = figure(figsize=(8.3,11.6))

	suptitle("Spectrum %s" % name)

	nplots = len(s.spec)
	nx = 2
	ny = (nplots + 1) / nx

	for i in range(len(s.spec)):
		subplot(ny, nx, i+1)
		plot(s.wavelength, smooth(s.spec[i]))

	xlabel("Wavelength")
	ylabel("Flux")
	savefig("spec_%s.png" % name)

	return 0


def make_components_plot(s, name):

	fig = figure(figsize=(8,8))
	suptitle("Spectrum components %s" % name)

	plot(s.wavelength, smooth(s.emitted), label="Emitted")
	plot(s.wavelength, smooth(s.disk), label="Disk")
	plot(s.wavelength, smooth(s.wind), label="Wind")
	plot(s.wavelength, smooth(s.hitsurf), label="HitSurf")
	plot(s.wavelength, smooth(s.scattered), label="Scattered")
	legend()


	xlabel("Wavelength")
	ylabel("Flux")
	savefig("spec_components_%s.png" % name)

	return 0



def make_log_spec_tot_plot(s, name):

	fig = figure(figsize=(8,8))
	suptitle("Logspectot: %s" % name)

	plot(s.wavelength, smooth(s.emitted), label="Emitted")
	plot(s.wavelength, smooth(s.disk), label="Disk")
	plot(s.wavelength, smooth(s.wind), label="Wind")
	plot(s.wavelength, smooth(s.hitsurf), label="HitSurf")
	plot(s.wavelength, smooth(s.scattered), label="Scattered")
	legend()


	xlabel("Wavelength")
	ylabel("Flux")
	savefig("logspectot_%s.png" % name)

	return 0

def make_log_spec_tot_comp_plot(s1, s2, name):

	fig = figure(figsize=(16,8))
	suptitle("Logspectot: %s (left) v Python 78 (right" % name)

	subplot(121)
	plot(s1.wavelength, smooth(s1.emitted), label="Emitted")
	plot(s1.wavelength, smooth(s1.disk), label="Disk")
	plot(s1.wavelength, smooth(s1.wind), label="Wind")
	plot(s1.wavelength, smooth(s1.hitsurf), label="HitSurf")
	plot(s1.wavelength, smooth(s1.scattered), label="Scattered")
	legend()

	subplot(122)
	plot(s2.wavelength, smooth(s2.emitted), label="Emitted")
	plot(s2.wavelength, smooth(s2.disk), label="Disk")
	plot(s2.wavelength, smooth(s2.wind), label="Wind")
	plot(s2.wavelength, smooth(s2.hitsurf), label="HitSurf")
	plot(s2.wavelength, smooth(s2.scattered), label="Scattered")
	legend()


	xlabel("Wavelength")
	ylabel("Flux")
	savefig("logspectot_comp_%s.png" % name)



def make_components_comp_plot(s1, s2, name):

	fig = figure(figsize=(16,8))
	suptitle("Spectrum components: %s (left) v Python 78 (right" % name)

	subplot(121)
	plot(s1.wavelength, smooth(s1.emitted), label="Emitted")
	plot(s1.wavelength, smooth(s1.disk), label="Disk")
	plot(s1.wavelength, smooth(s1.wind), label="Wind")
	plot(s1.wavelength, smooth(s1.hitsurf), label="HitSurf")
	plot(s1.wavelength, smooth(s1.scattered), label="Scattered")
	legend()

	subplot(122)
	plot(s2.wavelength, smooth(s2.emitted), label="Emitted")
	plot(s2.wavelength, smooth(s2.disk), label="Disk")
	plot(s2.wavelength, smooth(s2.wind), label="Wind")
	plot(s2.wavelength, smooth(s2.hitsurf), label="HitSurf")
	plot(s2.wavelength, smooth(s2.scattered), label="Scattered")
	legend()


	xlabel("Wavelength")
	ylabel("Flux")
	savefig("components_comp_%s.png" % name)


def make_geometry_plot(name):

	# read electron density from the file - could also try e.g. te or ionC4
	var = ["te", "tr", "ne", "nphot", "ioncH1", "ioncH2", "IP", "tot_lum"]


	fig = figure(figsize=(16.6,11.6))
	suptitle("Geometry: %s (left) v Python 78 (right)" % name)
	locs = [1,2,5,6,9,10,13,14]
	for i in range(len(var)):
		subplot(4,4,locs[i])
		x, z, value = sub.read_pywind_smart("%s.%s.dat" % (name, var[i]) )
		contourf(z,x,np.log10(value) )
		loglog()
		title("LOG " + var[i])
		colorbar()

		subplot(4,4,locs[i]+2)
		x, z, value = sub.read_pywind_smart("../../Python_78/wind_data/%s.%s.dat" % (name, var[i]) )
		contourf(z,x,np.log10(value) )
		loglog()
		title("LOG " + var[i])
		colorbar()

	savefig("geo_%s.png" % name)
	clf()


	var = ["ionHe1", "ionHe2", "ionC3", "ionC4", "ionC5", "ionN5", "ionO6", "ionSi4"]
	fig = figure(figsize=(16.6,11.6))
	suptitle("Ions: %s (left) v Python 78 (right)" % name)
	for i in range(len(var)):
		subplot(4,4,locs[i])
		x, z, value = sub.read_pywind_smart("%s.%s.dat" % (name, var[i]) )
		contourf(z,x,np.log10(value) )
		loglog()
		title("LOG " + var[i])
		colorbar()

		subplot(4,4,locs[i]+2)
		x, z, value = sub.read_pywind_smart("../../Python_78/wind_data/%s.%s.dat" % (name, var[i]) )
		contourf(z,x,np.log10(value) )
		loglog()
		title("LOG " + var[i])
		colorbar()

	savefig("ions_%s.png" % name)
	clf()

	return 0


def make_residual_plot(s1, s2, name):

	fig = figure(figsize=(8.3,11.6))

	nplots = len(s1.spec)
	nx = 2
	ny = (nplots + 1) / nx

	suptitle("Spectrum Residuals: %s v Python 78" % name)

	for i in range(len(s1.spec)):
		subplot(ny, nx, i+1)
		plot(s1.wavelength, smooth(s1.spec[i] - s2.spec[i]))

	xlabel("Wavelength")
	ylabel("Flux")
	savefig("residual_%s.png" % name)

	return 0


def make_comp_plot(s1, s2, name):

	fig = figure(figsize=(8.3,11.6))

	nplots = len(s1.spec)
	nx = 2
	ny = (nplots + 1) / nx

	suptitle("Comparison: %s v Python 78" % name)

	for i in range(len(s1.spec)):
		subplot(ny, nx, i+1)
		plot(s1.wavelength, smooth(s1.spec[i]), label=name)
		plot(s1.wavelength, smooth(s2.spec[i]), label="Python 78")
		if i == 0: legend()


	xlabel("Wavelength")
	ylabel("Flux")
	savefig("comp_%s.png" % name)

	return 0








def smooth(x,window_len=20,window='hanning'):
        if x.ndim != 1:
                raise ValueError, "smooth only accepts 1 dimension arrays."
        if x.size < window_len:
                raise ValueError, "Input vector needs to be bigger than window size."
        if window_len<3:
                return x
        if not window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman']:
                raise ValueError, "Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman'"
        s=np.r_[2*x[0]-x[window_len-1::-1],x,2*x[-1]-x[-1:-window_len:-1]]
        if window == 'flat': #moving average
                w=np.ones(window_len,'d')
        else:  
                w=eval('np.'+window+'(window_len)')
        y=np.convolve(w/w.sum(),s,mode='same')
        return y[window_len:-window_len+1]
