import os
import shutil
import json

# Function to scan client folders for loose files
def scan_client_folders(base_path):
    """Scan all client folders and create a list of those with loose files."""
    clients_with_loose_files = {}

    # Loop through each client folder
    for idx, client_folder in enumerate(os.listdir(base_path), start=1):
        client_path = os.path.join(base_path, client_folder)
        print(f"Checking directory: {client_path}")  # Debug print

        if not os.path.isdir(client_path):
            print(f"Skipped: {client_path} is not a directory")  # Debug print
            continue  # Skip if not a directory

        client_uploads_path = os.path.join(client_path, 'Client Uploads')

        if not os.path.isdir(client_uploads_path):
            print(f"Skipped: Client Uploads folder does not exist in {client_path}")  # Debug print
            continue  # Skip if 'Client Uploads' does not exist

        # Check for loose files in 'Client Uploads'
        for item in os.listdir(client_uploads_path):
            item_path = os.path.join(client_uploads_path, item)
            print(f"Found item: {item_path}")  # Debug print

            if os.path.isfile(item_path):
                clients_with_loose_files[idx] = client_folder
                print(f"{idx}: Loose file found in client folder: {client_folder}")  # Debug print
                break  # Stop after finding the first loose file

    # Save results to a JSON file
    if clients_with_loose_files:
        with open('client_loose_files.json', 'w') as json_file:
            json.dump(clients_with_loose_files, json_file, indent=4)
            print("JSON file written.")  # Debug print
    else:
        print("No loose files found to write to JSON.")  # Debug print

    return clients_with_loose_files

# Main script logic
base_path = r"\\path\to\your\directory"  # Adjust your base path accordingly

clients_with_loose_files = scan_client_folders(base_path)