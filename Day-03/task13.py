visitor_ids = [101, 102, 103, 101, 104, 102, 105, 103, 106, 101, 107, 105]

# Convert list into set
unique_visitors = set(visitor_ids)

# Count unique visitors
count = len(unique_visitors)

print("Visitor IDs:", visitor_ids)
print("Unique Visitors:", unique_visitors)
print("Total Unique Visitors:", count)