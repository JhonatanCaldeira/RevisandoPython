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
        cursor.execute(
            f'CREATE TABLE IF NOT EXISTS {TABLE_NAME} ('
            'id INT NOT NULL AUTO_INCREMENT, '
            'name VARCHAR(100) NOT NULL, '
            'age INT NOT NULL, '
            'PRIMARY KEY (id)'
            ')'
        )

        cursor.execute(f'TRUNCATE TABLE {TABLE_NAME}')
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%s, %s)'
        )

        data = ('Jhonatan', 31)
        cursor.execute(sql, data)
    connection.commit()

    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} '
            '(name, age) '
            'VALUES '
            '(%(nome)s, %(idade)s)'
        )

        data = [
            {"nome": "Brizzida", "idade": 32},
            {"nome": "Cadu", "idade": 28},
            {"nome": "Luciana", "idade": 53},
            {"nome": "Bruno", "idade": 35},
        ]
        cursor.executemany(sql, data)
    connection.commit()
