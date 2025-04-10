grammar NdfGrammar;

// 此文件用于生成lexer和parser
// 使用命令: java -jar .\antlr-4.13.2-complete.jar -Dlanguage=Python3 NdfGrammar.g4 -visitor -o parser

//=============================================
// 1. 基础结构
//=============================================
ndf_file : assignment* EOF;

assignment 
    : normal_assignment    
    | template_assignment  
    | member_assignment    
    | unnamed_assignment   
    ;

// 基础赋值
normal_assignment : ( export_prefix | private_prefix )? id K_IS r_value;
member_assignment : id '=' ( r_value | normal_assignment );
unnamed_assignment : K_UNNAMED r_value;

// 修饰符
private_prefix : K_PRIVATE;
export_prefix : K_EXPORT;
template_prefix : K_TEMPLATE;

//=============================================
// 2. 标识符系统
//=============================================
id : ID (':' type_specifier)? | array_access;
array_access : ID '[' int_value ']';

//=============================================
// 3. 右值系统
//=============================================
r_value 
    : arithmetic          // 算术表达式
    | builtin_type_value  // 基础类型值
    | special_value       // 特殊类型值
    | object             // 对象
    | obj_reference_value // 引用值
    | replace_value      // 替换值
    | concatination      // 连接
    | normal_assignment  // 嵌套赋值
    | member_assignment  
    | nil_value         // 空值
    | type_initialization // 类型初始化
    | ID                // 标识符
    ;

//=============================================
// 4. 值系统
//=============================================
// 基础值
builtin_type_value : primitive_value | data_structure_value;
primitive_value : bool_value | string_value | int_value | hex_value | float_value | guid_value;
data_structure_value : pair_value | vector_value | map_value;

// 具体值定义
bool_value : K_TRUE | K_FALSE;
nil_value : K_NIL;
string_value : STRING_SINGLE | STRING_DOUBLE;
int_value : INT;
float_value : FLOAT;
hex_value : HEX_INT;
guid_value : GUID;

// 特殊值
special_value : rgba_value | float2_value | float3_value;
rgba_value : K_RGBA '[' INT ',' INT ',' INT ',' INT ']';
float2_value : K_FLOAT2 '[' (float_value|int_value) ',' (float_value|int_value) ']';
float3_value : K_FLOAT3 '[' (float_value|int_value) ',' (float_value|int_value) ',' (float_value|int_value) ']';

//=============================================
// 5. 类型系统
//=============================================
type_specifier
    : type_label    
    | list_label    
    | map_label     
    ;

type_label 
    : builtin_type_label 
    | object_type
    | template_type
    ;

builtin_type_label 
    : K_BOOL | K_STRING | K_INT | K_FLOAT 
    | K_FLOAT2 | K_FLOAT3
    | pair_label | list_label | map_label
    ;

// 容器类型
pair_label : K_PAIR '<' type_label ',' type_label '>';
list_label : K_LIST '<' type_label '>';
map_label : K_MAP '<' type_label ',' type_label '>';

type_initialization
    : builtin_type_label vector_value
    | builtin_type_label '(' r_value ')'
    ;

//=============================================
// 6. 对象系统
//=============================================
object : object_type '(' ( block (',' block)* ','? )* ')';
object_type : ID;
block : normal_assignment | member_assignment | object_member;

object_member
    : member_assignment ','?    
    | array_access '=' r_value ','?
    | ID '.' ID '=' r_value ','?
    | ID '.' array_access '=' r_value ','?
    ;

//=============================================
// 7. 模板系统
//=============================================
template_assignment 
    : ( export_prefix | private_prefix )? 
      template_prefix 
      id 
      template_param_list
      K_IS 
      object
    ;

template_param : id ('=' r_value)?;
template_param_list : '[' (template_param (',' template_param)*)? ']';

template_param_type
    : type_label                            
    | type_label '<' template_param_type '>'
    | numeric_specialization                
    ;

