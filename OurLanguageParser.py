# Generated from .\OurLanguage.g4 by ANTLR 4.9.2
# encoding: utf-8
import sys
from io import StringIO
from typing import TextIO

from antlr4 import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("W\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\6\2\22\n\2\r\2\16\2\23\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3#\n\3\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4/\n\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\bJ\n\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\3\b\7\bR\n\b\f\b\16\bU\13\b\3\b\2\3\16\t\2\4\6\b")
        buf.write('\n\f\16\2\4\3\2\17\20\3\2\r\16\2Z\2\21\3\2\2\2\4"\3\2')
        buf.write("\2\2\6.\3\2\2\2\b\60\3\2\2\2\n\65\3\2\2\2\f:\3\2\2\2\16")
        buf.write("I\3\2\2\2\20\22\5\4\3\2\21\20\3\2\2\2\22\23\3\2\2\2\23")
        buf.write("\21\3\2\2\2\23\24\3\2\2\2\24\3\3\2\2\2\25\26\5\6\4\2\26")
        buf.write("\27\7\3\2\2\27#\3\2\2\2\30\31\5\b\5\2\31\32\7\3\2\2\32")
        buf.write("#\3\2\2\2\33\34\5\n\6\2\34\35\7\3\2\2\35#\3\2\2\2\36\37")
        buf.write('\5\f\7\2\37 \7\3\2\2 #\3\2\2\2!#\7\21\2\2"\25\3\2\2\2')
        buf.write('"\30\3\2\2\2"\33\3\2\2\2"\36\3\2\2\2"!\3\2\2\2#\5')
        buf.write("\3\2\2\2$%\7\b\2\2%&\7\22\2\2&'\7\4\2\2'/\5\16\b\2(")
        buf.write(")\7\b\2\2)*\7\22\2\2*+\7\4\2\2+,\7\13\2\2,-\7\5\2\2-/")
        buf.write("\7\6\2\2.$\3\2\2\2.(\3\2\2\2/\7\3\2\2\2\60\61\7\t\2\2")
        buf.write("\61\62\7\5\2\2\62\63\5\16\b\2\63\64\7\6\2\2\64\t\3\2\2")
        buf.write("\2\65\66\7\n\2\2\66\67\7\5\2\2\678\5\16\b\289\7\6\2\2")
        buf.write("9\13\3\2\2\2:;\7\f\2\2;<\7\5\2\2<=\5\16\b\2=>\7\7\2\2")
        buf.write(">?\5\16\b\2?@\7\6\2\2@\r\3\2\2\2AB\b\b\1\2BJ\7\24\2\2")
        buf.write("CJ\7\22\2\2DJ\7\23\2\2EF\7\5\2\2FG\5\16\b\2GH\7\6\2\2")
        buf.write("HJ\3\2\2\2IA\3\2\2\2IC\3\2\2\2ID\3\2\2\2IE\3\2\2\2JS\3")
        buf.write("\2\2\2KL\f\b\2\2LM\t\2\2\2MR\5\16\b\tNO\f\7\2\2OP\t\3")
        buf.write("\2\2PR\5\16\b\bQK\3\2\2\2QN\3\2\2\2RU\3\2\2\2SQ\3\2\2")
        buf.write('\2ST\3\2\2\2T\17\3\2\2\2US\3\2\2\2\b\23".IQS')
        return buf.getvalue()


