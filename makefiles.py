import json
import os

# Read the mint.json file
with open('mint.json') as file:
    data = json.load(file)

# Iterate over the navigation groups
for group in data['navigation']:
    # Skip the "Practice Speaking" group
    if group['group'] == "Practice Speaking":
        continue
    
    # Iterate over the pages in each group
    for page in group['pages']:
        # Extract the directory and filename from the page path
        page_dir, page_file = os.path.split(page)
        
        # Create the directory for the page if it doesn't already exist and page_dir is not empty
        if page_dir:
            os.makedirs(page_dir, exist_ok=True)
        
        # Create a markdown file for each page (section) if it doesn't already exist
        filename = f"{page}.mdx"
        if not os.path.exists(filename):
            with open(filename, 'w') as file:
                # Extract the page title from the path
                page_title = page_file.replace('-', ' ').title()
                file.write(f"# {page_title}\n\nAdd your content here.")
            
            print(f"Created: {filename}")
        else:
            print(f"Skipped: {filename} (already exists)")

print("Markdown file creation completed.")