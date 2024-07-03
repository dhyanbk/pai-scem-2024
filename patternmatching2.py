import re

def find_regex_matches(text, pattern):
    matches = re.finditer(pattern, text)
    match_positions = [match.start() for match in matches]
    return match_positions

# Example usage:
text = "Hello, my email is example123@gmail.com and backup is example.backup@gmail.com"
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
positions = find_regex_matches(text, pattern)
print(f"Email addresses found at positions: {positions}")
