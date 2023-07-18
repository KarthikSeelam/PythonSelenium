import mysql

db_host = '10.0.1.205'
db_port = 3306
db_user = 'root'
db_password = 'admin123'
db_name = 'peduba_demo'

connection = mysql.connector.connect(
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_password,
    database=db_name
)

cursor = connection.cursor()

# Insert the flight details into the MySQL database
for flight in data_list:
    flight_values = (
        flight['Flight Name'],
        flight['Departure Time'],
        flight['Source Location'],
        flight['Arrival Time'],
        flight['Destination'],
        flight['Ticket Price']
    )
    query = "INSERT INTO flights (flight_name, departure_time, source_location, arrival_time, destination, ticket_price) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, flight_values)
    connection.commit()

# Close the cursor and the database connection
cursor.close()
connection.close()

driver.quit()
