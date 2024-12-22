import base64
from stegano import lsb
from PIL import Image

# Paths for the input images
carrier_image_path = 'don.png'  # The image that will carry the hidden photo
hidden_image_path = 'rick.png'   # The image to be hidden
output_image_path = 'output.png'   # The output image with the hidden data

# Step 1: Encode the hidden image into a base64 string
with open(hidden_image_path, 'rb') as hidden_image:
    hidden_image_data = base64.b64encode(hidden_image.read()).decode('utf-8')

# Step 2: Hide the base64 string in the carrier image
lsb.hide(carrier_image_path, message=hidden_image_data).save(output_image_path)
print(f"Hidden image saved to {output_image_path}")
Image.open(output_image_path).show()