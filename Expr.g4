grammar Expr;

prog: statement+;

statement:
	letStatement ';'		 						#let
	| printStatement ';'							#print
	| pushStatement ';'  							#push
	| equalStatement ';'							#equal
	| NEWLINE 										#blankStatement
	;

letStatement:
	LET VAR '=' expr 								#letExprFunc
	| LET VAR '=' POP '(' ')' 						#letPopFunc
	| LET VAR '=' equalStatement					#letEqualStatement
	;

printStatement:
	PRINT '(' expr ')' 								#printFunc
	;

pushStatement:
	PUSH '(' expr ')' 								#pushFunc
	;

equalStatement:
	EQUAL '(' expr ',' expr ')' 					#equalFunc
	;

expr:
	expr op=('*'|'/') expr   						#muldivExpr
    | expr op=('+'|'-') expr   						#addsubExpr
    | INT                               			#int
	| VAR											#var
	| STRING										#string
    | '(' expr ')'                      			#parensExpr
    ;

LET : ('LET'|'let') ;
PRINT : ('PRINT'|'print') ;
PUSH: ('PUSH'|'push');
POP: ('POP'|'pop');
EQUAL: ('EQUAL'|'equal');

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

NEWLINE : [\r\n]+;
VAR		: [a-zA-Z_]+;
STRING	: '\''([a-zA-Z0-9]|(' '| '\t'))+'\'';
INT     : [0-9]+ ;
WS      : [ \t]+ -> skip;
