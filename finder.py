def display_banner():
    print(r"""
  __      ___     _      
  \ \    / (_)   (_)     
   \ \  / / _  __ _  ___ 
    \ \/ / | |/ _` |/ _ \
     \  /  | | (_| |  __/
      \/   |_|\__, |\___|
               __/ |      
              |___/       
      Filter Lines by Keyword
        Dev by Vidura
    """)

def filter_lines_by_keyword():
    # Display the banner
    display_banner()

    # Prompt the user for the input file, keyword, and output file
    input_file = input("Enter the name of the original file: ")
    keyword = input("Enter the keyword to search for: ")
    output_file = input("Enter the name of the output file: ")

    try:
        # Open the input file for reading
        with open(input_file, 'r') as infile:
            # Open the output file for writing
            with open(output_file, 'w') as outfile:
                # Iterate through each line in the input file
                for line in infile:
                    # Check if the keyword is in the line
                    if keyword in line:
                        # Write the line to the output file
                        outfile.write(line)
        print(f"Lines containing '{keyword}' have been saved to {output_file}.")
    except FileNotFoundError:
        print(f"The file '{input_file}' does not exist. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
filter_lines_by_keyword()
