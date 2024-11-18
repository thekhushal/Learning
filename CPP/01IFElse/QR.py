import qrcode

# Define the Instagram link
instagram_link = "https://www.instagram.com/"

# Generate QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(instagram_link)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image
img.save("instagram_qr_code.png")

print("QR code generated and saved as 'instagram_qr_code.png'")
