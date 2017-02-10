mi=input("Marks Obtained in mi")
java=input("Marks Obtained in java")
py=input("Marks Obtained in Python")
dbms=input("Marks Obtained in dbms")
co=input("Marks Obtained in Computer Organization")
total = mi + java + co + dbms + py
avg= total/5.0
print "The mean is %s" % (avg)
per=(total*100)/250
if per<=35 :
    print "YOU HAVE FAILED THE EXAAM AND YOU HAVE SCORED %s PERCENTAGE" % (per)

else :
    print "CONGRATULATIONS !!!!! YOU HAVE PASSED THE EXAM AND YOU HAVE SCORED %s PERCENTAGE" % (per)
