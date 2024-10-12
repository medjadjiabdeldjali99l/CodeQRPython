import streamlit as st
import qrcode
from PIL import Image
import io

# Title of the app
st.title("QR Code Generator")

# Explain the application
st.write("This application allows you to easily create a QR code from a URL you provide. A QR code, or 'Quick Response Code,' is a type of barcode that can be scanned by smartphones and other devices for quick access to stored information. Simply enter your desired URL, and you'll receive a QR code that you can download or share. The application displays the QR code clearly and prominently, ensuring it's easily scannable.")


# User input for URL
url = st.text_input("Enter URL:")

# Generate QR code when the URL is provided
if url:
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert the image to bytes
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_bytes = buffered.getvalue()

    # Display the QR code image
    st.image(img_bytes, caption='Your QR Code', use_column_width=True)
