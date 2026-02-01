import qrcode

def generate_qr_code(url, file_name="qr_code.png"):
    """
    Generates a QR code for the given URL and saves it as an image file.
    
    Parameters:
        url (str): The URL to encode in the QR code
        file_name (str): Output image file name
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

    print("QR Code generated successfully!")
    print(f"Saved as: {file_name}")

if __name__ == "__main__":
    user_url = input("Enter a URL to generate QR code: ")
    generate_qr_code(user_url)
