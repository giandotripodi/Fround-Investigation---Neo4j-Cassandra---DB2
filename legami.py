from tempfile import NamedTemporaryFile
import shutil
import csv
import random
from faker import Faker
fake = Faker(['en-US'])

reclami = ["Property damage", "Car damage", "Health damage"]



num_casuali_email_phone = [12,23,36,46,61,204,220,333,441,522,666,777]
num_casuali_ssn = [234,333,479,546,684,699,753,826,884,936,949,977]

filename = 'customer.csv'
tempfile = NamedTemporaryFile('w+t', newline='', delete=False)

fields = ['ID','NAME','ADDRESS','EMAIL','PHONE','SSN', 'CLAIM', 'LAWYER', 'EVALUATOR']

with open(filename,'r', newline='') as csv_file, tempfile:
    reader = csv.DictReader(csv_file, fieldnames=fields)
    writer = csv.DictWriter(tempfile, fieldnames=fields)
    next(reader) #Passo subito al primo id, quindi non leggo la riga "ID,NAME,ADDRESS,EMAIL,PHONE,SSN,CLAIM"

    k = 0
    q = 0
    first = 0

    for row in reader:

        id = int(row['ID'])

        if k >= 12:
            k = 0

        if q >= 12:
            q = 0

        if id == 1:
            iddi = "ID"
            name = "NAME"
            address = "ADDRESS"
            email = "EMAIL"
            phone = "PHONE"
            ssn = "SSN"
            claim = "CLAIM"
            lawyer = "LAWYER"
            evaluator = "EVALUATOR"
            row = {'ID': iddi, 'NAME': name, 'ADDRESS': address, 'EMAIL': email, 'PHONE': phone, 'SSN': ssn, 'CLAIM': claim, 'LAWYER': lawyer, 'EVALUATOR': evaluator}
            writer.writerow(row)

            first = 1

            name = fake.name()
            address = fake.street_address()
            email = fake.email()
            phone = fake.phone_number()
            ssn = fake.ssn()
            claim = None
            lawyer = fake.name()
            evaluator = fake.name()
            row = {'ID': first, 'NAME': name, 'ADDRESS': address, 'EMAIL': email, 'PHONE': phone, 'SSN': ssn, 'CLAIM': claim, 'LAWYER': lawyer, 'EVALUATOR': evaluator}
            writer.writerow(row)

        elif id % 10 == 0:
            name = row['NAME']
            address = row['ADDRESS']
            y = address  #Prendo l'indirizzo che mi servirà per il successivo
            email = row['EMAIL']
            phone = row['PHONE']
            ssn = row['SSN']
            claim = row['CLAIM']
            u = claim
            lawyer = row['LAWYER']
            w = lawyer
            evaluator = row['EVALUATOR']
            e = evaluator
            row = {'ID': id, 'NAME': name, 'ADDRESS': address, 'EMAIL': email, 'PHONE': phone, 'SSN': ssn, 'CLAIM': claim, 'LAWYER': lawyer, 'EVALUATOR': evaluator}
            writer.writerow(row) #scrivo la riga da cui prenderò l'indirizzo

            p = id + 1

            #Creo i dati
            name = fake.name()
            address = y
            email = fake.email()
            phone = fake.phone_number()
            ssn = fake.ssn()
            claim = u
            lawyer = w
            evaluator = e
            row = {'ID': p, 'NAME': name, 'ADDRESS': address, 'EMAIL': email, 'PHONE': phone, 'SSN': ssn, 'CLAIM': claim, 'LAWYER': lawyer, 'EVALUATOR': evaluator}
            writer.writerow(row) #scrivo la riga

            #Passo agli id successivi(+2)
            next(reader, None)
            p = 0

        elif id == num_casuali_email_phone[k]:
            var = random.randint(0,2)
            name = row['NAME']
            address = row['ADDRESS']
            email = row['EMAIL']
            y = row['EMAIL']  #Prendo l'email che mi servirà per il successivo
            phone = row['PHONE']
            ssn = row['SSN']
            if id % 2 == 0:
                claim = reclami[var]
                u = claim
            else:
                claim = None
                u = claim
            lawyer = row['LAWYER']
            w = lawyer
            evaluator = row['EVALUATOR']
            e = evaluator
            row = {'ID': id, 'NAME': name, 'ADDRESS': address, 'EMAIL': email, 'PHONE': phone, 'SSN': ssn, 'CLAIM': claim, 'LAWYER': lawyer, 'EVALUATOR': evaluator}
            writer.writerow(row) #scrivo la riga da cui prenderò l'email

            i = id + 1

            #Scrivo i dati
            var = random.randint(0,2)
            name = fake.name()
            address = fake.street_address()
            email = y
            phone = fake.phone_number()
            z = phone #Prendo il telefono che mi servirà per l'id successivo
            ssn = fake.ssn()
            claim = u
            lawyer = w
            evaluator = e
            row = {'ID': i, 'NAME': name, 'ADDRESS': address, 'EMAIL': email, 'PHONE': phone, 'SSN': ssn, 'CLAIM': claim, 'LAWYER': lawyer, 'EVALUATOR': evaluator}
            writer.writerow(row) #scrivo la riga

            i = i + 1

            var = random.randint(0,2)
            name = fake.name()
            address = fake.street_address()
            email = fake.email()
            phone = z
            ssn = fake.ssn()
            claim = u
            lawyer = w
            evaluator = e
            row = {'ID': i, 'NAME': name, 'ADDRESS': address, 'EMAIL': email, 'PHONE': z, 'SSN': ssn, 'CLAIM': claim, 'LAWYER': lawyer, 'EVALUATOR': evaluator}
            writer.writerow(row) #scrivo la riga

            #Passo agli id successivi (+2)
            next(reader)
            next(reader)
            i = 0
            k = k + 1

        elif id == num_casuali_ssn[q]:
            name = row['NAME']
            address = row['ADDRESS']
            email = row['EMAIL']
            phone = row['PHONE']
            ssn = row['SSN']
            y = row['SSN']  #Prendo l'ssn che mi servirà per il successivo
            claim = row['CLAIM']
            u = claim
            lawyer = row['LAWYER']
            w = lawyer
            evaluator = row['EVALUATOR']
            e = evaluator
            row = {'ID': id, 'NAME': name, 'ADDRESS': address, 'EMAIL': email, 'PHONE': phone, 'SSN': ssn, 'CLAIM': claim, 'LAWYER': lawyer, 'EVALUATOR': evaluator}
            writer.writerow(row) #scrivo la riga da cui prenderò l'email

            n = id + 1

            #Scrivo i dati
            var = random.randint(0,2)
            name = fake.name()
            address = fake.street_address()
            email = fake.email()
            phone = fake.phone_number()
            ssn = y
            claim = u
            lawyer = w
            evaluator = e
            row = {'ID': n, 'NAME': name, 'ADDRESS': address, 'EMAIL': email, 'PHONE': phone, 'SSN': ssn, 'CLAIM': claim, 'LAWYER': lawyer, 'EVALUATOR': evaluator}
            writer.writerow(row) #scrivo la riga

            #Passo agli id successivi (+1)
            next(reader, None)
            n = 0
            q = q + 1

        else:
            writer.writerow(row)

shutil.move(tempfile.name, filename) #sostituisco i valori del file temporaneo all'interno del file customer.csv
