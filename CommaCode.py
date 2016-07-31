# Define function to convert list to comma seperated list ending with and
def list2string(printlist):
    # Get length of list and minus last value
    printlistremovelast = (len(printlist) - 1)
    for i in range(printlistremovelast):
        # Print comma separated string from list
        print(printlist[i], end=', ')
    else:
        # End string with last list item prepended with 'and'
        print('and', (printlist[-1]))

# Create empty list to fill
UserEnteredList = []
while True:
    # User inputs list items
    print('Enter item ' + str(len(UserEnteredList) + 1) + ' (Or enter nothing to stop.):')
    item = input()
    # To end input user enters nothing
    if item == '':
        break
    UserEnteredList = UserEnteredList + [item]
# Call function with user entered list
list2string(UserEnteredList)
