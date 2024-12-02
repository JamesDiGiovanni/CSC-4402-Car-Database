import os
from datetime import datetime
from database import create_database
from operations import (add_vehicle, get_all_vehicles, add_customer, get_all_customers,
                       add_employee, get_all_employees, add_sale, get_all_sales,
                       add_service, get_all_services, get_db_connection)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def delete_vehicle(vin):
    conn = get_db_connection()  
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM vehicles WHERE vin = ?', (vin,))
        conn.commit()
        return cursor.rowcount > 0  
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

def delete_customer(customer_id):
    conn = get_db_connection()  
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM customers WHERE customer_id = ?', (customer_id,))
        conn.commit()
        return cursor.rowcount > 0  
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

def delete_employee(employee_id):
    conn = get_db_connection()  
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM employees WHERE employee_id = ?', (employee_id,))
        conn.commit()
        return cursor.rowcount > 0  
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

def delete_sale(sale_id):
    conn = get_db_connection() 
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM sales WHERE sale_id = ?', (sale_id,))
        conn.commit()
        return cursor.rowcount > 0  
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

def delete_service(service_id):
    conn = get_db_connection()  
    cursor = conn.cursor()
    try:
        cursor.execute('DELETE FROM services WHERE service_id = ?', (service_id,))
        conn.commit()
        return cursor.rowcount > 0  
    except sqlite3.Error as e:
        print(f"Error: {e}")
        return False
    finally:
        conn.close()

def main_menu():
    while True:
        clear_screen()
        print("\n--- Car Dealership Management System ---")
        print("1. Inventory Management")
        print("2. Customer Management")
        print("3. Employee Management")
        print("4. Sales Management")
        print("5. Service Management")
        # print("6. Add Sample Data")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            inventory_menu()
        elif choice == '2':
            customer_menu()
        elif choice == '3':
            employee_menu()
        elif choice == '4':
            sales_menu()
        elif choice == '5':
            service_menu()
        # elif choice == '6':
        #     add_sample_data()
        #     input("\nSample data added. Press Enter to continue...")
        elif choice == '6':
            print("\nThank you for using the Car Dealership Management System!")
            break
        else:
            input("\nInvalid choice. Press Enter to continue...")

def inventory_menu():
    while True:
        clear_screen()
        print("\n=== Inventory Management ===")
        print("1. Add New Vehicle")
        print("2. View All Vehicles")
        print("3. Delete Vehicle")
        print("4. Return to Main Menu")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            try:
                vin = input("Enter VIN: ")
                make = input("Enter Make: ")
                model = input("Enter Model: ")
                year = int(input("Enter Year: "))
                price = float(input("Enter Price: "))
                status = input("Enter Status (Available/Sold): ").capitalize() or "Available"
                color = input("Enter Color: ")
                mileage = int(input("Enter Mileage: "))
                transmission = input("Enter Transmission (Automatic/Manual): ").capitalize()
                fuel_type = input("Enter Fuel Type (Gasoline/Diesel/Electric): ").capitalize()
                
                if add_vehicle(vin, make, model, year, price, status, color, mileage, transmission, fuel_type):
                    print("\nVehicle added successfully!")
                else:
                    print("\nError adding vehicle.")
            except ValueError:
                print("\nInvalid input. Please enter correct data types.")
            input("Press Enter to continue...")
            
        elif choice == '2':
            vehicles = get_all_vehicles()
            print("\nCurrent Inventory:")
            print("VIN | Make | Model | Year | Price | Status")
            print("-" * 50)
            for vehicle in vehicles:
                print(f"{vehicle[0]} | {vehicle[1]} | {vehicle[2]} | {vehicle[3]} | ${vehicle[4]} | {vehicle[5]}")
            input("\nPress Enter to continue...")

        if choice == '3':
            vin = input("Enter the VIN of the vehicle to delete: ")
            if delete_vehicle(vin):
                print("Vehicle deleted successfully!")
            else:
                print("Error deleting vehicle.")
            input("Press Enter to continue...")
            
        elif choice == '4':
            break

def customer_menu():
    while True:
        clear_screen()
        print("\n=== Customer Management ===")
        print("1. Add New Customer")
        print("2. View All Customers")
        print("3. Delete Customer") 
        print("4. Return to Main Menu")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            name = input("Enter Customer Name: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email: ")
            address = input("Enter Address: ")
            drivers_license = input("Enter Driver's License: ") 
            
            if add_customer(name, phone, email, address, drivers_license): 
                print("\nCustomer added successfully!")
            else:
                print("\nError adding customer.")
            input("Press Enter to continue...")
            
        elif choice == '2':
            customers = get_all_customers()
            print("\nCustomer List:")
            print("ID | Name | Phone | Email | Address")
            print("-" * 50)
            for customer in customers:
                print(f"{customer[0]} | {customer[1]} | {customer[2]} | {customer[3]} | {customer[4]}")
            input("\nPress Enter to continue...")
        
        elif choice == '3':
            customer_id = input("Enter the ID of the customer to delete: ")
            if delete_customer(customer_id):
                print("Customer deleted successfully!")
            else:
                print("Error deleting customer.")
            input("Press Enter to continue...")
        
        elif choice == '4':
            break

