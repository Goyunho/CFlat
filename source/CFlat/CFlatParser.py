# Generated from CFlat.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3$")
        buf.write("V\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\6\2\20\n\2\r\2\16\2\21\3\3\5\3\25\n\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\7\4\34\n\4\f\4\16\4\37\13\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5\'\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\5\7\67\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\7\7Q\n\7\f\7\16\7T\13\7\3\7\2\3\f\b\2\4")
        buf.write("\6\b\n\f\2\t\4\2\13\13\32\32\4\2\27\30\33\33\3\2\31\32")
        buf.write("\3\2\25\26\3\2\f\17\3\2\20\21\3\2\22\24a\2\17\3\2\2\2")
        buf.write("\4\24\3\2\2\2\6\30\3\2\2\2\b&\3\2\2\2\n(\3\2\2\2\f\66")
        buf.write("\3\2\2\2\16\20\5\4\3\2\17\16\3\2\2\2\20\21\3\2\2\2\21")
        buf.write("\17\3\2\2\2\21\22\3\2\2\2\22\3\3\2\2\2\23\25\5\6\4\2\24")
        buf.write("\23\3\2\2\2\24\25\3\2\2\2\25\26\3\2\2\2\26\27\7!\2\2\27")
        buf.write("\5\3\2\2\2\30\35\5\b\5\2\31\32\7\3\2\2\32\34\5\b\5\2\33")
        buf.write("\31\3\2\2\2\34\37\3\2\2\2\35\33\3\2\2\2\35\36\3\2\2\2")
        buf.write("\36\7\3\2\2\2\37\35\3\2\2\2 \'\5\f\7\2!\'\5\n\6\2\"#\7")
        buf.write("\b\2\2#$\7\4\2\2$\'\5\f\7\2%\'\7\2\2\3& \3\2\2\2&!\3\2")
        buf.write("\2\2&\"\3\2\2\2&%\3\2\2\2\'\t\3\2\2\2()\7\5\2\2)*\5\f")
        buf.write("\7\2*+\7\6\2\2+\13\3\2\2\2,-\b\7\1\2-.\t\2\2\2.\67\5\f")
        buf.write("\7\17/\67\7\35\2\2\60\67\7\b\2\2\61\67\7\34\2\2\62\63")
        buf.write("\7\7\2\2\63\64\5\f\7\2\64\65\7\6\2\2\65\67\3\2\2\2\66")
        buf.write(",\3\2\2\2\66/\3\2\2\2\66\60\3\2\2\2\66\61\3\2\2\2\66\62")
        buf.write("\3\2\2\2\67R\3\2\2\289\f\16\2\29:\t\3\2\2:Q\5\f\7\17;")
        buf.write("<\f\r\2\2<=\t\4\2\2=Q\5\f\7\16>?\f\f\2\2?@\t\5\2\2@Q\5")
        buf.write("\f\7\rAB\f\13\2\2BC\t\6\2\2CQ\5\f\7\fDE\f\n\2\2EF\t\7")
        buf.write("\2\2FQ\5\f\7\13GH\f\t\2\2HI\t\b\2\2IQ\5\f\7\nJK\f\b\2")
        buf.write("\2KL\7\t\2\2LQ\5\f\7\tMN\f\7\2\2NO\7\n\2\2OQ\5\f\7\bP")
        buf.write("8\3\2\2\2P;\3\2\2\2P>\3\2\2\2PA\3\2\2\2PD\3\2\2\2PG\3")
        buf.write("\2\2\2PJ\3\2\2\2PM\3\2\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2")
        buf.write("\2S\r\3\2\2\2TR\3\2\2\2\t\21\24\35&\66PR")
        return buf.getvalue()


