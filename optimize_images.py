import os
import subprocess

directories = [
    'static/branda',
    'static/semsiye',
    'static/tekne'
]

extensions = ('.jpg', '.jpeg', '.png')

for directory in directories:
    if not os.path.exists(directory):
        print(f"Directory not found: {directory}")
        continue

    print(f"Processing directory: {directory}")
    for filename in os.listdir(directory):
        if filename.lower().endswith(extensions) and '_min' not in filename:
            filepath = os.path.join(directory, filename)
            name, ext = os.path.splitext(filename)
            new_filename = f"{name}_min{ext}"
            new_filepath = os.path.join(directory, new_filename)
            
            # Skip if min version already exists (unless we want to force regenerate, but let's just make it simple)
            # Actually, user asked to regenerate, so strict overwrite is good.
            
            print(f"Optimizing {filepath} -> {new_filepath}")
            try:
                # Resize to max 800px, preserve aspect ratio
                subprocess.run(['sips', '-Z', '800', filepath, '--out', new_filepath], check=True, stdout=subprocess.DEVNULL)
            except subprocess.CalledProcessError as e:
                print(f"Error optimizing {filepath}: {e}")

print("Image optimization complete.")
