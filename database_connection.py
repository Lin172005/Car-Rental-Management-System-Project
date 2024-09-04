import pymysql

try:
    # Establish a connection to the database
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',  # Replace with your MySQL username
        password='123456',  # Replace with your MySQL password
        database='CarRentalDB'  # Replace with your database name
    )

    # Update an employee's salary
    try:
        with connection.cursor() as cursor:
            sql = "UPDATE Employee SET Salary = %s WHERE Emp_ID = %s"
            cursor.execute(sql, (65000.00, 1))  # Update salary for Emp_ID 1
        connection.commit()  # Save changes
        print("Salary updated successfully.")
    
    except Exception as e:
        print(f"Error during update: {e}")

finally:
    connection.close()  # Ensure the connection is closed
