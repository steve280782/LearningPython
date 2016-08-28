# Function to print contents of inventory
def displayInventory(stuff):
    print ('Inventory:')
    for k, v in stuff.items():
        print (v, k)
    print ('Total number of items:', sum(stuff.values()))

def addToInventory(stuff, addedItems):
    for k in addedItems:
        if k in stuff.keys():
            stuff[k] = stuff[k] + 1

# Inventory dictionary
inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


# Call function
#displayInventory(inventory)
addToInventory(inventory, dragonLoot)
print(inventory)