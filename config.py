import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='sql102.infinityfree.com',  # Your MySQL hostname
        user='if0_37546575',             # Your MySQL username
        password='2002Yad25',            # Your MySQL password
        database='if0_37546575_educational_portal',  # Your MySQL database name
        port=3306  # Optional, default MySQL port
    )