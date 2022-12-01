// Generated from c:\Users\hoang\Desktop\Workspace\antlr\Expr.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class ExprLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, LET=6, PRINT=7, PUSH=8, POP=9,
		EQUAL=10, ADD=11, SUB=12, MUL=13, DIV=14, NEWLINE=15, VAR=16, STRING=17,
		INT=18, WS=19;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "LET", "PRINT", "PUSH", "POP",
			"EQUAL", "ADD", "SUB", "MUL", "DIV", "NEWLINE", "VAR", "STRING", "INT",
			"WS"
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
			null, null, null, null, null, null, "LET", "PRINT", "PUSH", "POP", "EQUAL",
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


	public ExprLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Expr.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25\u008b\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\4\24\t\24\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7"+
		"\3\7\3\7\3\7\3\7\3\7\5\7:\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b"+
		"\5\bF\n\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tP\n\t\3\n\3\n\3\n\3\n\3\n"+
		"\3\n\5\nX\n\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\5\13d"+
		"\n\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\6\20o\n\20\r\20\16\20p"+
		"\3\21\6\21t\n\21\r\21\16\21u\3\22\3\22\6\22z\n\22\r\22\16\22{\3\22\3\22"+
		"\3\23\6\23\u0081\n\23\r\23\16\23\u0082\3\24\6\24\u0086\n\24\r\24\16\24"+
		"\u0087\3\24\3\24\2\2\25\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f"+
		"\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25\3\2\7\4\2\f\f\17\17\5\2"+
		"C\\aac|\7\2\13\13\"\"\62;C\\c|\3\2\62;\4\2\13\13\"\"\2\u0094\2\3\3\2\2"+
		"\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3"+
		"\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2"+
		"\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2"+
		"\2\2\2\'\3\2\2\2\3)\3\2\2\2\5+\3\2\2\2\7-\3\2\2\2\t/\3\2\2\2\13\61\3\2"+
		"\2\2\r9\3\2\2\2\17E\3\2\2\2\21O\3\2\2\2\23W\3\2\2\2\25c\3\2\2\2\27e\3"+
		"\2\2\2\31g\3\2\2\2\33i\3\2\2\2\35k\3\2\2\2\37n\3\2\2\2!s\3\2\2\2#w\3\2"+
		"\2\2%\u0080\3\2\2\2\'\u0085\3\2\2\2)*\7=\2\2*\4\3\2\2\2+,\7?\2\2,\6\3"+
		"\2\2\2-.\7*\2\2.\b\3\2\2\2/\60\7+\2\2\60\n\3\2\2\2\61\62\7.\2\2\62\f\3"+
		"\2\2\2\63\64\7N\2\2\64\65\7G\2\2\65:\7V\2\2\66\67\7n\2\2\678\7g\2\28:"+
		"\7v\2\29\63\3\2\2\29\66\3\2\2\2:\16\3\2\2\2;<\7R\2\2<=\7T\2\2=>\7K\2\2"+
		">?\7P\2\2?F\7V\2\2@A\7r\2\2AB\7t\2\2BC\7k\2\2CD\7p\2\2DF\7v\2\2E;\3\2"+
		"\2\2E@\3\2\2\2F\20\3\2\2\2GH\7R\2\2HI\7W\2\2IJ\7U\2\2JP\7J\2\2KL\7r\2"+
		"\2LM\7w\2\2MN\7u\2\2NP\7j\2\2OG\3\2\2\2OK\3\2\2\2P\22\3\2\2\2QR\7R\2\2"+
		"RS\7Q\2\2SX\7R\2\2TU\7r\2\2UV\7q\2\2VX\7r\2\2WQ\3\2\2\2WT\3\2\2\2X\24"+
		"\3\2\2\2YZ\7G\2\2Z[\7S\2\2[\\\7W\2\2\\]\7C\2\2]d\7N\2\2^_\7g\2\2_`\7s"+
		"\2\2`a\7w\2\2ab\7c\2\2bd\7n\2\2cY\3\2\2\2c^\3\2\2\2d\26\3\2\2\2ef\7-\2"+
		"\2f\30\3\2\2\2gh\7/\2\2h\32\3\2\2\2ij\7,\2\2j\34\3\2\2\2kl\7\61\2\2l\36"+
		"\3\2\2\2mo\t\2\2\2nm\3\2\2\2op\3\2\2\2pn\3\2\2\2pq\3\2\2\2q \3\2\2\2r"+
		"t\t\3\2\2sr\3\2\2\2tu\3\2\2\2us\3\2\2\2uv\3\2\2\2v\"\3\2\2\2wy\7)\2\2"+
		"xz\t\4\2\2yx\3\2\2\2z{\3\2\2\2{y\3\2\2\2{|\3\2\2\2|}\3\2\2\2}~\7)\2\2"+
		"~$\3\2\2\2\177\u0081\t\5\2\2\u0080\177\3\2\2\2\u0081\u0082\3\2\2\2\u0082"+
		"\u0080\3\2\2\2\u0082\u0083\3\2\2\2\u0083&\3\2\2\2\u0084\u0086\t\6\2\2"+
		"\u0085\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087\u0085\3\2\2\2\u0087\u0088"+
		"\3\2\2\2\u0088\u0089\3\2\2\2\u0089\u008a\b\24\2\2\u008a(\3\2\2\2\16\2"+
		"9EOWcpuy{\u0082\u0087\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
