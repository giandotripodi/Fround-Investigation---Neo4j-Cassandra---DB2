import xlsxwriter
import time
from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
user = "neo4j"
psw = "admin"

driver = GraphDatabase.driver(uri, auth=(user, psw))
session = driver.session()

tempo = lambda: int(round(time.time() * 1000))
workbook = xlsxwriter.Workbook('query5_10k.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0

def query1(valueClaim):
    with driver.session() as session:
        session.run("""
                    MATCH (n:Name)-[r:HAS_CLAIM]->(c:Claim)
                    WHERE c.Claim = $valueClaim
                    RETURN n,r,c""", valueClaim = valueClaim)
def query2(valueClaim, valueName):
    with driver.session() as session:
        session.run("""
                    MATCH (n:Name)-[r:HAS_CLAIM]->(c:Claim)
                    WHERE c.Claim = $valueClaim AND n.NAME STARTS WITH $valueName
                    RETURN n,r,c""", valueClaim = valueClaim, valueName = valueName )

def query3(valueClaim,valueName,valueSSN):
    with driver.session() as session:
        session.run("""
                    MATCH (n:Name)-[r:HAS_CLAIM]->(c:Claim)
                    MATCH (n:Name)-[r1:HAS_SSN]->(s:Ssn)
                    WHERE c.Claim = $valueClaim AND n.NAME STARTS WITH $valueName AND s.SSN STARTS WITH $valueSSN
                    RETURN n,r,c,s,r1
                    """, valueClaim = valueClaim, valueName = valueName, valueSSN = valueSSN)
def query4(valueClaim,valueName,valueSSN):
    with driver.session() as session:
        session.run("""
                    MATCH (n:Name)-[r:HAS_CLAIM]->(c:Claim)<-[r2:IS_INVOLVED]-(l:Lawyer)
                    MATCH (n:Name)-[r1:HAS_SSN]->(s:Ssn)
                    WHERE c.Claim = $valueClaim AND n.NAME STARTS WITH $valueName AND s.SSN STARTS WITH $valueSSN
                    RETURN n,r,c,r2,l,r1,s
                    """, valueClaim = valueClaim, valueName = valueName, valueSSN = valueSSN)
def query5(valueClaim,valueName,valueSSN):
    with driver.session() as session:
        session.run("""
                    MATCH (n:Name)-[r:HAS_CLAIM]->(c:Claim)<-[r2:IS_INVOLVED]-(l:Lawyer)
                    MATCH (c:Claim)<-[r3:IS_INVOLVED]-(e:Evaluator)
                    MATCH (n:Name)-[r1:HAS_SSN]->(s:Ssn)
                    WHERE c.Claim = $valueClaim AND n.NAME STARTS WITH $valueName AND s.SSN STARTS WITH $valueSSN
                    RETURN n,r,c,r2,l,r3,e,r1,s
                    """, valueClaim = valueClaim, valueName = valueName, valueSSN = valueSSN)

for x in range(31):

    a1 = tempo()
    #query1('Car damage')
    #query2('Car damage','M')
    #query3('Car damage','M','4')
    #query4('Car damage','M','4')
    query5('Car damage','M','4') 
    a2 = tempo()
    row += 1
    worksheet.write(row, col, a2-a1)
    print("Il risultato di " ,x+1, " e'" ,a2-a1, " ms\n")

worksheet.write(row, col, a2-a1)
workbook.close()
