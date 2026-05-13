import csv
import random
from datetime import datetime, timedelta

def generate_data(filename, num_records):
    # Set up some parameters
    restaurants = ['Burger King', 'McDonalds', 'Pizza Hut', 'KFC', 'Subway', 'Local Diner', 'Sushi Spot', 'Taco Bell']
    regions = ['North', 'South', 'East', 'West', 'Central']
    customer_types = ['New', 'Returning', 'VIP']
    
    start_date = datetime(2025, 1, 1) # Recent year for relevance
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write header
        writer.writerow([
            'Order ID', 'Order Date', 'Region', 'Restaurant', 'Customer Type', 
            'Order Value ($)', 'Delivery Time (mins)', 'Marketing Spend (per user)',
            'Is Cancelled', 'Variable Costs ($)'
        ])
        
        # Generate records
        for i in range(num_records):
            order_id = 1000 + i
            
            # Weighted random date over 6 months
            days_offset = random.randint(0, 180)
            order_date = start_date + timedelta(days=days_offset)
            
            region = random.choice(regions)
            restaurant = random.choice(restaurants)
            
            # Weighted customer type
            cust_type_choices = ['New', 'Returning', 'VIP']
            cust_type_weights = [0.3, 0.6, 0.1]
            customer_type = random.choices(cust_type_choices, cust_type_weights)[0]
            
            # Order value logic based on customer type
            if customer_type == 'VIP':
                order_value = round(random.uniform(35.0, 80.0), 2)
            elif customer_type == 'Returning':
                order_value = round(random.uniform(15.0, 45.0), 2)
            else:
                order_value = round(random.uniform(10.0, 30.0), 2)
            
            # Marketing spend (CAC proxy)
            # High spend to get new customers, minimal to retain existing
            marketing_spend = round(random.uniform(10.0, 25.0), 2) if customer_type == 'New' else round(random.uniform(0.0, 5.0), 2)
            
            # Delivery time
            # 20 to 60 minutes
            delivery_time = random.randint(20, 60)
            
            # Cancellation rate (around 5%)
            is_cancelled = 'Yes' if random.random() < 0.05 else 'No'
            
            # Variable costs logic (Delivery pay + packaging etc. approx 30-40% of value)
            if is_cancelled == 'No':
                variable_costs = round(order_value * random.uniform(0.3, 0.45) + random.uniform(2.0, 5.0), 2)
                # Over time, VIP gets slightly lower variable percentage because of bulk size scaling
            else:
                variable_costs = 0 # Assume fully refunded/cancelled early, although in real world there might be a sunken cost
            
            writer.writerow([
                order_id, order_date.strftime('%Y-%m-%d'), region, restaurant, customer_type,
                order_value, delivery_time, marketing_spend,
                is_cancelled, variable_costs
            ])
            
generate_data('food_delivery_data.csv', 1000)
print('Dataset generated successfully.')
