import sqlite3
def setupdbAndTable():
    with sqlite3.connect("UserData.db") as db:
        cursor = db.cursor()
        sql = """
                CREATE TABLE IF NOT EXISTS UserNamePassword
                (UserID INTEGER PRIMARY KEY,
                Username TEXT,
                Password TEXT);
              """
        cursor.execute(sql)
def createPermissionsTable():
    with sqlite3.connect("UserData.db") as db:
        cursor = db.cursor()
        sql = """
                CREATE TABLE IF NOT EXISTS Permissions
                (PermissionsID INTEGER PRIMARY KEY,
                UserID INTEGER,
                Permissions TEXT,
                FOREIGN KEY(UserID) REFERENCES UserNamePassword(UserID));
              """
        cursor.execute(sql)
def setupCipTable():
    with sqlite3.connect("UserData.db") as db:
        cursor = db.cursor()
        sql = """
                CREATE TABLE IF NOT EXISTS CipherData
                (CipherID INTEGER PRIMARY KEY,
                UserID INTEGER,
                CipherText TEXT,
                CipherType TEXT,
                RVal INT,
                FOREIGN KEY(UserID) REFERENCES UserNamePassword(UserID));
              """
        cursor.execute(sql)
def setupAccoAcceTable():
    with sqlite3.connect("UserData.db") as db:
        cursor = db.cursor()
        sql = """
                CREATE TABLE IF NOT EXISTS AccountData
                (AccID INTEGER PRIMARY KEY,
                UserID INTEGER,
                MMN TEXT,
                FPN TEXT,
                PIN INT,
                FOREIGN KEY(UserID) REFERENCES UserNamePassword(UserID));
              """
        cursor.execute(sql)

if __name__ == "__main__":

    setupdbAndTable()
    createPermissionsTable()
    setupCipTable()
    setupAccoAcceTable()
    
