import numpy as np
import pandas as pd
import mysql.connector
from mysql.connector import Error

# Avant l'éxecution du code il faut installer les librairies : pandas, numpy, mysql-connector-python

def create_connection(host_name, user_name, user_password, db_name, db_port):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name,
            port=db_port
        )
        print("Connection to MariaDB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as e:
        print(f"The error '{e}' occurred")


def convert_types(row):
    converted_row = []
    for item in row:
        if pd.isna(item):
            converted_row.append(None)
        elif isinstance(item, np.int64):
            converted_row.append(int(item))
        elif isinstance(item, np.float64):
            converted_row.append(float(item))
        else:
            converted_row.append(item)
    return tuple(converted_row)


def insert_into_table(connection, table, dataframe, columns=None):
    cursor = connection.cursor()
    for i, row in dataframe.iterrows():
        row = row[columns] if columns else row
        converted_row = convert_types(row)
        placeholders = ', '.join(['%s'] * len(converted_row))
        columns_placeholder = ', '.join(columns)

        # Construct the ON DUPLICATE KEY UPDATE clause
        on_duplicate_key_update_clause = ', '.join([f"{col}=VALUES({col})" for col in columns])

        query = f"""
        INSERT INTO {table} ({columns_placeholder}) 
        VALUES ({placeholders})
        ON DUPLICATE KEY UPDATE {on_duplicate_key_update_clause}
        """

        cursor.execute(query, converted_row)
    connection.commit()


# Connect to the database
connection = create_connection("localhost", "jo", "jo", "jo", 3311)

# Drop tables if they exist
drop_table_athletes = "DROP TABLE IF EXISTS athletes;"
drop_table_results = "DROP TABLE IF EXISTS results;"
drop_table_medals = "DROP TABLE IF EXISTS medals;"

execute_query(connection, drop_table_athletes)
execute_query(connection, drop_table_results)
execute_query(connection, drop_table_medals)

# Read data from the combined Excel files
df_athletes = pd.read_excel('../data/olympic_athletes.xlsx')
df_medals = pd.read_excel('../data/olympic_medals.xlsx')
df_results = pd.read_excel('../data/olympic_results.xlsx')

# Create tables
create_table_athletes = """
CREATE TABLE athletes(
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    athlete_full_name VARCHAR(100) NULL,
    games_participations INTEGER NULL,
    first_game VARCHAR(100) NULL,
    athlete_year_birth INTEGER NULL,
    athlete_medals VARCHAR(100) NULL
);
"""
create_table_medals = """
CREATE TABLE medals (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    discipline_title VARCHAR(100) NULL,
    slug_game VARCHAR(100) NULL,
    event_title VARCHAR(100) NULL,
    event_gender VARCHAR(100) NULL,
    medal_type VARCHAR(100) NULL,
    participant_type VARCHAR(100) NULL,
    athlete_full_name VARCHAR(100) NULL,
    country_name VARCHAR(100) NULL
);
"""
create_table_results = """
CREATE TABLE results (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    discipline_title VARCHAR(500) NULL,
    event_title VARCHAR(500) NULL,
    rank_position VARCHAR(500) NULL,
    country_name VARCHAR(500) NULL,
    athlete_full_name VARCHAR(500) NULL
);
"""

execute_query(connection, create_table_athletes)
execute_query(connection, create_table_medals)
execute_query(connection, create_table_results)


# Insert data into tables
insert_into_table(connection, 'athletes', df_athletes,
                  ['athlete_full_name', 'games_participations', 'first_game', 'athlete_year_birth',
                   'athlete_medals'])
print('Done for athletes!')
insert_into_table(connection, 'medals', df_medals,
                  ['discipline_title', 'slug_game', 'event_title', 'event_gender', 'medal_type',
                   'participant_type', 'athlete_full_name', 'country_name'])
print('Done for medals!')
insert_into_table(connection, 'results', df_results,
                  ['discipline_title', 'event_title',
                   'rank_position', 'country_name', 'athlete_full_name'])
print('Done for results!')
# Close the connection
connection.close()
