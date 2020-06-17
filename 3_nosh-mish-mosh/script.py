import noshmishmosh
import numpy as np

# number of users visited the site
all_visitors = noshmishmosh.customer_visits
total_visitor_count = len(all_visitors)
# users that make purchases
paying_visitors = noshmishmosh.purchasing_customers
paying_visitor_count = len(paying_visitors)

# baseline calculation; returns 18.6
baseline_percent = (paying_visitor_count * 100.0) / total_visitor_count

# list of money spent by each customer
payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)
# number of customers needed to reach $1240 additional revenue
new_customers_needed = np.ceil(1240 / average_payment)

# percentage lift; returns 9.4
percentage_point_increase = new_customers_needed / total_visitor_count * 100.0

# minimum detectable effect; returns 50.5
minimum_detectable_effect = percentage_point_increase / baseline_percent * 100.0

# sample size calculated using a sample size calculator (statistical significance = 85%)
ab_sample_size = 290