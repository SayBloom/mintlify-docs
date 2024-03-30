import json
import os

# Read the mint.json file
with open('mint.json') as file:
    data = json.load(file)

# Iterate over the navigation groups
for group in data['navigation']:
    # Convert the group name to a URL-friendly format
    group_dir = group['group'].lower().replace(' ', '-')
    
    # Create a directory for each group
    os.makedirs(group_dir, exist_ok=True)
    
    # Iterate over the pages in each group
    for page in group['pages']:
        # Create a markdown file for each page (section)
        filename = f"{page}.mdx"
        with open(filename, 'w') as file:
            # Extract the page title from the path
            page_title = page.split('/')[-1].replace('-', ' ').title()
            file.write(f"# {page_title}\n\nAdd your content here.")
        
        print(f"Created: {filename}")

print("All markdown files have been created.")