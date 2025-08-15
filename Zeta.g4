grammar Zeta;

// Parser rules
prog: 'programa' decl bloco 'fimprog' '.' ;

decl: 'declare' ID (',' ID)* '.' ;

bloco: cmd+ ;

cmd
    : cmdLeitura
    | cmdEscrita
    | cmdExpr
    | cmdIf
    | cmdEnquanto
    | cmdFacaEnquanto
    ;

cmdLeitura: 'leia' '(' ID ')' '.' ;
cmdEscrita: 'escreva' '(' (TEXTO | expr) ')' '.' ;
cmdExpr: ID ':=' exprRel '.' ;

cmdIf: 'se' '(' exprRel ')' 'entao' '{' bloco '}' ('senao' '{' bloco '}')? ;
cmdEnquanto: 'enquanto' '(' exprRel ')' '{' bloco '}' ;
cmdFacaEnquanto: 'faça' '{' bloco '}' 'enquanto' '(' exprRel ')' '.' ;

// Expressions
exprRel: expr (( '<' | '>' | '<=' | '>=' | '==' | '!=' ) expr)? ;
expr: term (( '+' | '-' ) term)* ;
term: factor (( '*' | '/' ) factor)* ;
factor: NUM
      | ID
      | '(' expr ')'
      ;

// Lexer rules
NUM: [0-9]+ ('.' [0-9]+)? ;
ID: [a-zA-Z][a-zA-Z0-9]* ;
TEXTO: '"' (~["\r\n])* '"' ;

PLUS: '+' ;
MINUS: '-' ;
MULT: '*' ;
DIV: '/' ;

LT: '<' ;
GT: '>' ;
LE: '<=' ;
GE: '>=' ;
EQ: '==' ;
NEQ: '!=' ;

ASSIGN: ':=' ;
WS: [ \t\r\n]+ -> skip ;

