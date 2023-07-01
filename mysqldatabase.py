POINT:pay attention to the case sensitive.
POINT:before to connect to database,you should initiate mysql.
how to connect to mysql:
import mysql.connector
mydb = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "",
    database = "mynewdb"
)




print(mydb)
# output:<mysql.connector.connection_cext.CMySQLConnection object at 0x0000022D34E65550>

creating a database:
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE mynewdb")
you cannot use space in the name of database,instead use:(-)

check the existance of database:
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
 
for object in mycursor:
    print(object)
# output:
# ('information_schema',)
# ('mynewdb',)
# ('mysql',)
# ('performance_schema',)
# ('phpmyadmin',)
# ('test',)
creating a table:
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers(name VARCHAR(255),address VARCHAR(255))")
mycursor.execute("SHOW TABLES")
for tables in mycursor:
    print(tables)
# output:
# ('customers',)
# ('customers2',)

creating primary key:
primary key: when creating table ,each table gets a primary key(id)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers2 (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),address VARCHAR(255))")
if table exists without id,do this:
mycursor.execute("ALTER TABLE CUSTOMERS2 ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

fill the tables with INSERT INTO:
mycusror = mydb.cursor()
mycusror.execute("INSERT INTO customers2 (name,address) VALUES ('jennifer','france')")
mydb.commit()
print(mycusror.rowcount,"record inserted,ID:",mycusror.lastrowid)
# output:1 record inserted,ID: 8

getting what is in tables with SELECT:
mycursor = mydb.cursor()
mycursor.execute("SELECT name , address FROM customers")
result = mycursor.fetchall()
for i in result:
    print(i)
# output:
# ('jake', 'ARIZONA')
# ('jake', 'ARIZONA')
# ('john', 'ARIZONA')
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
result = mycursor.fetchall()
for tables in result:
    print(tables)
# output:
# ('jake', 'ARIZONA', 6)
# ('jake', 'ARIZONA', 7)
# ('john', 'ARIZONA', 8)

return the first row of the result with fetchone():
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
result = mycursor.fetchone()
print(result)
# output:('jake', 'ARIZONA', 6)

SELECT with a filter:
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers WHERE name = 'john'")
result = mycursor.fetchall()
print(result)
# output:[('john', 'ARIZONA', 8)]

to prevent sql injection,use placeholders:
mycursor = mydb.cursor()
name = 'john',
mycursor.execute("SELECT * FROM customers WHERE name = %s",name)
result = mycursor.fetchall()
print(result)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers WHERE id = '9' ")
result = mycursor.fetchall()
print(result)
# output:[('AUSTIN', 'MERILAND', 9)]

mycursor = mydb.cursor()
mycursor.execute("SELECT id FROM customers ")
result = mycursor.fetchall()
print(result)
# output:[(6,), (7,), (8,), (9,)]

SORTING THE RESULT:
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers ORDER BY name ")
result = mycursor.fetchall()
print(result)
output:[('AUSTIN', 'MERILAND', 9), ('jake', 'ARIZONA', 6), ('jake', 'ARIZONA', 7), ('john', 'ARIZONA', 8), ('sarah', 'hilton', 11)]

ORDER BY DESC:
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers ORDER BY name DESC ")
result = mycursor.fetchall()
for tables in result:
  print(tables)
# output:
# ('sarah', 'hilton', 11)
# ('john', 'ARIZONA', 8)
# ('jake', 'ARIZONA', 6)
# ('jake', 'ARIZONA', 7)
# ('AUSTIN', 'MERILAND', 9)

how to delete records:
mycursor = mydb.cursor()
mycursor.execute("DELETE FROM customers WHERE name = 'HILLARY'")
mydb.commit()
print(mycursor.rowcount,"record(s) deleted!")
# output:1 record(s) deleted!

 how to drop table:
 mycursor = mydb.cursor()
 mycursor.execute("DROP TABLE customers2")

 mycursor = mydb.cursor()
 mycursor.execute("DROP TABLE IF EXISTS customers ")

UPDATE TABLE:
mycursor = mydb.cursor()
mycursor.execute("UPDATE customers SET name = 'ali' WHERE name= 'aras' ")
mydb.commit()
print(mycursor.rowcount,"record(s) affected.")
# output:1 record(s) affected.

limit the number of records:
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 2")
result = mycursor.fetchall()
for limit in result:
    print(limit)
# output:
# (1, 'john', 'ARIZONA')
# (2, 'suzi', 'nebraska')

OFFSET:keyword for starting from a specified record.
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers LIMIT 2 OFFSET 0")
result = mycursor.fetchall()
for limit in result:
    print(limit)
# output:
# (1, 'john', 'ARIZONA')
# (2, 'suzi', 'nebraska')

