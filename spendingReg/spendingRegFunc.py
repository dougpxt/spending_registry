import sqlite3 as sq

#

def conectar():
    conn=sq.connect("spendingSQL.db")
    cursor = conn.cursor()
    return conn, cursor

def createTable():
    conn, cursor=conectar()
    cursor.execute("""CREATE TABLE  IF NOT EXISTS spendingReg(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name TEXT not null,
    quant INTEGER,
    seller TEXT,
    value REAL NOT NULL,
    date TEXT NOT NULL
    )
    """)
    conn.commit()

def addBuyedItems(name, quant, seller, value, date):
    createTable()
    conn, cursor = conectar()
    cursor.execute("""INSERT INTO spendingReg (name, quant, seller, value, date)
    values(?,?,?,?,?)
    """,(name, quant, seller, value, date))
    conn.commit()
    
def listTable():
    conn, cursor = conectar()
    cursor.execute("""SELECT * FROM spendingReg
    """)
    conn.commit()
    items = cursor.fetchall()
    return items

def delBuyedItems(id):
    conn, cursor = conectar()
    cursor.execute(''' DELETE FROM spendingReg WHERE id=?''',
                   (id,))
    conn.commit()