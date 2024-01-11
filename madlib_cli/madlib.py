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
    return template.format(*placeholders)

# Additional function to get user inputs
def get_user_inputs(prompts):
    user_inputs = {}
    for prompt in prompts:
        user_inputs[prompt] = input(f"Enter a {prompt}: ")
    return user_inputs

# Main Program
if __name__ == "__main__":
    template_path = 'assets/madlib_template.txt'

    # Read the template from the file
    template = read_template(template_path)

    # Parse the template to get a modified template and placeholders
    modified_template, placeholders = parse_template(template)

    # Get user inputs for each of the placeholders
    user_inputs = get_user_inputs(placeholders)

    # Merge the user inputs with the modified template
    completed_story = merge(modified_template, user_inputs.values())

    # Print or otherwise use the completed story
    print(completed_story)