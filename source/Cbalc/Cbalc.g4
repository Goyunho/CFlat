grammar Cbalc; 

prog:   line+ ;

//라인 종료
line : mulstat? NEWLINE ;

//stat 연결
mulstat: stat (',' stat)* ;

//행동 정의
stat:   expr                 # lavel_no1
    |   showme               # lavel_no1
    |   ID '=' expr          # assign
    |   EOF                  # lavel_no1
    ;

//print 함수 만듦
showme
    : 'print(' expr ')'
    ;

//value
expr:   expr op=('*'|'/') expr      # MulDiv
    |   expr op=('+'|'-') expr      # AddSub
    |   NUMBER                      # number
    |   ID                          # id
    |   STRING                      # string
    |   '(' expr ')'                # parens
    ;

//Valiable
ID  :   WORD+ (INT|WORD|'_')* ; 

MUL :   '*' ; // assigns token name to '*' used above in grammar
DIV :   '/' ;
ADD :   '+' ;
SUB :   '-' ;
STRING : '"' .*? '"' ;  //문자열
NUMBER 
    : INT
    | FLAOT
    ;
WORD:   [a-zA-Z]+ ;      // match identifiers
FLAOT : INT '.' INT ;     // match flaot
INT :   [0-9]+ ;         // match integers
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace
COMMENT_LINE : '//' .*? NEWLINE -> skip ; // comment_line
COMMENT_MULLINE : '/*' .*? '*/' -> skip ; // comment_mulline