def employee_menu():
    while True:
        clear_screen()
        print("\n=== Employee Management ===")
        print("1. Add New Employee")
        print("2. View All Employees")
        print("3. Delete Employee")  
        print("4. Return to Main Menu")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            name = input("Enter Employee Name: ")
            position = input("Enter Position: ")
            hire_date = datetime.now().strftime("%Y-%m-%d")
            salary = float(input("Enter Salary: "))  
            phone = input("Enter Phone Number: ")  
            
            if add_employee(name, position, hire_date, salary, phone): 
                print("\nEmployee added successfully!")
            else:
                print("\nError adding employee.")
            input("Press Enter to continue...")
            
        elif choice == '2':
            employees = get_all_employees()
            print("\nEmployee List:")
            print("ID | Name | Position | Hire Date | Salary | Phone")
            print("-" * 50)
            for employee in employees:
                print(f"{employee[0]} | {employee[1]} | {employee[2]} | {employee[3]} | ${employee[4]:.2f} | {employee[5]}")
            input("\nPress Enter to continue...")
        
        elif choice == '3':
            employee_id = input("Enter the ID of the employee to delete: ")
            if delete_employee(employee_id):
                print("Employee deleted successfully!")
            else:
                print("Error deleting employee.")
            input("Press Enter to continue...")
        
        elif choice == '4':
            break

def sales_menu():
    while True:
        clear_screen()
        print("\n=== Sales Management ===")
        print("1. Record New Sale")
        print("2. View All Sales")
        print("3. Delete Sale")  
        print("4. Return to Main Menu")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            try:
                vehicle_vin = input("Enter Vehicle VIN: ")
                customer_id = int(input("Enter Customer ID: "))
                employee_id = int(input("Enter Employee ID: "))
                sale_price = float(input("Enter Sale Price: "))
                payment_method = input("Enter Payment Method (Cash/Finance/Lease/Bank Transfer): ")
                sale_date = datetime.now().strftime("%Y-%m-%d")
                
                if add_sale(vehicle_vin, customer_id, employee_id, sale_date, sale_price, payment_method):
                    print("\nSale recorded successfully!")
                else:
                    print("\nError recording sale.")
            except ValueError:
                print("\nInvalid input. Please enter correct data types.")
            input("Press Enter to continue...")
            
        elif choice == '2':
            sales = get_all_sales()
            print("\nSales Record:")
            print("Sale ID | Vehicle VIN | Customer ID | Employee ID | Date | Price | Payment Method")
            print("-" * 80)
            for sale in sales:
                print(f"{sale[0]} | {sale[1]} | {sale[2]} | {sale[3]} | {sale[4]} | ${sale[5]:.2f} | {sale[6]}")
            input("\nPress Enter to continue...")
        
        elif choice == '3':
            sale_id = input("Enter the Sale ID to delete: ")
            if delete_sale(sale_id):
                print("Sale deleted successfully!")
            else:
                print("Error deleting sale.")
            input("Press Enter to continue...")
        
        elif choice == '4':
            break

def get_all_services():
    conn = get_db_connection()  
    cursor = conn.cursor()
    try:
        cursor.execute('''
            SELECT service_id, vehicle_vin, service_date, description, cost, technician_id 
            FROM services 
            ORDER BY service_date DESC
        ''')
        
        services = cursor.fetchall()
        return services
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []
    finally:
        conn.close()

def service_menu():
    while True:
        clear_screen()
        print("\n=== Service Management ===")
        print("1. Add New Service Record")
        print("2. View All Services")
        print("3. Delete Service Record")  
        print("4. Return to Main Menu")

        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            try:
                vehicle_vin = input("Enter Vehicle VIN: ")
                service_description = input("Enter Service Description: ")
                service_cost = float(input("Enter Service Cost: "))  
                technician_id = int(input("Enter Technician ID: ")) 

                if add_service(vehicle_vin, service_description, service_cost, technician_id):  
                    print("\nService record added successfully!")
                else:
                    print("\nError adding service record.")
            except ValueError as e:
                print(f"\nInvalid input: {e}. Please enter correct data types.")
            input("Press Enter to continue...")

        elif choice == '2':
            services = get_all_services()
            print("\nService Records:")
            print("Service ID | Vehicle VIN | Cost | Technician ID")
            print("-" * 70)
            for service in services:
                try:
                    cost_value = float(service[4]) 
                    print(f"{service[0]} | {service[1]} | {service[2]} | ${cost_value:.2f} | {service[5]}")
                except (ValueError, IndexError) as e:
                    print(f"Error processing service record: {service} - {e}")
            input("\nPress Enter to continue...")

        elif choice == '3':
            service_id = input("Enter the Service ID to delete: ")
            if delete_service(service_id):
                print("Service record deleted successfully!")
            else:
                print("Error deleting service record.")
            input("Press Enter to continue...")

        elif choice == '4':
            break

if __name__ == "__main__":
    create_database()  # initialize the database
    main_menu()