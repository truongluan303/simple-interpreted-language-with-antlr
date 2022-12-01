import sys

from antlr4 import *

from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor


def evaluate(visitor, stream) -> None:
    lexer = ExprLexer(stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
    visitor.visitProg(tree)


def main():
    visitor = ExprVisitor()

    use_file_stream = len(sys.argv) > 1

    if use_file_stream:
        evaluate(visitor, FileStream(sys.argv[1]))
    else:
        while True:
            input = sys.stdin.readline().strip()
            if input == "exit()":
                return
            evaluate(visitor, InputStream(input))


if __name__ == "__main__":
    main()
