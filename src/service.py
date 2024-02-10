import os
def rename_images_recursively(directory, prefix="img", start=0):
    """
    Renames images in the specified directory and its subdirectories recursively to a specified prefix and a sequence number.
    :param directory: The root directory to start renaming images.
    :param prefix: The prefix for renamed images.
    :param start: The starting index for renaming.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                old_path = os.path.join(root, file)
                new_path = os.path.join(root, f"{prefix} {start}{os.path.splitext(file)[1]}")
                os.rename(old_path, new_path)
                print(f"Renamed {old_path} to {new_path}")
                start += 1

# Example usage (replace '/path/to/imagefolder' with the actual path to your image folder)
# Note: This script should be run locally where you have access to the file system.
directory_path = r"jodys-website\images"
rename_images_recursively(directory_path)
# Use your specific path to the images folder
image_directory = r"jodys-website\images"
image_files = os.listdir(image_directory)

base_url = "https://raw.githubusercontent.com/Flissel/Jody-Website/master/images/"

# Generate the artworks.js content
artworks_js_content = "const artworks = [\n"

for idx, image in enumerate(image_files, start=1):
    image_url = f"{base_url}{image}"
    # Sample data for title, price, and description. Customize as needed.
    title = "Artwork " + str(idx)
    price = "Price " + str(idx)
    description = "Description for " + title
    
    artworks_js_content += f"    {{\n      id: {idx},\n      title: \"{title}\",\n      price: \"{price}\",\n      image: \"{image_url}\",\n      description: \"{description}.\"\n    }},\n"

# Close the array and the file content
artworks_js_content += "];\n\nexport default artworks;"

# Optionally, write the content to a file called artworks.js
with open(r"jodys-website\src\data\artworks.js", "w") as file:
    file.write(artworks_js_content)

print("artworks.js has been updated.")
