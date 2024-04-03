# Secure File Storage App

A Flask application designed to securely store and share files. Utilizing strong encryption, it ensures that files are encrypted before being stored on the server and decrypted only when downloaded, providing an added layer of security for sensitive information.

## Features

- **Secure File Upload**: Users can upload files securely. Each file is encrypted before being saved.
- **File Listing**: The application lists all files available for download.
- **Secure File Download**: Files are decrypted on-the-fly during the download process.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You'll need Python 3.6+ installed on your machine, as well as the Flask and Cryptography packages.

### Installation

1. Clone the Repository:
   ```
   git clone https://github.com/mlmurphythree/Secure-File-Storage-App.git
   ```
2. Navigate to the Project Directory:
   ```
   cd secure-file-storage-app
   ```
3. Install Requirements:
   Make sure you have pip installed and then run:
   ```
   pip install Flask cryptography
   ```
4. Start the Application:
   ```
   python app.py
   ```
   Navigate to `http://127.0.0.1:5000/` in your web browser to see the application in action.

## Usage

- **Uploading Files**: Use the upload form on the main page to select and upload files securely.
- **Downloading Files**: Click the "Download" link next to any file in the list to securely download and decrypt it.

## Contributing

Contributions are welcome! If you have suggestions for improving the application, feel free to fork the repo and create a pull request, or open an issue with the tag "enhancement". Please adhere to this project's code of conduct.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
