# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd


# STEP 1B
# Connect to the database
conn = sqlite3.connect("data.sqlite")
cursor = conn.cursor()


# Step 2: First five employees
df_first_five = pd.read_sql("SELECT employeeNumber, lastName FROM Employees", conn)

# Step 3: Reverse order
df_five_reverse = pd.read_sql("SELECT lastName, employeeNumber FROM Employees ORDER BY employeeNumber DESC", conn)

# Step 4: Aliasing
df_alias = pd.read_sql("SELECT employeeNumber AS ID, firstName AS Name FROM Employees", conn)

# Step 5: CASE function
df_executive = pd.read_sql("""
SELECT firstName, lastName,
       CASE WHEN jobTitle LIKE '%Manager%' THEN 'Manager'
            ELSE 'Staff'
       END AS role
FROM Employees
""", conn)


# Step 6: String function
df_name_length = pd.read_sql("SELECT lastName, LENGTH(lastName) AS name_length FROM Employees", conn)
# Step 7: Short title
df_short_title = pd.read_sql("SELECT jobTitle, SUBSTR(jobTitle, 1, 2) AS short_title FROM Employees", conn)

# Step 8: Numeric function
sum_total_price = pd.read_sql(
    "SELECT SUM(CAST(quantityOrdered * priceEach AS INT)) AS total FROM OrderDetails",
    conn
).values[0]




# Step 9: Date parts
df_day_month_year = pd.read_sql("""
SELECT orderDate,
       strftime('%d', orderDate) AS day,
       strftime('%m', orderDate) AS month,
       strftime('%Y', orderDate) AS year
FROM Orders
""", conn)


conn.close()
