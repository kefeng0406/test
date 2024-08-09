import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'path_to_your_file/coffee.csv'  # Update this with the path to your CSV file
coffee_df = pd.read_csv(file_path)

# Group by category and product to find the total order of each product type
total_orders_df = coffee_df.groupby(['category', 'product'])['order'].sum().reset_index()

# Rename columns to match the desired output
total_orders_df.columns = ['category', 'product', 'total_order']

# Display the DataFrame
print(total_orders_df)

# Plot the total orders of each product type
plt.figure(figsize=(12, 8))
for category in total_orders_df['category'].unique():
    category_data = total_orders_df[total_orders_df['category'] == category]
    plt.bar(category_data['product'], category_data['total_order'], label=category)

plt.xticks(rotation=45, ha='right')
plt.xlabel('Product')
plt.ylabel('Total Orders')
plt.title('Total Orders for Each Product Type')
plt.legend(title='Category')
plt.tight_layout()

# Save the plot to a file
plt.savefig('/mnt/data/coffee_orders_plot.png')

# Show the plot
plt.show()
