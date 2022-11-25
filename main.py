# Hello
import mysql.connector as connector

connection = connector.connect(
    host="localhost",
    user="nara",
    password="nara",
    database="bakery"
)


db = connection.cursor(buffered=True)


db.execute("SELECT * from item_records;")


# print(items)
# for item in items:
#     for col in item:
#         print(" | " + str(col), end=" ")
#     print()
# [
#     (1, 'Jalebi', 7, datetime.date(2022, 11, 30), 10),
#     (2, 'Ladoo', 10, datetime.date(2022, 11, 30), 7)
# ]


items = {
    "1": {
        "item_name": "Ladoo",
        "price": 10,
        "exp_date": "2022-12-30"
    },
    "2": {
        "item_name": "Jalebi",
        "price": 7,
        "exp_date": "2022-12-30"
    },
    "3": {
        "item_name": "Samosa",
        "price": 12,
        "exp_date": "2022-12-30"

    },
    "4": {
        "item_name": "Chips",
        "price": 70,
        "exp_date": "2022-12-30"
    }
}


# Main


def insert(choice):
    try:
        quantity = input("Enter the number of items: ")

        data = {
            'item_name': items[choice]["item_name"],
            'price': items[choice]["price"],
            'exp_date': items[choice]["exp_date"],
            "quan": int(quantity)
        }

        query = "INSERT INTO item_records (item_name, price, exp_date, quan) VALUES(%(item_name)s, %(price)s, %(exp_date)s, %(quan)s)"

        db.execute(query, data)

        connection.commit()

        print(db.rowcount, " was inserted.")

        total = data["quan"] * data["price"]

        print("Success!" + " Your Total is " + str(total))
        print("You chose " + items[choice]
              ["item_name"] + " Happy eating !!!! : ))))")

    except:
        print('An exception occurred please try again!')
        print()
        insert(choice)


def main():
    print("Welcome to Vinayak Bakery...")
    print("Please Enter a valid Item to purchase: ")

    print("1. Ladoo")
    print("2. Jalebi")
    print("3. Samosa")
    print("4. Chips")
    print("Enter e to exit")
    print("------------------")

    ans = input("Choice: ")

    if ans.lower() == "e":
        print("Bye!")
        return

    elif ans == "1" or ans == '2' or ans == '3' or ans == '4':
        insert(ans)

    else:
        print("Please Enter a valid input from 1-4 or [E/e] to exit!")
        print()
        main()


main()
