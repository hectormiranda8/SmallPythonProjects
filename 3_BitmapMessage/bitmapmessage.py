"""
This program uses a multiline string as a 
bitmap, a 2D image with only two possible 
colors for each pixel, to determine how it 
should display a message from the user. In this 
bitmap, space characters represent an empty space, 
and all other characters are replaced by characters in 
the user’s message. The provided bitmap resembles 
a world map, but you can change this to any image 
you’d like. The binary simplicity of the space-or-message-characters system makes it good for beginners. 
Try experimenting with different messages to 
see what the results look like!
"""


import os


def displayBitmap(bit_str: str) -> None:
    idx = 0
    str_len = len(bit_str)
    file_name = os.path.join(os.path.dirname(os.path.realpath(__file__)), "bitmap.txt")
    with open(file_name, 'r') as bm:
        while True:
            curr_line = bm.readline()
            if not curr_line:
                break
            new_line = ""
            for c in curr_line:
                if c == "." or c == "*":
                    new_line += bit_str[idx % str_len]
                    idx += 1
                else:
                    new_line += " "
            print(new_line)


if __name__ == "__main__":
    print("Enter the message to display with the bitmap.")
    user_input = input("> ")
    displayBitmap(user_input)