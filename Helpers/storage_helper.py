import mysql.connector
from mysql.connector import Error
import pandas as pd
import os

pw = os.environ['pw']

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as e:
        print(f"Error: '{e}'")

    return connection


def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successflly")
    except Error as e:
        print(f"Error: '{e}'")


def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as e:
        print(f"Error: '{e}'")

    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}")

def get_all_urls():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=pw,
        database="source"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT url FROM source")

    myresult = mycursor.fetchall()

    return myresult



create_source_table = """
CREATE TABLE source (
    id MEDIUMINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(1000) NOT NULL,
    type VARCHAR(1000) NOT NULL,
    url VARCHAR(1000) NOT NULL,
    description TEXT NOT NULL,
    countries VARCHAR(1000),
    employees INT,
    capterra_review_count INT,
    capterra_review_rating FLOAT,
    pricing_options INT ,
    user_count INT,
    logo_filepath VARCHAR(1000),
    PRIMARY KEY (id)
    );
"""

drop_source = """
DROP TABLE source
"""

alter_source_columns = """
ALTER TABLE source ALTER COLUMN name TEXT;
"""
"""
ALTER TABLE source ALTER COLUMN url VARCHAR (1000)
ALTER TABLE source ALTER COLUMN description VARCHAR (10000)
ALTER TABLE source ALTER COLUMN logo_filepath VARCHAR (1000);
"""


create_operator_table = """
CREATE TABLE operator (
    operator_id INT IDENTITY(1,1),
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    linkedin_profile_url VARCHAR(40) NOT NULL,
    email_1 VARCHAR(40) NOT NULL,
    email_2 VARCHAR (40) NOT NULL,
    phone_1 VARCHAR (40) NOT NULL,
    phone_2 VARCHAR (40) NOT NULL
);
"""


add_column_source = """
ALTER TABLE source
ADD operator INT
"""

add_operator_relationship = """
ALTER TABLE source
ADD FOREIGN KEY(operator)
REFERENCES operator(operator_id)
ON DELETE SET NULL;
"""



connection = create_db_connection("localhost", "root", pw, "source")
