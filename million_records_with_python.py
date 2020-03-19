import faker
import random
import csv

from faker import Faker
fake = Faker()

# Defining the phone number generator function
def phn():
    n = '00000000000'
    while '9' in n[3:6] or n[3:6]=='000' or n[6]==n[7]==n[8]==n[9]:
        n = str(random.randint(10**10, 10**11-1))
    return n[:3] + '-' + n[3:6] + '-' + n[6:]

#Creating the csv file
with open('million_py.csv', 'w', newline='') as n:
    thewriter = csv.writer(n)
    thewriter.writerow(['Name', 'Age', 'Phone', 'Country', 'Email'])

    for i in range(10): # you can change that to any number you want
        Name = str(fake.name())
        Age = str(random.randint(18,70))
        Phone = str(phn())
        Country = str(fake.country())
        Email = str(fake.email())

        thewriter.writerow([Name, Age, Phone, Country, Email])
