# Generated from Cbalc.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\25")
        buf.write("B\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\6\2\20\n\2\r\2\16\2\21\3\3\5\3\25\n\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\7\4\34\n\4\f\4\16\4\37\13\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\5\5\'\n\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3")
        buf.write("\7\3\7\5\7\65\n\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7=\n\7\f\7")
        buf.write("\16\7@\13\7\3\7\2\3\f\b\2\4\6\b\n\f\2\4\3\2\t\n\3\2\13")
        buf.write("\fF\2\17\3\2\2\2\4\24\3\2\2\2\6\30\3\2\2\2\b&\3\2\2\2")
        buf.write("\n(\3\2\2\2\f\64\3\2\2\2\16\20\5\4\3\2\17\16\3\2\2\2\20")
        buf.write("\21\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\3\3\2\2\2\23")
        buf.write("\25\5\6\4\2\24\23\3\2\2\2\24\25\3\2\2\2\25\26\3\2\2\2")
        buf.write("\26\27\7\22\2\2\27\5\3\2\2\2\30\35\5\b\5\2\31\32\7\3\2")
        buf.write("\2\32\34\5\b\5\2\33\31\3\2\2\2\34\37\3\2\2\2\35\33\3\2")
        buf.write("\2\2\35\36\3\2\2\2\36\7\3\2\2\2\37\35\3\2\2\2 \'\5\f\7")
        buf.write("\2!\'\5\n\6\2\"#\7\b\2\2#$\7\4\2\2$\'\5\f\7\2%\'\7\2\2")
        buf.write("\3& \3\2\2\2&!\3\2\2\2&\"\3\2\2\2&%\3\2\2\2\'\t\3\2\2")
        buf.write("\2()\7\5\2\2)*\5\f\7\2*+\7\6\2\2+\13\3\2\2\2,-\b\7\1\2")
        buf.write("-\65\7\16\2\2.\65\7\b\2\2/\65\7\r\2\2\60\61\7\7\2\2\61")
        buf.write("\62\5\f\7\2\62\63\7\6\2\2\63\65\3\2\2\2\64,\3\2\2\2\64")
        buf.write(".\3\2\2\2\64/\3\2\2\2\64\60\3\2\2\2\65>\3\2\2\2\66\67")
        buf.write("\f\b\2\2\678\t\2\2\28=\5\f\7\t9:\f\7\2\2:;\t\3\2\2;=\5")
        buf.write("\f\7\b<\66\3\2\2\2<9\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2")
        buf.write("\2\2?\r\3\2\2\2@>\3\2\2\2\t\21\24\35&\64<>")
        return buf.getvalue()


