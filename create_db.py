# Hello
import mysql.connector as connector

user = "nara"
password = "nara"

connection = connector.connect(
    host="localhost",
    user=user,
    password=password,
)


db = connection.cursor()


db.execute("CREATE DATABASE bakery;")

db.execute("use bakery")
db.execute("CREATE TABLE item_records(item_no INT PRIMARY KEY AUTO_INCREMENT, item_name VARCHAR(255), price INT, exp_date DATE, quan INT);")
print("Created.. Table....")
