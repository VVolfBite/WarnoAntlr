grammar NdfGrammar;

// 此文件用于生成lexer和parser
// 使用命令: java -jar .\antlr-4.13.2-complete.jar -Dlanguage=Python3 NdfGrammar.g4 -visitor -o parser

//=============================================
// Parser Rules - 基础结构
//=============================================

// 1. 基本文件结构
ndf_file : assignment* EOF;  // 文件由多个赋值语句组成

// 2. 赋值语句类型
assignment 
    : normal_assignment    // 普通赋值: MyVar IS 100
    | member_assignment    // 成员赋值: Name = "value"
    | unnamed_assignment   // 匿名赋值: UNNAMED ~/Reference
    | template_assignment  // 模板赋值: template MyTemplate[...] is Base(...)
    ;

// 2. 前缀修饰符
private_prefix : K_PRIVATE;
export_prefix : K_EXPORT;
template_prefix : K_TEMPLATE;

// 3. 右值表达式
r_value 
    : concatination 
    | arithmetic 
    | builtin_type_value 
    | object 
    | normal_assignment 
    | member_assignment 
    | obj_reference_value 
    | nil_value 
    | special_value 
    | replace_value 
    | type_initialization
    | ID
    ;

// 4. 赋值语句
normal_assignment : ( export_prefix | private_prefix )? id K_IS r_value;

template_assignment 
    : ( export_prefix | private_prefix )? 
      template_prefix 
      id 
      template_param_list
      K_IS 
      r_value
    ;

member_assignment : id '=' ( r_value | normal_assignment );
unnamed_assignment : K_UNNAMED r_value;

// 5. 模板系统
template_param 
    : id ':' type_label ('=' r_value)?
    | id ':' list_label ('=' vector_value)?
    | id ':' map_label ('=' map_value)?
    ;

template_param_list : '[' (template_param (',' template_param)* ','?)? ']';

// 6. 对象系统
object : object_type '(' ( block )* ')';
object_type : 'T'? ID;
block : normal_assignment | member_assignment | object_member;

object_member
    : member_assignment
    | array_access '=' r_value
    | ID '.' ID '=' r_value
    | ID '.' array_access '=' r_value
    ;

// 7. 标识符系统
id : ID (':' type_label)? | array_access;
array_access : ID '[' int_value ']';

// 8. 类型系统
type_label 
    : builtin_type_label 
    | object_type
    | template_type
    ;

builtin_type_label 
    : K_BOOL 
    | K_STRING 
    | K_INT 
    | K_FLOAT 
    | K_FLOAT2
    | K_FLOAT3
    | pair_label 
    | list_label 
    | map_label
    ;

pair_label : K_PAIR '<' type_label ',' type_label '>';
list_label : K_LIST '<' type_label '>';
map_label : K_MAP '<' type_label ',' type_label '>';
template_type 
    : ID '<' template_param_type (',' template_param_type)* '>'
    ;

// 新增模板参数类型规则
template_param_type
    : type_label                                    // 基本类型参数
    | type_label '<' template_param_type '>'        // 嵌套泛型参数
    | numeric_specialization                        // 数值特化
    ;

// 新增数值特化规则
numeric_specialization
    : int_value                                     // 整数特化 
    | float_value                                   // 浮点数特化
    | arithmetic                                    // 算术表达式特化
    ;

// 9. 类型初始化
type_initialization
    : builtin_type_label vector_value
    | builtin_type_label '(' r_value ')'
    ;

//=============================================
// Parser Rules - 值类型
//=============================================

// 10. 值系统
builtin_type_value : primitive_value | data_structure_value;
primitive_value : bool_value | string_value | int_value | hex_value | float_value | guid_value;
data_structure_value : pair_value | vector_value | map_value;

bool_value : K_TRUE | K_FALSE;
nil_value : K_NIL;
string_value : STRING_SINGLE | STRING_DOUBLE;
int_value : INT | HEX_INT;
float_value : FLOAT;
hex_value : HEXNUMBER;
guid_value : GUID;

// 14. 特殊类型值
special_value 
    : rgba_value      // RGBA颜色值
    | float2_value    // 2D向量值
    | float3_value    // 3D向量值
    ;

// RGBA颜色值: 红,绿,蓝,透明度 (0-255)
// 示例: RGBA[255, 128, 64, 255]  // 橙色不透明
rgba_value : K_RGBA '[' INT ',' INT ',' INT ',' INT ']';

// 2D向量值: x, y 坐标
// 示例: float2[100.0, 200.0]     // x=100.0, y=200.0
float2_value : K_FLOAT2 '[' (float_value|int_value) ',' (float_value|int_value) ']';

// 3D向量值: x, y, z 坐标
// 示例: float3[1.0, 2.0, 3.0]    // x=1.0, y=2.0, z=3.0
float3_value : K_FLOAT3 '[' (float_value|int_value) ',' (float_value|int_value) ',' (float_value|int_value) ']';

//=============================================
// Parser Rules - 复合类型
//=============================================

// 11. 复合类型值
// 示例: ("key", 100)
pair_value : '(' pair_element ',' pair_element ')';

// 示例: [1, 2, 3] 或 ["a", "b", "c"]
vector_value : '[' (r_value (',' r_value)* ','?)? ']';

// 示例: MAP[("key1", 100), ("key2", 200)]
map_value : K_MAP '[' (pair_value (',' pair_value)* ','?)? ']';

// 12. 路径系统
path_element
    : ID
    | INT
    | K_GUID
    ;

obj_reference_value
    : ('$'|'~')? ('/'? path_element)+ ('/' path_element)*
    | obj_reference_value '|' obj_reference_value
    | '$/' path_element ('/' path_element)*
    ;

// 13. 替换值
replace_value : '<' ID '>';

// 15. 算术系统
arithmetic 
    : '(' arithmetic ')' 
    | arithmetic op arithmetic 
    | '-' arithmetic 
    | atom
    ;

atom : int_value | float_value | hex_value | obj_reference_value;
op : '+' | '-' | '*' | K_DIV;

// 16. 并发引用
concatination : obj_reference_value ('|' obj_reference_value)+;

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