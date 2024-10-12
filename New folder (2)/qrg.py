import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    # Get the input text from the entry widget
    input_text = entry.get()
    
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter a URL or text.")
        return
    
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=4,
    )
    qr.add_data(input_text)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert the image to a format Tkinter can use
    img.save("qrcode.png")  # Save QR code as a PNG file
    img_tk = ImageTk.PhotoImage(img)

    # Display the QR code
    qr_label.config(image=img_tk)
    qr_label.image = img_tk  # Keep a reference to avoid garbage collection

# Create the main window
window = tk.Tk()
window.geometry('500x270')
window.title("QR Code Generator")

# Input field for the URL or text
entry = ttk.Entry(window, width=40)
entry.pack(pady=10)

# Button to generate the QR code
generate_button = ttk.Button(window, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

# Label to display the QR code
qr_label = ttk.Label(window)
qr_label.pack(pady=10)

# Start the Tkinter main loop
window.mainloop()

