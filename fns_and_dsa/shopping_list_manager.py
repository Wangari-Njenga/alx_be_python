def main():
    shopping_list = []

    while True:
        print("\nShopping List Manager")
        print("1. Add item")
        print("2. Remove item")
        print("3. View list")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' added to the shopping list.")
            else:
                print("Item name cannot be empty.")
        elif choice == "2":
            item = input("Enter the item to remove: ").strip()
            try:
                shopping_list.remove(item)
                print(f"'{item}' removed from the shopping list.")
            except ValueError:
                print(f"'{item}' not found in the shopping list.")
        elif choice == "3":
            if shopping_list:
                print("\nCurrent Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("\nYour shopping list is empty.")
        elif choice == "4":
            print("Exiting Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
           
 
