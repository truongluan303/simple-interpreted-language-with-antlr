import sys

from antlr4 import *

from OurLanguageLexer import OurLanguageLexer
from OurLanguageParser import OurLanguageParser
from OurLanguageVisitor import OurLanguageVisitor


def main():
    visitor = OurLanguageVisitor()

    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.readline())

    lexer = OurLanguageLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = OurLanguageParser(stream)
    tree = parser.prog()

    visitor.visitProg(tree)  # Evaluate the expression


if __name__ == "__main__":
    main()
