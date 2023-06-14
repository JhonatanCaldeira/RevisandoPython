import os
import pymysql
import dotenv

dotenv.load_dotenv()

TABLE_NAME = 'customers'

connection = pymysql.connect(
    host=os.environ['MYSQL_HOST'],
    user=os.environ['MYSQL_USER'],
    passwd=os.environ['MYSQL_PASSWORD'],
    database=os.environ['MYSQL_DATABASE']
)

with connection:
    with connection.cursor() as cursor:
        sql = (
            f'SELECT name, age from {TABLE_NAME} '
            'WHERE age BETWEEN %s AND %s'
        )
        cursor.execute(sql, (30, 50))

        for row in cursor.fetchall():
            print(row)
