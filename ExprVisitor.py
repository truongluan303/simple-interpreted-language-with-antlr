# Generated from .\Expr.g4 by ANTLR 4.9.2
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.


class ExprVisitor(ParseTreeVisitor):
    def __init__(self):
        self.varMap = {}  # Map for setting and getting variables
        self.varStack = []  # Stack for keeping variables

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx: ExprParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#let.
    def visitLet(self, ctx: ExprParser.LetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#print.
    def visitPrint(self, ctx: ExprParser.PrintContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#push.
    def visitPush(self, ctx: ExprParser.PushContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#compare.
    def visitCompare(self, ctx: ExprParser.CompareContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#blankStatement.
    def visitBlankStatement(self, ctx: ExprParser.BlankStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExprParser#letExprFunc.
    def visitLetExprFunc(self, ctx: ExprParser.LetExprFuncContext):
        varName = ctx.VAR().getText()
        value = self.visit(ctx.expr())
        self.varMap[varName] = value
        return value

    # Visit a parse tree produced by ExprParser#letPopFunc.
    def visitLetPopFunc(self, ctx: ExprParser.LetPopFuncContext):
        varName = ctx.VAR().getText()
        try:
            value = self.varStack[-1]
            self.varMap[varName] = value
            self.varStack.pop()
            return value
        except IndexError:
            print("The stack is empty !!")
            return

    # Visit a parse tree produced by ExprParser#printFunc.
    def visitPrintFunc(self, ctx: ExprParser.PrintFuncContext):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    # Visit a parse tree produced by ExprParser#pushFunc.
    def visitPushFunc(self, ctx: ExprParser.PushFuncContext):
        value = self.visit(ctx.expr())
        self.varStack.append(value)

    # Visit a parse tree produced by ExprParser#compareFunc.
    def visitCompareFunc(self, ctx: ExprParser.CompareFuncContext):
        value1 = self.visit(ctx.expr(0))
        value2 = self.visit(ctx.expr(1))
        print(value1 == value2)

    # Visit a parse tree produced by ExprParser#string.
    def visitString(self, ctx: ExprParser.StringContext):
        return ctx.getText().lstrip("'").rstrip("'")

    # Visit a parse tree produced by ExprParser#muldivExpr.
    def visitMuldivExpr(self, ctx: ExprParser.MuldivExprContext):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        if ctx.MUL():
            return left * right
        # Exception handling when dividing by 0
        try:
            # All divisions will be integer
            return int(left / right)
        except ZeroDivisionError:
            return "The denominator cannot be zero !!"

    # Visit a parse tree produced by ExprParser#var.
    def visitVar(self, ctx: ExprParser.VarContext):
        varName = ctx.VAR().getText()
        if varName in self.varMap:
            return self.varMap[varName]
        return "Undefined variable"

    # Visit a parse tree produced by ExprParser#addsubExpr.
    def visitAddsubExpr(self, ctx: ExprParser.AddsubExprContext):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        if ctx.ADD():
            return left + right
        return left - right

    # Visit a parse tree produced by ExprParser#parensExpr.
    def visitParensExpr(self, ctx: ExprParser.ParensExprContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by ExprParser#int.
    def visitInt(self, ctx: ExprParser.IntContext):
        return ctx.INT().getText()


del ExprParser
