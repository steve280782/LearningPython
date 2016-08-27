# Function to print contents of inventory
def displayInventory(stuff):
    print ('Inventory:')
    for k, v in stuff.items():
        print (v, k)
    print ('Total number of items:', sum(stuff.values()))

# Inventory dictionary
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# Call function
displayInventory(inventory)
