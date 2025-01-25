import os

# Specify the folder containing the files
folder_path = "/home/seif/Desktop/veetech/vee_web_api/app/models/koko.py"
output_file = "merged_file.txt"  # Name of the output file

# Open the output file in write mode
with open(output_file, "w", encoding="utf-8") as outfile:
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Check if it's a file (not a folder)
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as infile:
                # Read and write the contents
                outfile.write(infile.read())
                outfile.write("\n")  # Add a newline between files for clarity

print(f"All files have been merged into {output_file}")