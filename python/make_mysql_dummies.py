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


with connection.cursor() as cs:
    create_table_sql = """
        CREATE TABLE IF NOT EXISTS jelly_table (
        jelly_id INT(10) PRIMARY KEY AUTO_INCREMENT,
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
                name_list[index % len(name_list)],
                favor_list[index % len(favor_list)],
                str(uuid.uuid4())))
        print("index is : {}".format(index))

    
