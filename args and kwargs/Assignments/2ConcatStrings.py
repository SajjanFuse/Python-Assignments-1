"""
Write a Python function concat_strings that takes any number of strings as arguments 
and returns a single concatenated string.
"""

def concatStrings(*strings):
    result = ''
    for a in strings:
        result+=a
        
    return result

print(concatStrings("a", "se", "we", "wr", "tyer"))

# Test cases
test_cases = [
    ("hello", "world"),
    ("", "", ""),
    ("Number", "123", "Concatenation"),
    ("Special", "characters", "#$%^&*"),
    ("Unicode", "🌟", "strings"),
    ("Whitespace", " ", "Test"),
    ("Escape", "\n", "Characters"),
    ("Encoding", "test", "sträng"),
    ("<p>", "HTML", "</p>"),
    ("Short", "MediumLength", "VeryLongString" * 3)
]

# Run test cases
for i, case in enumerate(test_cases, 1):
    result = concatStrings(*case)
    print(f"Strings are:{case},\n Result:'{result}'")