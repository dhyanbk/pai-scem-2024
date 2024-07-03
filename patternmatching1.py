def find_pattern(string, pattern):
    # Initialize an empty list to store positions
    positions = []
    length = len(string)
    len_pattern = len(pattern)
    # Iterate through the string
    for i in range(length - len_pattern + 1):
        # Check if substring matches the pattern
        if string[i:i + len_pattern] == pattern:
            positions.append(i)
    return positions

# Example usage:
string = "abracadabra"
pattern = "abr"
positions = find_pattern(string, pattern)
print(f"Pattern '{pattern}' found at positions: {positions}")
