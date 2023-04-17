from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
user = "neo4j"
psw = "admin"

driver = GraphDatabase.driver(uri, auth=(user, psw))
session = driver.session()

session.run("""USING PERIODIC COMMIT 1000
                LOAD CSV WITH HEADERS FROM "file:///customer40000.csv" AS line WITH line WHERE line.CLAIM IS null
                CREATE (n:Name {NAME: line.NAME})
                MERGE (a:Address {ADDRESS: line.ADDRESS})
                MERGE (e:Email {EMAIL: line.EMAIL})
                MERGE (p:Phone {PHONE: line.PHONE})
                MERGE (s:Ssn {SSN: line.SSN})
                MERGE (n)-[:HAS_ADDRESS]->(a)
                MERGE (n)-[:HAS_MAIL]->(e)
                MERGE (n)-[:HAS_PHONE]->(p)
                MERGE (n)-[:HAS_SSN]->(s)
                """)

session.run("""USING PERIODIC COMMIT 1000
                LOAD CSV WITH HEADERS FROM "file:///customer40000.csv" AS line WITH line WHERE line.CLAIM IS NOT null
                CREATE (n:Name {NAME: line.NAME})
                CREATE (cl:Claim {Claim: line.CLAIM})
                MERGE (a:Address {ADDRESS: line.ADDRESS})
                MERGE (e:Email {EMAIL: line.EMAIL})
                MERGE (p:Phone {PHONE: line.PHONE})
                MERGE (s:Ssn {SSN: line.SSN})
                MERGE (l:Lawyer {LAWYER: line.LAWYER})
                MERGE (ev:Evaluator {EVALUATOR: line.EVALUATOR})
                MERGE (n)-[:HAS_ADDRESS]->(a)
                MERGE (n)-[:HAS_MAIL]->(e)
                MERGE (n)-[:HAS_PHONE]->(p)
                MERGE (n)-[:HAS_SSN]->(s)
                MERGE (n)-[:HAS_CLAIM]->(cl)
                MERGE (l)-[:IS_INVOLVED]->(cl)
                MERGE (ev)-[:IS_INVOLVED]->(cl)
                """)
