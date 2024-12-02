import sqlite3
import random
from datetime import datetime, timedelta
import faker
from database import create_database

fake = faker.Faker()

def generate_sample_data():
    conn = sqlite3.connect('dealership.db')
    cursor = conn.cursor()

    car_makes = ['Toyota', 'Honda', 'Ford', 'BMW', 'Mercedes', 'Audi', 'Chevrolet', 'Nissan']
    car_models = {
        'Toyota': ['Camry', 'Corolla', 'RAV4', 'Highlander'],
        'Honda': ['Civic', 'Accord', 'CR-V', 'Pilot'],
        'Ford': ['F-150', 'Mustang', 'Explorer', 'Escape'],
        'BMW': ['3 Series', '5 Series', 'X3', 'X5'],
        'Mercedes': ['C-Class', 'E-Class', 'GLC', 'GLE'],
        'Audi': ['A4', 'A6', 'Q5', 'Q7'],
        'Chevrolet': ['Silverado', 'Malibu', 'Equinox', 'Traverse'],
        'Nissan': ['Altima', 'Rogue', 'Sentra', 'Maxima']
    }
    colors = ['Black', 'White', 'Silver', 'Red', 'Blue', 'Gray']
    
    def generate_vin():
        return ''.join(random.choices('0123456789ABCDEFGHJKLMNPRSTUVWXYZ', k=17))

    print("Generating vehicles...")
    for _ in range(30):
        make = random.choice(car_makes)
        model = random.choice(car_models[make])
        year = random.randint(2018, 2024)
        price = random.randint(20000, 80000)
        status = random.choice(['Available', 'Sold', 'Under Maintenance', 'Reserved'])
        color = random.choice(colors)
        mileage = random.randint(0, 50000)
        transmission = random.choice(['Automatic', 'Manual'])
        fuel_type = random.choice(['Gasoline', 'Diesel', 'Electric', 'Hybrid'])
        
        try:
            cursor.execute('''
                INSERT INTO vehicles (vin, make, model, year, price, status, color, mileage, transmission, fuel_type)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (generate_vin(), make, model, year, price, status, color, mileage, transmission, fuel_type))
        except sqlite3.IntegrityError as e:
            print(f"Error inserting vehicle: {e}")

    print("Generating customers...")
    for _ in range(50):
        try:
            cursor.execute('''
                INSERT INTO customers (name, phone, email, address, drivers_license)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                fake.name(),
                f"555{random.randint(1000000,9999999)}",  
                fake.email(),
                fake.address(),
                fake.uuid4()[:10]
            ))
        except sqlite3.IntegrityError as e:
            print(f"Error inserting customer: {e}")

    print("Generating employees...")
    positions = ['Sales Representative', 'Service Technician', 'Manager', 'Finance Specialist', 'Administrative Staff']
    for _ in range(15):
        try:
            cursor.execute('''
                INSERT INTO employees (name, position, hire_date, salary, phone, email, status)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                fake.name(),
                random.choice(positions),
                fake.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d'),
                random.randint(30000, 80000),
                f"555{random.randint(1000000,9999999)}",  
                fake.email(),
                'Active'
            ))
        except sqlite3.IntegrityError as e:
            print(f"Error inserting employee: {e}")

    print("Generating sales...")
    cursor.execute("SELECT vin FROM vehicles WHERE status = 'Available'")
    available_vins = cursor.fetchall()
    cursor.execute("SELECT customer_id FROM customers")
    customer_ids = cursor.fetchall()
    cursor.execute("SELECT employee_id FROM employees WHERE position = 'Sales Representative'")
    sales_rep_ids = cursor.fetchall()

    for _ in range(20):
        if available_vins and customer_ids and sales_rep_ids:
            vin = random.choice(available_vins)[0]
            customer_id = random.choice(customer_ids)[0]
            employee_id = random.choice(sales_rep_ids)[0]
            sale_date = fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')
            sale_price = random.randint(20000, 80000)
            payment_method = random.choice(['Cash', 'Finance', 'Lease', 'Bank Transfer'])
            
            finance_term = None
            if payment_method == 'Finance':
                finance_term = random.choice([24, 36, 48, 60, 72])

            try:
                cursor.execute('''
                    INSERT INTO sales (vehicle_vin, customer_id, employee_id, sale_date, sale_price, payment_method, finance_term)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                ''', (vin, customer_id, employee_id, sale_date, sale_price, payment_method, finance_term))
                
                cursor.execute("UPDATE vehicles SET status = 'Sold' WHERE vin = ?", (vin,))
                available_vins.remove((vin,))
            except sqlite3.IntegrityError as e:
                print(f"Error inserting sale: {e}")


    print("Generating services...")
    cursor.execute("SELECT vin FROM vehicles")
    all_vins = cursor.fetchall()
    cursor.execute("SELECT employee_id FROM employees WHERE position = 'Service Technician'")
    technician_ids = cursor.fetchall()

    for _ in range(40):
        if all_vins and technician_ids:
            vin = random.choice(all_vins)[0]
            service_date = fake.date_between(start_date='-6m', end_date='today')
            completion_date = fake.date_between(start_date=service_date, end_date='today')
            
            cost = random.randint(50, 2000)  
            
            description = random.choice([
                "Oil Change",
                "Tire Rotation", 
                "Brake Inspection",
                "Engine Tune-Up",
                "Transmission Service",
                "Diagnostic Check",
                "Battery Replacement",
                "Coolant Flush"
            ])
            
            try:
                cursor.execute('''
                    INSERT INTO services (vehicle_vin, service_date, completion_date, description, cost, 
                                        technician_id, status, mileage_at_service)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    vin,
                    service_date.strftime('%Y-%m-%d'),
                    completion_date.strftime('%Y-%m-%d'),
                    description,  
                    cost, 
                    random.choice(technician_ids)[0],
                    'Completed',
                    random.randint(1000, 100000)
                ))
            except sqlite3.IntegrityError as e:
                print(f"Error inserting service: {e}")

    conn.commit()
    conn.close()
    print("Sample data generation completed!")

if __name__ == "__main__":
    create_database()

    generate_sample_data()