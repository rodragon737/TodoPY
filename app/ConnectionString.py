import pyodbc

SERVER = 'RR-PC'
DATABASE = 'PyApp'
USERNAME = 'rood'
PASSWORD = 'roro1234'


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

# for r in get_users:
#     print(f"{r.name}\t{r.passe}")