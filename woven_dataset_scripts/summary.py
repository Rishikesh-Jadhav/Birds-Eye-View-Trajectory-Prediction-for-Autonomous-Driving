import os
import json
from shutil import copyfile

# Folder path containing files to match
folder_path = 'lyft2'

# JSON file paths
json_file_path_4 = './lyft2/sample2/train_data/sample_data.json'
json_file_path_2 = './lyft2/sample2/train_data/sample_annotation.json'
json_file_path_3 = './lyft2/sample2/train_data/sample.json'
json_file_path_1 = './lyft2/sample2/train_data/scene.json'
output_json_file_path_annotations = './lyft2/sample2/annotations.json'
output_json_file_path = './lyft2/sample2/new_scene.json'
output_json_file_path_sample = './lyft2/sample2/new_sample.json'
output_json_file_path_sample_data = './lyft2/sample2/new_sample_data.json'


with open(json_file_path_1, 'r') as file:
    sample_data = json.load(file)

print(len(sample_data))
sample_tokens_set = set()
filename_set=set()

for block in sample_data:
    filename = block.get("name")
    sample_token = block.get("first_sample_token")

    # Match the filename with files in the folder
    # print(filename)
    print(sample_tokens_set)

    file_path = os.path.join(filename)
    if os.path.exists(file_path):
        sample_tokens_set.add(sample_token)
        filename_set.add(filename)

# Load the JSON data from the second file
with open(json_file_path_2, 'r') as file:
    sample_annotations = json.load(file)
# Filter blocks in the second file based on sample tokens from the first file
filtered_blocks = [block for block in sample_annotations if block.get("first_sample_token") in sample_tokens_set]

print(filtered_blocks)

with open(output_json_file_path_annotations, 'w') as file:
    json.dump(filtered_blocks, file, indent=2)




print(len(sample_data))
print("Done")