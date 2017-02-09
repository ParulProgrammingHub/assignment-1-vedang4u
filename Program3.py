cm=input("Enter the value in Centimeter")
m= float (cm/100)
km= float (m/1000)
choice = input("""Enter 1 to convert in Meter
and  2 to convert in Kilometer""")
if choice ==1:
    print "The Distance in Meter is %s" % (m)
elif choice ==2:
    print "The distance in Kilometer is %s" % (km)
else:
    print "Enter the valid Choice"
    
