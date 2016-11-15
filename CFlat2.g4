grammar CFlat;

run
    : translationUnit+
    ;

primaryExpression
    :   Identifier
    |   StringLiteral+
    |   '(' expression ')'
    |   genericSelection
    |   '__extension__'? '(' compoundStatement ')' 
    |   '__builtin_va_arg' '(' unaryExpression ',' typeName ')'
    |   '__builtin_offsetof' '(' typeName ',' unaryExpression ')'
    ;

genericSelection
    :   '_Generic' '(' assignmentExpression ',' genericAssocList ')'
    ;

genericAssocList
    :   genericAssociation
    |   genericAssocList ',' genericAssociation
    ;

genericAssociation
    :   typeName ':' assignmentExpression
    |   'default' ':' assignmentExpression
    ;

typeName
    :   specifierQualifierList
    ;

specifierQualifierList
    :   typeSpecifier specifierQualifierList?
    ;

postfixExpression
    :   primaryExpression
    |   postfixExpression '[' expression ']'
    |   postfixExpression '(' argumentExpressionList? ')'
    |   postfixExpression '.' Identifier
    |   postfixExpression '++'
    |   postfixExpression '--'
    |   '(' typeName ')' '{' initializerList '}'
    |   '(' typeName ')' '{' initializerList ',' '}'
    |   '__extension__' '(' typeName ')' '{' initializerList '}'
    |   '__extension__' '(' typeName ')' '{' initializerList ',' '}'
    ;

argumentExpressionList
    :   assignmentExpression
    |   argumentExpressionList ',' assignmentExpression
    ;

unaryExpression
    :   postfixExpression
    |   '++' unaryExpression
    |   '--' unaryExpression
    |   unaryOperator unaryExpression
    |   'sizeof' unaryExpression
    |   'sizeof' '(' typeName ')'
    |	'&&' Identifier
    ;

unaryOperator
	: '&' 
	| '*' 
	| '+' 
	| '-' 
	| '~' 
	| '!'
    ;

assignmentOperator
    :   '=' 
    ;

expression
    :   assignmentExpression
    |   expression ',' assignmentExpression
    ;

assignmentExpression
    :  unaryExpression assignmentOperator assignmentExpression
    ;

multiplicativeExpression
    :   unaryExpression
    |   multiplicativeExpression '*' unaryExpression
    |   multiplicativeExpression '/' unaryExpression
    |   multiplicativeExpression '%' unaryExpression
    ;

additiveExpression
    :   multiplicativeExpression
    |   additiveExpression '+' multiplicativeExpression
    |   additiveExpression '-' multiplicativeExpression
    ;

relationalExpression
    :   additiveExpression
    |   relationalExpression '<' additiveExpression
    |   relationalExpression '>' additiveExpression
    |   relationalExpression '<=' additiveExpression
    |   relationalExpression '>=' additiveExpression
    ;

equalityExpression
    :   relationalExpression
    |   equalityExpression '==' relationalExpression
    |   equalityExpression '!=' relationalExpression
    ;

andExpression
    :   equalityExpression
    |   andExpression '&' equalityExpression
    ;

exclusiveOrExpression
    :   andExpression
    |   exclusiveOrExpression '^' andExpression
    ;

inclusiveOrExpression
    :   exclusiveOrExpression
    |   inclusiveOrExpression '|' exclusiveOrExpression
    ;

logicalAndExpression
    :   inclusiveOrExpression
    |   logicalAndExpression '&&' inclusiveOrExpression
    ;

logicalOrExpression
    :   logicalAndExpression
    |   logicalOrExpression '||' logicalAndExpression
    ;

typeSpecifier
    :   'void'
    |   'char'
    |   'short'
    |   'int'
    |   'long'
    |   'float'
    |   'double'
    |   'signed'
    |   'unsigned'
    |   '_Bool'
    |   typedefName
    ;

typedefName
    :   Identifier
    ;

