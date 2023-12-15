import json

# Read sample data from an external JSON file
json_file_path = './lyft2/sample2/train_data/scene.json'  # Replace with the actual file path
with open(json_file_path, 'r') as file:
    sample_data = json.load(file)

user_input_prefix = input("Enter the prefix to extract details: ")


matching_entries = [entry for entry in sample_data if entry["name"].startswith(user_input_prefix)]

if matching_entries:
    output_filename = f"{user_input_prefix}_details.json"
    with open(output_filename, 'w') as file:
        json.dump({user_input_prefix: matching_entries}, file, indent=2)
    print(f"Details for entries starting with '{user_input_prefix}' have been written to '{output_filename}'")
else:
    print(f"No matching entries found for '{user_input_prefix}'")
