# Filter Lines by Keyword

A simple Python script to filter lines from a file based on a user-specified keyword and save them to a new file.

## Features

- Search for lines containing a specific keyword in a text file.
- Save the matching lines to a new file.
- Interactive input for file names and the keyword.
- ASCII art banner for a fun, welcoming interface.
- Error handling for missing files and other exceptions.

## How to Use

1. Clone or download this repository.
2. Run the script using Python:

   ```bash
   python filter_lines_by_keyword.py

    Enter the required details when prompted:
        Name of the input file (e.g., input.txt).
        Keyword to search for (e.g., default).
        Name of the output file (e.g., output.txt).

  The script will save all matching lines to the specified output file.

## Example

Here’s how the script works step-by-step:
  Launch the script:
  
    python filter_lines_by_keyword.py

Provide inputs when prompted:

    Enter the name of the original file: input.txt
    Enter the keyword to search for: admin
    Enter the name of the output file: filtered_lines.txt

## Output:
    Lines containing 'admin' have been saved to filtered_lines.txt.

## Requirements

    Python 3.6 or higher
