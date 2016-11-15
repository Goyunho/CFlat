grammar cflat;

run
    : line? EOF
    ;
/*
//영역(그룹)
brace_group
    : leftbrace
    ;
 */

line
    : action_end+ Newline?
    ;

action_end
    : ( 
        Initialisation
        | Assignment
        | Declaration
        | Value
      ) Semi
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
plus : '+' ;
increase : '++' ;
minus : '-' ;
decrease : '--' ;
asterisk : '*' ;
div : '/' ;
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
