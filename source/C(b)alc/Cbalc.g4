grammar Cbalc; 

//prog:   stat+ EOF ;
prog:   line+ ;

//라인 종료
line : mulstat NEWLINE ;

//stat 연결
mulstat: stat (',' stat)* ;

//행동 정의
stat:   expr                 # lavel_no
    |   showme               # lavel_no
    |   ID '=' expr          # assign
    |   NEWLINE                     # blank
    ;

//print 함수 만듦
showme
    : 'print(' expr ')'
    ;

//value
expr:   expr op=('*'|'/') expr      # MulDiv
    |   expr op=('+'|'-') expr      # AddSub
    |   INT                         # int
    |   ID                          # id
    |   '(' expr ')'                # parens
    ;

//Valiable
ID  :   WORD+ (INT|WORD|'_')* ; 

MUL :   '*' ; // assigns token name to '*' used above in grammar
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
WORD:   [a-zA-Z]+ ;      // match identifiers
//FLAOT : INT '.' INT
INT :   [0-9]+ ;         // match integers
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
