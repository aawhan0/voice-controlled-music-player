from PIL import Image
from io import BytesIO
import tkinter as tk

def show_album_art(song_path):
    from mutagen.id3 import ID3
    try:
        tags = ID3(song_path)
        for tag in tags.values():
            if tag.FrameID == "APIC":
                img_data = tag.data
                image = Image.open(BytesIO(img_data))
                
                # Create Tkinter window to show album art
                root = tk.Toplevel()
                root.title("Album Art")
                
                # Resize image if it's too big
                max_size = (300, 300)
                image.thumbnail(max_size)

                # Convert PIL Image to Tkinter-compatible format
                tk_image = tk.PhotoImage(image)
                
                label = tk.Label(root, image=tk_image)
                label.image = tk_image  # Keep reference
                label.pack()

                # Auto-close after 5 seconds
                root.after(5000, root.destroy)
                return
        print("No album art embedded.")
    except Exception as e:
        print(f"No album art found or error occurred: {e}")
