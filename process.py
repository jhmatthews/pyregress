#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import datetime, time
import os, sys




DATE = datetime.date.today()

os.system("/Users/jmatthews/Documents/quick_regression/latest/process") 

#time.sleep(30)


names = ["fiducial_agn", "cv_standard", "balmer_test", "cv_macro_benchmark"]


success = 0 

# check how many runs completed
for i in range(len(names)):

	name = names[i]

	run_passed = False

	f = open("outputs/"+name + ".sig")

	for line in f:
		if "COMPLETE" in line:
			success += 1
			run_passed = True

	if run_passed == False:
		failed.append(name)


# check successes
# if there's a failure, email me
if success == 4:
	print "Every run completed"
else:
	em = open("email.txt", "r")

	em.write("Failure on \n\n")
	em.write("Check Latest commit immediately\n\n")

	em.write("List of failures:")
	for model in failed:
		em.write("\tmodel")

	em.close()

	os.system("/Users/jmatthews/Documents/quick_regression/latest/email")



# commit to git and push
os.system("cd /Users/jmatthews/Documents/quick_regression/latest;\
          git commit -am 'Regression test for %s';\
          git push origin gh-pages" % DATE)


