def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range!"

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return "Element updated successfully!"
    except IndexError:
        return "Index out of range, cannot modify!"

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices, cannot slice!"

def index_game():
    # Initialize a sample list
    sample_list = [10, 20, 30, 40, 50, 60, 70]
    print("Current list:", sample_list)
    
    while True:
        print("\nOptions:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice list")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            index = int(input("Enter index to access: "))
            result = access_element(sample_list, index)
            print("Result:", result)
            
        elif choice == "2":
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            result = modify_element(sample_list, index, new_value)
            print(result)
            print("Updated list:", sample_list)
            
        elif choice == "3":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            result = slice_list(sample_list, start, end)
            print("Slice result:", result)
            
        elif choice == "4":
            print("Thanks for playing!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    index_game()