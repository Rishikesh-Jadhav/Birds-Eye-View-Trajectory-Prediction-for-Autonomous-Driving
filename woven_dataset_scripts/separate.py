import os
import json
from shutil import copyfile

# Folder path containing files to match
folder_path = 'trainval'

# JSON file paths
json_file_path_1 = './lyft2/sample2/train_data/sample_data.json'
json_file_path_2 = './lyft2/sample2/train_data/sample_annotation.json'
json_file_path_3 = './lyft2/sample2/train_data/sample.json'
json_file_path_4 = './lyft2/sample2/train_data/scene.json'
output_json_file_path_annotations = './lyft2/sample2/sample_annotations.json'
output_json_file_path = './lyft2/sample2/new_scene.json'
output_json_file_path_sample = './lyft2/sample2/sample.json'
output_json_file_path_sample_data = './lyft2/sample2/sample_data.json'

# Define the filename prefixes to filter
filename_prefixes = ["images/host-a004_", "images/host-a005_", "images/host-a006_", "images/host-a007_", "images/host-a102_","lidar/host-a004_", "lidar/host-a005_", "lidar/host-a006_", "lidar/host-a007_", "lidar/host-a102_"]

with open(json_file_path_1, 'r') as file:
    sample_data = json.load(file)

sample_tokens_set = set()
filename_set = set()

for block in sample_data:
    filename = block.get("filename")
    sample_token = block.get("sample_token")
    # print(filename)

    # Check if the filename has any of the specified prefixes
    if any(filename.startswith(prefix) for prefix in filename_prefixes):
        # Match the filename with files in the folder
        # file_path = os.path.join("/home/ubuntu/lyft2/samples2/",filename)
        # print("FAILE",file_path)
        # if os.path.exists(file_path):
        #     print("exits")
        sample_tokens_set.add(sample_token)
        filename_set.add(filename)
print(len(sample_tokens_set))
# Load the JSON data from the second file
with open(json_file_path_2, 'r') as file:
    sample_annotations = json.load(file)

# Filter blocks in the second file based on sample tokens from the first file
filtered_blocks = [block for block in sample_annotations if block.get("sample_token") in sample_tokens_set]
print("FILTERED_BLOCKS",len(filtered_blocks))
with open(output_json_file_path_annotations, 'w') as file:
    json.dump(filtered_blocks, file, indent=2)


# Load the JSON data from the first file
with open(json_file_path_3, 'r') as file:
    sample = json.load(file)

scene_tokens_set = set()

for block in sample:
    sample_token = block.get("token")
    scene_token = block.get("scene_token")

    if sample_token in sample_tokens_set:
        # Store the sample token and the entire block
        scene_tokens_set.add(scene_token)

with open(json_file_path_4, 'r') as file:
    scene = json.load(file)

# Filter blocks in the second file based on sample tokens from the first file
filtered_blocks_scene = [block for block in scene if block.get("token") in scene_tokens_set]

print("LENNN",len(filtered_blocks_scene))

# Output file
# Write the filtered blocks to a new JSON file
with open(output_json_file_path, 'w') as file:
    json.dump(filtered_blocks_scene, file, indent=2)

filtered_blocks_sample = [block for block in sample if block.get("scene_token") in scene_tokens_set]

print(len(filtered_blocks_sample))
with open(output_json_file_path_sample, 'w') as file1:
    json.dump(filtered_blocks_sample, file1, indent=2)

filtered_blocks_sample_data = [block for block in sample_data if block.get("filename") in filename_set]
print(len(sample_data))
print(len(filtered_blocks_sample_data))
with open(output_json_file_path_sample_data, 'w') as file1:
    json.dump(filtered_blocks_sample_data, file1, indent=2)

# Print a message indicating success
print("Done")
