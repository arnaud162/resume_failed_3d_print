#1 get file. scans for gcode files, if many are found asks which one of them

import os

def list_gcode_files(directory):
    gcode_files = [f for f in os.listdir(directory) if f.endswith('.gcode')]
    return gcode_files

def prompt_selection(files):
    for i, file in enumerate(files):
        print(f"{i + 1}. {file}")
    choice = int(input("Enter the number of the file you want to select: "))
    return files[choice - 1]

def read_file_line_by_line(filepath):
    try:
        with open(filepath, 'r') as file:
            print(f"\nReading file: {filepath}\n")
            for line in file:
                print(line.strip())  # Removes extra spaces or newline characters
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def main():
    # Use the current working directory
    directory = os.getcwd()
    print(f"Scanning the current directory: {directory}")

    gcode_files = list_gcode_files(directory)

    if not gcode_files:
        print("No .gcode files found in the current directory.")
        return

    selected_file = prompt_selection(gcode_files)
    selected_file_path = os.path.join(directory, selected_file)
    read_file_line_by_line(selected_file_path)

if __name__ == "__main__":
    main()



#2 asks for current height

#3 get layer height

#4 generates new gcode starting at height where print was interupted