iterationStatement
    :   'while' '(' expression ')' statement
    |   'do' statement 'while' '(' expression ')' ';'
    |   'for' '(' expression? ';' expression? ';' expression? ')' statement
    |   'for' '(' declaration expression? ';' expression? ')' statement
    ;

jumpStatement
    :   'goto' Identifier ';'
    |   'continue' ';'
    |   'break' ';'
    |   'return' expression? ';'
    |   'goto' unaryExpression ';'
    ;

compoundStatement
    :   '{' blockItemList? '}'
    ;

blockItemList
    :   blockItem
    |   blockItemList blockItem
    ;

blockItem
    :   declaration 
    |   statement 
    ;

compilationUnit
    :   translationUnit? EOF
    ;


translationUnit
    :   externalDeclaration
    |   translationUnit externalDeclaration
    ;

declaration
    :   declarationSpecifiers initDeclaratorList? ';'
    |   staticAssertDeclaration
    ;

staticAssertDeclaration
    :   '_Static_assert' '(' constantExpression ',' StringLiteral+ ')' ';'
    ;

initDeclaratorList
    :   initDeclarator
    |   initDeclaratorList ',' initDeclarator
    ;

externalDeclaration
    :   functionDefinition
    |   declaration
    |   ';' // stray ;
    ;

functionDefinition
    :   declarationSpecifiers? declarator declaration? compoundStatement
    ;

declarator
    :   directDeclarator 
    ;

directDeclarator
    :   Identifier
    |   '(' declarator ')'
    |   directDeclarator '[' typeQualifierList? assignmentExpression? ']'
    |   directDeclarator '[' 'static' typeQualifierList? assignmentExpression ']'
    |   directDeclarator '[' typeQualifierList 'static' assignmentExpression ']'
    |   directDeclarator '[' typeQualifierList? '*' ']'
    |   directDeclarator '(' parameterTypeList ')'
    |   directDeclarator '(' identifierList? ')'
    ;
    
identifierList
    :   Identifier
    |   identifierList ',' Identifier
    ;

typeQualifierList
    :   typeQualifier
    |   typeQualifierList typeQualifier
    ;

typeQualifier
    :   'const'
    ;

parameterTypeList
    :   parameterList
    |   parameterList ',' '...'
    ;

parameterList
    :   parameterDeclaration
    |   parameterList ',' parameterDeclaration
    ;

parameterDeclaration
    :   declarationSpecifiers declarator
    |   declarationSpecifiers2 
    ;

declarationList
    :   declaration
    |   declarationList declaration
    ;

declarationSpecifiers
    :   declarationSpecifier+
    ;

declarationSpecifiers2
    :   declarationSpecifier+
    ;

declarationSpecifier
    :   storageClassSpecifier
    |   typeSpecifier
    |   typeQualifier
    |   functionSpecifier
    ;

functionSpecifier
    :   ('inline'
    |   '_Noreturn'
    |   '__inline__' 
    |   '__stdcall')
    |   '__declspec' '(' Identifier ')'
    ;


storageClassSpecifier
    :   'typedef'
    |   'static'
    ;

initDeclarator
    :   declarator
    |   declarator '=' initializer
    ;

constantExpression
    :   conditionalExpression
    ;

conditionalExpression
    :   logicalOrExpression ('?' expression ':' conditionalExpression)?
    ;

initializer
    :   assignmentExpression
    |   '{' initializerList '}'
    |   '{' initializerList ',' '}'
    ;

initializerList
    :   designation? initializer
    |   initializerList ',' designation? initializer
    ;

designation
    :   designatorList '='
    ;

designatorList
    :   designator
    |   designatorList designator
    ;

designator
    :   '[' constantExpression ']'
    |   '.' Identifier
    ;

