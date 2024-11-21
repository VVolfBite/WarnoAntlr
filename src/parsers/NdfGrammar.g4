grammar NdfGrammar;

// 此文件用于生成lexer和parser
// 使用命令参考 java -jar .\antlr-4.13.2-complete.jar -Dlanguage=Python3 NdfGrammar.g4 -visitor -o parser

// --- parser rules --- //

// general structure

ndf_file : assignment* EOF;
assignment : normal_assignment | member_assignment | unnamed_assignment | template_assignment;
// 直接用private会导致导出文件使用关键字
private_prefix: K_PRIVATE;
export_prefix: K_EXPORT;
template_prefix: K_TEMPLATE;

r_value : concatination | arithmetic | builtin_type_value | object | normal_assignment | member_assignment | obj_reference_value | nil_value | special_value | replace_value | ID;
object_type : ID;
block : normal_assignment | member_assignment;


normal_assignment : ( export_prefix | private_prefix )? id K_IS r_value;
template_assignment : ( export_prefix | private_prefix )? template_prefix id  vector_value  K_IS r_value;
member_assignment : id '=' ( r_value | normal_assignment );
unnamed_assignment : K_UNNAMED r_value;

object : object_type '(' ( block )* ')';
id : ID (':' builtin_type_label)?;

// operations

arithmetic : '(' arithmetic ')' | arithmetic op arithmetic | '-' arithmetic | atom;
atom : int_value | float_value | hex_value | obj_reference_value;
op: '+' | '-' | '*' | K_DIV;
concatination : concatination '+' concatination | string_value | map_value | vector_value;

// builtin types: labels

builtin_type_label : K_BOOL | K_STRING | K_INT | K_FLOAT | pair_label | list_label | map_label;
pair_label : K_PAIR '<' builtin_type_label ',' builtin_type_label '>';
list_label : K_LIST '<' builtin_type_label '>';
map_label : K_MAP '<' builtin_type_label ',' builtin_type_label '>';

// builtin types: values

builtin_type_value : primitive_value | data_structure_value;
primitive_value: bool_value | string_value | int_value | hex_value | float_value | guid_value;
data_structure_value: pair_value | vector_value | map_value;
nil_value : K_NIL;
bool_value : K_TRUE | K_FALSE;
string_value : STRING;
int_value : INT;
hex_value: HEXNUMBER;
float_value: FLOAT;
guid_value: GUID;
pair_value: '(' r_value ',' r_value ')';
vector_value: '[' (r_value (',' r_value)* ','?)? ']';
map_value: K_MAP '[' (pair_value (',' pair_value)* ','?)? ']';
obj_reference_value: ('$'|'~')?  (ID|'/')* ID | obj_reference_value '|' obj_reference_value;
replace_value: '<' ID  '>';
// special types: values

special_value : rgba_value;
rgba_value : K_RGBA '[' INT ',' INT ',' INT ',' INT ']';

// --- lexer rules --- //

// keywords

K_TRUE : T R U E;
K_FALSE : F A L S E;
K_MAP : M A P;
K_IS : I S;
K_DIV : D I V;

K_NIL : N I L;
K_BOOL : B O O L;
K_STRING : S T R I N G;
K_INT : I N T;
K_FLOAT : F L O A T;

K_PAIR : P A I R;
K_LIST : L I S T;

K_EXPORT : E X P O R T;
K_PRIVATE : P R I V A T E;

K_UNNAMED : U N N A M E D;
K_TEMPLATE : T E M P L A T E;
// special keywords

K_RGBA : R G B A;

// data types

STRING : '"' ( '\\"' | . )*? '"' | '\'' ( '\\\'' | . )*? '\'';
INT : '-'? [0-9]+;
FLOAT: '-'? ( [0-9]+'.'[0-9]* | [0-9]*'.'[0-9]+ );

// @NOTE:部分文件中的GUID使用了大写，因此这里也加上大写规则
fragment HEXDIGIT : [0-9a-fA-F];
HEXNUMBER : '0' X HEXDIGIT+;
GUID: 'GUID:{' (HEXDIGIT|'-')* '}';

// other lexer rules

ID : [a-zA-Z0-9_]+ ;
WS : [ \t\r\n]+ -> skip ;

COMMENT : '//' ~[\r\n]* ( [\r\n] | EOF ) -> skip ;


// case insnensitivity

fragment A : [aA];
fragment B : [bB];
fragment C : [cC];
fragment D : [dD];
fragment E : [eE];
fragment F : [fF];
fragment G : [gG];
fragment H : [hH];
fragment I : [iI];
fragment J : [jJ];
fragment K : [kK];
fragment L : [lL];
fragment M : [mM];
fragment N : [nN];
fragment O : [oO];
fragment P : [pP];
fragment Q : [qQ];
fragment R : [rR];
fragment S : [sS];
fragment T : [tT];
fragment U : [uU];
fragment V : [vV];
fragment W : [wW];
fragment X : [xX];
fragment Y : [yY];
fragment Z : [zZ];