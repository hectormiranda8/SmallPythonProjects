"""
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.
In modern times, the Caesar cipher isn’t very sophisticated, but that 
makes it ideal for beginners. The program in Project 7, “Caesar Hacker,” 
can brute-force through all 26 possible keys to decrypt messages, even if 
you don’t know the original key. Also, if you encrypt the message with the 
key 13, the Caesar cipher becomes identical to Project 61, “ROT 13 Cipher.” 
30   Project #6
Learn more about the Caesar cipher at https://en.wikipedia.org/wiki/Caesar_
cipher. If you’d like to learn about ciphers and code breaking in general, you 
can read my book Cracking Codes with Python (No Starch Press, 2018; https://
nostarch.com/crackingcodes/).
"""

class CeasarCypher:
    def __init__(self) -> None:
        self.abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    def encrypt(self, to_encrypt: str, key: int) -> str:
        encrypted = ""
        for l in to_encrypt.upper():
            ec = l
            if l in self.abc:
                ec = self.abc[(self.abc.index(l) + key) % len(self.abc)]
            encrypted += ec
        return encrypted
    
    def decrypt(self, to_decrypt: str, key: int):
        decrypted = ""
        for l in to_decrypt.upper():
            dc = l
            if l in self.abc:
                dc = self.abc[(self.abc.index(l) - key) % len(self.abc)]
            decrypted += dc
        return decrypted


def validInput() -> str:
    user_input = input("> ").lower()
    while user_input != "e" and user_input != "d":
        print("Please choose a valid Option.")
        print("Do you want to (e)ncrypt or (d)crypt?")
        user_input = input("> ").lower()
    return user_input


def validKey() -> int:
    try:
        user_input = int(input("> "))
        while user_input < 0 and user_input > 25:
            print("Please enter the key (0 to 25) to use.")
            user_input = int(input("> "))
        return user_input
    except:
        print("Please choose a valid key.")
        return validKey()

if __name__ == "__main__":
    ceasarcypher = CeasarCypher()
    print("Do you want to (e)ncrypt or (d)crypt?")
    user_input = validInput()
    if user_input == "e":
        print("Enter message to encrypt.")
        msg = input("> ")
        print("Please enter the key (0 to 25) to use.")
        key = validKey()
        print(ceasarcypher.encrypt(msg, key))
    elif user_input == "d":
        print("Enter message to decrypt.")
        msg = input("> ")
        print("Please enter the key (0 to 25) to use.")
        key = validKey()
        print(ceasarcypher.decrypt(msg, key))
    else:
        raise Exception("No valid options were detected.")