class OurLanguageParser(Parser):

    grammarFileName = "OurLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = [
        "<INVALID>",
        "';'",
        "'='",
        "'('",
        "')'",
        "','",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "'+'",
        "'-'",
        "'*'",
        "'/'",
    ]

    symbolicNames = [
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "LET",
        "PRINT",
        "PUSH",
        "POP",
        "COMPARE",
        "ADD",
        "SUB",
        "MUL",
        "DIV",
        "NEWLINE",
        "VAR",
        "STRING",
        "INT",
        "WS",
    ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_letStatement = 2
    RULE_printStatement = 3
    RULE_pushStatement = 4
    RULE_compareStatement = 5
    RULE_expr = 6

    ruleNames = [
        "prog",
        "statement",
        "letStatement",
        "printStatement",
        "pushStatement",
        "compareStatement",
        "expr",
    ]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    LET = 6
    PRINT = 7
    PUSH = 8
    POP = 9
    COMPARE = 10
    ADD = 11
    SUB = 12
    MUL = 13
    DIV = 14
    NEWLINE = 15
    VAR = 16
    STRING = 17
    INT = 18
    WS = 19

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache
        )
        self._predicates = None

    class ProgContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(OurLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(OurLanguageParser.StatementContext, i)

        def getRuleIndex(self):
            return OurLanguageParser.RULE_prog

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterProg"):
                listener.enterProg(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitProg"):
                listener.exitProg(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitProg"):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)

    def prog(self):

        localctx = OurLanguageParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.statement()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (
                    (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << OurLanguageParser.LET)
                                | (1 << OurLanguageParser.PRINT)
                                | (1 << OurLanguageParser.PUSH)
                                | (1 << OurLanguageParser.COMPARE)
                                | (1 << OurLanguageParser.NEWLINE)
                            )
                        )
                        != 0
                    )
                ):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return OurLanguageParser.RULE_statement

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class PrintContext(StatementContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a OurLanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def printStatement(self):
            return self.getTypedRuleContext(OurLanguageParser.PrintStatementContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterPrint"):
                listener.enterPrint(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitPrint"):
                listener.exitPrint(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitPrint"):
                return visitor.visitPrint(self)
            else:
                return visitor.visitChildren(self)

    class CompareContext(StatementContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a OurLanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def compareStatement(self):
            return self.getTypedRuleContext(
                OurLanguageParser.CompareStatementContext, 0
            )

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterCompare"):
                listener.enterCompare(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitCompare"):
                listener.exitCompare(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitCompare"):
                return visitor.visitCompare(self)
            else:
                return visitor.visitChildren(self)

    class BlankStatementContext(StatementContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a OurLanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(OurLanguageParser.NEWLINE, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBlankStatement"):
                listener.enterBlankStatement(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBlankStatement"):
                listener.exitBlankStatement(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitBlankStatement"):
                return visitor.visitBlankStatement(self)
            else:
                return visitor.visitChildren(self)

    class LetContext(StatementContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a OurLanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def letStatement(self):
            return self.getTypedRuleContext(OurLanguageParser.LetStatementContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLet"):
                listener.enterLet(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLet"):
                listener.exitLet(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLet"):
                return visitor.visitLet(self)
            else:
                return visitor.visitChildren(self)

    class PushContext(StatementContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a OurLanguageParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def pushStatement(self):
            return self.getTypedRuleContext(OurLanguageParser.PushStatementContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterPush"):
                listener.enterPush(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitPush"):
                listener.exitPush(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitPush"):
                return visitor.visitPush(self)
            else:
                return visitor.visitChildren(self)

    def statement(self):

        localctx = OurLanguageParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OurLanguageParser.LET]:
                localctx = OurLanguageParser.LetContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.letStatement()
                self.state = 20
                self.match(OurLanguageParser.T__0)
            elif token in [OurLanguageParser.PRINT]:
                localctx = OurLanguageParser.PrintContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.printStatement()
                self.state = 23
                self.match(OurLanguageParser.T__0)
            elif token in [OurLanguageParser.PUSH]:
                localctx = OurLanguageParser.PushContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.pushStatement()
                self.state = 26
                self.match(OurLanguageParser.T__0)
            elif token in [OurLanguageParser.COMPARE]:
                localctx = OurLanguageParser.CompareContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.compareStatement()
                self.state = 29
                self.match(OurLanguageParser.T__0)
            elif token in [OurLanguageParser.NEWLINE]:
                localctx = OurLanguageParser.BlankStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 31
                self.match(OurLanguageParser.NEWLINE)
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LetStatementContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return OurLanguageParser.RULE_letStatement

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class LetPopFuncContext(LetStatementContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a OurLanguageParser.LetStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LET(self):
            return self.getToken(OurLanguageParser.LET, 0)

        def VAR(self):
            return self.getToken(OurLanguageParser.VAR, 0)

        def POP(self):
            return self.getToken(OurLanguageParser.POP, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLetPopFunc"):
                listener.enterLetPopFunc(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLetPopFunc"):
                listener.exitLetPopFunc(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLetPopFunc"):
                return visitor.visitLetPopFunc(self)
            else:
                return visitor.visitChildren(self)

    class LetExprFuncContext(LetStatementContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a OurLanguageParser.LetStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LET(self):
            return self.getToken(OurLanguageParser.LET, 0)

        def VAR(self):
            return self.getToken(OurLanguageParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(OurLanguageParser.ExprContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLetExprFunc"):
                listener.enterLetExprFunc(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLetExprFunc"):
                listener.exitLetExprFunc(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLetExprFunc"):
                return visitor.visitLetExprFunc(self)
            else:
                return visitor.visitChildren(self)

    def letStatement(self):

        localctx = OurLanguageParser.LetStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_letStatement)
        try:
            self.state = 44
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 2, self._ctx)
            if la_ == 1:
                localctx = OurLanguageParser.LetExprFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 34
                self.match(OurLanguageParser.LET)
                self.state = 35
                self.match(OurLanguageParser.VAR)
                self.state = 36
                self.match(OurLanguageParser.T__1)
                self.state = 37
                self.expr(0)

            elif la_ == 2:
                localctx = OurLanguageParser.LetPopFuncContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.match(OurLanguageParser.LET)
                self.state = 39
                self.match(OurLanguageParser.VAR)
                self.state = 40
                self.match(OurLanguageParser.T__1)
                self.state = 41
                self.match(OurLanguageParser.POP)
                self.state = 42
                self.match(OurLanguageParser.T__2)
                self.state = 43
                self.match(OurLanguageParser.T__3)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrintStatementContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return OurLanguageParser.RULE_printStatement

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class PrintFuncContext(PrintStatementContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a OurLanguageParser.PrintStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PRINT(self):
            return self.getToken(OurLanguageParser.PRINT, 0)

        def expr(self):
            return self.getTypedRuleContext(OurLanguageParser.ExprContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterPrintFunc"):
                listener.enterPrintFunc(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitPrintFunc"):
                listener.exitPrintFunc(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitPrintFunc"):
                return visitor.visitPrintFunc(self)
            else:
                return visitor.visitChildren(self)

    def printStatement(self):

        localctx = OurLanguageParser.PrintStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_printStatement)
        try:
            localctx = OurLanguageParser.PrintFuncContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(OurLanguageParser.PRINT)
            self.state = 47
            self.match(OurLanguageParser.T__2)
            self.state = 48
            self.expr(0)
            self.state = 49
            self.match(OurLanguageParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PushStatementContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return OurLanguageParser.RULE_pushStatement

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class PushFuncContext(PushStatementContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a OurLanguageParser.PushStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PUSH(self):
            return self.getToken(OurLanguageParser.PUSH, 0)

        def expr(self):
            return self.getTypedRuleContext(OurLanguageParser.ExprContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterPushFunc"):
                listener.enterPushFunc(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitPushFunc"):
                listener.exitPushFunc(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitPushFunc"):
                return visitor.visitPushFunc(self)
            else:
                return visitor.visitChildren(self)

    def pushStatement(self):

        localctx = OurLanguageParser.PushStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_pushStatement)
        try:
            localctx = OurLanguageParser.PushFuncContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(OurLanguageParser.PUSH)
            self.state = 52
            self.match(OurLanguageParser.T__2)
            self.state = 53
            self.expr(0)
            self.state = 54
            self.match(OurLanguageParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CompareStatementContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return OurLanguageParser.RULE_compareStatement

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class CompareFuncContext(CompareStatementContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a OurLanguageParser.CompareStatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def COMPARE(self):
            return self.getToken(OurLanguageParser.COMPARE, 0)

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(OurLanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(OurLanguageParser.ExprContext, i)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterCompareFunc"):
                listener.enterCompareFunc(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitCompareFunc"):
                listener.exitCompareFunc(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitCompareFunc"):
                return visitor.visitCompareFunc(self)
            else:
                return visitor.visitChildren(self)

    def compareStatement(self):

        localctx = OurLanguageParser.CompareStatementContext(
            self, self._ctx, self.state
        )
        self.enterRule(localctx, 10, self.RULE_compareStatement)
        try:
            localctx = OurLanguageParser.CompareFuncContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(OurLanguageParser.COMPARE)
            self.state = 57
            self.match(OurLanguageParser.T__2)
            self.state = 58
            self.expr(0)
            self.state = 59
            self.match(OurLanguageParser.T__4)
            self.state = 60
            self.expr(0)
            self.state = 61
            self.match(OurLanguageParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(
            self, parser, parent: ParserRuleContext = None, invokingState: int = -1
        ):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return OurLanguageParser.RULE_expr

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class StringContext(ExprContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a OurLanguageParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(OurLanguageParser.STRING, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterString"):
                listener.enterString(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitString"):
                listener.exitString(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitString"):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)

    class MuldivExprContext(ExprContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a OurLanguageParser.ExprContext
            super().__init__(parser)
            self.op = None  # Token
            self.copyFrom(ctx)

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(OurLanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(OurLanguageParser.ExprContext, i)

        def MUL(self):
            return self.getToken(OurLanguageParser.MUL, 0)

        def DIV(self):
            return self.getToken(OurLanguageParser.DIV, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterMuldivExpr"):
                listener.enterMuldivExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitMuldivExpr"):
                listener.exitMuldivExpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMuldivExpr"):
                return visitor.visitMuldivExpr(self)
            else:
                return visitor.visitChildren(self)

    class VarContext(ExprContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a OurLanguageParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(OurLanguageParser.VAR, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVar"):
                listener.enterVar(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVar"):
                listener.exitVar(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitVar"):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)

    class AddsubExprContext(ExprContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a OurLanguageParser.ExprContext
            super().__init__(parser)
            self.op = None  # Token
            self.copyFrom(ctx)

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(OurLanguageParser.ExprContext)
            else:
                return self.getTypedRuleContext(OurLanguageParser.ExprContext, i)

        def ADD(self):
            return self.getToken(OurLanguageParser.ADD, 0)

        def SUB(self):
            return self.getToken(OurLanguageParser.SUB, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAddsubExpr"):
                listener.enterAddsubExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAddsubExpr"):
                listener.exitAddsubExpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAddsubExpr"):
                return visitor.visitAddsubExpr(self)
            else:
                return visitor.visitChildren(self)

    class ParensExprContext(ExprContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a OurLanguageParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(OurLanguageParser.ExprContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterParensExpr"):
                listener.enterParensExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitParensExpr"):
                listener.exitParensExpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitParensExpr"):
                return visitor.visitParensExpr(self)
            else:
                return visitor.visitChildren(self)

    class IntContext(ExprContext):
        def __init__(
            self, parser, ctx: ParserRuleContext
        ):  # actually a OurLanguageParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(OurLanguageParser.INT, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterInt"):
                listener.enterInt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitInt"):
                listener.exitInt(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitInt"):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)

    def expr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = OurLanguageParser.ExprContext(self, self._ctx, _parentState)
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expr, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [OurLanguageParser.INT]:
                localctx = OurLanguageParser.IntContext(self, localctx)
                self._ctx = localctx

                self.state = 64
                self.match(OurLanguageParser.INT)
            elif token in [OurLanguageParser.VAR]:
                localctx = OurLanguageParser.VarContext(self, localctx)
                self._ctx = localctx
                self.state = 65
                self.match(OurLanguageParser.VAR)
            elif token in [OurLanguageParser.STRING]:
                localctx = OurLanguageParser.StringContext(self, localctx)
                self._ctx = localctx
                self.state = 66
                self.match(OurLanguageParser.STRING)
            elif token in [OurLanguageParser.T__2]:
                localctx = OurLanguageParser.ParensExprContext(self, localctx)
                self._ctx = localctx
                self.state = 67
                self.match(OurLanguageParser.T__2)
                self.state = 68
                self.expr(0)
                self.state = 69
                self.match(OurLanguageParser.T__3)
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 81
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 5, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    self.state = 79
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 4, self._ctx)
                    if la_ == 1:
                        localctx = OurLanguageParser.MuldivExprContext(
                            self,
                            OurLanguageParser.ExprContext(
                                self, _parentctx, _parentState
                            ),
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_expr
                        )
                        self.state = 73
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 6)"
                            )
                        self.state = 74
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not (
                            _la == OurLanguageParser.MUL or _la == OurLanguageParser.DIV
                        ):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 75
                        self.expr(7)

                    elif la_ == 2:
                        localctx = OurLanguageParser.AddsubExprContext(
                            self,
                            OurLanguageParser.ExprContext(
                                self, _parentctx, _parentState
                            ),
                        )
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_expr
                        )
                        self.state = 76
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 5)"
                            )
                        self.state = 77
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not (
                            _la == OurLanguageParser.ADD or _la == OurLanguageParser.SUB
                        ):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 78
                        self.expr(6)

                self.state = 83
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 5, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx: ExprContext, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 6)

        if predIndex == 1:
            return self.precpred(self._ctx, 5)
