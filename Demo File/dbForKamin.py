db_host = '10.0.1.205'
db_port = 3306
db_user = 'MySqlUser'
db_password = 'Admin@1234'
db_name = 'kaminhealth_test'

connection = mysql.connector.connect(
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_password,
    database=db_name
)

cursor = connection.cursor()
print("Connection Successful")
for _, row in df.iterrows():
    facility_name = row['Facility Name']
    facility_code = row['Facility Code']
    city = row['City']
    state = row['State']
    zip_code = row['Zip Code']
    pos = row['POS']

    insert_query = "INSERT INTO facilityMaster (facility_name, facility_code, city, state, zip_code, POS) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (facility_name, facility_code, city, state, zip_code, pos))

connection.commit()
connection.close()

print("Data inserted into MySQL successfully!")