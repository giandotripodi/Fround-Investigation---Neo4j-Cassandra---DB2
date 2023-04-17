import time
import xlsxwriter
from cassandra.cluster import Cluster

cluster = Cluster()

session = cluster.connect('insurance_fraud_investigation_40k')
session.execute("USE insurance_fraud_investigation_40k;")

tempo = lambda: int(round(time.time() * 1000))
workbook = xlsxwriter.Workbook('query1_40000.xlsx')
worksheet = workbook.add_worksheet()
row = 1
col = 0

def query1():
    session.execute("""SELECT name,claim FROM Customer WHERE claim = 'Car damage' ALLOW FILTERING;""")

def query2():
    session.execute("""SELECT name,claim FROM Customer WHERE claim = 'Car damage' AND name LIKE 'M%' ALLOW FILTERING;""")

def query3():
    session.execute("""SELECT name,claim,ssn FROM Customer WHERE claim = 'Car damage' AND name LIKE 'M%' AND ssn LIKE '4%' ALLOW FILTERING;""")

def query4():
    session.execute("""SELECT name,claim,ssn,lawyer FROM Customer WHERE claim = 'Car damage' AND name LIKE 'M%' AND ssn LIKE '4%' ALLOW FILTERING;""")

def query5():
    session.execute("""SELECT * FROM Customer WHERE claim = 'Car damage' AND name LIKE 'M%' AND ssn LIKE '4%' ALLOW FILTERING;""")



for x in range(31):
    a1 = tempo()
    query1()
    a2 = tempo()
    worksheet.write(row, col, a2-a1)
    row += 1
    print("Il risultato di " ,x+1, " e'" ,a2-a1, " millesecondi\n")

worksheet.write(row, col, a2-a1)
workbook.close()
