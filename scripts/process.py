#!/usr/bin/env python

import datetime, time
import os, sys
import numpy as np
import plot_output



DATE = datetime.date.today()

PYTEST = os.environ["PYTEST"]


#os.system("%s/scripts/process" % PYTEST) 

#time.sleep(30)


#names = ["fiducial_agn", "cv_standard", "balmer_test", "cv_macro_benchmark"]
names = ["1d_sn", "cv_standard"]
success = np.zeros(len(names))
failed = []

plot_output.make_plots(names)

# check how many runs completed
for i in range(len(names)):

	name = names[i]

	run_passed = False

	f = open("%s/outputs/%s.sig" % (PYTEST, name))

	for line in f:
		if "COMPLETE" in line:
			success[i] = 1
			run_passed = True

	if run_passed == False:
		success[i] = -1
		failed.append(name)


# check successes
# if there's a failure, email me
if success.all() == 1:
	print "Every run completed"
else:
	em = open("email.txt", "r")

	em.write("Failure on \n\n")
	em.write("Check Latest commit immediately\n\n")

	em.write("List of failures:")
	for model in failed:
		em.write("\tmodel")

	em.close()

	os.system("%s/scripts/email" % (PYTEST))



# commit to git and push
# os.system("cd %s;\
#           git commit -am 'Regression test for %s';\
#           git push origin gh-pages" % (PYTEST, DATE) )


