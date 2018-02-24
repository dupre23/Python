import cx_Oracle, logging

class SqlClass():

    def __init__(self, username, password):
        self.username = username
        self.password = password
        #implement logging

    def __enter__(self):
        self.connectToDb()

    def __exit__(self, type, value, traceback):
        self.disconnectFromDb()

    def connectToDb(self):
        try:
            self.db_conn = cx_Oracle.connect("{0}/{1}@//localhost:1521/xe".format(self.username, self.password))
            self.db_cursor = self.db_conn.cursor()
        except cx_Oracle.DatabaseError as e:
            print("Connection could not be completed: ", e)
        else:
            print("Connected successfully to database!")

    def disconnectFromDb(self):
        try:
            self.db_conn.close()
            print("Disconnected from database!")
        except AttributeError:
            print ("Connection could not be closed!")