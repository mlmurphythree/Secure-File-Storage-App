from flask import Flask, send_file, render_template, request, redirect, url_for
from cryptography.fernet import Fernet
import os
from io import BytesIO

app = Flask(__name__)

# Directory where uploaded (and encrypted) files will be stored
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)  # Create the directory if it does not exist

# Function to generate or load an encryption key
def generate_key():
    key = Fernet.generate_key()
    with open('fernet_key.key', 'wb') as key_file:
        key_file.write(key)  # Save the key to a file
    return key

def load_key():
    try:
        with open('fernet_key.key', 'rb') as key_file:
            key = key_file.read()  # Load the key from a file
    except FileNotFoundError:
        key = generate_key()  # Generate a key if it does not exist
    return key

key = load_key()

# Functions to encrypt and decrypt files
def encrypt_file(file_path, key):
    cipher_suite = Fernet(key)
    with open(file_path, 'rb') as file:
        file_data = file.read()
        encrypted_data = cipher_suite.encrypt(file_data)  # Encrypt the file data
    return encrypted_data

def decrypt_file(encrypted_data, key):
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)  # Decrypt the file data
    return decrypted_data

# Route for handling the main page and file uploads
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part in the request'
        file = request.files['file']
        if file.filename == '':
            return 'No file selected for uploading'
        
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)  # Save the uploaded file
        
        encrypted_data = encrypt_file(file_path, key)  # Encrypt the file
        with open(file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)  # Save the encrypted data

        return redirect(url_for('index'))  # Redirect back to the main page
    else:
        files = [f for f in os.listdir(UPLOAD_FOLDER) if os.path.isfile(os.path.join(UPLOAD_FOLDER, f))]
        return render_template('index.html', files=files)  # Pass the list of files to the template

# Route for handling file downloads
@app.route('/download/<filename>')
def download(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(file_path):
        return 'File not found', 404

    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()
    
    decrypted_data = decrypt_file(encrypted_data, key)  # Decrypt the file data
    decrypted_file = BytesIO(decrypted_data)
    decrypted_file.seek(0)
    
    return send_file(decrypted_file, as_attachment=True, download_name=f"decrypted_{filename}")  # Send the decrypted file

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode for development
