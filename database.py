import sqlite3

def create_database():
    conn = sqlite3.connect('dealership.db')
    cursor = conn.cursor()

    cursor.execute('PRAGMA foreign_keys = ON')
    # cursor.execute('DROP TABLE IF EXISTS services;')  

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vehicles (
            vin TEXT PRIMARY KEY CHECK(length(vin) = 17),
            make TEXT NOT NULL CHECK(length(make) > 0),
            model TEXT NOT NULL CHECK(length(model) > 0),
            year INTEGER NOT NULL CHECK(year BETWEEN 1900 AND 2024),
            price REAL NOT NULL CHECK(price > 0),
            status TEXT NOT NULL CHECK(status IN ('Available', 'Sold', 'Under Maintenance', 'Reserved')),
            color TEXT NOT NULL,
            mileage INTEGER NOT NULL CHECK(mileage >= 0),
            transmission TEXT CHECK(transmission IN ('Automatic', 'Manual')),
            fuel_type TEXT CHECK(fuel_type IN ('Gasoline', 'Diesel', 'Electric', 'Hybrid')),
            date_added DATE NOT NULL DEFAULT CURRENT_DATE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL CHECK(length(name) > 1),
            phone TEXT NOT NULL UNIQUE CHECK(length(phone) >= 10),
            email TEXT UNIQUE CHECK(email LIKE '%@%.%'),
            address TEXT NOT NULL,
            drivers_license TEXT UNIQUE NOT NULL,
            registration_date DATE NOT NULL DEFAULT CURRENT_DATE,
            last_visit_date DATE,
            CONSTRAINT valid_dates CHECK(last_visit_date IS NULL OR last_visit_date >= registration_date)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL CHECK(length(name) > 1),
            position TEXT NOT NULL CHECK(position IN (
                'Sales Representative', 
                'Service Technician', 
                'Manager', 
                'Finance Specialist',
                'Administrative Staff'
            )),
            hire_date DATE NOT NULL,
            salary REAL NOT NULL CHECK(salary > 0),
            phone TEXT UNIQUE NOT NULL CHECK(length(phone) >= 10),
            email TEXT UNIQUE CHECK(email LIKE '%@%.%'),
            status TEXT NOT NULL DEFAULT 'Active' CHECK(status IN ('Active', 'On Leave', 'Terminated')),
            supervisor_id INTEGER,
            FOREIGN KEY (supervisor_id) REFERENCES employees(employee_id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_vin TEXT NOT NULL,
            customer_id INTEGER NOT NULL,
            employee_id INTEGER NOT NULL,
            sale_date DATE NOT NULL,
            sale_price REAL NOT NULL CHECK(sale_price > 0),
            payment_method TEXT NOT NULL CHECK(payment_method IN ('Cash', 'Finance', 'Lease', 'Bank Transfer')),
            finance_term INTEGER CHECK(
                (payment_method = 'Finance' AND finance_term IS NOT NULL AND finance_term > 0) OR
                (payment_method != 'Finance' AND finance_term IS NULL)
            ),
            FOREIGN KEY (vehicle_vin) REFERENCES vehicles (vin) ON DELETE RESTRICT,
            FOREIGN KEY (customer_id) REFERENCES customers (customer_id) ON DELETE RESTRICT,
            FOREIGN KEY (employee_id) REFERENCES employees (employee_id) ON DELETE RESTRICT,
            CONSTRAINT sale_date_check CHECK(sale_date <= CURRENT_DATE)
        )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS services (
        service_id INTEGER PRIMARY KEY AUTOINCREMENT,
        vehicle_vin TEXT NOT NULL,
        service_date DATE NOT NULL,
        completion_date DATE,
        description TEXT NOT NULL,  
        cost REAL NOT NULL CHECK(cost >= 0), 
        technician_id INTEGER NOT NULL,
        status TEXT NOT NULL DEFAULT 'Pending' CHECK(status IN ('Pending', 'In Progress', 'Completed', 'Cancelled')),
        mileage_at_service INTEGER NOT NULL CHECK(mileage_at_service >= 0),
        FOREIGN KEY (vehicle_vin) REFERENCES vehicles (vin) ON DELETE RESTRICT,
        FOREIGN KEY (technician_id) REFERENCES employees (employee_id),
        CONSTRAINT valid_service_dates CHECK(
            completion_date IS NULL OR completion_date >= service_date
        )
    )
''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()