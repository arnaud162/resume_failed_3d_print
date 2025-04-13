#1 get file. scans for gcode files, if many are found asks which one of them

import os

def list_gcode_files(directory):
    gcode_files = [f for f in os.listdir(directory) if f.endswith('.gcode')]
    return gcode_files

def prompt_selection(files):
    if len(files)==1:
        print(files[0] , " selected")
        return files[0]
    else:
        print(len(files),"gcode files detected : ")
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


def get_gcode_from_height(gcode_file, start_height):
    try:
        filtered_lines = []
        include_lines = False  # Indicateur pour commencer à inclure les lignes

        final_height = 0
        with open(gcode_file, 'r') as file:
            for line in file:
                # Vérifier si la ligne contient un mouvement en Z
                if 'Z' in line and 'G0' in line :
                    parts = line.split()
                    for part in parts:
                        if part.startswith('Z'):
                            z_value = float(part[1:])
                            # Commencer à inclure les lignes lorsque Z atteint ou dépasse start_height
                            final_height = z_value
                            if z_value >= start_height:
                                include_lines = True
                
                # Ajouter les lignes une fois que l'on commence à inclure
                if include_lines:
                    filtered_lines.append(line.strip())
        
    
            # Écrire les lignes filtrées dans le fichier de sortie
        
        if (final_height <= start_height):
            print(" height of interupted part ", start_height, " was superior to height of the part ", final_height,". please recheck the height of the interupted part and the selected gcode : ", gcode_file)

        else:
        
            output_file = gcode_file.split(".")[0]+"_from_"+str(start_height).replace(".",",")+"mm.gcode"
            with open(output_file, 'w') as output:
                output.write("\n".join(filtered_lines))
            
            print(f"Filtered G-code successfully written to {output_file}.")

    except Exception as e:
        print(f"An error occurred while processing the G-code file: {e}")

def wait_for_exit():
    print("Press any key to exit...")
    os.system("pause")  # Fonctionne sur Windows

def main():
    # Use the current working directory
    directory = os.getcwd()
    print(f"Scanning the current directory: {directory}")

    gcode_files = list_gcode_files(directory)

    if not gcode_files:
        print("No .gcode files found in the current directory. copy the gcode file at the following location", os.getcwd(), " and rerun ")
        return

    selected_file = prompt_selection(gcode_files)
    selected_file_path = os.path.join(directory, selected_file)
    # read_file_line_by_line(selected_file_path)

    #2 asks for current height
    height = float(input("Enter height of interupted part in mm : "))



    #4 generates new gcode starting at height where print was interupted
    get_gcode_from_height(selected_file_path, height)
    

if __name__ == "__main__":
    main()
    wait_for_exit()
