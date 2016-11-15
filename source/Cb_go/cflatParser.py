# Generated from cflat.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3;")
        buf.write("u\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\5\2*\n\2\3\2\3\2\3\3\6\3/\n\3\r\3\16\3")
        buf.write("\60\3\3\3\3\3\3\6\3\66\n\3\r\3\16\3\67\5\3:\n\3\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\5\5D\n\5\3\6\6\6G\n\6\r\6\16")
        buf.write("\6H\3\7\6\7L\n\7\r\7\16\7M\3\b\3\b\3\b\3\b\3\t\3\t\7\t")
        buf.write("V\n\t\f\t\16\tY\13\t\3\t\3\t\3\n\3\n\5\n_\n\n\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3")
        buf.write("\21\3\22\3\22\3\23\3\23\3\24\3\24\3\24\3W\2\25\2\4\6\b")
        buf.write("\n\f\16\20\22\24\26\30\32\34\36 \"$&\2\5\3\2\21\22\3\2")
        buf.write("\4\6\3\2\7\tm\2)\3\2\2\2\49\3\2\2\2\6;\3\2\2\2\bC\3\2")
        buf.write("\2\2\nF\3\2\2\2\fK\3\2\2\2\16O\3\2\2\2\20S\3\2\2\2\22")
        buf.write("^\3\2\2\2\24`\3\2\2\2\26b\3\2\2\2\30d\3\2\2\2\32f\3\2")
        buf.write("\2\2\34h\3\2\2\2\36j\3\2\2\2 l\3\2\2\2\"n\3\2\2\2$p\3")
        buf.write("\2\2\2&r\3\2\2\2(*\5\4\3\2)(\3\2\2\2)*\3\2\2\2*+\3\2\2")
        buf.write("\2+,\7\2\2\3,\3\3\2\2\2-/\5\6\4\2.-\3\2\2\2/\60\3\2\2")
        buf.write("\2\60.\3\2\2\2\60\61\3\2\2\2\61\62\3\2\2\2\62\63\79\2")
        buf.write("\2\63:\3\2\2\2\64\66\5\6\4\2\65\64\3\2\2\2\66\67\3\2\2")
        buf.write("\2\67\65\3\2\2\2\678\3\2\2\28:\3\2\2\29.\3\2\2\29\65\3")
        buf.write("\2\2\2:\5\3\2\2\2;<\5\b\5\2<=\7\61\2\2=\7\3\2\2\2>D\5")
        buf.write("\f\7\2?D\5\16\b\2@D\5\20\t\2AD\5\22\n\2BD\5\24\13\2C>")
        buf.write("\3\2\2\2C?\3\2\2\2C@\3\2\2\2CA\3\2\2\2CB\3\2\2\2D\t\3")
        buf.write("\2\2\2EG\t\2\2\2FE\3\2\2\2GH\3\2\2\2HF\3\2\2\2HI\3\2\2")
        buf.write("\2I\13\3\2\2\2JL\7\21\2\2KJ\3\2\2\2LM\3\2\2\2MK\3\2\2")
        buf.write("\2MN\3\2\2\2N\r\3\2\2\2OP\5\f\7\2PQ\7/\2\2QR\5\f\7\2R")
        buf.write("\17\3\2\2\2SW\7\3\2\2TV\13\2\2\2UT\3\2\2\2VY\3\2\2\2W")
        buf.write("X\3\2\2\2WU\3\2\2\2XZ\3\2\2\2YW\3\2\2\2Z[\7\3\2\2[\21")
        buf.write("\3\2\2\2\\_\5\26\f\2]_\5\30\r\2^\\\3\2\2\2^]\3\2\2\2_")
        buf.write("\23\3\2\2\2`a\7!\2\2a\25\3\2\2\2bc\t\3\2\2c\27\3\2\2\2")
        buf.write("de\t\4\2\2e\31\3\2\2\2fg\7\n\2\2g\33\3\2\2\2hi\7\13\2")
        buf.write("\2i\35\3\2\2\2jk\7\f\2\2k\37\3\2\2\2lm\7\r\2\2m!\3\2\2")
        buf.write("\2no\7\16\2\2o#\3\2\2\2pq\7\17\2\2q%\3\2\2\2rs\7\20\2")
        buf.write("\2s\'\3\2\2\2\13)\60\679CHMW^")
        return buf.getvalue()


