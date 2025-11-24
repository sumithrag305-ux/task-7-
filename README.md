# task-7-
The goal of this task is to create a small SQLite database, store sample sales data, run SQL queries inside Python, and visualize the total revenue using a bar chart.
📄 Task 7 – Basic Sales Summary Using SQLite & Python
📌 Objective

The goal of this task is to create a small SQLite database, store sample sales data, run SQL queries inside Python, and visualize the total revenue using a bar chart.

🛠 Tools Used

Python

SQLite3

Pandas

Matplotlib

🗂 Steps Performed
1. Created SQLite Database

Connected to sales_data.db

Created a sales table with columns: product, quantity, price

2. Inserted Sample Sales Data

Added multiple records for Laptop, Mobile, and Headphones

Ensured the table starts clean by deleting old data

3. Executed SQL Query

Used SQL to calculate:

Total quantity sold (SUM(quantity))

Total revenue (SUM(quantity * price))

Grouped results by product

Query Used
SELECT 
    product,
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;

4. Loaded Results into Pandas

Displayed the summary table using print(df)

5. Visualized Revenue

Created a bar chart using Matplotlib

Saved the chart as sales_chart.png

📊 Output Generated

Total Quantity Sold per Product

Total Revenue per Product

Bar chart showing revenue for each product

📁 Files Included in Repository

task7.py — Complete Python code

sales_data.db — SQLite Database

sales_chart.png — Revenue Visualization

README.md — Description of the task

🎯 What I Learned

How to connect Python with SQLite

Creating and inserting data into a database

Running SQL queries inside Python

Using Pandas for data handling

Creating visual charts with Matplotlib
