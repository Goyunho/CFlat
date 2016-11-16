grammar cflat;

//File 전체
run
    : frame EOF
    ;

//전체적인 틀, 구조
frame
    : group+
    ;
/*
//제어문
statement
    : iterationStatement
    | selectionStatement
    ;
// - 반복문
iterationStatement
    :   While Leftparen Calculator_logic Rightparen group
    |   'do' group While Leftparen Calculator_logic Rightparen Semi
    |   'for' Leftparen (Calculator_logic|Assignment)? Semi 
                Calculator_logic? Semi 
                (Calculator_logic|Assignment)? 
                Rightparen group
    ;
// - 조건문
selectionStatement
    :   'if' '(' Calculator_logic ')' group ('else' group)?
    |   'switch' '(' Calculator_logic ')' Leftbrace switch_group+ Rightbrace
    ;
// - - switch 그룹
switch_group
    : (
        Case Value
        | Default
      ) Colon line* (Break|RETURN)?
    ;
// - 이동제어
jumpStatement
    :   Continue
    |   Break
    |   RETURN Value?
    ;
 */
//하위 영역 (if, while, function 등)
group
    : brace_group
//    | statement
    | line
    ;

//영역(그룹)
brace_group
    : Leftbrace group* Rightbrace
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
//    | jumpStatement
    ;

action
    : Initialisation
    | Assignment
    | Declaration
    | Calculator
    ;

//초기화
Initialisation
    : Type Assignment
    ;

//대입
Assignment
    : Valiable Assign ( Calculator | Valiable )
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
    | Valiable
    ;

//연산
Calculator
    : Calculator_bit
    | Calculator_logic
    | Calculator_pmad
    | Value
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
    : Value (Logic Value)?
    | Not Value
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
NULL : ('null'|'NULL'|'Null');

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
Bit
    : And
    | Or
    | Caret
    | Leftshift
    | Rightshift
    ;
And : '&' ;
Or : '|' ;
Caret : '^' ;
Leftshift : '<<' ;
Rightshift : '>>' ;
Logic
    : Andand
    | Oror
    | Equal
    | Notequal
    | Less
    | Lessequal
    | Greater
    | Greaterequal
    ;
Andand : '&&' ;
Oror : '||' ;
Not : '!' ;
Equal : '==' ;
Notequal : '!=' ;
Less : '<' ;
Lessequal : '<=' ;
Greater : '>' ;
Greaterequal : '>=' ;
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
