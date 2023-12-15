import os
import shutil

def segregate_files(source_folder, target_folder, prefix):
    # Create target folder if it doesn't exist
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Print the length of the prefix
    # prefix_length = len(prefix)
    # print(f"The length of the prefix '{prefix}' is: {prefix_length}")

    # Iterate over files in the source folder
    for filename in os.listdir(source_folder):
        # Check if the file starts with the specified prefix
        if filename.startswith(prefix):
            source_path = os.path.join(source_folder, filename)
            prefix_length = len(source_path)

            print(f"The length of the prefix '{prefix}' is: {prefix_length}")
            target_path = os.path.join(target_folder, filename)

            # Check if the file already exists in the target folder
            if os.path.exists(target_path):
                print(f"File '{filename}' already exists in the target folder. Skipping.")
            else:
                # Use shutil.copy2 to preserve metadata
                shutil.copy2(source_path, target_path)
                print(f"File '{filename}' copied to '{target_folder}'.")

if __name__ == "__main__":
    # source_folder = "/home/ubuntu/PowerBEV/lyft2/sample/images"
    # target_folder = "/home/ubuntu/PowerBEV/lyft2/sample2/image"
    # prefix = "host-a004_cam"

    source_folder = "/home/ubuntu/PowerBEV/lyft2/sample/train_lidar"
    target_folder = "/home/ubuntu/PowerBEV/lyft2/sample2/train_lidar"
    prefix = "host-a004_lidar"

    segregate_files(source_folder, target_folder, prefix)
    print(f"Files starting with '{prefix}' have been segregated into '{target_folder}' folder.")
