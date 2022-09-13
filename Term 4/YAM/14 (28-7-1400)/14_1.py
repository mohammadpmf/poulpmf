import mysql.connector
try:
    mydb = mysql.connector.connect(host="localhost", user='root', password = 'root')
    print('Connected succesfully.')
    mycursor = mydb.cursor()
    # mycursor.execute("Show databases;")
    # mycursor.execute("SELECT * FROM jjjjj.products")
    my_command = "UPDATE jjjjj.products SET product_remained = '20' WHERE id_products = '1';"
    mycursor.execute(my_command)
    mydb.commit()
    # print(mycursor.fetchall())
# except ConnectionError as err:
#     print(err)
# except IndexError:
#     print('Index error')
except:
    print ('Unknown error')