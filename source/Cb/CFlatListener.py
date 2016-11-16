# Generated from CFlat.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CFlatParser import CFlatParser
else:
    from CFlatParser import CFlatParser

# This class defines a complete listener for a parse tree produced by CFlatParser.
class CFlatListener(ParseTreeListener):

    # Enter a parse tree produced by CFlatParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:CFlatParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by CFlatParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:CFlatParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by CFlatParser#genericSelection.
    def enterGenericSelection(self, ctx:CFlatParser.GenericSelectionContext):
        pass

    # Exit a parse tree produced by CFlatParser#genericSelection.
    def exitGenericSelection(self, ctx:CFlatParser.GenericSelectionContext):
        pass


    # Enter a parse tree produced by CFlatParser#genericAssocList.
    def enterGenericAssocList(self, ctx:CFlatParser.GenericAssocListContext):
        pass

    # Exit a parse tree produced by CFlatParser#genericAssocList.
    def exitGenericAssocList(self, ctx:CFlatParser.GenericAssocListContext):
        pass


    # Enter a parse tree produced by CFlatParser#genericAssociation.
    def enterGenericAssociation(self, ctx:CFlatParser.GenericAssociationContext):
        pass

    # Exit a parse tree produced by CFlatParser#genericAssociation.
    def exitGenericAssociation(self, ctx:CFlatParser.GenericAssociationContext):
        pass


    # Enter a parse tree produced by CFlatParser#typeName.
    def enterTypeName(self, ctx:CFlatParser.TypeNameContext):
        pass

    # Exit a parse tree produced by CFlatParser#typeName.
    def exitTypeName(self, ctx:CFlatParser.TypeNameContext):
        pass


    # Enter a parse tree produced by CFlatParser#specifierQualifierList.
    def enterSpecifierQualifierList(self, ctx:CFlatParser.SpecifierQualifierListContext):
        pass

    # Exit a parse tree produced by CFlatParser#specifierQualifierList.
    def exitSpecifierQualifierList(self, ctx:CFlatParser.SpecifierQualifierListContext):
        pass


    # Enter a parse tree produced by CFlatParser#postfixExpression.
    def enterPostfixExpression(self, ctx:CFlatParser.PostfixExpressionContext):
        pass

    # Exit a parse tree produced by CFlatParser#postfixExpression.
    def exitPostfixExpression(self, ctx:CFlatParser.PostfixExpressionContext):
        pass


    # Enter a parse tree produced by CFlatParser#argumentExpressionList.
    def enterArgumentExpressionList(self, ctx:CFlatParser.ArgumentExpressionListContext):
        pass

    # Exit a parse tree produced by CFlatParser#argumentExpressionList.
    def exitArgumentExpressionList(self, ctx:CFlatParser.ArgumentExpressionListContext):
        pass


    # Enter a parse tree produced by CFlatParser#unaryExpression.
    def enterUnaryExpression(self, ctx:CFlatParser.UnaryExpressionContext):
        pass

    # Exit a parse tree produced by CFlatParser#unaryExpression.
    def exitUnaryExpression(self, ctx:CFlatParser.UnaryExpressionContext):
        pass


    # Enter a parse tree produced by CFlatParser#unaryOperator.
    def enterUnaryOperator(self, ctx:CFlatParser.UnaryOperatorContext):
        pass

    # Exit a parse tree produced by CFlatParser#unaryOperator.
    def exitUnaryOperator(self, ctx:CFlatParser.UnaryOperatorContext):
        pass


    # Enter a parse tree produced by CFlatParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:CFlatParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by CFlatParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:CFlatParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by CFlatParser#expression.
    def enterExpression(self, ctx:CFlatParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CFlatParser#expression.
    def exitExpression(self, ctx:CFlatParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CFlatParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:CFlatParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by CFlatParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:CFlatParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by CFlatParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:CFlatParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by CFlatParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:CFlatParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by CFlatParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:CFlatParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by CFlatParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:CFlatParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by CFlatParser#relationalExpression.
    def enterRelationalExpression(self, ctx:CFlatParser.RelationalExpressionContext):
        pass

    # Exit a parse tree produced by CFlatParser#relationalExpression.
    def exitRelationalExpression(self, ctx:CFlatParser.RelationalExpressionContext):
        pass


    # Enter a parse tree produced by CFlatParser#equalityExpression.
    def enterEqualityExpression(self, ctx:CFlatParser.EqualityExpressionContext):
        pass

    # Exit a parse tree produced by CFlatParser#equalityExpression.
    def exitEqualityExpression(self, ctx:CFlatParser.EqualityExpressionContext):
        pass


    # Enter a parse tree produced by CFlatParser#andExpression.
    def enterAndExpression(self, ctx:CFlatParser.AndExpressionContext):
        pass

    # Exit a parse tree produced by CFlatParser#andExpression.
    def exitAndExpression(self, ctx:CFlatParser.AndExpressionContext):
        pass


    # Enter a parse tree produced by CFlatParser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:CFlatParser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by CFlatParser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:CFlatParser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by CFlatParser#inclusiveOrExpression.
    def enterInclusiveOrExpression(self, ctx:CFlatParser.InclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by CFlatParser#inclusiveOrExpression.
    def exitInclusiveOrExpression(self, ctx:CFlatParser.InclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by CFlatParser#logicalAndExpression.
    def enterLogicalAndExpression(self, ctx:CFlatParser.LogicalAndExpressionContext):
        pass

    # Exit a parse tree produced by CFlatParser#logicalAndExpression.
    def exitLogicalAndExpression(self, ctx:CFlatParser.LogicalAndExpressionContext):
        pass


    # Enter a parse tree produced by CFlatParser#logicalOrExpression.
    def enterLogicalOrExpression(self, ctx:CFlatParser.LogicalOrExpressionContext):
        pass

    # Exit a parse tree produced by CFlatParser#logicalOrExpression.
    def exitLogicalOrExpression(self, ctx:CFlatParser.LogicalOrExpressionContext):
        pass


    # Enter a parse tree produced by CFlatParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:CFlatParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by CFlatParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:CFlatParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by CFlatParser#typedefName.
    def enterTypedefName(self, ctx:CFlatParser.TypedefNameContext):
        pass

    # Exit a parse tree produced by CFlatParser#typedefName.
    def exitTypedefName(self, ctx:CFlatParser.TypedefNameContext):
        pass


    # Enter a parse tree produced by CFlatParser#statement.
    def enterStatement(self, ctx:CFlatParser.StatementContext):
        pass

    # Exit a parse tree produced by CFlatParser#statement.
    def exitStatement(self, ctx:CFlatParser.StatementContext):
        pass


    # Enter a parse tree produced by CFlatParser#iterationStatement.
    def enterIterationStatement(self, ctx:CFlatParser.IterationStatementContext):
        pass

    # Exit a parse tree produced by CFlatParser#iterationStatement.
    def exitIterationStatement(self, ctx:CFlatParser.IterationStatementContext):
        pass


    # Enter a parse tree produced by CFlatParser#jumpStatement.
    def enterJumpStatement(self, ctx:CFlatParser.JumpStatementContext):
        pass

    # Exit a parse tree produced by CFlatParser#jumpStatement.
    def exitJumpStatement(self, ctx:CFlatParser.JumpStatementContext):
        pass


    # Enter a parse tree produced by CFlatParser#expressionStatement.
    def enterExpressionStatement(self, ctx:CFlatParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by CFlatParser#expressionStatement.
    def exitExpressionStatement(self, ctx:CFlatParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by CFlatParser#selectionStatement.
    def enterSelectionStatement(self, ctx:CFlatParser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by CFlatParser#selectionStatement.
    def exitSelectionStatement(self, ctx:CFlatParser.SelectionStatementContext):
        pass


    # Enter a parse tree produced by CFlatParser#labeledStatement.
    def enterLabeledStatement(self, ctx:CFlatParser.LabeledStatementContext):
        pass

    # Exit a parse tree produced by CFlatParser#labeledStatement.
    def exitLabeledStatement(self, ctx:CFlatParser.LabeledStatementContext):
        pass


    # Enter a parse tree produced by CFlatParser#compoundStatement.
    def enterCompoundStatement(self, ctx:CFlatParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by CFlatParser#compoundStatement.
    def exitCompoundStatement(self, ctx:CFlatParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by CFlatParser#blockItemList.
    def enterBlockItemList(self, ctx:CFlatParser.BlockItemListContext):
        pass

    # Exit a parse tree produced by CFlatParser#blockItemList.
    def exitBlockItemList(self, ctx:CFlatParser.BlockItemListContext):
        pass


    # Enter a parse tree produced by CFlatParser#blockItem.
    def enterBlockItem(self, ctx:CFlatParser.BlockItemContext):
        pass

    # Exit a parse tree produced by CFlatParser#blockItem.
    def exitBlockItem(self, ctx:CFlatParser.BlockItemContext):
        pass


    # Enter a parse tree produced by CFlatParser#compilationUnit.
    def enterCompilationUnit(self, ctx:CFlatParser.CompilationUnitContext):
        pass

    # Exit a parse tree produced by CFlatParser#compilationUnit.
    def exitCompilationUnit(self, ctx:CFlatParser.CompilationUnitContext):
        pass


    # Enter a parse tree produced by CFlatParser#translationUnit.
    def enterTranslationUnit(self, ctx:CFlatParser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by CFlatParser#translationUnit.
    def exitTranslationUnit(self, ctx:CFlatParser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by CFlatParser#declaration.
    def enterDeclaration(self, ctx:CFlatParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CFlatParser#declaration.
    def exitDeclaration(self, ctx:CFlatParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CFlatParser#staticAssertDeclaration.
    def enterStaticAssertDeclaration(self, ctx:CFlatParser.StaticAssertDeclarationContext):
        pass

    # Exit a parse tree produced by CFlatParser#staticAssertDeclaration.
    def exitStaticAssertDeclaration(self, ctx:CFlatParser.StaticAssertDeclarationContext):
        pass


    # Enter a parse tree produced by CFlatParser#initDeclaratorList.
    def enterInitDeclaratorList(self, ctx:CFlatParser.InitDeclaratorListContext):
        pass

    # Exit a parse tree produced by CFlatParser#initDeclaratorList.
    def exitInitDeclaratorList(self, ctx:CFlatParser.InitDeclaratorListContext):
        pass


    # Enter a parse tree produced by CFlatParser#externalDeclaration.
    def enterExternalDeclaration(self, ctx:CFlatParser.ExternalDeclarationContext):
        pass

    # Exit a parse tree produced by CFlatParser#externalDeclaration.
    def exitExternalDeclaration(self, ctx:CFlatParser.ExternalDeclarationContext):
        pass


    # Enter a parse tree produced by CFlatParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:CFlatParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by CFlatParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:CFlatParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by CFlatParser#declarator.
    def enterDeclarator(self, ctx:CFlatParser.DeclaratorContext):
        pass

    # Exit a parse tree produced by CFlatParser#declarator.
    def exitDeclarator(self, ctx:CFlatParser.DeclaratorContext):
        pass


    # Enter a parse tree produced by CFlatParser#directDeclarator.
    def enterDirectDeclarator(self, ctx:CFlatParser.DirectDeclaratorContext):
        pass

    # Exit a parse tree produced by CFlatParser#directDeclarator.
    def exitDirectDeclarator(self, ctx:CFlatParser.DirectDeclaratorContext):
        pass


    # Enter a parse tree produced by CFlatParser#identifierList.
    def enterIdentifierList(self, ctx:CFlatParser.IdentifierListContext):
        pass

    # Exit a parse tree produced by CFlatParser#identifierList.
    def exitIdentifierList(self, ctx:CFlatParser.IdentifierListContext):
        pass


    # Enter a parse tree produced by CFlatParser#typeQualifierList.
    def enterTypeQualifierList(self, ctx:CFlatParser.TypeQualifierListContext):
        pass

    # Exit a parse tree produced by CFlatParser#typeQualifierList.
    def exitTypeQualifierList(self, ctx:CFlatParser.TypeQualifierListContext):
        pass


    # Enter a parse tree produced by CFlatParser#typeQualifier.
    def enterTypeQualifier(self, ctx:CFlatParser.TypeQualifierContext):
        pass

    # Exit a parse tree produced by CFlatParser#typeQualifier.
    def exitTypeQualifier(self, ctx:CFlatParser.TypeQualifierContext):
        pass


    # Enter a parse tree produced by CFlatParser#parameterTypeList.
    def enterParameterTypeList(self, ctx:CFlatParser.ParameterTypeListContext):
        pass

    # Exit a parse tree produced by CFlatParser#parameterTypeList.
    def exitParameterTypeList(self, ctx:CFlatParser.ParameterTypeListContext):
        pass


    # Enter a parse tree produced by CFlatParser#parameterList.
    def enterParameterList(self, ctx:CFlatParser.ParameterListContext):
        pass

    # Exit a parse tree produced by CFlatParser#parameterList.
    def exitParameterList(self, ctx:CFlatParser.ParameterListContext):
        pass


    # Enter a parse tree produced by CFlatParser#parameterDeclaration.
    def enterParameterDeclaration(self, ctx:CFlatParser.ParameterDeclarationContext):
        pass

    # Exit a parse tree produced by CFlatParser#parameterDeclaration.
    def exitParameterDeclaration(self, ctx:CFlatParser.ParameterDeclarationContext):
        pass


    # Enter a parse tree produced by CFlatParser#declarationList.
    def enterDeclarationList(self, ctx:CFlatParser.DeclarationListContext):
        pass

    # Exit a parse tree produced by CFlatParser#declarationList.
    def exitDeclarationList(self, ctx:CFlatParser.DeclarationListContext):
        pass


    # Enter a parse tree produced by CFlatParser#declarationSpecifiers.
    def enterDeclarationSpecifiers(self, ctx:CFlatParser.DeclarationSpecifiersContext):
        pass

    # Exit a parse tree produced by CFlatParser#declarationSpecifiers.
    def exitDeclarationSpecifiers(self, ctx:CFlatParser.DeclarationSpecifiersContext):
        pass


    # Enter a parse tree produced by CFlatParser#declarationSpecifiers2.
    def enterDeclarationSpecifiers2(self, ctx:CFlatParser.DeclarationSpecifiers2Context):
        pass

    # Exit a parse tree produced by CFlatParser#declarationSpecifiers2.
    def exitDeclarationSpecifiers2(self, ctx:CFlatParser.DeclarationSpecifiers2Context):
        pass


    # Enter a parse tree produced by CFlatParser#declarationSpecifier.
    def enterDeclarationSpecifier(self, ctx:CFlatParser.DeclarationSpecifierContext):
        pass

    # Exit a parse tree produced by CFlatParser#declarationSpecifier.
    def exitDeclarationSpecifier(self, ctx:CFlatParser.DeclarationSpecifierContext):
        pass


    # Enter a parse tree produced by CFlatParser#storageClassSpecifier.
    def enterStorageClassSpecifier(self, ctx:CFlatParser.StorageClassSpecifierContext):
        pass

    # Exit a parse tree produced by CFlatParser#storageClassSpecifier.
    def exitStorageClassSpecifier(self, ctx:CFlatParser.StorageClassSpecifierContext):
        pass


    # Enter a parse tree produced by CFlatParser#initDeclarator.
    def enterInitDeclarator(self, ctx:CFlatParser.InitDeclaratorContext):
        pass

    # Exit a parse tree produced by CFlatParser#initDeclarator.
    def exitInitDeclarator(self, ctx:CFlatParser.InitDeclaratorContext):
        pass


    # Enter a parse tree produced by CFlatParser#constantExpression.
    def enterConstantExpression(self, ctx:CFlatParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by CFlatParser#constantExpression.
    def exitConstantExpression(self, ctx:CFlatParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by CFlatParser#conditionalExpression.
    def enterConditionalExpression(self, ctx:CFlatParser.ConditionalExpressionContext):
        pass

    # Exit a parse tree produced by CFlatParser#conditionalExpression.
    def exitConditionalExpression(self, ctx:CFlatParser.ConditionalExpressionContext):
        pass


    # Enter a parse tree produced by CFlatParser#initializer.
    def enterInitializer(self, ctx:CFlatParser.InitializerContext):
        pass

    # Exit a parse tree produced by CFlatParser#initializer.
    def exitInitializer(self, ctx:CFlatParser.InitializerContext):
        pass


    # Enter a parse tree produced by CFlatParser#initializerList.
    def enterInitializerList(self, ctx:CFlatParser.InitializerListContext):
        pass

    # Exit a parse tree produced by CFlatParser#initializerList.
    def exitInitializerList(self, ctx:CFlatParser.InitializerListContext):
        pass


    # Enter a parse tree produced by CFlatParser#designation.
    def enterDesignation(self, ctx:CFlatParser.DesignationContext):
        pass

    # Exit a parse tree produced by CFlatParser#designation.
    def exitDesignation(self, ctx:CFlatParser.DesignationContext):
        pass


    # Enter a parse tree produced by CFlatParser#designatorList.
    def enterDesignatorList(self, ctx:CFlatParser.DesignatorListContext):
        pass

    # Exit a parse tree produced by CFlatParser#designatorList.
    def exitDesignatorList(self, ctx:CFlatParser.DesignatorListContext):
        pass


    # Enter a parse tree produced by CFlatParser#designator.
    def enterDesignator(self, ctx:CFlatParser.DesignatorContext):
        pass

    # Exit a parse tree produced by CFlatParser#designator.
    def exitDesignator(self, ctx:CFlatParser.DesignatorContext):
        pass


    # Enter a parse tree produced by CFlatParser#atomicTypeSpecifier.
    def enterAtomicTypeSpecifier(self, ctx:CFlatParser.AtomicTypeSpecifierContext):
        pass

    # Exit a parse tree produced by CFlatParser#atomicTypeSpecifier.
    def exitAtomicTypeSpecifier(self, ctx:CFlatParser.AtomicTypeSpecifierContext):
        pass