class CbalcParser ( Parser ):

    grammarFileName = "Cbalc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'='", "'print('", "')'", "'('", 
                     "<INVALID>", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "MUL", "DIV", "ADD", 
                      "SUB", "STRING", "NUMBER", "WORD", "FLAOT", "INT", 
                      "NEWLINE", "WS", "COMMENT_LINE", "COMMENT_MULLINE" ]

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
    MUL=7
    DIV=8
    ADD=9
    SUB=10
    STRING=11
    NUMBER=12
    WORD=13
    FLAOT=14
    INT=15
    NEWLINE=16
    WS=17
    COMMENT_LINE=18
    COMMENT_MULLINE=19

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
                return self.getTypedRuleContexts(CbalcParser.LineContext)
            else:
                return self.getTypedRuleContext(CbalcParser.LineContext,i)


        def getRuleIndex(self):
            return CbalcParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CbalcParser.ProgContext(self, self._ctx, self.state)
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
            return self.getToken(CbalcParser.NEWLINE, 0)

        def mulstat(self):
            return self.getTypedRuleContext(CbalcParser.MulstatContext,0)


        def getRuleIndex(self):
            return CbalcParser.RULE_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = CbalcParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            _la = self._input.LA(1)
            if ((((_la - -1)) & ~0x3f) == 0 and ((1 << (_la - -1)) & ((1 << (CbalcParser.EOF - -1)) | (1 << (CbalcParser.T__2 - -1)) | (1 << (CbalcParser.T__4 - -1)) | (1 << (CbalcParser.ID - -1)) | (1 << (CbalcParser.STRING - -1)) | (1 << (CbalcParser.NUMBER - -1)))) != 0):
                self.state = 17
                self.mulstat()


            self.state = 20
            self.match(CbalcParser.NEWLINE)
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
                return self.getTypedRuleContexts(CbalcParser.StatContext)
            else:
                return self.getTypedRuleContext(CbalcParser.StatContext,i)


        def getRuleIndex(self):
            return CbalcParser.RULE_mulstat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulstat" ):
                return visitor.visitMulstat(self)
            else:
                return visitor.visitChildren(self)




    def mulstat(self):

        localctx = CbalcParser.MulstatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mulstat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.stat()
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==CbalcParser.T__0:
                self.state = 23
                self.match(CbalcParser.T__0)
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
            return CbalcParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Lavel_no1Context(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CbalcParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CbalcParser.ExprContext,0)

        def showme(self):
            return self.getTypedRuleContext(CbalcParser.ShowmeContext,0)

        def EOF(self):
            return self.getToken(CbalcParser.EOF, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLavel_no1" ):
                return visitor.visitLavel_no1(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CbalcParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CbalcParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(CbalcParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def stat(self):

        localctx = CbalcParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_stat)
        try:
            self.state = 36
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = CbalcParser.Lavel_no1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = CbalcParser.Lavel_no1Context(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.showme()
                pass

            elif la_ == 3:
                localctx = CbalcParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.match(CbalcParser.ID)
                self.state = 33
                self.match(CbalcParser.T__1)
                self.state = 34
                self.expr(0)
                pass

            elif la_ == 4:
                localctx = CbalcParser.Lavel_no1Context(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.match(CbalcParser.EOF)
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
            return self.getTypedRuleContext(CbalcParser.ExprContext,0)


        def getRuleIndex(self):
            return CbalcParser.RULE_showme

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitShowme" ):
                return visitor.visitShowme(self)
            else:
                return visitor.visitChildren(self)




    def showme(self):

        localctx = CbalcParser.ShowmeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_showme)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(CbalcParser.T__2)
            self.state = 39
            self.expr(0)
            self.state = 40
            self.match(CbalcParser.T__3)
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
            return CbalcParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumberContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CbalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(CbalcParser.NUMBER, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber" ):
                return visitor.visitNumber(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CbalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(CbalcParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class StringContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CbalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(CbalcParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitString" ):
                return visitor.visitString(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CbalcParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CbalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CbalcParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CbalcParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CbalcParser.ExprContext)
            else:
                return self.getTypedRuleContext(CbalcParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CbalcParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CbalcParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitId" ):
                return visitor.visitId(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CbalcParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            token = self._input.LA(1)
            if token in [CbalcParser.NUMBER]:
                localctx = CbalcParser.NumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 43
                self.match(CbalcParser.NUMBER)

            elif token in [CbalcParser.ID]:
                localctx = CbalcParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(CbalcParser.ID)

            elif token in [CbalcParser.STRING]:
                localctx = CbalcParser.StringContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.match(CbalcParser.STRING)

            elif token in [CbalcParser.T__4]:
                localctx = CbalcParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 46
                self.match(CbalcParser.T__4)
                self.state = 47
                self.expr(0)
                self.state = 48
                self.match(CbalcParser.T__3)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 58
                    self._errHandler.sync(self);
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = CbalcParser.MulDivContext(self, CbalcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 52
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 53
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CbalcParser.MUL or _la==CbalcParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 54
                        self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = CbalcParser.AddSubContext(self, CbalcParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 55
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 56
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==CbalcParser.ADD or _la==CbalcParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 57
                        self.expr(6)
                        pass

             
                self.state = 62
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
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




