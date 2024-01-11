
def read_template(path):
    with open(path) as file:
        contents = file.read()
    return contents.strip()

def extract_parts_from_template(template):
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

# Example usage:
template = "Hello {name}, your age is {age}."
result = extract_parts_from_template(template)
print(result)

def merge(stripped_template, parts):
    return stripped_template.format(*parts)



