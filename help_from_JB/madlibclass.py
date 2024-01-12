# Python Cheatsheet for Mad Libs Program

# Function to read the template from a file
def read_template(path):
    """
    Reads the content of a file and returns it stripped.
    
    Parameters:
    path (str): The path to the file.
    
    Returns:
    str: The stripped content of the file.
    """
    with open(path) as file:
        contents = file.read()
    return contents.strip()


# Function to extract parts from a template
def extract_parts_from_template(template):
    """
    Extracts parts enclosed in curly braces from a template.
    
    Parameters:
    template (str): The template string.
    
    Returns:
    tuple: A tuple containing the stripped template and a tuple of parts.
    """
    parts = []
    stripped = ""

    capturing = False
    capture = ""

    for char in template:
        if not capturing:
            if char == "{":
                capturing = True
                capture = ""
        else:
            stripped += char
            if char == "}":
                capturing = False
                parts.append(capture)
                capture = ""
            else:
                capture += char

    return stripped, tuple(parts)


# Function to merge parts with a stripped template
def merge(stripped_template, responses):
    """
    Merges parts with a stripped template using the .format() method.
    
    Parameters:
    stripped_template (str): The stripped template string.
    parts (tuple): A tuple of parts to be merged.
    
    Returns:
    str: The completed story after merging the template and parts.
    """
    return stripped_template.format(*responses)


template_path = 'assets/madlib_template.txt'

template = read_template(template_path)

stripped_template, parts = parse_template(template)

responses = []

for part in parts:
    response = input(f"Enter a {part}: ")
    responses.append(response)

merged = merge(stripped_template, responses)

print(merged)

with open('completed_madlib.txt', 'w+') as file:
    file.write(merged)  








