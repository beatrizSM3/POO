import sqlite3 as db

class DataBase():
    def connect(self):
        global cursor

        self.dataBase = db.connect("Database.db")
        cursor= self.dataBase.cursor()
        cursor.execute("CREATE table if not EXISTS data(Place TEXT not null unique)")

    def adicionar(self,address_save):
        self.connect()
        cursor.execute(f"SELECT * FROM data")
        if len(cursor.fetchall())>=15:
                print("lista de endereços chegou ao limite")
        else:
            cursor.execute(f"INSERT into data values('{address_save}')")
            self.dataBase.commit()                            
            self.dataBase.close()

    def select(self):
        self.connect()
        values=[]
        cursor.execute(f"SELECT * FROM data")
        result=cursor.fetchall()
        for result in result:
            values.append(result[0])
        self.dataBase.close()
        return values

    def delete(self, address_save):
        self.connect()
        cursor.execute(f"DELETE FROM data WHERE Place = '{address_save}'")
        self.dataBase.commit()                            
        self.dataBase.close()

