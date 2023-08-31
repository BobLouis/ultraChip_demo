import argparse

def format_data(data_str):
    # Remove all commas, spaces, and newlines
    data_str = data_str.replace(',', '').replace(' ', '').replace('\n', '')
    
    # Create a new string, two characters per line
    formatted_data = ""
    for i in range(0, len(data_str), 2):
        formatted_data += data_str[i:i+2] + '\n'
        
    return formatted_data

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Format data from a text file.')
    
    # Add argument for the input file
    parser.add_argument('input_file', type=str, help='Path to the input text file')
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Read the data from the input file
    with open(args.input_file, 'r') as f:
        data_str = f.read()
    
    # Format the data
    formatted_data = format_data(data_str)
    
    # Print the formatted data
    # print("Formatted Data:")
    print(formatted_data)

if __name__ == '__main__':
    main()