template_type : ID '<' template_param_type (',' template_param_type)* '>';
numeric_specialization
    : int_value                                    
    | float_value                                   
    | arithmetic                                    
    ;

//=============================================
// 8. 复合数据系统
//=============================================
// Vector
vector_value : '[' (r_value (',' r_value)* ','?)? ']';

// Pair
pair_value : '(' pair_element ',' pair_element ')';
pair_element : r_value;

// Map
map_value : K_MAP '[' (pair_value (',' pair_value)* ','?)? ']';

//=============================================
// 9. 引用系统
//=============================================
path_element : ID | INT | K_GUID;

obj_reference_value
    : ('$'|'~')? ('/'? path_element)+ ('/' path_element)*
    | obj_reference_value '|' obj_reference_value
    | '$/' path_element ('/' path_element)*
    ;

replace_value : '<' ID '>';
concatination : obj_reference_value ('|' obj_reference_value)+;

//=============================================
// 10. 算术系统
//=============================================
arithmetic 
    : '(' arithmetic ')' 
    | arithmetic op arithmetic 
    | '-' arithmetic 
    | atom
    ;

atom : int_value | float_value | hex_value | obj_reference_value;
op : '+' | '-' | '*' | K_DIV;

//=============================================
// Lexer Rules
//=============================================

// 1. 关键字定义
K_TRUE : T R U E;      // True
K_FALSE : F A L S E;   // False
K_MAP : M A P;         // MAP
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
K_FLOAT2 : F L O A T '2';
K_FLOAT3 : F L O A T '3';
K_RGBA : R G B A;
K_GUID : G U I D;  // 新增GUID关键字定义

// 2. 字符串定义
// 示例: 'single quote' 或 "double quote"
STRING_SINGLE : '\'' ( ESC_CHAR | ~[\\'\r\n] )* '\'';
STRING_DOUBLE : '"' ( ESC_CHAR | ~[\\"\r\n] )* '"';

fragment ESC_CHAR
    : '\\' [btnfr"'\\]
    | '\\' 'u' HEXDIGIT HEXDIGIT HEXDIGIT HEXDIGIT
    ;

// 3. 数值定义
// 示例: 123, -456
INT : '-'? [0-9]+;

// 示例: 1.23, .45, 6.0e-7
FLOAT : '-'? [0-9]* '.' [0-9]+ ([eE] [+-]? [0-9]+)?
      | '-'? [0-9]+ '.' [0-9]* ([eE] [+-]? [0-9]+)?
      | '-'? [0-9]+ [eE] [+-]? [0-9]+
      ;

// 示例: 0xFF, 0x123ABC
HEX_INT : '0' [xX] [0-9a-fA-F]+;

// 示例: GUID:{12345678-1234-5678-1234-567812345678}
GUID : 'GUID:{' (HEXDIGIT|'-')* '}';

// 4. 标识符
ID : [a-zA-Z_] [a-zA-Z0-9_]*;

// 5. 空白字符和注释
WS : [ \t\r\n]+ -> skip;
BLOCK_COMMENT : '/*' .*? '*/' -> skip;
LINE_COMMENT : '//' ~[\r\n]* -> skip;

// 6. 字母片段(用于大小写不敏感)
fragment A : [aA]; fragment B : [bB]; fragment C : [cC];
fragment D : [dD]; fragment E : [eE]; fragment F : [fF];
fragment G : [gG]; fragment H : [hH]; fragment I : [iI];
fragment J : [jJ]; fragment K : [kK]; fragment L : [lL];
fragment M : [mM]; fragment N : [nN]; fragment O : [oO];
fragment P : [pP]; fragment Q : [qQ]; fragment R : [rR];
fragment S : [sS]; fragment T : [tT]; fragment U : [uU];
fragment V : [vV]; fragment W : [wW]; fragment X : [xX];
fragment Y : [yY]; fragment Z : [zZ];

// 添加 HEXDIGIT 片段定义 (在字母片段定义区域)
fragment HEXDIGIT : [0-9a-fA-F];