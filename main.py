from antlr4 import *

from ExprLexer import ExprLexer
from ExprParser import ExprParser
from MyExprVisitor import MyExprVisitor


def main():
    input = InputStream("1 + 12 * (123 + 1234) - 12345 / 123456")

    lexer = ExprLexer(input)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()

    res = MyExprVisitor().visitProg(tree)  # Evaluate the expression

    print(input, "=", res)


if __name__ == "__main__":
    main()
