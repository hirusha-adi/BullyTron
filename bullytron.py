import clipboard


def change(sentence: str):
    sentence = str(sentence).lower()
    final = ''

    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

    # https://gist.github.com/StevenACoffman/a5f6f682d94e38ed804182dc2693ed4b
    characters = {
        'a': 'а',
        'b': 'b',
        'c': 'с',
        'd': 'ԁ',
        'e': 'е',
        'f': 'f',
        'g': 'ġ',
        'h': 'һ',
        'i': 'і',
        'j': 'ј',
        'k': 'κ',
        'l': 'ӏ',
        'm': 'm',
        'n': 'ո',
        'o': 'о',
        'p': 'р',
        'q': 'զ',
        'r': 'r',
        's': 'ʂ',
        'u': 'ս',
        'v': 'ν',
        'x': 'х',
        'y': 'у',
        'z': 'ʐ'
    }

    for letter in sentence:
        if letter in ascii_lowercase:
            letter = characters[letter]
        final += letter

    clipboard.copy(final)
    print('Copied \n', final, '\n\nTo Clipboard')