class cflatParser ( Parser ):

    grammarFileName = "cflat.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\"'", "'true'", "'Ture'", "'TRUE'", 
                     "'false'", "'False'", "'FALSE'", "'+'", "'++'", "'-'", 
                     "'--'", "'*'", "'/'", "'%'", "<INVALID>", "<INVALID>", 
                     "'case'", "'break'", "'continue'", "'default'", "'for'", 
                     "'while'", "'if'", "'else'", "'return'", "'switch'", 
                     "'int'", "'float'", "'string'", "'boolean'", "'void'", 
                     "'&'", "'&&'", "'|'", "'||'", "'^'", "'!'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'='", "'.'", 
                     "':'", "';'", "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "Digit", "Nondigit", 
                      "Case", "Break", "Continue", "Default", "For", "While", 
                      "If", "Else", "RETURN", "Switch", "Int", "Float", 
                      "String", "Boolean", "Void", "And", "Andand", "Or", 
                      "Oror", "Caret", "Not", "Equal", "Notequal", "Less", 
                      "Lessequal", "Greater", "Greaterequal", "Assign", 
                      "Dot", "Colon", "Semi", "Leftparen", "Rightparen", 
                      "Leftbracket", "Rightbracket", "Leftbrace", "Rightbrace", 
                      "Whitespace", "Newline", "Block_comment", "Line_comment" ]

    RULE_run = 0
    RULE_line = 1
    RULE_action_end = 2
    RULE_value = 3
    RULE_valiable = 4
    RULE_v_int = 5
    RULE_v_float = 6
    RULE_v_string = 7
    RULE_v_boolean = 8
    RULE_v_void = 9
    RULE_true = 10
    RULE_false = 11
    RULE_plus = 12
    RULE_increase = 13
    RULE_minus = 14
    RULE_decrease = 15
    RULE_asterisk = 16
    RULE_div = 17
    RULE_percent = 18

    ruleNames =  [ "run", "line", "action_end", "value", "valiable", "v_int", 
                   "v_float", "v_string", "v_boolean", "v_void", "true", 
                   "false", "plus", "increase", "minus", "decrease", "asterisk", 
                   "div", "percent" ]

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
    Digit=15
    Nondigit=16
    Case=17
    Break=18
    Continue=19
    Default=20
    For=21
    While=22
    If=23
    Else=24
    RETURN=25
    Switch=26
    Int=27
    Float=28
    String=29
    Boolean=30
    Void=31
    And=32
    Andand=33
    Or=34
    Oror=35
    Caret=36
    Not=37
    Equal=38
    Notequal=39
    Less=40
    Lessequal=41
    Greater=42
    Greaterequal=43
    Assign=44
    Dot=45
    Colon=46
    Semi=47
    Leftparen=48
    Rightparen=49
    Leftbracket=50
    Rightbracket=51
    Leftbrace=52
    Rightbrace=53
    Whitespace=54
    Newline=55
    Block_comment=56
    Line_comment=57

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RunContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(cflatParser.EOF, 0)

        def line(self):
            return self.getTypedRuleContext(cflatParser.LineContext,0)


        def getRuleIndex(self):
            return cflatParser.RULE_run

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRun" ):
                listener.enterRun(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRun" ):
                listener.exitRun(self)




    def run(self):

        localctx = cflatParser.RunContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_run)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cflatParser.T__0) | (1 << cflatParser.T__1) | (1 << cflatParser.T__2) | (1 << cflatParser.T__3) | (1 << cflatParser.T__4) | (1 << cflatParser.T__5) | (1 << cflatParser.T__6) | (1 << cflatParser.Digit) | (1 << cflatParser.Void))) != 0):
                self.state = 38
                self.line()


            self.state = 41
            self.match(cflatParser.EOF)
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

        def Newline(self):
            return self.getToken(cflatParser.Newline, 0)

        def action_end(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cflatParser.Action_endContext)
            else:
                return self.getTypedRuleContext(cflatParser.Action_endContext,i)


        def getRuleIndex(self):
            return cflatParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)




    def line(self):

        localctx = cflatParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.state = 55
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 43
                    self.action_end()
                    self.state = 46 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cflatParser.T__0) | (1 << cflatParser.T__1) | (1 << cflatParser.T__2) | (1 << cflatParser.T__3) | (1 << cflatParser.T__4) | (1 << cflatParser.T__5) | (1 << cflatParser.T__6) | (1 << cflatParser.Digit) | (1 << cflatParser.Void))) != 0)):
                        break

                self.state = 48
                self.match(cflatParser.Newline)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 50
                    self.action_end()
                    self.state = 53 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cflatParser.T__0) | (1 << cflatParser.T__1) | (1 << cflatParser.T__2) | (1 << cflatParser.T__3) | (1 << cflatParser.T__4) | (1 << cflatParser.T__5) | (1 << cflatParser.T__6) | (1 << cflatParser.Digit) | (1 << cflatParser.Void))) != 0)):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Action_endContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Semi(self):
            return self.getToken(cflatParser.Semi, 0)

        def value(self):
            return self.getTypedRuleContext(cflatParser.ValueContext,0)


        def getRuleIndex(self):
            return cflatParser.RULE_action_end

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction_end" ):
                listener.enterAction_end(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction_end" ):
                listener.exitAction_end(self)




    def action_end(self):

        localctx = cflatParser.Action_endContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_action_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.value()
            self.state = 58
            self.match(cflatParser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def v_int(self):
            return self.getTypedRuleContext(cflatParser.V_intContext,0)


        def v_float(self):
            return self.getTypedRuleContext(cflatParser.V_floatContext,0)


        def v_string(self):
            return self.getTypedRuleContext(cflatParser.V_stringContext,0)


        def v_boolean(self):
            return self.getTypedRuleContext(cflatParser.V_booleanContext,0)


        def v_void(self):
            return self.getTypedRuleContext(cflatParser.V_voidContext,0)


        def getRuleIndex(self):
            return cflatParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = cflatParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_value)
        try:
            self.state = 65
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.v_int()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.v_float()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.v_string()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.v_boolean()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 64
                self.v_void()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValiableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Nondigit(self, i:int=None):
            if i is None:
                return self.getTokens(cflatParser.Nondigit)
            else:
                return self.getToken(cflatParser.Nondigit, i)

        def Digit(self, i:int=None):
            if i is None:
                return self.getTokens(cflatParser.Digit)
            else:
                return self.getToken(cflatParser.Digit, i)

        def getRuleIndex(self):
            return cflatParser.RULE_valiable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValiable" ):
                listener.enterValiable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValiable" ):
                listener.exitValiable(self)




    def valiable(self):

        localctx = cflatParser.ValiableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_valiable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 67
                _la = self._input.LA(1)
                if not(_la==cflatParser.Digit or _la==cflatParser.Nondigit):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 70 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==cflatParser.Digit or _la==cflatParser.Nondigit):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class V_intContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Digit(self, i:int=None):
            if i is None:
                return self.getTokens(cflatParser.Digit)
            else:
                return self.getToken(cflatParser.Digit, i)

        def getRuleIndex(self):
            return cflatParser.RULE_v_int

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterV_int" ):
                listener.enterV_int(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitV_int" ):
                listener.exitV_int(self)




    def v_int(self):

        localctx = cflatParser.V_intContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_v_int)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 72
                self.match(cflatParser.Digit)
                self.state = 75 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==cflatParser.Digit):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class V_floatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def v_int(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cflatParser.V_intContext)
            else:
                return self.getTypedRuleContext(cflatParser.V_intContext,i)


        def Dot(self):
            return self.getToken(cflatParser.Dot, 0)

        def getRuleIndex(self):
            return cflatParser.RULE_v_float

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterV_float" ):
                listener.enterV_float(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitV_float" ):
                listener.exitV_float(self)




    def v_float(self):

        localctx = cflatParser.V_floatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_v_float)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.v_int()
            self.state = 78
            self.match(cflatParser.Dot)
            self.state = 79
            self.v_int()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class V_stringContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cflatParser.RULE_v_string

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterV_string" ):
                listener.enterV_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitV_string" ):
                listener.exitV_string(self)




    def v_string(self):

        localctx = cflatParser.V_stringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_v_string)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(cflatParser.T__0)
            self.state = 85
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 82
                    self.matchWildcard() 
                self.state = 87
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 88
            self.match(cflatParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class V_booleanContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def true(self):
            return self.getTypedRuleContext(cflatParser.TrueContext,0)


        def false(self):
            return self.getTypedRuleContext(cflatParser.FalseContext,0)


        def getRuleIndex(self):
            return cflatParser.RULE_v_boolean

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterV_boolean" ):
                listener.enterV_boolean(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitV_boolean" ):
                listener.exitV_boolean(self)




    def v_boolean(self):

        localctx = cflatParser.V_booleanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_v_boolean)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            token = self._input.LA(1)
            if token in [cflatParser.T__1, cflatParser.T__2, cflatParser.T__3]:
                self.state = 90
                self.true()

            elif token in [cflatParser.T__4, cflatParser.T__5, cflatParser.T__6]:
                self.state = 91
                self.false()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class V_voidContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cflatParser.RULE_v_void

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterV_void" ):
                listener.enterV_void(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitV_void" ):
                listener.exitV_void(self)




    def v_void(self):

        localctx = cflatParser.V_voidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_v_void)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(cflatParser.Void)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TrueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cflatParser.RULE_true

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrue" ):
                listener.enterTrue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrue" ):
                listener.exitTrue(self)




    def true(self):

        localctx = cflatParser.TrueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_true)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cflatParser.T__1) | (1 << cflatParser.T__2) | (1 << cflatParser.T__3))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FalseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cflatParser.RULE_false

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFalse" ):
                listener.enterFalse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFalse" ):
                listener.exitFalse(self)




    def false(self):

        localctx = cflatParser.FalseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_false)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cflatParser.T__4) | (1 << cflatParser.T__5) | (1 << cflatParser.T__6))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PlusContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cflatParser.RULE_plus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlus" ):
                listener.enterPlus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlus" ):
                listener.exitPlus(self)




    def plus(self):

        localctx = cflatParser.PlusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_plus)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(cflatParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IncreaseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cflatParser.RULE_increase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncrease" ):
                listener.enterIncrease(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncrease" ):
                listener.exitIncrease(self)




    def increase(self):

        localctx = cflatParser.IncreaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_increase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(cflatParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MinusContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cflatParser.RULE_minus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinus" ):
                listener.enterMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinus" ):
                listener.exitMinus(self)




    def minus(self):

        localctx = cflatParser.MinusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_minus)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(cflatParser.T__9)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DecreaseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cflatParser.RULE_decrease

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecrease" ):
                listener.enterDecrease(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecrease" ):
                listener.exitDecrease(self)




    def decrease(self):

        localctx = cflatParser.DecreaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_decrease)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(cflatParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AsteriskContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cflatParser.RULE_asterisk

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsterisk" ):
                listener.enterAsterisk(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsterisk" ):
                listener.exitAsterisk(self)




    def asterisk(self):

        localctx = cflatParser.AsteriskContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_asterisk)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(cflatParser.T__11)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DivContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cflatParser.RULE_div

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiv" ):
                listener.enterDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiv" ):
                listener.exitDiv(self)




    def div(self):

        localctx = cflatParser.DivContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_div)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(cflatParser.T__12)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PercentContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return cflatParser.RULE_percent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPercent" ):
                listener.enterPercent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPercent" ):
                listener.exitPercent(self)




    def percent(self):

        localctx = cflatParser.PercentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_percent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(cflatParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





