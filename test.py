import psycopg2

conn = psycopg2.connect('dbname=test user=postgres password=1234')
cursor = conn.cursor()

# Need to drop vehicles first before drivers as vehicles has a foreign key that refernces drivers
cursor.execute('DROP TABLE IF EXISTS vehicles;')
cursor.execute('DROP TABLE IF EXISTS drivers;')

cursor.execute(
    '''
    CREATE TABLE drivers (
        id SERIAL PRIMARY KEY,
        first_name VARCHAR(100),
        last_name VARCHAR(100)
    );

    CREATE TABLE vehicles (
        ID serial primary key,
        make varchar(100),
        model varchar(100),
        driver_id integer references drivers(id)
    );
    '''
)

cursor.execute('''
    INSERT INTO drivers (first_name, last_name) VALUES ('amy', 'hua');
    INSERT INTO drivers (first_name, last_name) VALUES ('john', 'doe');
    INSERT INTO drivers (first_name, last_name) VALUES ('lisa', 'smith');
    INSERT INTO drivers (first_name, last_name) VALUES ('michael', 'brown');
    INSERT INTO drivers (first_name, last_name) VALUES ('emily', 'davis');
    INSERT INTO drivers (first_name, last_name) VALUES ('Ellson', 'Phang');
    INSERT INTO drivers (first_name, last_name) VALUES ('amy', 'wellington');

    INSERT INTO vehicles (make, model, driver_id) VALUES ('Toyota', 'Corolla', 1); 
    INSERT INTO vehicles (make, model, driver_id) VALUES ('Honda', 'Civic', 2);    
    INSERT INTO vehicles (make, model, driver_id) VALUES ('Ford', 'Focus', 3);     
    INSERT INTO vehicles (make, model, driver_id) VALUES ('Ford', 'Territory', 3); 
    INSERT INTO vehicles (make, model, driver_id) VALUES ('Toyota', 'Prado', 4); 
    INSERT INTO vehicles (make, model, driver_id) VALUES ('Nissan', 'GTR', 6);
''')

cursor.execute('''
    INSERT INTO vehicles (make, model, driver_id) VALUES ('BMW', 'IX3', 7);
''')
conn.commit()  # Don't forget to commit the transaction

# adding multiple values
cursor.execute(
    '''INSERT INTO drivers (first_name, last_name) VALUES 
    ('sarah', 'connor'),
    ('richard','branson');'''
)

# passing tuple as 2nd argument
cursor.execute(
    '''INSERT INTO vehicles (make, model, driver_id) VALUES (%s, %s, %s);''',('Tesla', 'Model 3', 8)
)

# using string parameters %(foo)s by passing dictionary instead
dict_parameters_sql= '''INSERT INTO vehicles (make, model, driver_id) VALUES (%(make)s, %(model)s, %(driver_id)s);'''
dict_parameters_data={'make': 'Mazda', 'model': 'CX-5', 'driver_id': 3}
cursor.execute(dict_parameters_sql, dict_parameters_data)

# cursor.execute('''
#     SELECT * 
#     from drivers
#     INNER JOIN vehicles ON drivers.id=vehicles.driver_id
#     WHERE drivers.first_name='amy';
# ''')

cursor.execute(
    '''SELECT * FROM vehicles;
'''
)

# result_many=cursor.fetchmany(3)
# print(f"result_many: {result_many}")

result_one=cursor.fetchone()
print(f"fetch_one: {result_one}")

result_all=cursor.fetchall()
# print(result_all[1][1])
print(f"result_all: {result_all}")



cursor.close()
conn.close()