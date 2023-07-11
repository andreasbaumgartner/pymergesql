import csv
import sqlite3


def export_csv_to_sqlite(csv_file, sqlite_file, table_name):
    # Connect to SQLite database
    conn = sqlite3.connect(sqlite_file)
    cursor = conn.cursor()

    # Create table in the SQLite database
    create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} "
    create_table_query += "(id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
    cursor.execute(create_table_query)

    # Read data from CSV and insert into the SQLite table
    with open(csv_file, 'r') as file:
        csv_data = csv.reader(file)
        next(csv_data)  # Skip header row

        for row in csv_data:
            insert_query = f"INSERT INTO {table_name} (name, age) VALUES (?, ?)"
            cursor.execute(insert_query, (row[0], int(row[1])))

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print("Data export completed successfully.")


if __name__ == "__main__":
    # Usage example
    csv_file_path = 'data.csv'
    sqlite_file_path = 'database.sqlite3'
    table_name = 'person'
    export_csv_to_sqlite(csv_file_path, sqlite_file_path, table_name)
