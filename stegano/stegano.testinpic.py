from stegano import lsb
output_image_path = 'stegano_textinpng.png'
# Message to hide
msg = 'This is a secret message.'

# Hide the message in the image and save the output as PNG
lsb.hide('don.png', message=msg).save(output_image_path)

print(f'Encrypt success!\nHidden image saved to {output_image_path} ')
 