from mysql import connector

try:
    mydb = connector.connect(host="localhost", user='root', password = 'root')
    print('Connected succesfully.')
# except ConnectionError as err:
#     print(err)
# except IndexError:
#     print('Index error')
except:
    print ('Unknown error')

if mydb is not None:
    mycursor = mydb.cursor()
    # mycursor.execute("Show databases;")
    mycursor.execute("SELECT * FROM jjjjj.products")
    print(mycursor.fetchall())
