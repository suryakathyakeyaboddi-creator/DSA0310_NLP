
import re

# Sample product database
products = [
    "Apple iPhone 15",
    "Apple MacBook Air",
    "Samsung Galaxy S24",
    "Samsung Galaxy Buds",
    "Sony Wireless Headphones",
    "Sony Bravia TV",
    "Dell Laptop",
    "HP Laptop",
    "OnePlus Smartphone",
    "Logitech Wireless Mouse",
    "Apple iPad",
    "Samsung Smart Watch"
]

# Function to search products using Regular Expressions
def search_products(keyword, search_type):
    matching_products = []

    # Escape special regex characters in user input
    keyword = re.escape(keyword)

    # Define pattern based on search type
    if search_type == "exact":
        pattern = r"^" + keyword + r"$"
    elif search_type == "prefix":
        pattern = r"^" + keyword
    elif search_type == "suffix":
        pattern = keyword + r"$"
    elif search_type == "partial":
        pattern = keyword
    else:
        print("Invalid search type!")
        return []

    # Case-insensitive matching
    for product in products:
        if re.search(pattern, product, re.IGNORECASE):
            matching_products.append(product)

    return matching_products


# Function to display results and generate report
def generate_report(keyword, search_type):
    results = search_products(keyword, search_type)

    print("\n" + "=" * 55)
    print("Search Type :", search_type.upper())
    print("Search Keyword:", keyword)
    print("-" * 55)

    if results:
        print("Matching Products:")
        for product in results:
            print("-", product)
    else:
        print("No matching products found.")

    print("-" * 55)
    print("Total Matching Products:", len(results))

    return {
        "Keyword": keyword,
        "Search Type": search_type,
        "Total Matches": len(results),
        "Matching Products": results
    }


# Perform different types of searches
search_report = []

search_report.append(generate_report("Apple iPhone 15", "exact"))
search_report.append(generate_report("Samsung", "prefix"))
search_report.append(generate_report("Laptop", "suffix"))
search_report.append(generate_report("Wireless", "partial"))
search_report.append(generate_report("apple", "partial"))

# Final summary report
print("\n" + "=" * 55)
print("FINAL PRODUCT SEARCH SUMMARY")
print("=" * 55)

for report in search_report:
    print(
        f"Keyword: {report['Keyword']:<20} | "
        f"Type: {report['Search Type']:<7} | "
        f"Matches: {report['Total Matches']}"
    )
