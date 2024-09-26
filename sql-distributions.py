import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect('student_adaptivity.db')

# Read the SQL file
with open('distributions.sql', 'r') as file:
    sql_queries = [line.strip() for line in file if line.strip()]  # Read and strip each line

# Execute each query and plot the results
for query in sql_queries:
    df = pd.read_sql_query(query, conn)
    df.plot(kind='bar', x=df.columns[0], y='count', legend=False)
    plt.title(df.columns[0] + ' Distribution')
    plt.ylabel('Count')
    plt.xlabel(df.columns[0])
    plt.show()

# Close the database connection
conn.close()
