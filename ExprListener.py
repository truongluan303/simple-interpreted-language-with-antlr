# Generated from Expr.g4 by ANTLR 4.11.1
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#prog.
    def enterProg(self, ctx: ExprParser.ProgContext):
        pass

    # Exit a parse tree produced by ExprParser#prog.
    def exitProg(self, ctx: ExprParser.ProgContext):
        pass

    # Enter a parse tree produced by ExprParser#let.
    def enterLet(self, ctx: ExprParser.LetContext):
        pass

    # Exit a parse tree produced by ExprParser#let.
    def exitLet(self, ctx: ExprParser.LetContext):
        pass

    # Enter a parse tree produced by ExprParser#print.
    def enterPrint(self, ctx: ExprParser.PrintContext):
        pass

    # Exit a parse tree produced by ExprParser#print.
    def exitPrint(self, ctx: ExprParser.PrintContext):
        pass

    # Enter a parse tree produced by ExprParser#push.
    def enterPush(self, ctx: ExprParser.PushContext):
        pass

    # Exit a parse tree produced by ExprParser#push.
    def exitPush(self, ctx: ExprParser.PushContext):
        pass

    # Enter a parse tree produced by ExprParser#equal.
    def enterEqual(self, ctx: ExprParser.EqualContext):
        pass

    # Exit a parse tree produced by ExprParser#equal.
    def exitEqual(self, ctx: ExprParser.EqualContext):
        pass

    # Enter a parse tree produced by ExprParser#blankStatement.
    def enterBlankStatement(self, ctx: ExprParser.BlankStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#blankStatement.
    def exitBlankStatement(self, ctx: ExprParser.BlankStatementContext):
        pass

    # Enter a parse tree produced by ExprParser#letExprFunc.
    def enterLetExprFunc(self, ctx: ExprParser.LetExprFuncContext):
        pass

    # Exit a parse tree produced by ExprParser#letExprFunc.
    def exitLetExprFunc(self, ctx: ExprParser.LetExprFuncContext):
        pass

    # Enter a parse tree produced by ExprParser#letPopFunc.
    def enterLetPopFunc(self, ctx: ExprParser.LetPopFuncContext):
        pass

    # Exit a parse tree produced by ExprParser#letPopFunc.
    def exitLetPopFunc(self, ctx: ExprParser.LetPopFuncContext):
        pass

    # Enter a parse tree produced by ExprParser#letEqualStatement.
    def enterLetEqualStatement(self, ctx: ExprParser.LetEqualStatementContext):
        pass

    # Exit a parse tree produced by ExprParser#letEqualStatement.
    def exitLetEqualStatement(self, ctx: ExprParser.LetEqualStatementContext):
        pass

    # Enter a parse tree produced by ExprParser#printFunc.
    def enterPrintFunc(self, ctx: ExprParser.PrintFuncContext):
        pass

    # Exit a parse tree produced by ExprParser#printFunc.
    def exitPrintFunc(self, ctx: ExprParser.PrintFuncContext):
        pass

    # Enter a parse tree produced by ExprParser#pushFunc.
    def enterPushFunc(self, ctx: ExprParser.PushFuncContext):
        pass

    # Exit a parse tree produced by ExprParser#pushFunc.
    def exitPushFunc(self, ctx: ExprParser.PushFuncContext):
        pass

    # Enter a parse tree produced by ExprParser#equalFunc.
    def enterEqualFunc(self, ctx: ExprParser.EqualFuncContext):
        pass

    # Exit a parse tree produced by ExprParser#equalFunc.
    def exitEqualFunc(self, ctx: ExprParser.EqualFuncContext):
        pass

    # Enter a parse tree produced by ExprParser#string.
    def enterString(self, ctx: ExprParser.StringContext):
        pass

    # Exit a parse tree produced by ExprParser#string.
    def exitString(self, ctx: ExprParser.StringContext):
        pass

    # Enter a parse tree produced by ExprParser#muldivExpr.
    def enterMuldivExpr(self, ctx: ExprParser.MuldivExprContext):
        pass

    # Exit a parse tree produced by ExprParser#muldivExpr.
    def exitMuldivExpr(self, ctx: ExprParser.MuldivExprContext):
        pass

    # Enter a parse tree produced by ExprParser#var.
    def enterVar(self, ctx: ExprParser.VarContext):
        pass

    # Exit a parse tree produced by ExprParser#var.
    def exitVar(self, ctx: ExprParser.VarContext):
        pass

    # Enter a parse tree produced by ExprParser#addsubExpr.
    def enterAddsubExpr(self, ctx: ExprParser.AddsubExprContext):
        pass

    # Exit a parse tree produced by ExprParser#addsubExpr.
    def exitAddsubExpr(self, ctx: ExprParser.AddsubExprContext):
        pass

    # Enter a parse tree produced by ExprParser#parensExpr.
    def enterParensExpr(self, ctx: ExprParser.ParensExprContext):
        pass

    # Exit a parse tree produced by ExprParser#parensExpr.
    def exitParensExpr(self, ctx: ExprParser.ParensExprContext):
        pass

    # Enter a parse tree produced by ExprParser#int.
    def enterInt(self, ctx: ExprParser.IntContext):
        pass

    # Exit a parse tree produced by ExprParser#int.
    def exitInt(self, ctx: ExprParser.IntContext):
        pass


del ExprParser
