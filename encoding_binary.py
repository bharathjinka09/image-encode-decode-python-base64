import base64

def encode_image(image_name):

	with open(image_name, 'rb') as binary_file:
	    binary_file_data = binary_file.read()
	    base64_encoded_data = base64.b64encode(binary_file_data)
	    base64_message = base64_encoded_data.decode('utf-8')
	    print('Encoded')
	    return base64_message

encoded_data = encode_image('logo.png')
print(encoded_data)