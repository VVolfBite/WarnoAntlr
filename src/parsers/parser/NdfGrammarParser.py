# Generated from NdfGrammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,40,310,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,1,0,5,0,74,8,0,10,0,12,0,77,9,0,1,0,1,0,
        1,1,1,1,1,1,3,1,84,8,1,1,2,1,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,3,4,98,8,4,1,5,1,5,1,6,1,6,3,6,104,8,6,1,7,1,7,3,7,108,8,7,
        1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,3,8,118,8,8,1,9,1,9,1,9,1,10,1,10,
        1,10,5,10,126,8,10,10,10,12,10,129,9,10,1,10,1,10,1,11,1,11,1,11,
        3,11,136,8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,146,8,
        12,1,12,1,12,1,12,1,12,5,12,152,8,12,10,12,12,12,155,9,12,1,13,1,
        13,1,13,1,13,3,13,161,8,13,1,14,1,14,1,15,1,15,1,15,1,15,3,15,169,
        8,15,1,15,1,15,1,15,5,15,174,8,15,10,15,12,15,177,9,15,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,3,16,186,8,16,1,17,1,17,1,17,1,17,1,17,
        1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,
        1,19,1,20,1,20,3,20,209,8,20,1,21,1,21,1,21,1,21,1,21,1,21,3,21,
        217,8,21,1,22,1,22,1,22,3,22,222,8,22,1,23,1,23,1,24,1,24,1,25,1,
        25,1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,1,30,1,30,1,30,1,30,1,
        30,1,30,1,31,1,31,1,31,1,31,5,31,248,8,31,10,31,12,31,251,9,31,1,
        31,3,31,254,8,31,3,31,256,8,31,1,31,1,31,1,32,1,32,1,32,1,32,1,32,
        5,32,265,8,32,10,32,12,32,268,9,32,1,32,3,32,271,8,32,3,32,273,8,
        32,1,32,1,32,1,33,1,33,3,33,279,8,33,1,33,5,33,282,8,33,10,33,12,
        33,285,9,33,1,33,1,33,1,33,1,33,1,33,5,33,292,8,33,10,33,12,33,295,
        9,33,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,
        1,35,1,35,0,3,24,30,66,36,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,0,
        4,2,0,5,7,21,21,1,0,17,18,1,0,13,14,2,0,15,15,38,38,321,0,75,1,0,
        0,0,2,83,1,0,0,0,4,85,1,0,0,0,6,87,1,0,0,0,8,97,1,0,0,0,10,99,1,
        0,0,0,12,103,1,0,0,0,14,107,1,0,0,0,16,113,1,0,0,0,18,119,1,0,0,
        0,20,122,1,0,0,0,22,132,1,0,0,0,24,145,1,0,0,0,26,160,1,0,0,0,28,
        162,1,0,0,0,30,168,1,0,0,0,32,185,1,0,0,0,34,187,1,0,0,0,36,194,
        1,0,0,0,38,199,1,0,0,0,40,208,1,0,0,0,42,216,1,0,0,0,44,221,1,0,
        0,0,46,223,1,0,0,0,48,225,1,0,0,0,50,227,1,0,0,0,52,229,1,0,0,0,
        54,231,1,0,0,0,56,233,1,0,0,0,58,235,1,0,0,0,60,237,1,0,0,0,62,243,
        1,0,0,0,64,259,1,0,0,0,66,276,1,0,0,0,68,296,1,0,0,0,70,298,1,0,
        0,0,72,74,3,2,1,0,73,72,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,
        1,0,0,0,76,78,1,0,0,0,77,75,1,0,0,0,78,79,5,0,0,1,79,1,1,0,0,0,80,
        84,3,14,7,0,81,84,3,16,8,0,82,84,3,18,9,0,83,80,1,0,0,0,83,81,1,
        0,0,0,83,82,1,0,0,0,84,3,1,0,0,0,85,86,5,30,0,0,86,5,1,0,0,0,87,
        88,5,29,0,0,88,7,1,0,0,0,89,98,3,30,15,0,90,98,3,24,12,0,91,98,3,
        40,20,0,92,98,3,20,10,0,93,98,3,14,7,0,94,98,3,66,33,0,95,98,3,46,
        23,0,96,98,3,68,34,0,97,89,1,0,0,0,97,90,1,0,0,0,97,91,1,0,0,0,97,
        92,1,0,0,0,97,93,1,0,0,0,97,94,1,0,0,0,97,95,1,0,0,0,97,96,1,0,0,
        0,98,9,1,0,0,0,99,100,5,38,0,0,100,11,1,0,0,0,101,104,3,14,7,0,102,
        104,3,16,8,0,103,101,1,0,0,0,103,102,1,0,0,0,104,13,1,0,0,0,105,
        108,3,6,3,0,106,108,3,4,2,0,107,105,1,0,0,0,107,106,1,0,0,0,107,
        108,1,0,0,0,108,109,1,0,0,0,109,110,3,22,11,0,110,111,5,20,0,0,111,
        112,3,8,4,0,112,15,1,0,0,0,113,114,3,22,11,0,114,117,5,1,0,0,115,
        118,3,8,4,0,116,118,3,14,7,0,117,115,1,0,0,0,117,116,1,0,0,0,118,
        17,1,0,0,0,119,120,5,31,0,0,120,121,3,8,4,0,121,19,1,0,0,0,122,123,
        3,10,5,0,123,127,5,2,0,0,124,126,3,12,6,0,125,124,1,0,0,0,126,129,
        1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,130,1,0,0,0,129,127,
        1,0,0,0,130,131,5,3,0,0,131,21,1,0,0,0,132,135,5,38,0,0,133,134,
        5,4,0,0,134,136,3,32,16,0,135,133,1,0,0,0,135,136,1,0,0,0,136,23,
        1,0,0,0,137,138,6,12,-1,0,138,139,5,2,0,0,139,140,3,24,12,0,140,
        141,5,3,0,0,141,146,1,0,0,0,142,143,5,5,0,0,143,146,3,24,12,2,144,
        146,3,26,13,0,145,137,1,0,0,0,145,142,1,0,0,0,145,144,1,0,0,0,146,
        153,1,0,0,0,147,148,10,3,0,0,148,149,3,28,14,0,149,150,3,24,12,4,
        150,152,1,0,0,0,151,147,1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,
        153,154,1,0,0,0,154,25,1,0,0,0,155,153,1,0,0,0,156,161,3,52,26,0,
        157,161,3,56,28,0,158,161,3,54,27,0,159,161,3,66,33,0,160,156,1,
        0,0,0,160,157,1,0,0,0,160,158,1,0,0,0,160,159,1,0,0,0,161,27,1,0,
        0,0,162,163,7,0,0,0,163,29,1,0,0,0,164,165,6,15,-1,0,165,169,3,50,
        25,0,166,169,3,64,32,0,167,169,3,62,31,0,168,164,1,0,0,0,168,166,
        1,0,0,0,168,167,1,0,0,0,169,175,1,0,0,0,170,171,10,4,0,0,171,172,
        5,6,0,0,172,174,3,30,15,5,173,170,1,0,0,0,174,177,1,0,0,0,175,173,
        1,0,0,0,175,176,1,0,0,0,176,31,1,0,0,0,177,175,1,0,0,0,178,186,5,
        23,0,0,179,186,5,24,0,0,180,186,5,25,0,0,181,186,5,26,0,0,182,186,
        3,34,17,0,183,186,3,36,18,0,184,186,3,38,19,0,185,178,1,0,0,0,185,
        179,1,0,0,0,185,180,1,0,0,0,185,181,1,0,0,0,185,182,1,0,0,0,185,
        183,1,0,0,0,185,184,1,0,0,0,186,33,1,0,0,0,187,188,5,27,0,0,188,
        189,5,8,0,0,189,190,3,32,16,0,190,191,5,9,0,0,191,192,3,32,16,0,
        192,193,5,10,0,0,193,35,1,0,0,0,194,195,5,28,0,0,195,196,5,8,0,0,
        196,197,3,32,16,0,197,198,5,10,0,0,198,37,1,0,0,0,199,200,5,19,0,
        0,200,201,5,8,0,0,201,202,3,32,16,0,202,203,5,9,0,0,203,204,3,32,
        16,0,204,205,5,10,0,0,205,39,1,0,0,0,206,209,3,42,21,0,207,209,3,
        44,22,0,208,206,1,0,0,0,208,207,1,0,0,0,209,41,1,0,0,0,210,217,3,
        48,24,0,211,217,3,50,25,0,212,217,3,52,26,0,213,217,3,54,27,0,214,
        217,3,56,28,0,215,217,3,58,29,0,216,210,1,0,0,0,216,211,1,0,0,0,
        216,212,1,0,0,0,216,213,1,0,0,0,216,214,1,0,0,0,216,215,1,0,0,0,
        217,43,1,0,0,0,218,222,3,60,30,0,219,222,3,62,31,0,220,222,3,64,
        32,0,221,218,1,0,0,0,221,219,1,0,0,0,221,220,1,0,0,0,222,45,1,0,
        0,0,223,224,5,22,0,0,224,47,1,0,0,0,225,226,7,1,0,0,226,49,1,0,0,
        0,227,228,5,33,0,0,228,51,1,0,0,0,229,230,5,34,0,0,230,53,1,0,0,
        0,231,232,5,36,0,0,232,55,1,0,0,0,233,234,5,35,0,0,234,57,1,0,0,
        0,235,236,5,37,0,0,236,59,1,0,0,0,237,238,5,2,0,0,238,239,3,8,4,
        0,239,240,5,9,0,0,240,241,3,8,4,0,241,242,5,3,0,0,242,61,1,0,0,0,
        243,255,5,11,0,0,244,249,3,8,4,0,245,246,5,9,0,0,246,248,3,8,4,0,
        247,245,1,0,0,0,248,251,1,0,0,0,249,247,1,0,0,0,249,250,1,0,0,0,
        250,253,1,0,0,0,251,249,1,0,0,0,252,254,5,9,0,0,253,252,1,0,0,0,
        253,254,1,0,0,0,254,256,1,0,0,0,255,244,1,0,0,0,255,256,1,0,0,0,
        256,257,1,0,0,0,257,258,5,12,0,0,258,63,1,0,0,0,259,260,5,19,0,0,
        260,272,5,11,0,0,261,266,3,60,30,0,262,263,5,9,0,0,263,265,3,60,
        30,0,264,262,1,0,0,0,265,268,1,0,0,0,266,264,1,0,0,0,266,267,1,0,
        0,0,267,270,1,0,0,0,268,266,1,0,0,0,269,271,5,9,0,0,270,269,1,0,
        0,0,270,271,1,0,0,0,271,273,1,0,0,0,272,261,1,0,0,0,272,273,1,0,
        0,0,273,274,1,0,0,0,274,275,5,12,0,0,275,65,1,0,0,0,276,278,6,33,
        -1,0,277,279,7,2,0,0,278,277,1,0,0,0,278,279,1,0,0,0,279,283,1,0,
        0,0,280,282,7,3,0,0,281,280,1,0,0,0,282,285,1,0,0,0,283,281,1,0,
        0,0,283,284,1,0,0,0,284,286,1,0,0,0,285,283,1,0,0,0,286,287,5,38,
        0,0,287,293,1,0,0,0,288,289,10,1,0,0,289,290,5,16,0,0,290,292,3,
        66,33,2,291,288,1,0,0,0,292,295,1,0,0,0,293,291,1,0,0,0,293,294,
        1,0,0,0,294,67,1,0,0,0,295,293,1,0,0,0,296,297,3,70,35,0,297,69,
        1,0,0,0,298,299,5,32,0,0,299,300,5,11,0,0,300,301,5,34,0,0,301,302,
        5,9,0,0,302,303,5,34,0,0,303,304,5,9,0,0,304,305,5,34,0,0,305,306,
        5,9,0,0,306,307,5,34,0,0,307,308,5,12,0,0,308,71,1,0,0,0,26,75,83,
        97,103,107,117,127,135,145,153,160,168,175,185,208,216,221,249,253,
        255,266,270,272,278,283,293
    ]

