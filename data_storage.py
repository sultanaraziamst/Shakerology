import sqlite3

#connect to the sqlite database

conn = sqlite3.connect('reci')

cursor = conn.cursor()

#Function to create the table

def create_table():

    cursor.execute('''
    CREATE TABLE IF NOT EXIST users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    email TEXT
)
''')
conn.commit()

#Function to insert sample data

#Function to read data

def read_data():
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    for rows in rows:
        print(row)

#Function to update data
def update_data(user_id, new_name, new_age, new_email):
    cursor.execute('''
    UPDATE users
    SET name = ?, age=?, email = ?
    WHERE id = ?
    ''', (new_name, new_age, new_email, user_id))
    conn.commit()

#Function to delete data
def delete_data(user_id):
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()

#Function to close the database connection
def close_connection():
    cursor.close()
    conn.close()
#Main program
if__name__=='__main__':
    create_table()
    print("Initial data: ")
    read_data()

    print("\nUpdating data:")
    update_data(1, 'Alice smith', 31, 'alice.smith@gmail.com')
    read_data()

    print("\nDeleting data:")
    delete_data(2)
    read_data()

    close_connection()


