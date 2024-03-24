# Image Encryption and Decryption Application

This application allows you to encrypt and decrypt images using various algorithms such as AES, DES, and RSA. It provides a user-friendly interface for loading images, encrypting them, decrypting them, and displaying the results.

## Features

- Load images in common formats such as JPG, JPEG, PNG, and BMP.
- Encrypt images using different encryption algorithms.
- Decrypt encrypted images with the correct decryption key.
- Automatically select encrypted images for decryption.
- Display the decrypted image in the interface.

## Requirements

- Python 3.x
- Tkinter
- cryptography library
- Pillow (Python Imaging Library)

## Installation

1. Clone the repository to your local machine:

    ```
    git clone https://github.com/your-username/image-encryption-app.git
    ```

2. Install the required Python packages using pip:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the application by executing the `image_encryption_app.py` file:

    ```
    python image_encryption_app.py
    ```

2. Use the interface to perform the following actions:
   - Load an image: Click the "Load Image" button and select an image file from your filesystem.
   - Encrypt the loaded image: Click the "Encrypt Image" button to encrypt the loaded image using the selected encryption algorithm.
   - Decrypt an encrypted image: Click the "Decrypt Image" button to decrypt an encrypted image. You will be prompted to enter the decryption key.
   - Load an encrypted image: Click the "Load Encrypted Image" button to automatically select an encrypted image file from your filesystem.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push the branch (`git push origin feature/improvement`).
5. Create a new pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
