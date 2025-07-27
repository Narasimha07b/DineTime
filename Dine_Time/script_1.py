# Let's read the complete content of all HTML files to understand the full functionality
files = ['bookings.html', 'indexx.html', 'restaurant.html']

for file in files:
    print(f"\n{'='*50}")
    print(f"COMPLETE CONTENT OF {file}")
    print(f"{'='*50}")
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        print(content)