statement
    :   labeledStatement
    |   compoundStatement
    |   expressionStatement
    |   selectionStatement
    |   iterationStatement
    |   jumpStatement
    |   '(' (logicalOrExpression (',' logicalOrExpression)*)? (':' (logicalOrExpression (',' logicalOrExpression)*)?)* ')' ';'
    ;

expressionStatement
    :   expression? ';'
    ;

selectionStatement
    :   'if' '(' expression ')' statement ('else' statement)?
    |   'switch' '(' expression ')' statement
    ;    

labeledStatement
    :   Identifier ':' statement
    |   'case' constantExpression ':' statement
    |   'default' ':' statement
    ;


Break : 'break';
Case : 'case';
Char : 'char';
Const : 'const';
Continue : 'continue';
Default : 'default';
Do : 'do';
Double : 'double';
Else : 'else';
Extern : 'extern';
Float : 'float';
For : 'for';
Goto : 'goto';
If : 'if';
Int : 'int';
Inline : 'inline';
Long : 'long';
Return : 'return';
Short : 'short';
Signed : 'signed';
Sizeof : 'sizeof';
Switch : 'switch';
Typedef : 'typedef';
Unsigned : 'unsigned';
Void : 'void';
While : 'while';

Bool : '_Bool';
Generic : '_Generic';
Noreturn : '_Noreturn';
StaticAssert : '_Static_assert';

LeftParen : '(';
RightParen : ')';
LeftBracket : '[';
RightBracket : ']';
LeftBrace : '{';
RightBrace : '}';

Less : '<';
LessEqual : '<=';
Greater : '>';
GreaterEqual : '>=';

Plus : '+';
PlusPlus : '++';
Minus : '-';
MinusMinus : '--';
Star : '*';
Div : '/';
Mod : '%';

And : '&';
Or : '|';
AndAnd : '&&';
OrOr : '||';
Caret : '^';
Not : '!';

Colon : ':';
Semi : ';';
Comma : ',';

Assign : '=';

Equal : '==';
NotEqual : '!=';

Dot : '.';

Identifier
    :   IdentifierNondigit
        (   IdentifierNondigit
        |   Digit
        )*
    ;

fragment
IdentifierNondigit
    :   Nondigit
    |   UniversalCharacterName
    //|   // other implementation-defined characters...
    ;

fragment
Nondigit
    :   [a-zA-Z_]
    ;

fragment
Digit
    :   [0-9]
    ;

fragment
UniversalCharacterName
    :   '\\u' HexQuad
    |   '\\U' HexQuad HexQuad
    ;

fragment
HexQuad
    :   HexadecimalDigit HexadecimalDigit HexadecimalDigit HexadecimalDigit
    ;

Constant
    :   IntegerConstant
    |   FloatingConstant
    //|   EnumerationConstant
    |   CharacterConstant
    ;

fragment
IntegerConstant
    :   DecimalConstant IntegerSuffix?
    |   OctalConstant IntegerSuffix?
    |   HexadecimalConstant IntegerSuffix?
    |   BinaryConstant
    ;

fragment
BinaryConstant
    :   '0' [bB] [0-1]+
    ;

fragment
DecimalConstant
    :   NonzeroDigit Digit*
    ;

fragment
OctalConstant
    :   '0' OctalDigit*
    ;

fragment
HexadecimalConstant
    :   HexadecimalPrefix HexadecimalDigit+
    ;

fragment
HexadecimalPrefix
    :   '0' [xX]
    ;

fragment
NonzeroDigit
    :   [1-9]
    ;

fragment
OctalDigit
    :   [0-7]
    ;

fragment
HexadecimalDigit
    :   [0-9a-fA-F]
    ;

fragment
IntegerSuffix
    :   UnsignedSuffix LongSuffix?
    |   UnsignedSuffix LongLongSuffix
    |   LongSuffix UnsignedSuffix?
    |   LongLongSuffix UnsignedSuffix?
    ;

fragment
UnsignedSuffix
    :   [uU]
    ;

