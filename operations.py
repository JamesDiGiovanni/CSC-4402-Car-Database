import sqlite3
from datetime import datetime

def get_db_connection():
    return sqlite3.connect('dealership.db')

def add_vehicle(vin, make, model, year, price, status, color, mileage, transmission, fuel_type):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO vehicles (
                vin, make, model, year, price, status, color, 
                mileage, transmission, fuel_type
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (vin, make, model, year, price, status, color, 
              mileage, transmission, fuel_type))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

def get_all_vehicles():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM vehicles')
    vehicles = cursor.fetchall()
    conn.close()
    return vehicles

def add_customer(name, phone, email, address, drivers_license):  
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO customers (name, phone, email, address, drivers_license)
            VALUES (?, ?, ?, ?, ?) 
        ''', (name, phone, email, address, drivers_license))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

def get_all_customers():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers')
    customers = cursor.fetchall()
    conn.close()
    return customers

def add_employee(name, position, hire_date, salary, phone):  
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO employees (name, position, hire_date, salary, phone)
            VALUES (?, ?, ?, ?, ?)  
        ''', (name, position, hire_date, salary, phone))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

def get_all_employees():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    conn.close()
    return employees

def add_sale(vehicle_vin, customer_id, employee_id, sale_date, sale_price, payment_method):  
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO sales (vehicle_vin, customer_id, employee_id, sale_date, sale_price, payment_method)
            VALUES (?, ?, ?, ?, ?, ?)  
        ''', (vehicle_vin, customer_id, employee_id, sale_date, sale_price, payment_method))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

def get_all_sales():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sales')
    sales = cursor.fetchall()
    conn.close()
    return sales

def add_service(vehicle_vin, description, cost, technician_id): 
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute('''
            INSERT INTO services (vehicle_vin, service_date, completion_date, description, cost, technician_id, status, mileage_at_service)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)  
        ''', (vehicle_vin, datetime.now().strftime('%Y-%m-%d'), None, description, cost, technician_id, 'Pending', 0)) 
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return False
    finally:
        conn.close()

def get_all_services():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM services')
    services = cursor.fetchall()
    conn.close()
    return services