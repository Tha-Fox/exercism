def is_isogram(string):
    for character in string:
        if character.isalnum():# Leave out hyphens etc.
            character_low = character.lower() # Prevent mixed case to cause assertion to fail.
            other_characters = string[string.index(character) + 1:]
            if character_low in other_characters:
                return False
    return True

