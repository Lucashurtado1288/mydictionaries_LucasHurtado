"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $60,000



"""

import json

#opening the JSON file
file = open('school_data.json', 'r')

#converting the JSON data into a python list of dictionaries
schools = json.load(file)



# (a) Graduation report
# Looping through every school in the list, school represents one dictionary at a time
for school in schools: 
    grad_rate = school["Graduation rate  women (DRVGR2020)"]
    if grad_rate != None and grad_rate > 75:
        # Printing university name
        print ("University: " + school["instnm"])
        # Convert grad_rate to str and add % symbol to match format
        print("Graduation Rate for Women: " + str(grad_rate) + "%")
        print()

# (b) Cost report
# Look through all schools again 
for school in schools:
    # Total price for in-state students living off campus
    cost = school["Total price for in-state students living on campus 2020-21 (DRVIC2020)"]
    if cost != None and cost > 60000:
        # Print school name
        print("University: " + school["instnm"])
        print("Total price for in-state students living off campus: $" + format(cost, ",.2f"))
        print()


