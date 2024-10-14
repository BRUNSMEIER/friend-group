# Define the group of acquaintances
week3_group = [
    {
        "name": "Jill",
        "age": 26,
        "job": "biologist",
        "connections": [{"name": "Zalika", "relationship": "friend"}, {"name": "John", "relationship": "partner"}]
    },
    {
        "name": "Zalika",
        "age": 28,
        "job": "artist",
        "connections": [{"name": "Jill", "relationship": "friend"}]
    },
    {
        "name": "John",
        "age": 27,
        "job": "writer",
        "connections": [{"name": "Jill", "relationship": "partner"}]
    },
    {
        "name": "Nash",
        "age": 34,
        "job": "chef",
        "connections": [{"name": "John", "relationship": "cousin"}, {"name": "Zalika", "relationship": "landlord"}]
    }
]


# my_group =
# Print function to display information about each person
def print_group_info(group):
    for person in group:
        print(f"{person['name']} is {person['age']}, a {person['job']} and they have the following connections:")
        if person["connections"]:
            for connection in person["connections"]:
                print(f"- {connection['relationship']} with {connection['name']}")
        else:
            print("- No connections")
        print()  # Blank line for better readability


# Example usage
print_group_info(week3_group)
