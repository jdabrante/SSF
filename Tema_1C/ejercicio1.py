import sys

import pycheck


def run(text: str) -> str:
    VOWELS = "aeiou"
    new_text = ""

    for letter in text:
        if letter.lower() in VOWELS:
            new_text += ""
        else:
            new_text += letter

    # Mirar, ya que no seria necesario el if para introducir el espacio.

    output = new_text

    return output


if __name__ == "__main__":
    pycheck.check("pro.ut2.pop0.ej1", sys.argv, run)
