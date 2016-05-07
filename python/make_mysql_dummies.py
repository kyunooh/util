import pymysql
import uuid

connection = pymysql.connect(
    user="root",
    password="",
    host="localhost",
    db="jelly_dummy",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
    autocommit=True
)

name_list = ['choi', 'hyeon', 'mook', 'kyun', 'jelly']
favor_list = ['apple', 'banana', 'melon', 'lime', 'rasberry', 'coffee']

try:
    with connection.cursors as cs:
        create_table_sql = """
        CREATE TABLE IF NOT EXIST jelly_table (
        jelly_id INT(10) PRIMARY KEY AUTO_INCREAMENT,
        jelly_name VARCHAR(150),
        jelly_favor VARCHAR(50),
        jelly_description TEXT
        )"""
        cs.execute(create_table_sql)
        print("creating table is done")
        
        for index in range(1, 10000):
            insert_sql = """
            INSERT INTO jelly_table (
            jelly_name,
            jelly_favor,
            jelly_description
            ) VALUES (%s, %s, %s)"""
            
            cs.execute(insert_sql, (
                name_list[len(name_list) % index],
                favor_list[len(favor_list) % index],
                uuid.uuid4()))
            print("index is : {}".format(index))

