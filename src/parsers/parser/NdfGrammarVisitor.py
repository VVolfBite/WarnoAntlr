# Generated from NdfGrammar.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .NdfGrammarParser import NdfGrammarParser
else:
    from NdfGrammarParser import NdfGrammarParser

# This class defines a complete generic visitor for a parse tree produced by NdfGrammarParser.

class NdfGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NdfGrammarParser#ndf_file.
    def visitNdf_file(self, ctx:NdfGrammarParser.Ndf_fileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#assignment.
    def visitAssignment(self, ctx:NdfGrammarParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#private_prefix.
    def visitPrivate_prefix(self, ctx:NdfGrammarParser.Private_prefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#export_prefix.
    def visitExport_prefix(self, ctx:NdfGrammarParser.Export_prefixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#r_value.
    def visitR_value(self, ctx:NdfGrammarParser.R_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#object_type.
    def visitObject_type(self, ctx:NdfGrammarParser.Object_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#block.
    def visitBlock(self, ctx:NdfGrammarParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#normal_assignment.
    def visitNormal_assignment(self, ctx:NdfGrammarParser.Normal_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#member_assignment.
    def visitMember_assignment(self, ctx:NdfGrammarParser.Member_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#unnamed_assignment.
    def visitUnnamed_assignment(self, ctx:NdfGrammarParser.Unnamed_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#object.
    def visitObject(self, ctx:NdfGrammarParser.ObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#id.
    def visitId(self, ctx:NdfGrammarParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#arithmetic.
    def visitArithmetic(self, ctx:NdfGrammarParser.ArithmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#atom.
    def visitAtom(self, ctx:NdfGrammarParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#op.
    def visitOp(self, ctx:NdfGrammarParser.OpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#concatination.
    def visitConcatination(self, ctx:NdfGrammarParser.ConcatinationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#builtin_type_label.
    def visitBuiltin_type_label(self, ctx:NdfGrammarParser.Builtin_type_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#pair_label.
    def visitPair_label(self, ctx:NdfGrammarParser.Pair_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#list_label.
    def visitList_label(self, ctx:NdfGrammarParser.List_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#map_label.
    def visitMap_label(self, ctx:NdfGrammarParser.Map_labelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#builtin_type_value.
    def visitBuiltin_type_value(self, ctx:NdfGrammarParser.Builtin_type_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#primitive_value.
    def visitPrimitive_value(self, ctx:NdfGrammarParser.Primitive_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#data_structure_value.
    def visitData_structure_value(self, ctx:NdfGrammarParser.Data_structure_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#nil_value.
    def visitNil_value(self, ctx:NdfGrammarParser.Nil_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#bool_value.
    def visitBool_value(self, ctx:NdfGrammarParser.Bool_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#string_value.
    def visitString_value(self, ctx:NdfGrammarParser.String_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#int_value.
    def visitInt_value(self, ctx:NdfGrammarParser.Int_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#hex_value.
    def visitHex_value(self, ctx:NdfGrammarParser.Hex_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#float_value.
    def visitFloat_value(self, ctx:NdfGrammarParser.Float_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#guid_value.
    def visitGuid_value(self, ctx:NdfGrammarParser.Guid_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#pair_value.
    def visitPair_value(self, ctx:NdfGrammarParser.Pair_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#vector_value.
    def visitVector_value(self, ctx:NdfGrammarParser.Vector_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#map_value.
    def visitMap_value(self, ctx:NdfGrammarParser.Map_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#obj_reference_value.
    def visitObj_reference_value(self, ctx:NdfGrammarParser.Obj_reference_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#special_value.
    def visitSpecial_value(self, ctx:NdfGrammarParser.Special_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NdfGrammarParser#rgba_value.
    def visitRgba_value(self, ctx:NdfGrammarParser.Rgba_valueContext):
        return self.visitChildren(ctx)



del NdfGrammarParser