#!/usr/bin/python3

def uppercase(str):
    output = ""
    for character in str:
        if 'a' <= character <= 'z':
            character = chr(ord(character) - 32)
        output += character
    print(output)
