# Madlib - File IO and Exceptions

**Author**: Stephanie G. Johnson

## Overview
The terminal version of the Mad Libs Game.


## Getting Started
1. In terminal navigate to the folder with the madlib.py.
2. Run command "python madlib.py".
3. Read through the rules, type "y" to play, type other to quit
4. Input the words following the prompt (21 words)
5. Receive your output
6. Check you current result in the madlib_result.txt file
7. To run test use "pytest -s" command

## Architecture
* Python 
* Venv
* Pytest

*             write_file()
*                   |
*          _____handle_IO()_____
*         |                     |
*   print_prompts()     |     empty_template()
*       |
*   prompt_list()
*       |
*   read_file()