class NdfGrammarParser ( Parser ):

    grammarFileName = "NdfGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "':'", "'-'", "'+'", 
                     "'*'", "'<'", "','", "'>'", "'['", "']'", "'$'", "'~'", 
                     "'/'", "'|'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "K_TRUE", "K_FALSE", "K_MAP", "K_IS", 
                      "K_DIV", "K_NIL", "K_BOOL", "K_STRING", "K_INT", "K_FLOAT", 
                      "K_PAIR", "K_LIST", "K_EXPORT", "K_PRIVATE", "K_UNNAMED", 
                      "K_RGBA", "STRING", "INT", "FLOAT", "HEXNUMBER", "GUID", 
                      "ID", "WS", "COMMENT" ]

    RULE_ndf_file = 0
    RULE_assignment = 1
    RULE_private_prefix = 2
    RULE_export_prefix = 3
    RULE_r_value = 4
    RULE_object_type = 5
    RULE_block = 6
    RULE_normal_assignment = 7
    RULE_member_assignment = 8
    RULE_unnamed_assignment = 9
    RULE_object = 10
    RULE_id = 11
    RULE_arithmetic = 12
    RULE_atom = 13
    RULE_op = 14
    RULE_concatination = 15
    RULE_builtin_type_label = 16
    RULE_pair_label = 17
    RULE_list_label = 18
    RULE_map_label = 19
    RULE_builtin_type_value = 20
    RULE_primitive_value = 21
    RULE_data_structure_value = 22
    RULE_nil_value = 23
    RULE_bool_value = 24
    RULE_string_value = 25
    RULE_int_value = 26
    RULE_hex_value = 27
    RULE_float_value = 28
    RULE_guid_value = 29
    RULE_pair_value = 30
    RULE_vector_value = 31
    RULE_map_value = 32
    RULE_obj_reference_value = 33
    RULE_special_value = 34
    RULE_rgba_value = 35

    ruleNames =  [ "ndf_file", "assignment", "private_prefix", "export_prefix", 
                   "r_value", "object_type", "block", "normal_assignment", 
                   "member_assignment", "unnamed_assignment", "object", 
                   "id", "arithmetic", "atom", "op", "concatination", "builtin_type_label", 
                   "pair_label", "list_label", "map_label", "builtin_type_value", 
                   "primitive_value", "data_structure_value", "nil_value", 
                   "bool_value", "string_value", "int_value", "hex_value", 
                   "float_value", "guid_value", "pair_value", "vector_value", 
                   "map_value", "obj_reference_value", "special_value", 
                   "rgba_value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    K_TRUE=17
    K_FALSE=18
    K_MAP=19
    K_IS=20
    K_DIV=21
    K_NIL=22
    K_BOOL=23
    K_STRING=24
    K_INT=25
    K_FLOAT=26
    K_PAIR=27
    K_LIST=28
    K_EXPORT=29
    K_PRIVATE=30
    K_UNNAMED=31
    K_RGBA=32
    STRING=33
    INT=34
    FLOAT=35
    HEXNUMBER=36
    GUID=37
    ID=38
    WS=39
    COMMENT=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Ndf_fileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(NdfGrammarParser.EOF, 0)

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NdfGrammarParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(NdfGrammarParser.AssignmentContext,i)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_ndf_file

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNdf_file" ):
                listener.enterNdf_file(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNdf_file" ):
                listener.exitNdf_file(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNdf_file" ):
                return visitor.visitNdf_file(self)
            else:
                return visitor.visitChildren(self)




    def ndf_file(self):

        localctx = NdfGrammarParser.Ndf_fileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_ndf_file)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 278636003328) != 0):
                self.state = 72
                self.assignment()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(NdfGrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normal_assignment(self):
            return self.getTypedRuleContext(NdfGrammarParser.Normal_assignmentContext,0)


        def member_assignment(self):
            return self.getTypedRuleContext(NdfGrammarParser.Member_assignmentContext,0)


        def unnamed_assignment(self):
            return self.getTypedRuleContext(NdfGrammarParser.Unnamed_assignmentContext,0)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = NdfGrammarParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assignment)
        try:
            self.state = 83
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 80
                self.normal_assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.member_assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self.unnamed_assignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Private_prefixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_PRIVATE(self):
            return self.getToken(NdfGrammarParser.K_PRIVATE, 0)

        def getRuleIndex(self):
            return NdfGrammarParser.RULE_private_prefix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrivate_prefix" ):
                listener.enterPrivate_prefix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrivate_prefix" ):
                listener.exitPrivate_prefix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrivate_prefix" ):
                return visitor.visitPrivate_prefix(self)
            else:
                return visitor.visitChildren(self)




    def private_prefix(self):

        localctx = NdfGrammarParser.Private_prefixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_private_prefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(NdfGrammarParser.K_PRIVATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Export_prefixContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_EXPORT(self):
            return self.getToken(NdfGrammarParser.K_EXPORT, 0)

        def getRuleIndex(self):
            return NdfGrammarParser.RULE_export_prefix

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExport_prefix" ):
                listener.enterExport_prefix(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExport_prefix" ):
                listener.exitExport_prefix(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExport_prefix" ):
                return visitor.visitExport_prefix(self)
            else:
                return visitor.visitChildren(self)




    def export_prefix(self):

        localctx = NdfGrammarParser.Export_prefixContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_export_prefix)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(NdfGrammarParser.K_EXPORT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class R_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def concatination(self):
            return self.getTypedRuleContext(NdfGrammarParser.ConcatinationContext,0)


        def arithmetic(self):
            return self.getTypedRuleContext(NdfGrammarParser.ArithmeticContext,0)


        def builtin_type_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Builtin_type_valueContext,0)


        def object_(self):
            return self.getTypedRuleContext(NdfGrammarParser.ObjectContext,0)


        def normal_assignment(self):
            return self.getTypedRuleContext(NdfGrammarParser.Normal_assignmentContext,0)


        def obj_reference_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Obj_reference_valueContext,0)


        def nil_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Nil_valueContext,0)


        def special_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Special_valueContext,0)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_r_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR_value" ):
                listener.enterR_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR_value" ):
                listener.exitR_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR_value" ):
                return visitor.visitR_value(self)
            else:
                return visitor.visitChildren(self)




    def r_value(self):

        localctx = NdfGrammarParser.R_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_r_value)
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.concatination(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.arithmetic(0)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.builtin_type_value()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 92
                self.object_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 93
                self.normal_assignment()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 94
                self.obj_reference_value(0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 95
                self.nil_value()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 96
                self.special_value()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(NdfGrammarParser.ID, 0)

        def getRuleIndex(self):
            return NdfGrammarParser.RULE_object_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_type" ):
                listener.enterObject_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_type" ):
                listener.exitObject_type(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject_type" ):
                return visitor.visitObject_type(self)
            else:
                return visitor.visitChildren(self)




    def object_type(self):

        localctx = NdfGrammarParser.Object_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_object_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(NdfGrammarParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def normal_assignment(self):
            return self.getTypedRuleContext(NdfGrammarParser.Normal_assignmentContext,0)


        def member_assignment(self):
            return self.getTypedRuleContext(NdfGrammarParser.Member_assignmentContext,0)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = NdfGrammarParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        try:
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 101
                self.normal_assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 102
                self.member_assignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Normal_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(NdfGrammarParser.IdContext,0)


        def K_IS(self):
            return self.getToken(NdfGrammarParser.K_IS, 0)

        def r_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.R_valueContext,0)


        def export_prefix(self):
            return self.getTypedRuleContext(NdfGrammarParser.Export_prefixContext,0)


        def private_prefix(self):
            return self.getTypedRuleContext(NdfGrammarParser.Private_prefixContext,0)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_normal_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNormal_assignment" ):
                listener.enterNormal_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNormal_assignment" ):
                listener.exitNormal_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNormal_assignment" ):
                return visitor.visitNormal_assignment(self)
            else:
                return visitor.visitChildren(self)




    def normal_assignment(self):

        localctx = NdfGrammarParser.Normal_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_normal_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29]:
                self.state = 105
                self.export_prefix()
                pass
            elif token in [30]:
                self.state = 106
                self.private_prefix()
                pass
            elif token in [38]:
                pass
            else:
                pass
            self.state = 109
            self.id_()
            self.state = 110
            self.match(NdfGrammarParser.K_IS)
            self.state = 111
            self.r_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Member_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(NdfGrammarParser.IdContext,0)


        def r_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.R_valueContext,0)


        def normal_assignment(self):
            return self.getTypedRuleContext(NdfGrammarParser.Normal_assignmentContext,0)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_member_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMember_assignment" ):
                listener.enterMember_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMember_assignment" ):
                listener.exitMember_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMember_assignment" ):
                return visitor.visitMember_assignment(self)
            else:
                return visitor.visitChildren(self)




    def member_assignment(self):

        localctx = NdfGrammarParser.Member_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_member_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.id_()
            self.state = 114
            self.match(NdfGrammarParser.T__0)
            self.state = 117
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 115
                self.r_value()
                pass

            elif la_ == 2:
                self.state = 116
                self.normal_assignment()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Unnamed_assignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_UNNAMED(self):
            return self.getToken(NdfGrammarParser.K_UNNAMED, 0)

        def r_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.R_valueContext,0)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_unnamed_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnnamed_assignment" ):
                listener.enterUnnamed_assignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnnamed_assignment" ):
                listener.exitUnnamed_assignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnnamed_assignment" ):
                return visitor.visitUnnamed_assignment(self)
            else:
                return visitor.visitChildren(self)




    def unnamed_assignment(self):

        localctx = NdfGrammarParser.Unnamed_assignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_unnamed_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(NdfGrammarParser.K_UNNAMED)
            self.state = 120
            self.r_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_type(self):
            return self.getTypedRuleContext(NdfGrammarParser.Object_typeContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NdfGrammarParser.BlockContext)
            else:
                return self.getTypedRuleContext(NdfGrammarParser.BlockContext,i)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_object

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject" ):
                listener.enterObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject" ):
                listener.exitObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObject" ):
                return visitor.visitObject(self)
            else:
                return visitor.visitChildren(self)




    def object_(self):

        localctx = NdfGrammarParser.ObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_object)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.object_type()
            self.state = 123
            self.match(NdfGrammarParser.T__1)
            self.state = 127
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 276488519680) != 0):
                self.state = 124
                self.block()
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 130
            self.match(NdfGrammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(NdfGrammarParser.ID, 0)

        def builtin_type_label(self):
            return self.getTypedRuleContext(NdfGrammarParser.Builtin_type_labelContext,0)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)




    def id_(self):

        localctx = NdfGrammarParser.IdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(NdfGrammarParser.ID)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 133
                self.match(NdfGrammarParser.T__3)
                self.state = 134
                self.builtin_type_label()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NdfGrammarParser.ArithmeticContext)
            else:
                return self.getTypedRuleContext(NdfGrammarParser.ArithmeticContext,i)


        def atom(self):
            return self.getTypedRuleContext(NdfGrammarParser.AtomContext,0)


        def op(self):
            return self.getTypedRuleContext(NdfGrammarParser.OpContext,0)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_arithmetic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic" ):
                listener.enterArithmetic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic" ):
                listener.exitArithmetic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic" ):
                return visitor.visitArithmetic(self)
            else:
                return visitor.visitChildren(self)



    def arithmetic(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = NdfGrammarParser.ArithmeticContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_arithmetic, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 138
                self.match(NdfGrammarParser.T__1)
                self.state = 139
                self.arithmetic(0)
                self.state = 140
                self.match(NdfGrammarParser.T__2)
                pass
            elif token in [5]:
                self.state = 142
                self.match(NdfGrammarParser.T__4)
                self.state = 143
                self.arithmetic(2)
                pass
            elif token in [13, 14, 15, 34, 35, 36, 38]:
                self.state = 144
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 153
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = NdfGrammarParser.ArithmeticContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic)
                    self.state = 147
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 148
                    self.op()
                    self.state = 149
                    self.arithmetic(4) 
                self.state = 155
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def int_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Int_valueContext,0)


        def float_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Float_valueContext,0)


        def hex_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Hex_valueContext,0)


        def obj_reference_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Obj_reference_valueContext,0)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtom" ):
                return visitor.visitAtom(self)
            else:
                return visitor.visitChildren(self)




    def atom(self):

        localctx = NdfGrammarParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_atom)
        try:
            self.state = 160
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self.int_value()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.float_value()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 158
                self.hex_value()
                pass
            elif token in [13, 14, 15, 38]:
                self.enterOuterAlt(localctx, 4)
                self.state = 159
                self.obj_reference_value(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_DIV(self):
            return self.getToken(NdfGrammarParser.K_DIV, 0)

        def getRuleIndex(self):
            return NdfGrammarParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOp" ):
                return visitor.visitOp(self)
            else:
                return visitor.visitChildren(self)




    def op(self):

        localctx = NdfGrammarParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2097376) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConcatinationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def string_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.String_valueContext,0)


        def map_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Map_valueContext,0)


        def vector_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Vector_valueContext,0)


        def concatination(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NdfGrammarParser.ConcatinationContext)
            else:
                return self.getTypedRuleContext(NdfGrammarParser.ConcatinationContext,i)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_concatination

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConcatination" ):
                listener.enterConcatination(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConcatination" ):
                listener.exitConcatination(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConcatination" ):
                return visitor.visitConcatination(self)
            else:
                return visitor.visitChildren(self)



    def concatination(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = NdfGrammarParser.ConcatinationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_concatination, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.state = 165
                self.string_value()
                pass
            elif token in [19]:
                self.state = 166
                self.map_value()
                pass
            elif token in [11]:
                self.state = 167
                self.vector_value()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 175
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = NdfGrammarParser.ConcatinationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_concatination)
                    self.state = 170
                    if not self.precpred(self._ctx, 4):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                    self.state = 171
                    self.match(NdfGrammarParser.T__5)
                    self.state = 172
                    self.concatination(5) 
                self.state = 177
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Builtin_type_labelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_BOOL(self):
            return self.getToken(NdfGrammarParser.K_BOOL, 0)

        def K_STRING(self):
            return self.getToken(NdfGrammarParser.K_STRING, 0)

        def K_INT(self):
            return self.getToken(NdfGrammarParser.K_INT, 0)

        def K_FLOAT(self):
            return self.getToken(NdfGrammarParser.K_FLOAT, 0)

        def pair_label(self):
            return self.getTypedRuleContext(NdfGrammarParser.Pair_labelContext,0)


        def list_label(self):
            return self.getTypedRuleContext(NdfGrammarParser.List_labelContext,0)


        def map_label(self):
            return self.getTypedRuleContext(NdfGrammarParser.Map_labelContext,0)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_builtin_type_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuiltin_type_label" ):
                listener.enterBuiltin_type_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuiltin_type_label" ):
                listener.exitBuiltin_type_label(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuiltin_type_label" ):
                return visitor.visitBuiltin_type_label(self)
            else:
                return visitor.visitChildren(self)




    def builtin_type_label(self):

        localctx = NdfGrammarParser.Builtin_type_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_builtin_type_label)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.match(NdfGrammarParser.K_BOOL)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.match(NdfGrammarParser.K_STRING)
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.match(NdfGrammarParser.K_INT)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 181
                self.match(NdfGrammarParser.K_FLOAT)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 5)
                self.state = 182
                self.pair_label()
                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 6)
                self.state = 183
                self.list_label()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 7)
                self.state = 184
                self.map_label()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pair_labelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_PAIR(self):
            return self.getToken(NdfGrammarParser.K_PAIR, 0)

        def builtin_type_label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NdfGrammarParser.Builtin_type_labelContext)
            else:
                return self.getTypedRuleContext(NdfGrammarParser.Builtin_type_labelContext,i)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_pair_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair_label" ):
                listener.enterPair_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair_label" ):
                listener.exitPair_label(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair_label" ):
                return visitor.visitPair_label(self)
            else:
                return visitor.visitChildren(self)




    def pair_label(self):

        localctx = NdfGrammarParser.Pair_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_pair_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(NdfGrammarParser.K_PAIR)
            self.state = 188
            self.match(NdfGrammarParser.T__7)
            self.state = 189
            self.builtin_type_label()
            self.state = 190
            self.match(NdfGrammarParser.T__8)
            self.state = 191
            self.builtin_type_label()
            self.state = 192
            self.match(NdfGrammarParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_labelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_LIST(self):
            return self.getToken(NdfGrammarParser.K_LIST, 0)

        def builtin_type_label(self):
            return self.getTypedRuleContext(NdfGrammarParser.Builtin_type_labelContext,0)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_list_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterList_label" ):
                listener.enterList_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitList_label" ):
                listener.exitList_label(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_label" ):
                return visitor.visitList_label(self)
            else:
                return visitor.visitChildren(self)




    def list_label(self):

        localctx = NdfGrammarParser.List_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_list_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.match(NdfGrammarParser.K_LIST)
            self.state = 195
            self.match(NdfGrammarParser.T__7)
            self.state = 196
            self.builtin_type_label()
            self.state = 197
            self.match(NdfGrammarParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Map_labelContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_MAP(self):
            return self.getToken(NdfGrammarParser.K_MAP, 0)

        def builtin_type_label(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NdfGrammarParser.Builtin_type_labelContext)
            else:
                return self.getTypedRuleContext(NdfGrammarParser.Builtin_type_labelContext,i)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_map_label

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMap_label" ):
                listener.enterMap_label(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMap_label" ):
                listener.exitMap_label(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMap_label" ):
                return visitor.visitMap_label(self)
            else:
                return visitor.visitChildren(self)




    def map_label(self):

        localctx = NdfGrammarParser.Map_labelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_map_label)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(NdfGrammarParser.K_MAP)
            self.state = 200
            self.match(NdfGrammarParser.T__7)
            self.state = 201
            self.builtin_type_label()
            self.state = 202
            self.match(NdfGrammarParser.T__8)
            self.state = 203
            self.builtin_type_label()
            self.state = 204
            self.match(NdfGrammarParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Builtin_type_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Primitive_valueContext,0)


        def data_structure_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Data_structure_valueContext,0)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_builtin_type_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuiltin_type_value" ):
                listener.enterBuiltin_type_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuiltin_type_value" ):
                listener.exitBuiltin_type_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBuiltin_type_value" ):
                return visitor.visitBuiltin_type_value(self)
            else:
                return visitor.visitChildren(self)




    def builtin_type_value(self):

        localctx = NdfGrammarParser.Builtin_type_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_builtin_type_value)
        try:
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18, 33, 34, 35, 36, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 206
                self.primitive_value()
                pass
            elif token in [2, 11, 19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.data_structure_value()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bool_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Bool_valueContext,0)


        def string_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.String_valueContext,0)


        def int_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Int_valueContext,0)


        def hex_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Hex_valueContext,0)


        def float_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Float_valueContext,0)


        def guid_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Guid_valueContext,0)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_primitive_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimitive_value" ):
                listener.enterPrimitive_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimitive_value" ):
                listener.exitPrimitive_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_value" ):
                return visitor.visitPrimitive_value(self)
            else:
                return visitor.visitChildren(self)




    def primitive_value(self):

        localctx = NdfGrammarParser.Primitive_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_primitive_value)
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18]:
                self.enterOuterAlt(localctx, 1)
                self.state = 210
                self.bool_value()
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 2)
                self.state = 211
                self.string_value()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 3)
                self.state = 212
                self.int_value()
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 4)
                self.state = 213
                self.hex_value()
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 5)
                self.state = 214
                self.float_value()
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 6)
                self.state = 215
                self.guid_value()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_structure_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pair_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Pair_valueContext,0)


        def vector_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Vector_valueContext,0)


        def map_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Map_valueContext,0)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_data_structure_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_structure_value" ):
                listener.enterData_structure_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_structure_value" ):
                listener.exitData_structure_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_structure_value" ):
                return visitor.visitData_structure_value(self)
            else:
                return visitor.visitChildren(self)




    def data_structure_value(self):

        localctx = NdfGrammarParser.Data_structure_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_data_structure_value)
        try:
            self.state = 221
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.pair_value()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 219
                self.vector_value()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 220
                self.map_value()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Nil_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_NIL(self):
            return self.getToken(NdfGrammarParser.K_NIL, 0)

        def getRuleIndex(self):
            return NdfGrammarParser.RULE_nil_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNil_value" ):
                listener.enterNil_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNil_value" ):
                listener.exitNil_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNil_value" ):
                return visitor.visitNil_value(self)
            else:
                return visitor.visitChildren(self)




    def nil_value(self):

        localctx = NdfGrammarParser.Nil_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_nil_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(NdfGrammarParser.K_NIL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bool_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_TRUE(self):
            return self.getToken(NdfGrammarParser.K_TRUE, 0)

        def K_FALSE(self):
            return self.getToken(NdfGrammarParser.K_FALSE, 0)

        def getRuleIndex(self):
            return NdfGrammarParser.RULE_bool_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool_value" ):
                listener.enterBool_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool_value" ):
                listener.exitBool_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBool_value" ):
                return visitor.visitBool_value(self)
            else:
                return visitor.visitChildren(self)




    def bool_value(self):

        localctx = NdfGrammarParser.Bool_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_bool_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            _la = self._input.LA(1)
            if not(_la==17 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class String_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(NdfGrammarParser.STRING, 0)

        def getRuleIndex(self):
            return NdfGrammarParser.RULE_string_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString_value" ):
                listener.enterString_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString_value" ):
                listener.exitString_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString_value" ):
                return visitor.visitString_value(self)
            else:
                return visitor.visitChildren(self)




    def string_value(self):

        localctx = NdfGrammarParser.String_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_string_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(NdfGrammarParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Int_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(NdfGrammarParser.INT, 0)

        def getRuleIndex(self):
            return NdfGrammarParser.RULE_int_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt_value" ):
                listener.enterInt_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt_value" ):
                listener.exitInt_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt_value" ):
                return visitor.visitInt_value(self)
            else:
                return visitor.visitChildren(self)




    def int_value(self):

        localctx = NdfGrammarParser.Int_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_int_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(NdfGrammarParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Hex_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HEXNUMBER(self):
            return self.getToken(NdfGrammarParser.HEXNUMBER, 0)

        def getRuleIndex(self):
            return NdfGrammarParser.RULE_hex_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHex_value" ):
                listener.enterHex_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHex_value" ):
                listener.exitHex_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHex_value" ):
                return visitor.visitHex_value(self)
            else:
                return visitor.visitChildren(self)




    def hex_value(self):

        localctx = NdfGrammarParser.Hex_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_hex_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(NdfGrammarParser.HEXNUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(NdfGrammarParser.FLOAT, 0)

        def getRuleIndex(self):
            return NdfGrammarParser.RULE_float_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_value" ):
                listener.enterFloat_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_value" ):
                listener.exitFloat_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloat_value" ):
                return visitor.visitFloat_value(self)
            else:
                return visitor.visitChildren(self)




    def float_value(self):

        localctx = NdfGrammarParser.Float_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_float_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(NdfGrammarParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Guid_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GUID(self):
            return self.getToken(NdfGrammarParser.GUID, 0)

        def getRuleIndex(self):
            return NdfGrammarParser.RULE_guid_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGuid_value" ):
                listener.enterGuid_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGuid_value" ):
                listener.exitGuid_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGuid_value" ):
                return visitor.visitGuid_value(self)
            else:
                return visitor.visitChildren(self)




    def guid_value(self):

        localctx = NdfGrammarParser.Guid_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_guid_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(NdfGrammarParser.GUID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pair_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def r_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NdfGrammarParser.R_valueContext)
            else:
                return self.getTypedRuleContext(NdfGrammarParser.R_valueContext,i)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_pair_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPair_value" ):
                listener.enterPair_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPair_value" ):
                listener.exitPair_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPair_value" ):
                return visitor.visitPair_value(self)
            else:
                return visitor.visitChildren(self)




    def pair_value(self):

        localctx = NdfGrammarParser.Pair_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_pair_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(NdfGrammarParser.T__1)
            self.state = 238
            self.r_value()
            self.state = 239
            self.match(NdfGrammarParser.T__8)
            self.state = 240
            self.r_value()
            self.state = 241
            self.match(NdfGrammarParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vector_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def r_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NdfGrammarParser.R_valueContext)
            else:
                return self.getTypedRuleContext(NdfGrammarParser.R_valueContext,i)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_vector_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVector_value" ):
                listener.enterVector_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVector_value" ):
                listener.exitVector_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVector_value" ):
                return visitor.visitVector_value(self)
            else:
                return visitor.visitChildren(self)




    def vector_value(self):

        localctx = NdfGrammarParser.Vector_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_vector_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(NdfGrammarParser.T__10)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 547076630564) != 0):
                self.state = 244
                self.r_value()
                self.state = 249
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 245
                        self.match(NdfGrammarParser.T__8)
                        self.state = 246
                        self.r_value() 
                    self.state = 251
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

                self.state = 253
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 252
                    self.match(NdfGrammarParser.T__8)




            self.state = 257
            self.match(NdfGrammarParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Map_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_MAP(self):
            return self.getToken(NdfGrammarParser.K_MAP, 0)

        def pair_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NdfGrammarParser.Pair_valueContext)
            else:
                return self.getTypedRuleContext(NdfGrammarParser.Pair_valueContext,i)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_map_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMap_value" ):
                listener.enterMap_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMap_value" ):
                listener.exitMap_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMap_value" ):
                return visitor.visitMap_value(self)
            else:
                return visitor.visitChildren(self)




    def map_value(self):

        localctx = NdfGrammarParser.Map_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_map_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(NdfGrammarParser.K_MAP)
            self.state = 260
            self.match(NdfGrammarParser.T__10)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 261
                self.pair_value()
                self.state = 266
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 262
                        self.match(NdfGrammarParser.T__8)
                        self.state = 263
                        self.pair_value() 
                    self.state = 268
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==9:
                    self.state = 269
                    self.match(NdfGrammarParser.T__8)




            self.state = 274
            self.match(NdfGrammarParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Obj_reference_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(NdfGrammarParser.ID)
            else:
                return self.getToken(NdfGrammarParser.ID, i)

        def obj_reference_value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NdfGrammarParser.Obj_reference_valueContext)
            else:
                return self.getTypedRuleContext(NdfGrammarParser.Obj_reference_valueContext,i)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_obj_reference_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObj_reference_value" ):
                listener.enterObj_reference_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObj_reference_value" ):
                listener.exitObj_reference_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitObj_reference_value" ):
                return visitor.visitObj_reference_value(self)
            else:
                return visitor.visitChildren(self)



    def obj_reference_value(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = NdfGrammarParser.Obj_reference_valueContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_obj_reference_value, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13 or _la==14:
                self.state = 277
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 283
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 280
                    _la = self._input.LA(1)
                    if not(_la==15 or _la==38):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 285
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

            self.state = 286
            self.match(NdfGrammarParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 293
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = NdfGrammarParser.Obj_reference_valueContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_obj_reference_value)
                    self.state = 288
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 289
                    self.match(NdfGrammarParser.T__15)
                    self.state = 290
                    self.obj_reference_value(2) 
                self.state = 295
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Special_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rgba_value(self):
            return self.getTypedRuleContext(NdfGrammarParser.Rgba_valueContext,0)


        def getRuleIndex(self):
            return NdfGrammarParser.RULE_special_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecial_value" ):
                listener.enterSpecial_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecial_value" ):
                listener.exitSpecial_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecial_value" ):
                return visitor.visitSpecial_value(self)
            else:
                return visitor.visitChildren(self)




    def special_value(self):

        localctx = NdfGrammarParser.Special_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_special_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.rgba_value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rgba_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def K_RGBA(self):
            return self.getToken(NdfGrammarParser.K_RGBA, 0)

        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(NdfGrammarParser.INT)
            else:
                return self.getToken(NdfGrammarParser.INT, i)

        def getRuleIndex(self):
            return NdfGrammarParser.RULE_rgba_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRgba_value" ):
                listener.enterRgba_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRgba_value" ):
                listener.exitRgba_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRgba_value" ):
                return visitor.visitRgba_value(self)
            else:
                return visitor.visitChildren(self)




    def rgba_value(self):

        localctx = NdfGrammarParser.Rgba_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_rgba_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.match(NdfGrammarParser.K_RGBA)
            self.state = 299
            self.match(NdfGrammarParser.T__10)
            self.state = 300
            self.match(NdfGrammarParser.INT)
            self.state = 301
            self.match(NdfGrammarParser.T__8)
            self.state = 302
            self.match(NdfGrammarParser.INT)
            self.state = 303
            self.match(NdfGrammarParser.T__8)
            self.state = 304
            self.match(NdfGrammarParser.INT)
            self.state = 305
            self.match(NdfGrammarParser.T__8)
            self.state = 306
            self.match(NdfGrammarParser.INT)
            self.state = 307
            self.match(NdfGrammarParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[12] = self.arithmetic_sempred
        self._predicates[15] = self.concatination_sempred
        self._predicates[33] = self.obj_reference_value_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithmetic_sempred(self, localctx:ArithmeticContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

    def concatination_sempred(self, localctx:ConcatinationContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

    def obj_reference_value_sempred(self, localctx:Obj_reference_valueContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




