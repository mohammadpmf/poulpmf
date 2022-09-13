import mysql.connector

class Connector():
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(host="localhost", user='root', password = 'root')
            self.is_connected = True
        except:
            self.is_connected = False
    def connect_to_selected_db(self, db_name):
        if self.is_connected:
            try:
                self.mydb = mysql.connector.connect(host="localhost", user='root',
                                         password = 'root', database = db_name)
                self.db_name = db_name
                return f'connected to {db_name} succecfully!'
            except:
                self.db_name = None
                return f'connection to {db_name} failed!!!'
        else:
            self.db_name = None
            return 'connection is not established'
    def get_tbl_info(self, tbl_name):
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute(f"SELECT * FROM {self.db_name}.{tbl_name}")
            return self.mycursor.fetchall()
            # # mycursor.execute("Show databases;")
            # my_command = "UPDATE jjjjj.products SET product_remained = '20' WHERE id_products = '1';"
            # mycursor.execute(my_command)
            # mydb.commit()
