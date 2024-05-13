
def reverse(text):
    return text[::-1]

def flip_capitalization(text):
    flipped = ""
    for char in text:
        flipped += char.lower() if char == char.upper() else char.upper()
    return flipped