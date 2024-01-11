import re

def read_template(file_path):
    try:
        with open(file_path, 'r') as template_file:
            template = template_file.read()
        return template.strip()  # Added strip to remove leading/trailing whitespaces
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

def parse_template(template):
    pattern = re.compile(r'{(.*?)}')
    placeholders = pattern.findall(template)
    modified_template = re.sub(r'{(.*?)}', '{}', template)
    return modified_template, tuple(placeholders)  # Return placeholders as a tuple

def merge(template, placeholders):
    placeholders = list(placeholders)
    print(placeholders)
    for placeholder in placeholders:
        template = template.replace('{}', placeholders.pop(0), 1)
        print(template)
    return template

# Additional function to get user inputs
def get_user_inputs(prompts):
    user_inputs = {}
    for prompt in prompts:
        user_inputs[prompt] = input(f"Enter a {prompt}: ")
    return user_inputs

# Main Program
if __name__ == "__main__":
    template_path = 'assets/dark_and_stormy_night_template.txt'