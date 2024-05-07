"""
This program can hack messages encrypted 
with the Caesar cipher from Project 6, even 
if you don’t know the key. There are only 26 
possible keys for the Caesar cipher, so a computer can easily
try all possible decryptions and display the results to the user.
In cryptography, we call 
this technique a brute-force attack. If you’d like to learn 
more about ciphers and code breaking, you can read 
my book Cracking Codes with Python (No Starch Press, 
2018; https://nostarch.com/crackingcodes/).
"""

class CeasarHacker:
    def __init__(self) -> None:
        self.__abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __decrypt(self, to_decrypt: str, key: int) -> str:
        decrypted = ""
        for l in to_decrypt.upper():
            dc = l
            if l in self.__abc:
                dc = self.__abc[(self.__abc.index(l) - key) % len(self.__abc)]
            decrypted += dc
        return decrypted

    def bruteForce(self, msg: str) -> None:
        for i in range(len(self.__abc)):
            print(f"Key #{i}: {self.__decrypt(msg, i)}")


if __name__ == "__main__":
    ceasarhacker = CeasarHacker()
    print("Enter the encrypted Ceasar cipher message to hack.")
    user_input = input("> ")
    ceasarhacker.bruteForce(user_input)