class CFlatParser ( Parser ):

    grammarFileName = "CFlat.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'='", "'print('", "')'", "'('", 
                     "<INVALID>", "'&&'", "'||'", "'!'", "'>'", "'>='", 
                     "'<'", "'<='", "'=='", "'!='", "'&'", "'|'", "'^'", 
                     "'<<'", "'>>'", "'*'", "'/'", "'+'", "'-'", "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "AND2", "OR2", "NOT", 
                      "GRT", "GRE", "LES", "LEE", "EQL", "NEQ", "AND", "OR", 
                      "XOR", "SHL", "SHR", "MUL", "DIV", "ADD", "SUB", "AMP", 
                      "STRING", "NUMBER", "WORD", "FLAOT", "INT", "NEWLINE", 
                      "WS", "COMMENT_LINE", "COMMENT_MULLINE" ]

    RULE_prog = 0
    RULE_line = 1
    RULE_mulstat = 2
    RULE_stat = 3
    RULE_showme = 4
    RULE_expr = 5

    ruleNames =  [ "prog", "line", "mulstat", "stat", "showme", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    ID=6
    AND2=7
    OR2=8
    NOT=9
    GRT=10
    GRE=11
    LES=12
    LEE=13
    EQL=14
    NEQ=15
    AND=16
    OR=17
    XOR=18
    SHL=19
    SHR=20
    MUL=21
    DIV=22
    ADD=23
    SUB=24
    AMP=25
    STRING=26
    NUMBER=27
    WORD=28
    FLAOT=29
    INT=30
    NEWLINE=31
    WS=32
    COMMENT_LINE=33
    COMMENT_MULLINE=34

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CFlatParser.LineContext)
            else:
                return self.getTypedRuleContext(CFlatParser.LineContext,i)


        def getRuleIndex(self):
            return CFlatParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CFlatParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 12
                    self.line()

                else:
                    raise NoViableAltException(self)
                self.state = 15 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LineContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(CFlatParser.NEWLINE, 0)

        def mulstat(self):
            return self.getTypedRuleContext(CFlatParser.MulstatContext,0)


        def getRuleIndex(self):
            return CFlatParser.RULE_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = CFlatParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            _la = self._input.LA(1)
            if ((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (CFlatParser.EOF - -1)) | (1 << (CFlatParser.T__2 - -1)) | (1 << (CFlatParser.T__4 - -1)) | (1 << (CFlatParser.ID - -1)) | (1 << (CFlatParser.NOT - -1)) | (1 << (CFlatParser.SUB - -1)) | (1 << (CFlatParser.STRING - -1)) | (1 << (CFlatParser.NUMBER - -1)))) != 0):
                self.state = 17
                self.mulstat()


            self.state = 20
            self.match(CFlatParser.NEWLINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MulstatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CFlatParser.StatContext)
            else:
                return self.getTypedRuleContext(CFlatParser.StatContext,i)


        def getRuleIndex(self):
            return CFlatParser.RULE_mulstat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulstat" ):
                return visitor.visitMulstat(self)
            else:
                return visitor.visitChildren(self)




    def mulstat(self):

        localctx = CFlatParser.MulstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mulstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.stat()
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CFlatParser.T__0:
                self.state = 23
                self.match(CFlatParser.T__0)
                self.state = 24
                self.stat()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CFlatParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Lavel_no1Context(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CFlatParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CFlatParser.ExprContext,0)

        def showme(self):
            return self.getTypedRuleContext(CFlatParser.ShowmeContext,0)

        def EOF(self):
            return self.getToken(CFlatParser.EOF, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLavel_no1" ):
                return visitor.visitLavel_no1(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CFlatParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CFlatParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(CFlatParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = CFlatParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stat)
        try:
            self.state = 36
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = CFlatParser.Lavel_no1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = CFlatParser.Lavel_no1Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.showme()
                pass

            elif la_ == 3:
                localctx = CFlatParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.match(CFlatParser.ID)
                self.state = 33
                self.match(CFlatParser.T__1)
                self.state = 34
                self.expr(0)
                pass

            elif la_ == 4:
                localctx = CFlatParser.Lavel_no1Context(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.match(CFlatParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ShowmeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(CFlatParser.ExprContext,0)


        def getRuleIndex(self):
            return CFlatParser.RULE_showme

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShowme" ):
                return visitor.visitShowme(self)
            else:
                return visitor.visitChildren(self)




    def showme(self):

        localctx = CFlatParser.ShowmeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_showme)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(CFlatParser.T__2)
            self.state = 39
            self.expr(0)
            self.state = 40
            self.match(CFlatParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CFlatParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CFlatParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CFlatParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CFlatParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(CFlatParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CFlatParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CFlatParser.ExprContext)
            else:
                return self.getTypedRuleContext(CFlatParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CFlatParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CFlatParser.ExprContext)
            else:
                return self.getTypedRuleContext(CFlatParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class LogicOperOrContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CFlatParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CFlatParser.ExprContext)
            else:
                return self.getTypedRuleContext(CFlatParser.ExprContext,i)

        def OR2(self):
            return self.getToken(CFlatParser.OR2, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicOperOr" ):
                return visitor.visitLogicOperOr(self)
            else:
                return visitor.visitChildren(self)


    class CompOper2Context(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CFlatParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CFlatParser.ExprContext)
            else:
                return self.getTypedRuleContext(CFlatParser.ExprContext,i)

        def EQL(self):
            return self.getToken(CFlatParser.EQL, 0)
        def NEQ(self):
            return self.getToken(CFlatParser.NEQ, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompOper2" ):
                return visitor.visitCompOper2(self)
            else:
                return visitor.visitChildren(self)


    class BitOperContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CFlatParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CFlatParser.ExprContext)
            else:
                return self.getTypedRuleContext(CFlatParser.ExprContext,i)

        def AND(self):
            return self.getToken(CFlatParser.AND, 0)
        def XOR(self):
            return self.getToken(CFlatParser.XOR, 0)
        def OR(self):
            return self.getToken(CFlatParser.OR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBitOper" ):
                return visitor.visitBitOper(self)
            else:
                return visitor.visitChildren(self)


    class CompOperContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CFlatParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CFlatParser.ExprContext)
            else:
                return self.getTypedRuleContext(CFlatParser.ExprContext,i)

        def GRT(self):
            return self.getToken(CFlatParser.GRT, 0)
        def GRE(self):
            return self.getToken(CFlatParser.GRE, 0)
        def LES(self):
            return self.getToken(CFlatParser.LES, 0)
        def LEE(self):
            return self.getToken(CFlatParser.LEE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompOper" ):
                return visitor.visitCompOper(self)
            else:
                return visitor.visitChildren(self)


    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CFlatParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(CFlatParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class SingleOperContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CFlatParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CFlatParser.ExprContext,0)

        def NOT(self):
            return self.getToken(CFlatParser.NOT, 0)
        def SUB(self):
            return self.getToken(CFlatParser.SUB, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSingleOper" ):
                return visitor.visitSingleOper(self)
            else:
                return visitor.visitChildren(self)


    class LogicOperAndContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CFlatParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CFlatParser.ExprContext)
            else:
                return self.getTypedRuleContext(CFlatParser.ExprContext,i)

        def AND2(self):
            return self.getToken(CFlatParser.AND2, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicOperAnd" ):
                return visitor.visitLogicOperAnd(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CFlatParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CFlatParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)


    class ShiftOperContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CFlatParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CFlatParser.ExprContext)
            else:
                return self.getTypedRuleContext(CFlatParser.ExprContext,i)

        def SHL(self):
            return self.getToken(CFlatParser.SHL, 0)
        def SHR(self):
            return self.getToken(CFlatParser.SHR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShiftOper" ):
                return visitor.visitShiftOper(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CFlatParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            token = self._input.LA(1)
            if token in [CFlatParser.NOT, CFlatParser.SUB]:
                localctx = CFlatParser.SingleOperContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 43
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==CFlatParser.NOT or _la==CFlatParser.SUB):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 44
                self.expr(13)

            elif token in [CFlatParser.NUMBER]:
                localctx = CFlatParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.match(CFlatParser.NUMBER)

            elif token in [CFlatParser.ID]:
                localctx = CFlatParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 46
                self.match(CFlatParser.ID)

            elif token in [CFlatParser.STRING]:
                localctx = CFlatParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 47
                self.match(CFlatParser.STRING)

            elif token in [CFlatParser.T__4]:
                localctx = CFlatParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 48
                self.match(CFlatParser.T__4)
                self.state = 49
                self.expr(0)
                self.state = 50
                self.match(CFlatParser.T__3)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 80
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 78
                    self._errHandler.sync(self);
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = CFlatParser.MulDivContext(self, CFlatParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 54
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 55
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CFlatParser.MUL) | (1 << CFlatParser.DIV) | (1 << CFlatParser.AMP))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 56
                        self.expr(13)
                        pass

                    elif la_ == 2:
                        localctx = CFlatParser.AddSubContext(self, CFlatParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 57
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 58
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CFlatParser.ADD or _la==CFlatParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 59
                        self.expr(12)
                        pass

                    elif la_ == 3:
                        localctx = CFlatParser.ShiftOperContext(self, CFlatParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 60
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 61
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CFlatParser.SHL or _la==CFlatParser.SHR):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 62
                        self.expr(11)
                        pass

                    elif la_ == 4:
                        localctx = CFlatParser.CompOperContext(self, CFlatParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 63
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 64
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CFlatParser.GRT) | (1 << CFlatParser.GRE) | (1 << CFlatParser.LES) | (1 << CFlatParser.LEE))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 65
                        self.expr(10)
                        pass

                    elif la_ == 5:
                        localctx = CFlatParser.CompOper2Context(self, CFlatParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 66
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 67
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CFlatParser.EQL or _la==CFlatParser.NEQ):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 68
                        self.expr(9)
                        pass

                    elif la_ == 6:
                        localctx = CFlatParser.BitOperContext(self, CFlatParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 69
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 70
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << CFlatParser.AND) | (1 << CFlatParser.OR) | (1 << CFlatParser.XOR))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 71
                        self.expr(8)
                        pass

                    elif la_ == 7:
                        localctx = CFlatParser.LogicOperAndContext(self, CFlatParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 72
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 73
                        self.match(CFlatParser.AND2)
                        self.state = 74
                        self.expr(7)
                        pass

                    elif la_ == 8:
                        localctx = CFlatParser.LogicOperOrContext(self, CFlatParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 75
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 76
                        self.match(CFlatParser.OR2)
                        self.state = 77
                        self.expr(6)
                        pass

             
                self.state = 82
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 5)
         




