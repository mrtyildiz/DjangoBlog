import psycopg2
conn = psycopg2.connect(
   database="postgres", user='postgres', password='PJjhVpnW41lPQ2Y', host='172.66.0.5', port= '5432'
)
conn.autocommit = True
cursor = conn.cursor()
sql = '''CREATE database blog''';
cursor.execute(sql)
print("Database created successfully........")
conn.close()