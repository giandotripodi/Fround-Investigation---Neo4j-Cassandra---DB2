import csv
import random
from faker import Faker
fake = Faker(['en-US'])

reclami = ["Property damage", "Vehicle damage", "Health damage"]

#Creo ed apro il file csv
with open('customer.csv', 'w', newline='') as customer:
    fieldnames = ['ID','NAME', 'ADDRESS','EMAIL','PHONE','SSN', 'CLAIM', 'LAWYER', 'EVALUATOR']
    writer = csv.DictWriter(customer, fieldnames=fieldnames)
    writer.writeheader()
    id = 1

    #Creo ed inserisco i dati all'interno del file .csv, ogni 10 persone avranno l'indirizzo di casa uguale per creare un legame familiare
    for x in range(1000):

        if id % 2 == 0:
            k = random.randint(0,2)
            name = fake.name()
            address = fake.street_address()
            email = fake.email()
            phone = fake.phone_number()
            ssn = fake.ssn()
            claim = reclami[k]
            lawyer = fake.name()
            evaluator = fake.name()
            writer.writerow({'ID' : id, 'NAME': name, 'ADDRESS' : address, 'EMAIL' : email, 'PHONE' : phone, 'SSN': ssn, 'CLAIM': claim, 'LAWYER': lawyer, 'EVALUATOR': evaluator })
            customer = [id,name,address,email,phone,ssn,claim,lawyer,evaluator]
            id += 1

        else:
            name = fake.name()
            address = fake.street_address()
            email = fake.email()
            phone = fake.phone_number()
            ssn = fake.ssn()
            claim = None
            lawyer = None
            evaluator = None
            writer.writerow({'ID' : id, 'NAME': name, 'ADDRESS' : address, 'EMAIL' : email, 'PHONE' : phone, 'SSN': ssn, 'CLAIM': claim, 'LAWYER': lawyer, 'EVALUATOR': evaluator })
            customer = [id,name,address,email,phone,ssn,claim,lawyer,evaluator]
            id += 1
