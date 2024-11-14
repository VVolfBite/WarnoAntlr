# Generated from NdfGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .NdfGrammarParser import NdfGrammarParser
else:
    from NdfGrammarParser import NdfGrammarParser

# This class defines a complete listener for a parse tree produced by NdfGrammarParser.
class NdfGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by NdfGrammarParser#ndf_file.
    def enterNdf_file(self, ctx:NdfGrammarParser.Ndf_fileContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#ndf_file.
    def exitNdf_file(self, ctx:NdfGrammarParser.Ndf_fileContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#assignment.
    def enterAssignment(self, ctx:NdfGrammarParser.AssignmentContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#assignment.
    def exitAssignment(self, ctx:NdfGrammarParser.AssignmentContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#private_prefix.
    def enterPrivate_prefix(self, ctx:NdfGrammarParser.Private_prefixContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#private_prefix.
    def exitPrivate_prefix(self, ctx:NdfGrammarParser.Private_prefixContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#export_prefix.
    def enterExport_prefix(self, ctx:NdfGrammarParser.Export_prefixContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#export_prefix.
    def exitExport_prefix(self, ctx:NdfGrammarParser.Export_prefixContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#r_value.
    def enterR_value(self, ctx:NdfGrammarParser.R_valueContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#r_value.
    def exitR_value(self, ctx:NdfGrammarParser.R_valueContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#object_type.
    def enterObject_type(self, ctx:NdfGrammarParser.Object_typeContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#object_type.
    def exitObject_type(self, ctx:NdfGrammarParser.Object_typeContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#block.
    def enterBlock(self, ctx:NdfGrammarParser.BlockContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#block.
    def exitBlock(self, ctx:NdfGrammarParser.BlockContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#normal_assignment.
    def enterNormal_assignment(self, ctx:NdfGrammarParser.Normal_assignmentContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#normal_assignment.
    def exitNormal_assignment(self, ctx:NdfGrammarParser.Normal_assignmentContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#member_assignment.
    def enterMember_assignment(self, ctx:NdfGrammarParser.Member_assignmentContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#member_assignment.
    def exitMember_assignment(self, ctx:NdfGrammarParser.Member_assignmentContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#unnamed_assignment.
    def enterUnnamed_assignment(self, ctx:NdfGrammarParser.Unnamed_assignmentContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#unnamed_assignment.
    def exitUnnamed_assignment(self, ctx:NdfGrammarParser.Unnamed_assignmentContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#object.
    def enterObject(self, ctx:NdfGrammarParser.ObjectContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#object.
    def exitObject(self, ctx:NdfGrammarParser.ObjectContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#id.
    def enterId(self, ctx:NdfGrammarParser.IdContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#id.
    def exitId(self, ctx:NdfGrammarParser.IdContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#arithmetic.
    def enterArithmetic(self, ctx:NdfGrammarParser.ArithmeticContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#arithmetic.
    def exitArithmetic(self, ctx:NdfGrammarParser.ArithmeticContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#atom.
    def enterAtom(self, ctx:NdfGrammarParser.AtomContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#atom.
    def exitAtom(self, ctx:NdfGrammarParser.AtomContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#op.
    def enterOp(self, ctx:NdfGrammarParser.OpContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#op.
    def exitOp(self, ctx:NdfGrammarParser.OpContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#concatination.
    def enterConcatination(self, ctx:NdfGrammarParser.ConcatinationContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#concatination.
    def exitConcatination(self, ctx:NdfGrammarParser.ConcatinationContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#builtin_type_label.
    def enterBuiltin_type_label(self, ctx:NdfGrammarParser.Builtin_type_labelContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#builtin_type_label.
    def exitBuiltin_type_label(self, ctx:NdfGrammarParser.Builtin_type_labelContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#pair_label.
    def enterPair_label(self, ctx:NdfGrammarParser.Pair_labelContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#pair_label.
    def exitPair_label(self, ctx:NdfGrammarParser.Pair_labelContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#list_label.
    def enterList_label(self, ctx:NdfGrammarParser.List_labelContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#list_label.
    def exitList_label(self, ctx:NdfGrammarParser.List_labelContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#map_label.
    def enterMap_label(self, ctx:NdfGrammarParser.Map_labelContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#map_label.
    def exitMap_label(self, ctx:NdfGrammarParser.Map_labelContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#builtin_type_value.
    def enterBuiltin_type_value(self, ctx:NdfGrammarParser.Builtin_type_valueContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#builtin_type_value.
    def exitBuiltin_type_value(self, ctx:NdfGrammarParser.Builtin_type_valueContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#primitive_value.
    def enterPrimitive_value(self, ctx:NdfGrammarParser.Primitive_valueContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#primitive_value.
    def exitPrimitive_value(self, ctx:NdfGrammarParser.Primitive_valueContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#data_structure_value.
    def enterData_structure_value(self, ctx:NdfGrammarParser.Data_structure_valueContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#data_structure_value.
    def exitData_structure_value(self, ctx:NdfGrammarParser.Data_structure_valueContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#nil_value.
    def enterNil_value(self, ctx:NdfGrammarParser.Nil_valueContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#nil_value.
    def exitNil_value(self, ctx:NdfGrammarParser.Nil_valueContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#bool_value.
    def enterBool_value(self, ctx:NdfGrammarParser.Bool_valueContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#bool_value.
    def exitBool_value(self, ctx:NdfGrammarParser.Bool_valueContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#string_value.
    def enterString_value(self, ctx:NdfGrammarParser.String_valueContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#string_value.
    def exitString_value(self, ctx:NdfGrammarParser.String_valueContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#int_value.
    def enterInt_value(self, ctx:NdfGrammarParser.Int_valueContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#int_value.
    def exitInt_value(self, ctx:NdfGrammarParser.Int_valueContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#hex_value.
    def enterHex_value(self, ctx:NdfGrammarParser.Hex_valueContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#hex_value.
    def exitHex_value(self, ctx:NdfGrammarParser.Hex_valueContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#float_value.
    def enterFloat_value(self, ctx:NdfGrammarParser.Float_valueContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#float_value.
    def exitFloat_value(self, ctx:NdfGrammarParser.Float_valueContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#guid_value.
    def enterGuid_value(self, ctx:NdfGrammarParser.Guid_valueContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#guid_value.
    def exitGuid_value(self, ctx:NdfGrammarParser.Guid_valueContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#pair_value.
    def enterPair_value(self, ctx:NdfGrammarParser.Pair_valueContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#pair_value.
    def exitPair_value(self, ctx:NdfGrammarParser.Pair_valueContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#vector_value.
    def enterVector_value(self, ctx:NdfGrammarParser.Vector_valueContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#vector_value.
    def exitVector_value(self, ctx:NdfGrammarParser.Vector_valueContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#map_value.
    def enterMap_value(self, ctx:NdfGrammarParser.Map_valueContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#map_value.
    def exitMap_value(self, ctx:NdfGrammarParser.Map_valueContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#obj_reference_value.
    def enterObj_reference_value(self, ctx:NdfGrammarParser.Obj_reference_valueContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#obj_reference_value.
    def exitObj_reference_value(self, ctx:NdfGrammarParser.Obj_reference_valueContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#special_value.
    def enterSpecial_value(self, ctx:NdfGrammarParser.Special_valueContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#special_value.
    def exitSpecial_value(self, ctx:NdfGrammarParser.Special_valueContext):
        pass


    # Enter a parse tree produced by NdfGrammarParser#rgba_value.
    def enterRgba_value(self, ctx:NdfGrammarParser.Rgba_valueContext):
        pass

    # Exit a parse tree produced by NdfGrammarParser#rgba_value.
    def exitRgba_value(self, ctx:NdfGrammarParser.Rgba_valueContext):
        pass



del NdfGrammarParser