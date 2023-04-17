from cassandra.cluster import Cluster
import csv

cluster = Cluster()

session = cluster.connect('insurance_fraud_investigation_10k')
session.execute("USE insurance_fraud_investigation_10k;")

session.execute("""
                CREATE TABLE IF NOT EXISTS Customer (
                ID text,
                Name text,
                Address varchar,
                Email varchar,
                Phone text,
                Ssn text,
                Claim text,
                Lawyer text,
                Evaluator text,
                PRIMARY KEY (ID)
                )
                """)

fields = ['ID','NAME','ADDRESS','EMAIL','PHONE','SSN','CLAIM','LAWYER','EVALUATOR']

with open('customer10000.csv', 'rb') as customer:
    reader = csv.DictReader(customer, fieldnames=fields)
    next(reader)  #Salto la prima riga con i fields
    for row in reader:
        #Sostituiamo il trattino con uno spazio vuoto altrimenti non ci stampa i dati
        phone = row['PHONE'].replace("-"," ")
        ssn = row['SSN'].replace("-"," ")
        CQLString = ("INSERT INTO Customer (ID,Name,Address,Email,Phone,Ssn,Claim,Lawyer,Evaluator) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        session.execute(CQLString, (row['ID'],row['NAME'],row['ADDRESS'],row['EMAIL'],phone,ssn,row['CLAIM'],row['LAWYER'],row['EVALUATOR']))
