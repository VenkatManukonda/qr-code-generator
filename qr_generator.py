import qrcode

def generate_qr_code(url, output_file="qr_code.png"):
    """
    Generates a QR code image from the provided URL.

    Parameters:
        url (str): The URL to be encoded in the QR code
        output_file (str): The name of the output image file
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    qr.add_data(url)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")
    qr_image.save(output_file)

    print("QR Code generated successfully.")
    print(f"Output file: {output_file}")

def main():
    """
    Main function to accept user input and generate QR code.
    """
    url = input("Enter a URL to generate QR code: ")
    generate_qr_code(url)

if __name__ == "__main__":
    main()
