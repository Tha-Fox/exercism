from string import ascii_lowercase
def is_pangram(sentence):
    for character in ascii_lowercase:
        if character not in sentence.lower():
            return False
    return True
