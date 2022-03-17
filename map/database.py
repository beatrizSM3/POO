import sqlite3 as db


class DataBase():
    def connect(self):
        global cursor

        self.dataBase = db.connect("Database.db")
        cursor= self.dataBase.cursor()
        cursor.execute("CREATE table if not EXISTS data(Local TEXT not null unique)")

    def adicionar(self,address_save):
        self.connect()
        select=f"SELECT * FROM data"
        cursor.execute(select)
        if len(cursor.fetchall())>16:
                print("lista de endereços chegou ao limite")
        else:
            sql1=f"INSERT into data values('{address_save}')"
            cursor.execute(sql1)
            self.dataBase.commit()                            
            self.dataBase.close()

    def select(self):
        self.connect()
        values=[]
        select=f"SELECT * FROM data"
        cursor.execute(select)
        result=cursor.fetchall()
        for result in result:
            values.append(result[0])
        self.dataBase.close()
        return values

    #função delete
    #...