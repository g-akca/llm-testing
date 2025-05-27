import re

def fix_spaces(text: str) -> str:
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    fix_spaces("  Two   Spaces") == "__Two-Spaces" 
    """
    # First, replace all sequences of 3 or more spaces with a hyphen.
    # We do this first because otherwise replacing single spaces would break
    # up these longer sequences.
    # r' {3,}' matches exactly the space character, repeated 3 or more times.
    text = re.sub(r' {3,}', '-', text)
    
    # Second, replace all remaining single spaces with underscores.
    # Any sequences of exactly two spaces from the original input 
    # will now be treated as two individual spaces and replaced accordingly.
    text = text.replace(' ', '_')
    
    return text

# Example Usage (from docstring):
print(f"'Example' -> '{fix_spaces('Example')}'")
print(f"'Example 1' -> '{fix_spaces('Example 1')}'")
print(f"' Example 2' -> '{fix_spaces(' Example 2')}'")
print(f"' Example   3' -> '{fix_spaces(' Example   3')}'")
# Additional test case for exactly two spaces
print(f"'  Two   Spaces' -> '{fix_spaces('  Two   Spaces')}'") 
print(f"'Test  with  double  spaces' -> '{fix_spaces('Test  with  double  spaces')}'")
print(f"'Test   with   triple   spaces' -> '{fix_spaces('Test   with   triple   spaces')}'")
print(f"' Leading and trailing   spaces  ' -> '{fix_spaces(' Leading and trailing   spaces  ')}'")
