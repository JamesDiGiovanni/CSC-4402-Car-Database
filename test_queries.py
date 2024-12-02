import sqlite3
import sys

def execute_query(query, params=None):
    """
    Execute a SQL query and return the results
    
    :param query: SQL query string
    :param params: Optional tuple of parameters for parameterized queries
    :return: List of query results
    """
    try:
        conn = sqlite3.connect('dealership.db')
        cursor = conn.cursor()
        
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        column_names = [description[0] for description in cursor.description]
        
        results = cursor.fetchall()
        conn.close()
        return results, column_names
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return [], []

def format_query_results(query_func):
    """
    Decorator to handle query execution and formatting
    """
    def wrapper(*args, **kwargs):
        try:
            results, column_names = query_func(*args, **kwargs)
            
            print(f"\n{query_func.__name__.replace('_', ' ').title()}")
            header = " | ".join(column_names)
            print(header)
            print("-" * len(header))
            
            for result in results:
                formatted_result = []
                for item in result:
                    if isinstance(item, (int, float)):
                        formatted_result.append(f"{item:,}")
                    elif isinstance(item, str):
                        formatted_result.append(item)
                    else:
                        formatted_result.append(str(item))
                print(" | ".join(formatted_result))
            
            return results
        except Exception as e:
            print(f"Error in {query_func.__name__}: {e}")
            return []
    return wrapper

@format_query_results
def query_1_most_expensive_vehicles():
    """
    Query 1: Find the top 5 most expensive vehicles
    """
    query = """
    SELECT vin, make, model, year, price 
    FROM vehicles 
    ORDER BY price DESC 
    LIMIT 5
    """
    return execute_query(query)

@format_query_results
def query_2_sales_by_employee():
    """
    Query 2: Total sales amount for each sales representative
    """
    query = """
    SELECT 
        e.employee_id, 
        e.name, 
        COALESCE(COUNT(s.sale_id), 0) as total_sales,
        COALESCE(ROUND(SUM(s.sale_price), 2), 0) as total_sales_amount
    FROM 
        employees e
    LEFT JOIN 
        sales s ON e.employee_id = s.employee_id
    WHERE 
        e.position = 'Sales Representative'
    GROUP BY 
        e.employee_id, e.name
    ORDER BY 
        total_sales_amount DESC
    """
    return execute_query(query)

@format_query_results
def query_3_vehicles_by_status():
    """
    Query 3: Count of vehicles by status
    """
    query = """
    SELECT 
        status, 
        COUNT(*) as vehicle_count, 
        ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM vehicles), 2) as percentage
    FROM 
        vehicles
    GROUP BY 
        status
    ORDER BY 
        vehicle_count DESC
    """
    return execute_query(query)

@format_query_results
def query_4_customer_purchase_history():
    """
    Query 4: Customers with their total purchase amount
    """
    query = """
    SELECT 
        c.customer_id, 
        c.name, 
        COALESCE(COUNT(s.sale_id), 0) as total_purchases,
        COALESCE(ROUND(SUM(s.sale_price), 2), 0) as total_purchase_amount
    FROM 
        customers c
    LEFT JOIN 
        sales s ON c.customer_id = s.customer_id
    GROUP BY 
        c.customer_id, c.name
    HAVING 
        total_purchases > 0
    ORDER BY 
        total_purchase_amount DESC
    LIMIT 10
    """
    return execute_query(query)

@format_query_results
def query_5_service_analysis():
    """
    Query 5: Service analysis by vehicle and type
    """
    query = """
    SELECT 
        v.make, 
        v.model, 
        COUNT(s.service_id) as total_services,
        ROUND(AVG(s.cost), 2) as avg_service_cost,
        ROUND(SUM(s.cost), 2) as total_service_cost
    FROM 
        vehicles v
    JOIN 
        services s ON v.vin = s.vehicle_vin
    GROUP BY 
        v.make, v.model
    ORDER BY 
        total_services DESC
    LIMIT 10
    """
    return execute_query(query)

def run_all_queries():
    """
    Run all test queries
    """
    query_1_most_expensive_vehicles()
    query_2_sales_by_employee()
    query_3_vehicles_by_status()
    query_4_customer_purchase_history()
    query_5_service_analysis()

if __name__ == "__main__":
    run_all_queries()