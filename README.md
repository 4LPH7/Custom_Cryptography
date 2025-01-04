# Custom Cryptography Tool

This application provides a graphical user interface (GUI) for encrypting and decrypting text using a custom cryptographic algorithm. Built with **CustomTkinter**, the tool features a modern and responsive interface for ease of use.

## Features

- **Encrypt & Decrypt**: Supports encryption and decryption of text with a user-defined numeric key.
- **Custom Algorithm**: Implements XOR operations and rearrangement techniques for secure text transformation.
- **Modern Interface**: Styled with CustomTkinter for a sleek, user-friendly design.
- **Responsive Layout**: Aligns components symmetrically for better aesthetics and usability.
- **Dark Mode**: Default dark theme for a professional look.

## Requirements

- **Python 3.7+**
- **CustomTkinter**: Install via pip using the following command:

  ```bash
  pip install customtkinter
  ```

## How to Run

1. Clone or download this repository.
2. Navigate to the project directory.
3. Run the following command to start the application:

   ```bash
   python app.py
   ```

## Usage

1. **Input Text**: Enter the plaintext (for encryption) or ciphertext (for decryption) in the input field.
2. **Key**: Provide an integer key in the designated field.
3. **Encrypt/Decrypt**: Click the corresponding button to transform the text.
4. **View Results**: The output will appear in the result box.

### Example

#### Encryption
- **Plaintext**: `Hello world`
- **Key**: `2`
- **Encrypted Output**: `350635654b9b224b303538`

#### Decryption
- **Ciphertext**: `350635654b9b224b303538`
- **Key**: `2`
- **Decrypted Output**: `Hello world`

## License

This project is licensed under the MIT License. Feel free to use and modify the code.

## Author

Feel free to reach out for support or feedback!


