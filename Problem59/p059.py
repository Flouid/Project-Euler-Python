"""
Each character on a computer is assigned a unique code and the preferred standard is ASCII
(American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42,
and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key.
The advantage with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message,
and the key is made up of random bytes.
The user would keep the encrypted message and the encryption key in different locations,
and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key.
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message.
The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters.
Using p059_cipher.txt (right click and 'Save Link/Target As...'),
a file containing the encrypted ASCII codes, and the
knowledge that the plain text must contain common English words,
decrypt the message and find the sum of the ASCII values in the original text.

Louis Keith
12-26-21
"""

from time import time
from statistics import mode


# returns a list of integers with the ascii codes for the encrypted data
def ingest_data(filename='p059_cipher.txt') -> [int]:
    with open(filename) as f:
        characters = f.readline().split(',')
    return list(map(int, characters))


# use the bitwise xor function to encrypt a list of integers with a given key
def xor(data: [int], key: [int]) -> [int]:
    return [data[i] ^ key[i % len(key)] for i in range(len(data))]


# calculate the key using the assumption that space is the most common character
def extract_key(data: [int], key_length=3) -> [int]:
    # split the data into n sub-lists where n is the length of the key
    sub_lists = [[] for _ in range(key_length)]
    for i in range(len(data)):
        sub_lists[i % key_length].append(data[i])
    # each sub-list contains all of the characters that would be mapped using a specific character from the key
    # the most common character should be space, use that fact to calculate the offset for the key for each character
    key = [0 for _ in range(key_length)]
    for i in range(key_length):
        key[i] = mode(sub_lists[i]) ^ 32
    return key


# convert a list of integers to a string value using the ascii table
def convert_to_string(data: [int]) -> str:
    return ''.join(map(chr, data))


# main driver code
def main():
    data = ingest_data()

    key = extract_key(data)
    decode = xor(data, key)

    print('KEY:\t\t', convert_to_string(key))
    print('DECODE:\t\t', convert_to_string(decode))
    print('ASCII SUM:\t', sum(decode))


if __name__ == '__main__':
    start = time()
    main()
    print('FINISHED IN %d SECONDS' % round(time() - start, 4))
