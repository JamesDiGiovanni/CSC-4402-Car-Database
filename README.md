To run the project:

    1. Run 'python main.py' 
    
    The user will then be greeted with choices (1-6), in the terminal, and the user has the ability to choose what they want to explore.

To run the test queries:

    1. Run 'python test_queries.py'

    These test queries will show :

    1: Query 1 Fetches the Most Expensive Vehicles in the database.

        Query 1 Most Expensive Vehicles
        vin | make | model | year | price
        ---------------------------------
        ATFE4Z9MRTD1LHVVJ | Mercedes | GLE | 2,019 | 79,962.0
        7TL4W0781J28HUDMU | Ford | Explorer | 2,021 | 79,388.0
        C38V77KDC0ZHZH8BD | Ford | F-150 | 2,021 | 76,858.0
        901HAT5L61JL6PRE1 | Nissan | Rogue | 2,023 | 75,724.0
        5ENLUXGUDL5PHSYFT | Toyota | Highlander | 2,020 | 75,414.0

    2: Query 2 Sales By Employee shows total sales per employees as well as total sale amount.

        Query 2 Sales By Employee
        employee_id | name | total_sales | total_sales_amount
        -----------------------------------------------------
        15 | Mr. Michael Martinez DDS | 2 | 135,175.0
        8 | James Burns | 3 | 107,201.0
        5 | Chad Morris | 2 | 99,047.0
        2 | Tiffany King | 2 | 65,302.0
        3 | Scott Key | 1 | 40,488.0

    3: Query 3 Vehicles By Status shows how many vehicles are sold, reserved, or in the shop. 

        Query 3 Vehicles By Status
        status | vehicle_count | percentage
        -----------------------------------
        Sold | 17 | 56.67
        Reserved | 7 | 23.33
        Under Maintenance | 6 | 20.0
    
    4: Query 4 Customer Purchase History shows how many cars customers purchased, as well as how much they bought it for.

        Query 4 Customer Purchase History
        customer_id | name | total_purchases | total_purchase_amount
        ------------------------------------------------------------
        24 | Heidi Klein | 1 | 77,071.0
        31 | Brooke Miller | 1 | 71,099.0
        49 | Christopher Larson | 1 | 64,076.0
        3 | Jimmy Hughes | 1 | 61,566.0
        4 | Michael Owens | 1 | 44,390.0
        16 | Deborah Roberts | 1 | 40,488.0
        35 | Willie Hall | 1 | 23,823.0
        46 | Tina Carlson | 1 | 21,976.0
        44 | Christina Peters | 1 | 21,812.0
        39 | Angela Perry | 1 | 20,912.0

    5: Query 5 Service Analysis shows which cars had services, how many services it had, as well as how much it cost.

        Query 5 Service Analysis
        make | model | total_services | avg_service_cost | total_service_cost
        ---------------------------------------------------------------------
        Audi | Q7 | 7 | 1,080.43 | 7,563.0
        Mercedes | GLC | 6 | 862.0 | 5,172.0
        Mercedes | E-Class | 5 | 1,262.0 | 6,310.0
        Nissan | Maxima | 4 | 663.25 | 2,653.0
        Ford | Explorer | 3 | 1,281.0 | 3,843.0
        Audi | A4 | 2 | 1,076.0 | 2,152.0
        Chevrolet | Equinox | 2 | 1,440.5 | 2,881.0
        Mercedes | GLE | 2 | 1,556.0 | 3,112.0
        Nissan | Rogue | 2 | 851.5 | 1,703.0
        Chevrolet | Silverado | 1 | 1,278.0 | 1,278.0

    The test_queries.py file provides a set of five test queries designed to check the database's functionality, including queries on vehicle prices, sales by employees, vehicle status counts, customer purchase history, and service analysis.