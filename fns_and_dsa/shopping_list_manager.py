def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        


        if choice == '1':
            # Prompt for and add an item
            item = input('Enter the item to add: ')
            item = item.lower()
            shopping_list.append(item)
            print(f'You have sucessfully added {item} to the list')
        
        elif choice == '2':
            # Prompt for and remove an item
            item = input('Enter the item to remove (1-4): ')
            item = item.lower()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f'You have sucessfully removed {item} from the list')
            else:
                print('Item you entered is not in the list.')
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()