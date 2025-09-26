# shopping_list_manager.py

shopping_list = []

def display_menu():
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def add_item():
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' added to the shopping list.")
    else:
        print("Item name cannot be empty.")

def remove_item():
    item = input("Enter the item to remove: ").strip()
    try:
        shopping_list.remove(item)
        print(f"'{item}' removed from the shopping list.")
    except ValueError:
        print(f"'{item}' not found in the shopping list.")

def view_list():
    if shopping_list:
        print("\nCurrent Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("\nYour shopping list is empty.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            view_list()
        elif choice == "4":
            print("Exiting Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
           
 
