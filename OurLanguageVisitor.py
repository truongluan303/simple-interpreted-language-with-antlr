# Generated from .\OurLanguage.g4 by ANTLR 4.9.2
from antlr4 import *

from .OurLanguageParser import OurLanguageParser

# This class defines a complete generic visitor for a parse tree produced by OurLanguageParser.


class OurLanguageVisitor(ParseTreeVisitor):
    def __init__(self):
        self.varMap = {}  # Map for setting and getting variables
        self.varStack = []  # Stack for keeping variables

    # Visit a parse tree produced by OurLanguageParser#prog.
    def visitProg(self, ctx: OurLanguageParser.ProgContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by OurLanguageParser#let.
    def visitLet(self, ctx: OurLanguageParser.LetContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by OurLanguageParser#print.
    def visitPrint(self, ctx: OurLanguageParser.PrintContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by OurLanguageParser#push.
    def visitPush(self, ctx: OurLanguageParser.PushContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by OurLanguageParser#compare.
    def visitCompare(self, ctx: OurLanguageParser.CompareContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by OurLanguageParser#blankStatement.
    def visitBlankStatement(self, ctx: OurLanguageParser.BlankStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by OurLanguageParser#letExprFunc.
    def visitLetExprFunc(self, ctx: OurLanguageParser.LetExprFuncContext):
        varName = ctx.VAR().getText()
        value = self.visit(ctx.expr())
        self.varMap[varName] = value
        return value

    # Visit a parse tree produced by OurLanguageParser#letPopFunc.
    def visitLetPopFunc(self, ctx: OurLanguageParser.LetPopFuncContext):
        varName = ctx.VAR().getText()
        try:
            value = self.varStack[-1]
            self.varMap[varName] = value
            self.varStack.pop()
            return value
        except IndexError:
            print("The stack is empty !!")
            return

    # Visit a parse tree produced by OurLanguageParser#printFunc.
    def visitPrintFunc(self, ctx: OurLanguageParser.PrintFuncContext):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    # Visit a parse tree produced by OurLanguageParser#pushFunc.
    def visitPushFunc(self, ctx: OurLanguageParser.PushFuncContext):
        value = self.visit(ctx.expr())
        self.varStack.append(value)

    # Visit a parse tree produced by OurLanguageParser#compareFunc.
    def visitCompareFunc(self, ctx: OurLanguageParser.CompareFuncContext):
        value1 = self.visit(ctx.expr(0))
        value2 = self.visit(ctx.expr(1))
        print(value1 == value2)

    # Visit a parse tree produced by OurLanguageParser#string.
    def visitString(self, ctx: OurLanguageParser.StringContext):
        return ctx.getText().lstrip("'").rstrip("'")

    # Visit a parse tree produced by OurLanguageParser#muldivExpr.
    def visitMuldivExpr(self, ctx: OurLanguageParser.MuldivExprContext):
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

    # Visit a parse tree produced by OurLanguageParser#var.
    def visitVar(self, ctx: OurLanguageParser.VarContext):
        varName = ctx.VAR().getText()
        if varName in self.varMap:
            return self.varMap[varName]
        return "Undefined variable"

    # Visit a parse tree produced by OurLanguageParser#addsubExpr.
    def visitAddsubExpr(self, ctx: OurLanguageParser.AddsubExprContext):
        left = int(self.visit(ctx.expr(0)))
        right = int(self.visit(ctx.expr(1)))
        if ctx.ADD():
            return left + right
        return left - right

    # Visit a parse tree produced by OurLanguageParser#parensExpr.
    def visitParensExpr(self, ctx: OurLanguageParser.ParensExprContext):
        return self.visit(ctx.expr())

    # Visit a parse tree produced by OurLanguageParser#int.
    def visitInt(self, ctx: OurLanguageParser.IntContext):
        return ctx.INT().getText()


del OurLanguageParser
