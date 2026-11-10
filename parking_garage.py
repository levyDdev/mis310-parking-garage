# Damon Levy - Parking Garage
# Python for Data & Analytics
# Chapter 3 - Decisions
# Parking Lot - initial problem - if/else

# input
hours = float(input('Enter hours parked: '))

# processing
charge = 5 + 2.5 * hours

if charge < 10:
    charge = 10
elif charge > 20:
    charge = 20

# output
print('Parking fee: $', format(charge, '.2f'))
