import sqlite3 as sql

class DatabaseHandler:
    def __init__(self,databaseName = "appData.db"):
        self.databaseName = databaseName

    def createTables(self):
        conn = sql.connect(self.databaseName)
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                       username TEXT PRIMARY KEY NOT NULL,
                       password TEXT NOT NULL,
                       CHECK( length(password) >=8)
                       )""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
                       taskId INTEGER PRIMARY KEY AUTOINCREMENT,
                       description TEXT NOT NULL,
                       username TEXT NOT NULL,
                       CHECK (length(description)>=10),
                       FOREIGN KEY (username) REFERENCES users(username)
                       ON DELETE CASCADE
                       ON UPDATE CASCADE

                       )""")
        
        cursor.execute("PRAGMA foreign_keys = ON")

        conn.close()

    def createUser(self,username,password):
        try:
            conn = sql.connect(self.databaseName)
            cursor = conn.cursor()

            cursor.execute(""" INSERT INTO users VALUES (?, ?)""",(username,password))
            conn.commit()

            
            return True,"signup successful"
        except:
            return False, "an error occured signing up"
        finally:
            conn.close()

    def readUser(self):
        pass

    def readUserPasswordHash(self,username):
        try:
            conn = sql.connect(self.databaseName)
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM users WHERE username = ?", (username, ))
            results = cursor.fetchone()

            return True, results
        except:
            return False, "an error occured"
        finally:
            conn.close()

    def updateUserPassword(self):
        pass

    def updateUserUsername(self):
        pass

    def deleteUser(self):
        pass

    def createTask(self,description,username):
        try:
            conn = sql.connect(self.databaseName)
            cursor = conn.cursor()

            cursor.execute(""" INSERT INTO tasks (description,username)
                            VALUES 
                           (?,?)""", (description,username)) 
            conn.commit()

            return True, "Task created successfully"

        except:
            return False, "An error occured making the task."

        finally:
            conn.close()

    def readAllTasks(self,username):
        try:
            conn = sql.connect(self.databaseName)
            cursor = conn.cursor()
            cursor.execute("""SELECT taskId,description FROM tasks WHERE username = ?""",(username, ))
            results = cursor.fetchall()
            return True,results
        
        except:
            return False,[]
        finally:
            conn.close()