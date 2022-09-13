import mysql.connector

class Connector():
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(host="localhost", user='root', password = 'root')
            self.is_connected = True
        except:
            self.is_connected = False

            # mycursor = mydb.cursor()
            # # mycursor.execute("Show databases;")
            # # mycursor.execute("SELECT * FROM jjjjj.products")
            # my_command = "UPDATE jjjjj.products SET product_remained = '20' WHERE id_products = '1';"
            # mycursor.execute(my_command)
            # mydb.commit()
            # # print(mycursor.fetchall())
