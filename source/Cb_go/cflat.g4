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
    : action_end+ Newline
    | action_end+
    ;

action_end
    : ( value
      ) Semi
    ;

//값 구분
value
    : v_int
    | v_float
    | v_string
    | v_boolean
    | v_void
    ;

//변수명
valiable : (Nondigit|Digit)+ ;


//값/타입
v_int : Digit+ ;
v_float : v_int Dot v_int ;
v_string : '"' .*? '"' ;
v_boolean : (true|false) ;
v_void : 'void' ;
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
Int : 'int' ;
Float : 'float' ;
String : 'string' ;
Boolean : 'boolean' ;
Void : 'void' ;

//상수
true : ('true'|'Ture'|'TRUE') ;
false : ('false'|'False'|'FALSE') ;

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
