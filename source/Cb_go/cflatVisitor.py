# Generated from cflat.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cflatParser import cflatParser
else:
    from cflatParser import cflatParser

# This class defines a complete generic visitor for a parse tree produced by cflatParser.

class cflatVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by cflatParser#run.
    def visitRun(self, ctx:cflatParser.RunContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cflatParser#frame.
    def visitFrame(self, ctx:cflatParser.FrameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cflatParser#group.
    def visitGroup(self, ctx:cflatParser.GroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cflatParser#brace_group.
    def visitBrace_group(self, ctx:cflatParser.Brace_groupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cflatParser#line.
    def visitLine(self, ctx:cflatParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cflatParser#action_end.
    def visitAction_end(self, ctx:cflatParser.Action_endContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cflatParser#actions.
    def visitActions(self, ctx:cflatParser.ActionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cflatParser#action.
    def visitAction(self, ctx:cflatParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cflatParser#initialisation.
    def visitInitialisation(self, ctx:cflatParser.InitialisationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cflatParser#assignment.
    def visitAssignment(self, ctx:cflatParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cflatParser#declaration.
    def visitDeclaration(self, ctx:cflatParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cflatParser#calculator.
    def visitCalculator(self, ctx:cflatParser.CalculatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cflatParser#AddSub.
    def visitAddSub(self, ctx:cflatParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cflatParser#MulDiv.
    def visitMulDiv(self, ctx:cflatParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cflatParser#Cal_Bit.
    def visitCal_Bit(self, ctx:cflatParser.Cal_BitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cflatParser#calculator_logic.
    def visitCalculator_logic(self, ctx:cflatParser.Calculator_logicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cflatParser#increase.
    def visitIncrease(self, ctx:cflatParser.IncreaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cflatParser#decrease.
    def visitDecrease(self, ctx:cflatParser.DecreaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cflatParser#percent.
    def visitPercent(self, ctx:cflatParser.PercentContext):
        return self.visitChildren(ctx)



del cflatParser