# Function to read names from a file
def read_names(file_path):
    with open(file_path, 'r') as file:
        names = file.readlines()
    # Remove any leading/trailing whitespace and convert to lowercase
    names = [name.strip().lower() for name in names]
    return names

# Function to compare two lists of names and find new names
def find_new_names(old_names, new_names):
    new_names_list = [name for name in new_names if name not in old_names]
    return new_names_list

# Full paths to the old and new lists of names
old_names_path = "C:/Users/xhenx/Vscode/old_names.txt"
new_names_path = "C:/Users/xhenx/Vscode/new_names.txt"

# Read the old and new lists of names
old_names = read_names(old_names_path)
new_names = read_names(new_names_path)

# Find new names in the new list
new_names_list = find_new_names(old_names, new_names)

# Output the new names
print("New names:")
for name in new_names_list:
    print(name)
