import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host="sql102.infinityfree.com",  
        user="if0_37546575",  
        password="2002@Yad25",  
        database="if0_37546575_educational_portal"  
    )
    return conn