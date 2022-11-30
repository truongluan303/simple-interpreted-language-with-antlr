# Generated from .\OurLanguage.g4 by ANTLR 4.9.2
from antlr4 import *

from .OurLanguageParser import OurLanguageParser


# This class defines a complete listener for a parse tree produced by OurLanguageParser.
class OurLanguageListener(ParseTreeListener):

    # Enter a parse tree produced by OurLanguageParser#prog.
    def enterProg(self, ctx: OurLanguageParser.ProgContext):
        pass

    # Exit a parse tree produced by OurLanguageParser#prog.
    def exitProg(self, ctx: OurLanguageParser.ProgContext):
        pass

    # Enter a parse tree produced by OurLanguageParser#let.
    def enterLet(self, ctx: OurLanguageParser.LetContext):
        pass

    # Exit a parse tree produced by OurLanguageParser#let.
    def exitLet(self, ctx: OurLanguageParser.LetContext):
        pass

    # Enter a parse tree produced by OurLanguageParser#print.
    def enterPrint(self, ctx: OurLanguageParser.PrintContext):
        pass

    # Exit a parse tree produced by OurLanguageParser#print.
    def exitPrint(self, ctx: OurLanguageParser.PrintContext):
        pass

    # Enter a parse tree produced by OurLanguageParser#push.
    def enterPush(self, ctx: OurLanguageParser.PushContext):
        pass

    # Exit a parse tree produced by OurLanguageParser#push.
    def exitPush(self, ctx: OurLanguageParser.PushContext):
        pass

    # Enter a parse tree produced by OurLanguageParser#compare.
    def enterCompare(self, ctx: OurLanguageParser.CompareContext):
        pass

    # Exit a parse tree produced by OurLanguageParser#compare.
    def exitCompare(self, ctx: OurLanguageParser.CompareContext):
        pass

    # Enter a parse tree produced by OurLanguageParser#blankStatement.
    def enterBlankStatement(self, ctx: OurLanguageParser.BlankStatementContext):
        pass

    # Exit a parse tree produced by OurLanguageParser#blankStatement.
    def exitBlankStatement(self, ctx: OurLanguageParser.BlankStatementContext):
        pass

    # Enter a parse tree produced by OurLanguageParser#letExprFunc.
    def enterLetExprFunc(self, ctx: OurLanguageParser.LetExprFuncContext):
        pass

    # Exit a parse tree produced by OurLanguageParser#letExprFunc.
    def exitLetExprFunc(self, ctx: OurLanguageParser.LetExprFuncContext):
        pass

    # Enter a parse tree produced by OurLanguageParser#letPopFunc.
    def enterLetPopFunc(self, ctx: OurLanguageParser.LetPopFuncContext):
        pass

    # Exit a parse tree produced by OurLanguageParser#letPopFunc.
    def exitLetPopFunc(self, ctx: OurLanguageParser.LetPopFuncContext):
        pass

    # Enter a parse tree produced by OurLanguageParser#printFunc.
    def enterPrintFunc(self, ctx: OurLanguageParser.PrintFuncContext):
        pass

    # Exit a parse tree produced by OurLanguageParser#printFunc.
    def exitPrintFunc(self, ctx: OurLanguageParser.PrintFuncContext):
        pass

    # Enter a parse tree produced by OurLanguageParser#pushFunc.
    def enterPushFunc(self, ctx: OurLanguageParser.PushFuncContext):
        pass

    # Exit a parse tree produced by OurLanguageParser#pushFunc.
    def exitPushFunc(self, ctx: OurLanguageParser.PushFuncContext):
        pass

    # Enter a parse tree produced by OurLanguageParser#compareFunc.
    def enterCompareFunc(self, ctx: OurLanguageParser.CompareFuncContext):
        pass

    # Exit a parse tree produced by OurLanguageParser#compareFunc.
    def exitCompareFunc(self, ctx: OurLanguageParser.CompareFuncContext):
        pass

    # Enter a parse tree produced by OurLanguageParser#string.
    def enterString(self, ctx: OurLanguageParser.StringContext):
        pass

    # Exit a parse tree produced by OurLanguageParser#string.
    def exitString(self, ctx: OurLanguageParser.StringContext):
        pass

    # Enter a parse tree produced by OurLanguageParser#muldivExpr.
    def enterMuldivExpr(self, ctx: OurLanguageParser.MuldivExprContext):
        pass

    # Exit a parse tree produced by OurLanguageParser#muldivExpr.
    def exitMuldivExpr(self, ctx: OurLanguageParser.MuldivExprContext):
        pass

    # Enter a parse tree produced by OurLanguageParser#var.
    def enterVar(self, ctx: OurLanguageParser.VarContext):
        pass

    # Exit a parse tree produced by OurLanguageParser#var.
    def exitVar(self, ctx: OurLanguageParser.VarContext):
        pass

    # Enter a parse tree produced by OurLanguageParser#addsubExpr.
    def enterAddsubExpr(self, ctx: OurLanguageParser.AddsubExprContext):
        pass

    # Exit a parse tree produced by OurLanguageParser#addsubExpr.
    def exitAddsubExpr(self, ctx: OurLanguageParser.AddsubExprContext):
        pass

    # Enter a parse tree produced by OurLanguageParser#parensExpr.
    def enterParensExpr(self, ctx: OurLanguageParser.ParensExprContext):
        pass

    # Exit a parse tree produced by OurLanguageParser#parensExpr.
    def exitParensExpr(self, ctx: OurLanguageParser.ParensExprContext):
        pass

    # Enter a parse tree produced by OurLanguageParser#int.
    def enterInt(self, ctx: OurLanguageParser.IntContext):
        pass

    # Exit a parse tree produced by OurLanguageParser#int.
    def exitInt(self, ctx: OurLanguageParser.IntContext):
        pass


del OurLanguageParser
