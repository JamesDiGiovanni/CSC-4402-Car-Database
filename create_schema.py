import sqlite3

def create_schema():
    conn = sqlite3.connect('dealership.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vehicles (
            vin TEXT PRIMARY KEY,
            make TEXT,
            model TEXT,
            year INTEGER,
            price INTEGER,
            status TEXT,
            color TEXT,
            mileage INTEGER,
            transmission TEXT,
            fuel_type TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phone TEXT,
            email TEXT,
            address TEXT,
            drivers_license TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            position TEXT,
            hire_date TEXT,
            salary INTEGER,
            phone TEXT,
            email TEXT,
            status TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_vin TEXT,
            customer_id INTEGER,
            employee_id INTEGER,
            sale_date TEXT,
            sale_price INTEGER,
            payment_method TEXT,
            finance_term INTEGER,
            FOREIGN KEY (vehicle_vin) REFERENCES vehicles (vin),
            FOREIGN KEY (customer_id) REFERENCES customers (customer_id),
            FOREIGN KEY (employee_id) REFERENCES employees (employee_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS services (
            service_id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_vin TEXT,
            service_date TEXT,
            completion_date TEXT,
            description TEXT,
            cost INTEGER,
            technician_id INTEGER,
            status TEXT,
            mileage_at_service INTEGER,
            FOREIGN KEY (vehicle_vin) REFERENCES vehicles (vin),
            FOREIGN KEY (technician_id) REFERENCES employees (employee_id)
        )
    ''')

    conn.commit()
    conn.close()
    print("Database schema created successfully!")

if __name__ == "__main__":
    create_schema()