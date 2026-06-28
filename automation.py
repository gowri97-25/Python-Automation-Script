import os
import shutil

folder = input("Enter the folder path: ")

log_file = os.path.join(folder, "logs.txt")
try:
    # Create folders
    folders = ["Images", "Documents", "Audio", "Others"]

    for f in folders:
        os.makedirs(os.path.join(folder, f), exist_ok=True)

    with open(log_file, "a") as log:

        for file in os.listdir(folder):

            file_path = os.path.join(folder, file)

            if os.path.isfile(file_path) and file != "logs.txt":

                extension = os.path.splitext(file)[1].lower()

                if extension in [".jpg", ".jpeg", ".png"]:
                    destination = os.path.join(folder, "Images")

                elif extension in [".pdf", ".txt"]:
                    destination = os.path.join(folder, "Documents")

                elif extension in [".mp3", ".wav"]:
                    destination = os.path.join(folder, "Audio")

                else:
                    destination = os.path.join(folder, "Others")

                shutil.move(file_path, os.path.join(destination, file))

                message = f"Moved: {file} -> {os.path.basename(destination)}"

                print(message)
                log.write(message + "\n")

    print("\nAutomation completed successfully!")

except Exception as e:
    print("Error:", e)