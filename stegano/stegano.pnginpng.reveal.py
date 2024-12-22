import base64
from stegano import lsb
from PIL import Image

output_image_path = 'output.png'   # The output image with the hidden data

# Step 1: Reveal the hidden base64 string
revealed_data = lsb.reveal(output_image_path)

# Step 2: Decode the base64 string back into the original image
decoded_image_path = 'revealed.png'
with open(decoded_image_path, 'wb') as decoded_image:
    decoded_image.write(base64.b64decode(revealed_data))

print(f"Revealed image saved to {decoded_image_path}")
Image.open(decoded_image_path).show()