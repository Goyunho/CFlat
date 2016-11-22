# Generated from CFlat.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CFlatParser import CFlatParser
else:
    from CFlatParser import CFlatParser

# This class defines a complete generic visitor for a parse tree produced by CFlatParser.

class CFlatVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CFlatParser#prog.
    def visitProg(self, ctx:CFlatParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFlatParser#line.
    def visitLine(self, ctx:CFlatParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFlatParser#mulstat.
    def visitMulstat(self, ctx:CFlatParser.MulstatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFlatParser#lavel_no1.
    def visitLavel_no1(self, ctx:CFlatParser.Lavel_no1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFlatParser#assign.
    def visitAssign(self, ctx:CFlatParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFlatParser#showme.
    def visitShowme(self, ctx:CFlatParser.ShowmeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFlatParser#parens.
    def visitParens(self, ctx:CFlatParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFlatParser#string.
    def visitString(self, ctx:CFlatParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFlatParser#MulDiv.
    def visitMulDiv(self, ctx:CFlatParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFlatParser#AddSub.
    def visitAddSub(self, ctx:CFlatParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFlatParser#logicOperOr.
    def visitLogicOperOr(self, ctx:CFlatParser.LogicOperOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFlatParser#CompOper2.
    def visitCompOper2(self, ctx:CFlatParser.CompOper2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFlatParser#BitOper.
    def visitBitOper(self, ctx:CFlatParser.BitOperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFlatParser#CompOper.
    def visitCompOper(self, ctx:CFlatParser.CompOperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFlatParser#number.
    def visitNumber(self, ctx:CFlatParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFlatParser#SingleOper.
    def visitSingleOper(self, ctx:CFlatParser.SingleOperContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFlatParser#logicOperAnd.
    def visitLogicOperAnd(self, ctx:CFlatParser.LogicOperAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFlatParser#id.
    def visitId(self, ctx:CFlatParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CFlatParser#ShiftOper.
    def visitShiftOper(self, ctx:CFlatParser.ShiftOperContext):
        return self.visitChildren(ctx)



del CFlatParser