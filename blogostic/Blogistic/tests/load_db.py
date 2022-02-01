import psycopg2
conn=psycopg2.connect(dbname='blogistic',user='admin',password='1111', host='localhost')
cursor=conn.cursor()
for i in range(3,4):
    cursor.execute(f"insert into blogistic_client values ({i},'Попова Анна Артуровна','18-4-1999','7791209537378302');")
cursor.execute('select * from blogistic_client')
records = cursor.fetchall()
for k in records:
    print(k)
cursor.close()
conn.close()