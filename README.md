Caesar Cipher Implementation
This project is a simple Python implementation of the Caesar cipher, a classic encryption technique. The Caesar cipher is a substitution cipher where each letter in the text is replaced by a letter a fixed number of positions down the alphabet. In this implementation, the shift is set to 5, but it can easily be modified.

Features:
Encryption:

Encrypts input strings by shifting each character forward by the specified number of positions.

Maintains the case (uppercase or lowercase) of letters.

Non-alphabetic characters (e.g., spaces, punctuation) remain unchanged.

Decryption:

Decrypts previously encrypted strings by reversing the shift.

Case sensitivity is preserved, and non-alphabetic characters are retained as is.

User Interaction:

Provides a menu for selecting between encryption and decryption.

Prompts the user to input the string to be encrypted or decrypted.

Usage:
Clone the repository and run the Python script.

Follow the prompts to input your string and choose an operation (encryption or decryption).

Example:
If the shift is 5:

Input: Hello, World!

Encrypted: Mjqqt, Btwqi!

Decrypted: Hello, World!

Future Improvements:
Allow users to customize the shift value dynamically.

Add error handling for invalid inputs.
