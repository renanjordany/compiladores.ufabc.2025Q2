grammar Zeta;

prog : 'programa' declara bloco 'fimprog' ;

declara : 'declare' ID (',' ID)* '.' ;

bloco : cmd+ ;

cmd : cmdLeitura
    | cmdEscrita
    | cmdExpr
    | cmdIf
    | cmdEnquanto
    ;

cmdLeitura : 'leia' '(' ID ')' '.' ;
cmdEscrita : 'escreva' '(' (ID | TEXTO) ')' '.' ;
cmdExpr : ID ':=' expr '.' ;
cmdIf : 'se' '(' cond ')' 'entao' '{' bloco '}' ('senao' '{' bloco '}')? ;
cmdEnquanto : 'enquanto' '(' cond ')' '{' bloco '}' ;

cond : expr op_rel expr ;

op_rel : '<' | '>' | '<=' | '>=' | '==' | '!=' ;

expr : termo (( '+' | '-' ) termo)* ;
termo : fator (( '*' | '/' ) fator)* ;
fator : NUM | ID | '(' expr ')' ;

ID : [a-zA-Z][a-zA-Z0-9]* ;
NUM : [0-9]+ ('.' [0-9]+)? ;
TEXTO : '"' (~["\r\n])* '"' ;

WS : [ \t\r\n]+ -> skip ;

