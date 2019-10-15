#!/usr/bin/env python3

# Created by DJ Watson
# Created on October 2019
# this program gets a number from th euser and converts it to a calender month


def main():
    # input
    vowels = set("aeiou")
    consonants = set("bcdfghjklmnpqrstvwxz")

    letinput = input("input letter (lowercase): ")
    # process and output

    if any((c in vowels) for c in letinput):
        print("vowel")
    elif "y" in letinput:
        print("both")
    elif any((c in consonants) for c in letinput):
        print("consonant")
    else:
        print("Invalid input")


if __name__ == "__main__":
    main()
