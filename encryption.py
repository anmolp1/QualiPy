from cryptography.fernet import Fernet
import pandas as pd
import os

# Function to generate a new encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Function to load the existing encryption key
def load_key():
    return open("secret.key", "rb").read()

# Function to encrypt a DataFrame column
def encrypt_column(dataframe, column_name):
    """Encrypts a DataFrame column."""
    key = load_key()
    fernet = Fernet(key)
    # Ensure the column is converted to string and encode it
    encrypted_column = dataframe[column_name].apply(lambda x: fernet.encrypt(str(x).encode()) if pd.notna(x) else x)
    return encrypted_column

# Function to decrypt a DataFrame column
def decrypt_column(encrypted_column):
    """Decrypts a DataFrame column."""
    key = load_key()
    fernet = Fernet(key)
    # Decrypt and convert back to original data type if needed
    decrypted_column = encrypted_column.apply(lambda x: fernet.decrypt(x).decode() if pd.notna(x) else x)
    return decrypted_column

# Example usage of the encryption functions
if __name__ == "__main__":
    # Generate key (only once, should be kept secret)
    # generate_key()  # Uncomment this line the first time you run this code

    # Create a sample DataFrame
    data = pd.DataFrame({
        'A': [1, 2, 3, 4, 5],
        'B': ['apple', 'banana', 'cherry', 'date', 'elderberry']
    })

    # Encrypt a column
    data['B_encrypted'] = encrypt_column(data, 'B')
    print("Encrypted DataFrame:")
    print(data['B_encrypted'])

    # Decrypt the column
    data['B_decrypted'] = decrypt_column(data['B_encrypted'])
    print("\nDecrypted DataFrame:")
    print(data['B_decrypted'])
