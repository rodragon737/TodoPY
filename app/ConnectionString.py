import pyodbc

SERVER = 'nombreServer'
DATABASE = 'laDB'
USERNAME = 'userAca'
PASSWORD = 'acaPassword'


connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

conn = pyodbc.connect(connectionString)

cursor = conn.cursor()

list_users = """
SELECT * FROM dbo.users
ORDER BY 
name DESC;
"""

cursor.execute(list_users)

get_users = cursor.fetchall()