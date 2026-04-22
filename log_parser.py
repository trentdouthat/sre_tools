import sys
import re

def main():
    file_path = "journal.log" 
    pattern = r"\[.*Error.*\]" 
    
    stats = {"INFO": 0, "ERROR": 0}
    error_list = []

    try:
        # Use a Context Manager (with) to safely open the file
        # It handles closing the file automatically, even if the script crashes
        with open(file_path, "r") as file:
            for line in file:
                # Clean up whitespace from the line
                clean_line = line.strip()


                if re.search(pattern, clean_line):
                    stats["ERROR"] += 1
                    error_list.append(clean_line)
                elif "info" in clean_line.lower():
                    stats["INFO"] += 1
        
        # Output the report
        print(f"--- Analysis of {file_path} ---")
        print(f"Total Lines Processed: {stats['INFO'] + stats['ERROR']}")
        print(f"Errors Found: {stats['ERROR']}")
        
        print("\n--- Detailed Error Log ---")
        for err in error_list:
            print(err)

    except FileNotFoundError:
        print(f"CRITICAL ERROR: The file '{file_path}' was not found.")
    except PermissionError:
        print(f"CRITICAL ERROR: Permission denied. Try running with 'sudo'.")

if __name__ == "__main__":
    main()