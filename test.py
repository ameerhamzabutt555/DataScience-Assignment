# Function to display the menu options
def ShowMenu():
    print("\n1. Show All Products\n2. Add New Product\n3. Delete a Product\n4. Update Product Rating\n5. Exit")

# Function to get user input for menu options
# It takes an optional argument 'prompt' to customize the input message
def GetInput(prompt="Enter Option to Continue.."): 
    return int(input(prompt))

# Function to display all products in a neatly formatted table
def ShowAllProducts(products):
    keys = products.keys()  # Extract the column headers (keys) from the dictionary
    
    # Print the column headers (keys) with 20 character-wide columns
    for key in keys:
        print(f"{key:<20}", end="")
    print()  # Move to the next line

    rows = len(products["pid"])  # Get the number of rows (length of the "pid" list)
    
    # Print each row's values in a tabular format
    for i in range(rows):
        for key in keys:
            print(f"{str(products[key][i]):<20}", end="")  # Align the text to 20 characters
        print()  # Move to the next row after printing all columns for the current row

    # Display the number of rows and columns at the end
    print(f"\n[{rows} rows x {len(keys)} columns]\n")

# Function to add a new product by collecting user input
def AddNewProducts(products):
    # Collect details for the new product from user input
    new_product = {
        "pid": input("Enter Product Id: "), 
        "name": input("Enter Product Name: "), 
        "details": input("Enter Product Description: "), 
        "image": input("Enter Product Image: "), 
        "rating": float(input("Enter Product Rating: "))  # Convert rating input to float
    }

    # Append the new product's details to each corresponding key's list in the products dictionary
    for key in products:
        products[key].append(new_product[key])

# Function to delete a product based on its Product Id
def DeleteProduct(products):
    pid = input("Enter Product Id to delete or -1 to exit: ")  # Get the Product Id from the user
    if pid != "-1" and pid in products["pid"]:  # Check if the product exists
        idx = products["pid"].index(pid)  # Get the index of the product to delete
        for key in products:
            products[key].pop(idx)  # Remove the product from each list by index
        print("Product deleted.\n")
    else:
        print("Product id doesn't exist or operation cancelled.\n")  # Handle invalid Product Ids

# Function to update the rating of an existing product
def UpdateProductRating(products):
    pid = input("Enter product id to update: ")  # Get the Product Id from the user
    if pid in products["pid"]:  # Check if the product exists
        idx = products["pid"].index(pid)  # Get the index of the product to update
        products["rating"][idx] = float(input("Enter new product rating: "))  # Update the rating
        print("Product rating updated.\n")
    else:
        print("Product id doesn't exist!\n")  # Handle invalid Product Ids

# Initial data for products, represented as a dictionary of lists
products = {
    "pid": ["p01", "p04", "p05", "p06", "p07", "p08", "p10", "p11", "p12"],  # List of product ids
    "name": ["refrigerator", "dishwasher", "washing machine", "air purifier", "water dispenser", "iron", "hair dryer", "stove", "rack"],  # List of product names
    "details": ["..."] * 9,  # Placeholder for product descriptions
    "image": ["refrigerator.png", "dishwasher.png", "washingmachine.png", "airpurifier.png", "waterdispenser.png", "iron.png", "hairdryer.png", "stove.png", "rack.png"],  # List of product images
    "rating": [4.5, 5.0, 3.0, 2.5, 3.3, 4.5, 5.0, 1.0, 2.7]  # List of product ratings
}

# Main loop to continuously display the menu and perform actions based on user input
while True:
    ShowMenu()  # Display the menu options before each input
    userInput = GetInput()  # Get the user input (menu selection)
    
    # Perform action based on user's input
    if userInput == 1:
        ShowAllProducts(products)  # Display all products
    elif userInput == 2:
        AddNewProducts(products)  # Add a new product
    elif userInput == 3:
        DeleteProduct(products)  # Delete a product by its id
    elif userInput == 4:
        UpdateProductRating(products)  # Update the rating of a product
    elif userInput == 5:
        break  # Exit the program when user selects option 5
    else:
        print("Invalid option, try again!")  # Handle invalid input
