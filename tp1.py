from art import *

def generate_ascii_art(text):
    ascii_art = text2art(text)
    return ascii_art

def main():
    text = input("Enter text : ")
    result = generate_ascii_art(text)
    print(result)

if __name__ == "__main__":
    main()
