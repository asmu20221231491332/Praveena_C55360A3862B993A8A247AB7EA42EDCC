def linear_search_product(product_list, target_product_name):
    indices = []
    for index, product in enumerate(product_list):
        if product['name'] == target_product_name:
            indices.append(index)
    return indices

# Example list of products (replace with your own data)
products = [
    {'name': 'Laptop', 'price': 999.99},
    {'name': 'Mouse', 'price': 19.99},
    {'name': 'Keyboard', 'price': 49.99},
    {'name': 'Laptop', 'price': 799.99},
]

# Example target product name to search for
target_product_name = 'Laptop'

# Call the function to search for the target product
result = linear_search_product(products, target_product_name)

# Print the result
if result:
    print(f"The target product '{target_product_name}' was found at indices: {result}")
else:
    print(f"The target product '{target_product_name}' was not found.")