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