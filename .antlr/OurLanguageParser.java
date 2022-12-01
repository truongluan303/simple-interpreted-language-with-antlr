// Generated from c:\Users\hoang\Desktop\Workspace\antlr\OurLanguage.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class OurLanguageParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, LET=6, PRINT=7, PUSH=8, POP=9,
		COMPARE=10, ADD=11, SUB=12, MUL=13, DIV=14, NEWLINE=15, VAR=16, STRING=17,
		INT=18, WS=19;
	public static final int
		RULE_prog = 0, RULE_statement = 1, RULE_letStatement = 2, RULE_printStatement = 3,
		RULE_pushStatement = 4, RULE_compareStatement = 5, RULE_expr = 6;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "statement", "letStatement", "printStatement", "pushStatement",
			"compareStatement", "expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'='", "'('", "')'", "','", null, null, null, null, null,
			"'+'", "'-'", "'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, "LET", "PRINT", "PUSH", "POP", "COMPARE",
			"ADD", "SUB", "MUL", "DIV", "NEWLINE", "VAR", "STRING", "INT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "OurLanguage.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public OurLanguageParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(15);
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(14);
				statement();
				}
				}
				setState(17);
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << LET) | (1L << PRINT) | (1L << PUSH) | (1L << COMPARE) | (1L << NEWLINE))) != 0) );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }

		public StatementContext() { }
		public void copyFrom(StatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class PrintContext extends StatementContext {
		public PrintStatementContext printStatement() {
			return getRuleContext(PrintStatementContext.class,0);
		}
		public PrintContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class CompareContext extends StatementContext {
		public CompareStatementContext compareStatement() {
			return getRuleContext(CompareStatementContext.class,0);
		}
		public CompareContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class BlankStatementContext extends StatementContext {
		public TerminalNode NEWLINE() { return getToken(OurLanguageParser.NEWLINE, 0); }
		public BlankStatementContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class LetContext extends StatementContext {
		public LetStatementContext letStatement() {
			return getRuleContext(LetStatementContext.class,0);
		}
		public LetContext(StatementContext ctx) { copyFrom(ctx); }
	}
	public static class PushContext extends StatementContext {
		public PushStatementContext pushStatement() {
			return getRuleContext(PushStatementContext.class,0);
		}
		public PushContext(StatementContext ctx) { copyFrom(ctx); }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_statement);
		try {
			setState(32);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case LET:
				_localctx = new LetContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(19);
				letStatement();
				setState(20);
				match(T__0);
				}
				break;
			case PRINT:
				_localctx = new PrintContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(22);
				printStatement();
				setState(23);
				match(T__0);
				}
				break;
			case PUSH:
				_localctx = new PushContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(25);
				pushStatement();
				setState(26);
				match(T__0);
				}
				break;
			case COMPARE:
				_localctx = new CompareContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(28);
				compareStatement();
				setState(29);
				match(T__0);
				}
				break;
			case NEWLINE:
				_localctx = new BlankStatementContext(_localctx);
				enterOuterAlt(_localctx, 5);
				{
				setState(31);
				match(NEWLINE);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LetStatementContext extends ParserRuleContext {
		public LetStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_letStatement; }

		public LetStatementContext() { }
		public void copyFrom(LetStatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class LetPopFuncContext extends LetStatementContext {
		public TerminalNode LET() { return getToken(OurLanguageParser.LET, 0); }
		public TerminalNode VAR() { return getToken(OurLanguageParser.VAR, 0); }
		public TerminalNode POP() { return getToken(OurLanguageParser.POP, 0); }
		public LetPopFuncContext(LetStatementContext ctx) { copyFrom(ctx); }
	}
	public static class LetExprFuncContext extends LetStatementContext {
		public TerminalNode LET() { return getToken(OurLanguageParser.LET, 0); }
		public TerminalNode VAR() { return getToken(OurLanguageParser.VAR, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public LetExprFuncContext(LetStatementContext ctx) { copyFrom(ctx); }
	}

	public final LetStatementContext letStatement() throws RecognitionException {
		LetStatementContext _localctx = new LetStatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_letStatement);
		try {
			setState(44);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				_localctx = new LetExprFuncContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(34);
				match(LET);
				setState(35);
				match(VAR);
				setState(36);
				match(T__1);
				setState(37);
				expr(0);
				}
				break;
			case 2:
				_localctx = new LetPopFuncContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(38);
				match(LET);
				setState(39);
				match(VAR);
				setState(40);
				match(T__1);
				setState(41);
				match(POP);
				setState(42);
				match(T__2);
				setState(43);
				match(T__3);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PrintStatementContext extends ParserRuleContext {
		public PrintStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_printStatement; }

		public PrintStatementContext() { }
		public void copyFrom(PrintStatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class PrintFuncContext extends PrintStatementContext {
		public TerminalNode PRINT() { return getToken(OurLanguageParser.PRINT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public PrintFuncContext(PrintStatementContext ctx) { copyFrom(ctx); }
	}

	public final PrintStatementContext printStatement() throws RecognitionException {
		PrintStatementContext _localctx = new PrintStatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_printStatement);
		try {
			_localctx = new PrintFuncContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			match(PRINT);
			setState(47);
			match(T__2);
			setState(48);
			expr(0);
			setState(49);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PushStatementContext extends ParserRuleContext {
		public PushStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pushStatement; }

		public PushStatementContext() { }
		public void copyFrom(PushStatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class PushFuncContext extends PushStatementContext {
		public TerminalNode PUSH() { return getToken(OurLanguageParser.PUSH, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public PushFuncContext(PushStatementContext ctx) { copyFrom(ctx); }
	}

	public final PushStatementContext pushStatement() throws RecognitionException {
		PushStatementContext _localctx = new PushStatementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_pushStatement);
		try {
			_localctx = new PushFuncContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			match(PUSH);
			setState(52);
			match(T__2);
			setState(53);
			expr(0);
			setState(54);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CompareStatementContext extends ParserRuleContext {
		public CompareStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compareStatement; }

		public CompareStatementContext() { }
		public void copyFrom(CompareStatementContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class CompareFuncContext extends CompareStatementContext {
		public TerminalNode COMPARE() { return getToken(OurLanguageParser.COMPARE, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public CompareFuncContext(CompareStatementContext ctx) { copyFrom(ctx); }
	}

	public final CompareStatementContext compareStatement() throws RecognitionException {
		CompareStatementContext _localctx = new CompareStatementContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_compareStatement);
		try {
			_localctx = new CompareFuncContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(56);
			match(COMPARE);
			setState(57);
			match(T__2);
			setState(58);
			expr(0);
			setState(59);
			match(T__4);
			setState(60);
			expr(0);
			setState(61);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }

		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class StringContext extends ExprContext {
		public TerminalNode STRING() { return getToken(OurLanguageParser.STRING, 0); }
		public StringContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class MuldivExprContext extends ExprContext {
		public Token op;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MUL() { return getToken(OurLanguageParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(OurLanguageParser.DIV, 0); }
		public MuldivExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class VarContext extends ExprContext {
		public TerminalNode VAR() { return getToken(OurLanguageParser.VAR, 0); }
		public VarContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class AddsubExprContext extends ExprContext {
		public Token op;
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode ADD() { return getToken(OurLanguageParser.ADD, 0); }
		public TerminalNode SUB() { return getToken(OurLanguageParser.SUB, 0); }
		public AddsubExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class ParensExprContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ParensExprContext(ExprContext ctx) { copyFrom(ctx); }
	}
	public static class IntContext extends ExprContext {
		public TerminalNode INT() { return getToken(OurLanguageParser.INT, 0); }
		public IntContext(ExprContext ctx) { copyFrom(ctx); }
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 12;
		enterRecursionRule(_localctx, 12, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				{
				_localctx = new IntContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(64);
				match(INT);
				}
				break;
			case VAR:
				{
				_localctx = new VarContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(65);
				match(VAR);
				}
				break;
			case STRING:
				{
				_localctx = new StringContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(66);
				match(STRING);
				}
				break;
			case T__2:
				{
				_localctx = new ParensExprContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(67);
				match(T__2);
				setState(68);
				expr(0);
				setState(69);
				match(T__3);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(81);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(79);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
					case 1:
						{
						_localctx = new MuldivExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(73);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(74);
						((MuldivExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==MUL || _la==DIV) ) {
							((MuldivExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(75);
						expr(7);
						}
						break;
					case 2:
						{
						_localctx = new AddsubExprContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(76);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(77);
						((AddsubExprContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==ADD || _la==SUB) ) {
							((AddsubExprContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(78);
						expr(6);
						}
						break;
					}
					}
				}
				setState(83);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 6:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 6);
		case 1:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25W\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\3\2\6\2\22\n\2\r\2\16\2\23"+
		"\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3#\n\3\3\4\3\4"+
		"\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4/\n\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6"+
		"\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3"+
		"\b\5\bJ\n\b\3\b\3\b\3\b\3\b\3\b\3\b\7\bR\n\b\f\b\16\bU\13\b\3\b\2\3\16"+
		"\t\2\4\6\b\n\f\16\2\4\3\2\17\20\3\2\r\16\2Z\2\21\3\2\2\2\4\"\3\2\2\2\6"+
		".\3\2\2\2\b\60\3\2\2\2\n\65\3\2\2\2\f:\3\2\2\2\16I\3\2\2\2\20\22\5\4\3"+
		"\2\21\20\3\2\2\2\22\23\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24\3\3\2\2"+
		"\2\25\26\5\6\4\2\26\27\7\3\2\2\27#\3\2\2\2\30\31\5\b\5\2\31\32\7\3\2\2"+
		"\32#\3\2\2\2\33\34\5\n\6\2\34\35\7\3\2\2\35#\3\2\2\2\36\37\5\f\7\2\37"+
		" \7\3\2\2 #\3\2\2\2!#\7\21\2\2\"\25\3\2\2\2\"\30\3\2\2\2\"\33\3\2\2\2"+
		"\"\36\3\2\2\2\"!\3\2\2\2#\5\3\2\2\2$%\7\b\2\2%&\7\22\2\2&\'\7\4\2\2\'"+
		"/\5\16\b\2()\7\b\2\2)*\7\22\2\2*+\7\4\2\2+,\7\13\2\2,-\7\5\2\2-/\7\6\2"+
		"\2.$\3\2\2\2.(\3\2\2\2/\7\3\2\2\2\60\61\7\t\2\2\61\62\7\5\2\2\62\63\5"+
		"\16\b\2\63\64\7\6\2\2\64\t\3\2\2\2\65\66\7\n\2\2\66\67\7\5\2\2\678\5\16"+
		"\b\289\7\6\2\29\13\3\2\2\2:;\7\f\2\2;<\7\5\2\2<=\5\16\b\2=>\7\7\2\2>?"+
		"\5\16\b\2?@\7\6\2\2@\r\3\2\2\2AB\b\b\1\2BJ\7\24\2\2CJ\7\22\2\2DJ\7\23"+
		"\2\2EF\7\5\2\2FG\5\16\b\2GH\7\6\2\2HJ\3\2\2\2IA\3\2\2\2IC\3\2\2\2ID\3"+
		"\2\2\2IE\3\2\2\2JS\3\2\2\2KL\f\b\2\2LM\t\2\2\2MR\5\16\b\tNO\f\7\2\2OP"+
		"\t\3\2\2PR\5\16\b\bQK\3\2\2\2QN\3\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2"+
		"T\17\3\2\2\2US\3\2\2\2\b\23\".IQS";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