fragment
LongSuffix
    :   [lL]
    ;

fragment
LongLongSuffix
    :   'll' | 'LL'
    ;

fragment
FloatingConstant
    :   DecimalFloatingConstant
    |   HexadecimalFloatingConstant
    ;

fragment
DecimalFloatingConstant
    :   FractionalConstant ExponentPart? FloatingSuffix?
    |   DigitSequence ExponentPart FloatingSuffix?
    ;

fragment
HexadecimalFloatingConstant
    :   HexadecimalPrefix HexadecimalFractionalConstant BinaryExponentPart FloatingSuffix?
    |   HexadecimalPrefix HexadecimalDigitSequence BinaryExponentPart FloatingSuffix?
    ;

fragment
FractionalConstant
    :   DigitSequence? '.' DigitSequence
    |   DigitSequence '.'
    ;

fragment
ExponentPart
    :   'e' Sign? DigitSequence
    |   'E' Sign? DigitSequence
    ;

fragment
Sign
    :   '+' | '-'
    ;

fragment
DigitSequence
    :   Digit+
    ;

fragment
HexadecimalFractionalConstant
    :   HexadecimalDigitSequence? '.' HexadecimalDigitSequence
    |   HexadecimalDigitSequence '.'
    ;

fragment
BinaryExponentPart
    :   'p' Sign? DigitSequence
    |   'P' Sign? DigitSequence
    ;

fragment
HexadecimalDigitSequence
    :   HexadecimalDigit+
    ;

fragment
FloatingSuffix
    :   'f' | 'l' | 'F' | 'L'
    ;

fragment
CharacterConstant
    :   '\'' CCharSequence '\''
    |   'L\'' CCharSequence '\''
    |   'u\'' CCharSequence '\''
    |   'U\'' CCharSequence '\''
    ;

fragment
CCharSequence
    :   CChar+
    ;

fragment
CChar
    :   ~['\\\r\n]
    |   EscapeSequence
    ;
fragment
EscapeSequence
    :   SimpleEscapeSequence
    |   OctalEscapeSequence
    |   HexadecimalEscapeSequence
    |   UniversalCharacterName
    ;
fragment
SimpleEscapeSequence
    :   '\\' ['"?abfnrtv\\]
    ;
fragment
OctalEscapeSequence
    :   '\\' OctalDigit
    |   '\\' OctalDigit OctalDigit
    |   '\\' OctalDigit OctalDigit OctalDigit
    ;
fragment
HexadecimalEscapeSequence
    :   '\\x' HexadecimalDigit+
    ;
StringLiteral
    :   EncodingPrefix? '"' SCharSequence? '"'
    ;
fragment
EncodingPrefix
    :   'u8'
    |   'u'
    |   'U'
    |   'L'
    ;
fragment
SCharSequence
    :   SChar+
    ;
fragment
SChar
    :   ~["\\\r\n]
    |   EscapeSequence
    |   '\\\n'   // Added line
    |   '\\\r\n' // Added line
    ;

ComplexDefine
    :   '#' Whitespace? 'define'  ~[#]*
        -> skip
    ;

ComplexDefine
    :   '#' Whitespace? 'define'  ~[#]*
        -> skip
    ;

LineAfterPreprocessing
    :   '#line' Whitespace* ~[\r\n]*
        -> skip
    ;  

LineDirective
    :   '#' Whitespace? DecimalConstant Whitespace? StringLiteral ~[\r\n]*
        -> skip
    ;

PragmaDirective
    :   '#' Whitespace? 'pragma' Whitespace ~[\r\n]*
        -> skip
    ;

Whitespace
    :   [ \t]+
        -> skip
    ;

Newline
    :   (   '\r' '\n'?
        |   '\n'
        )
        -> skip
    ;

BlockComment
    :   '/*' .*? '*/'
        -> skip
    ;

LineComment
    :   '//' ~[\r\n]*
        -> skip
    ;




