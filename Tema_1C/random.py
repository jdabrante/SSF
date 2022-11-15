import sys

import pycheck

CHECK_CASES = [
    [["sergio delgado quintero"], "srg dlgd qntr"],
    [["PEPE BENAVENTE"], "PP BNVNT"],
    [["volando VOY, volando VENGO"], "vlnd VY, vlnd VNG"],
]


def run(text: str) -> str:
    # TU CÓDIGO AQUÍ
    return output


if __name__ == "__main__":
    pycheck.check(run, CHECK_CASES, sys.argv)
