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
        self.tbl_name = tbl_name
        return self.mycursor.fetchall()
    def insert_to_tbl(self, info):
        self.mycursor = self.mydb.cursor()
        print(info)
        command = f"INSERT INTO {self.db_name}.{self.tbl_name} (`product_name`, `product_brand`, `product_remained`, `product_price`) VALUES {info};"
        print(command)
        self.mycursor.execute(command)
        self.mydb.commit()
            # # mycursor.execute("Show databases;")
            # my_command = "UPDATE jjjjj.products SET product_remained = '20' WHERE id_products = '1';"
            # mycursor.execute(my_command)
    def search_data(self, tbl_name, column_name, txt):
            self.mycursor = self.mydb.cursor()
            self.mycursor.execute(f"SELECT * FROM {self.db_name}.{tbl_name} WHERE {column_name}='{txt}'")
            self.tbl_name = tbl_name
            return self.mycursor.fetchall()
    def update_tbl(self, id, name, brand, remained, price, tbl_name):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(f"UPDATE {self.db_name}.{tbl_name} SET product_name='{name}', product_brand='{brand}', product_remained={remained}, product_price = '{price}' WHERE id_products={id}")

    def delete_data(self, tbl_name, id):
        self.mycursor = self.mydb.cursor()
        self.mycursor.execute(f"Delete From {tbl_name} WHERE id_products={id}")

        
