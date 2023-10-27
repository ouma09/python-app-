import tkinter as tk
import mysql.connector as mysql

db_connection = mysql.connect(
    host="localhost",
    port=3306,
    user="root",
    password="hoshi",
    database="calculations",
    auth_plugin='mysql_native_password'
)
cursor = db_connection.cursor()

def add_numbers():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result_value = num1 + num2
    result.set(f"The sum of {num1} and {num2} is {result_value}")

    # Store the result in the database
    insert_query = "INSERT INTO calculation (num1, num2, result) VALUES (%s, %s, %s)"
    values = (num1, num2, result_value)
    cursor.execute(insert_query, values)
    db_connection.commit()  # Commit the changes to the database

# Initialize the MySQL connection


window = tk.Tk()
window.title("Simple Calculator")
window.configure(bg="lightgray")

label_num1 = tk.Label(window, text="Enter the first number:", bg="lightgray")
label_num1.grid(row=0, column=0)
entry_num1 = tk.Entry(window, font=("Arial", 12))
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(window, text="Enter the second number:", bg="lightgray")
label_num2.grid(row=1, column=0)
entry_num2 = tk.Entry(window, font=("Arial", 12))
entry_num2.grid(row=1, column=1)

calculate_button = tk.Button(window, text="Calculate", command=add_numbers, bg="green", fg="white", font=("Arial", 12), relief="raised")
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result = tk.StringVar()
result_label = tk.Label(window, textvariable=result, bg="lightgray", font=("Arial", 14), fg="blue")
result_label.grid(row=3, column=0, columnspan=2)

window.mainloop()

# Close the database connection when the application is closed
db_connection.close()
