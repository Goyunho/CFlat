grammar cflat;

//File 전체
run
    : frame EOF
    ;

//전체적인 틀, 구조
frame
    : (line|brace_group)+
    ;

//조건문
iterationStatement
    :   'while' '(' Calculator_logic ')' brace_group
    |   'do' brace_group 'while' '(' Calculator_logic ')' ';'
    |   'for' '(' (Calculator_logic|Assignment)? ';' Calculator_logic? ';' (Calculator_logic|Assignment)? ')' brace_group
    ;

//영역(그룹)
brace_group
    : Leftbrace (line|brace_group)* Rightbrace
    ;

//한줄 끝
line
    : action_end+ Newline?
    ;

//액션의 끝;
action_end
    : actions Semi
    ;

actions
    : action (Coma action)*
    ;

action
    : Initialisation
    | Assignment
    | Declaration
    | Value
    | Calculator
    ;

//초기화
Initialisation
    : Type Assignment
    ;

//대입
Assignment
    : Valiable Assign ( Value | Valiable )
    ;

//선언
Declaration : Type Whitespace Valiable ;

//값 구분
Value
    : Val_int
    | Val_float
    | Val_string
    | Val_boolean
    | Val_void
    | Calculator
    | Valiable
    ;

//연산
Calculator
    : Calculator_bit
    | Calculator_logic
    | Calculator_pmad
    ;
// - 사칙연산
Calculator_pmad
    : (Val_int|Val_float) (Plus|Minus) (Val_int|Val_float|Calculator_pmad)
    | (Val_int|Val_float) (Asterisk|Div) (Val_int|Val_float|Calculator_pmad)
    ;
// - 비트연산
Calculator_bit
    : Val_int (And|Or|Caret) Val_int
    ;
// - 논리연산
Calculator_logic
    : (TRUE|FALSE) (Andand|Oror|Equal|Notequal|Less|Lessequal|Greater|Greaterequal) (TRUE|FALSE)
    | Not (TRUE|FALSE)
    ;

//변수명
Valiable : (Nondigit|Digit)+ ;

//값/타입
Val_int : Digit+ ;
Val_float : Val_int Dot Val_int ;
Val_string : '"' .*? '"' ;
Val_boolean : (TRUE|FALSE) ;
Val_void : 'void' ;
// - 세부 요소
Digit : [0-9] ;
Nondigit : [a-zA-Z_] ;

//예약어
// - 조건, 행동
Case : 'case' ;
Break : 'break' ;
Continue : 'continue' ;
Default : 'default' ;
For : 'for' ;
While : 'while' ;
If : 'if' ;
Else : 'else' ;
RETURN : 'return' ;
Switch : 'switch' ;
// - 타입
Type
    : Int
    | Float
    | String
    | Boolean
    | Void
    ;
Int : 'int' ;
Float : 'float' ;
String : 'string' ;
Boolean : 'boolean' ;
Void : 'void' ;

//상수
TRUE : ('true'|'Ture'|'TRUE') ;
FALSE : ('false'|'False'|'FALSE') ;

//연산자
// - 산술
Plus : '+' ;
increase : '++' ;
Minus : '-' ;
decrease : '--' ;
Asterisk : '*' ;
Div : '/' ;
percent : '%' ;
// - 논리, 비트
And : '&' ;
Andand : '&&' ;
Or : '|' ;
Oror : '||' ;
Caret : '^' ;
Not : '!' ;
Equal : '==' ;
Notequal : '!=' ;
Less : '<' ;
Lessequal : '<=' ;
Greater : '>' ;
Greaterequal : '>=' ;
Leftshift : '<<' ;
Rightshift : '>>' ;
// - 그 외 기호
Assign : '=' ;
Dot : '.' ;
Colon : ':';
Semi : ';' ;
Coma : ',' ;
Leftparen : '(' ;
Rightparen : ')' ;
Leftbracket : '[' ;
Rightbracket : ']' ;
Leftbrace : '{' ;
Rightbrace : '}' ;

//스킵영역
Whitespace
    : [ \t]+ -> skip
    ;

Newline
    : [\r\n]+ -> skip
    ;

Block_comment
    : '/*' .*? '*/' -> skip
    ;

Line_comment
    : '//' ~[\r\n]* -> skip
    ;
