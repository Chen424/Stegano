from stegano import lsb

output_image_path = 'stegano_textinpng.png'
# Reveal the hidden message
message = lsb.reveal(output_image_path)
print(f'Reveal message: {message}')
 