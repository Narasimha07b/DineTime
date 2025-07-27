# Let's read all the attached files to understand the project structure
import os

# List all files in the current directory
files = os.listdir('.')
print("Available files:", files)

# Read the HTML files
html_files = ['bookings.html', 'indexx.html', 'restaurant.html']
for file in html_files:
    if file in files:
        print(f"\n=== {file} ===")
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            print(content[:2000])  # First 2000 characters
            if len(content) > 2000:
                print(f"... (truncated, total length: {len(content)} characters)")
    else:
        print(f"{file} not found")

# Read the JSON file
if 'restaurants.json' in files:
    print(f"\n=== restaurants.json ===")
    with open('restaurants.json', 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)