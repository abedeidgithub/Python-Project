import sqlite3


def insert_record(db, row):
    db.execute('INSERT INTO USER(USER_NAME, PASSWORD) VALUES (?,?)', (row['USER_NAME'], row['PASSWORD']))
    db.commit()

def insert_total(db, row):
    db.execute('INSERT INTO TOTAL(TOTAL_NAME, TOTAL_PRICE) VALUES (?,?)',(row['TOTAL_NAME'], row['TOTAL_PRICE']))
    db.commit()
def query_total(db):
    cursor = db.execute('SELECT * FROM TOTAL ORDER BY TOTAL_ID')
    i=""
    for row in cursor:
        i+=str('{}  {}  {}'.format(row['TOTAL_ID'], row['TOTAL_NAME'], row['TOTAL_PRICE']))+"\n"
    return i
def insert_record_meal(db, row):
    db.execute('INSERT INTO MEAL(MEAL_NAME, PRICE) VALUES (?,?)', (row['MEAL_NAME'], row['PRICE']))
    db.commit()


def query_MEAL(db):
    i = ""
    cursor = db.execute('SELECT * FROM MEAL ORDER BY MEAL_ID')
    for row in cursor:
        i += str(('{}'.format(row['MEAL_ID'])) + "\t" + ('{}'.format(row['MEAL_NAME'])).ljust(17, ' ') + "\t" + (
            '{}'.format(row['PRICE'])) + "\n")
    return i


def query_ORDER_(db):
    i = ""
    cursor = db.execute('SELECT TOTAL_ID ,TOTAL_PRICE FROM TOTAL ORDER BY TOTAL_ID')
    for row in cursor:
        i+=str('{}  {} '.format(row['TOTAL_ID'], row['TOTAL_PRICE']))+"\n"
    print(i)
    return i



def query(db):
    cursor = db.execute('SELECT * FROM USER ORDER BY USER_ID')
    for row in cursor:
        print('{}  {}  {}'.format(row['USER_ID'], row['USER_NAME'], row['PASSWORD']))


def delete(db, username):
    db.execute('DELETE FROM USER WHERE USER_NAME = ?', (username,))
    db.commit()


def update(db, row):
    db.execute('UPDATE USER SET USER_NAME = ? , PASSWORD = ?  WHERE USER_ID = ? ',
               (row['USER_NAME'], row['PASSWORD'], row['USER_ID']))
    db.commit()


def update_MEAL(db, row):
    db.execute('UPDATE MEAL SET PRICE = ?   WHERE MEAL_ID = ? ',
               (row['PRICE'], row['MEAL_ID']))
    db.commit()


def select_item(db, row):
    cursor = db.execute('select * from USER where  USER_NAME = ? and PASSWORD = ?', (row['USER_NAME'], row['PASSWORD']))
    for row in cursor:
        print('{}  {}  {}'.format(row['USER_ID'], row['USER_NAME'], row['PASSWORD']))
        return (row['USER_ID'])
        break

    db.commit
    return 0


def select(db, row):
    cursor = db.execute('SELECT PRICE FROM MEAL WHERE  MEAL_NAME = ? ', (row['MEAL_NAME'],))
    for row in cursor:
        return ('{}'.format(row['PRICE']))

    db.commit()

def select_MEAL_ID(db, row):
    cursor = db.execute('SELECT MEAL_ID FROM MEAL WHERE  MEAL_NAME = ? ', (row['MEAL_NAME'],))
    for row in cursor:
        return ('{}'.format(row['MEAL_ID']))

    db.commit()


db = sqlite3.connect('db')
db.row_factory = sqlite3.Row

# db.execute('drop table if exists TOTAL')
db.execute(
    'CREATE TABLE IF NOT EXISTS USER (USER_ID INTEGER PRIMARY KEY AUTOINCREMENT , USER_NAME TEXT , PASSWORD TEXT)')
db.execute(
    'CREATE TABLE IF NOT EXISTS MEAL (MEAL_ID INTEGER PRIMARY KEY AUTOINCREMENT , MEAL_NAME TEXT , PRICE DOUBLE)')
db.execute('CREATE TABLE IF NOT EXISTS TOTAL(TOTAL_ID INTEGER PRIMARY KEY AUTOINCREMENT, TOTAL_NAME TEXT, TOTAL_PRICE DOUBLE)')

# query_MEAL(db)
#
# insert_total(db,dict(TOTAL_NAME= 'bbbbb',TOTAL_PRICE= '266'))
# query_total(db)


#
# query(db)
# query(db)
