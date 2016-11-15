# Generated from cflat.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3B")
        buf.write("\65\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\5\2\30\n\2\3\2\3")
        buf.write("\2\3\3\6\3\35\n\3\r\3\16\3\36\3\3\5\3\"\n\3\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\3\3\2\n\r-")
        buf.write("\2\27\3\2\2\2\4\34\3\2\2\2\6#\3\2\2\2\b&\3\2\2\2\n(\3")
        buf.write("\2\2\2\f*\3\2\2\2\16,\3\2\2\2\20.\3\2\2\2\22\60\3\2\2")
        buf.write("\2\24\62\3\2\2\2\26\30\5\4\3\2\27\26\3\2\2\2\27\30\3\2")
        buf.write("\2\2\30\31\3\2\2\2\31\32\7\2\2\3\32\3\3\2\2\2\33\35\5")
        buf.write("\6\4\2\34\33\3\2\2\2\35\36\3\2\2\2\36\34\3\2\2\2\36\37")
        buf.write("\3\2\2\2\37!\3\2\2\2 \"\7@\2\2! \3\2\2\2!\"\3\2\2\2\"")
        buf.write("\5\3\2\2\2#$\t\2\2\2$%\7\67\2\2%\7\3\2\2\2&\'\7\3\2\2")
        buf.write("\'\t\3\2\2\2()\7\4\2\2)\13\3\2\2\2*+\7\5\2\2+\r\3\2\2")
        buf.write("\2,-\7\6\2\2-\17\3\2\2\2./\7\7\2\2/\21\3\2\2\2\60\61\7")
        buf.write("\b\2\2\61\23\3\2\2\2\62\63\7\t\2\2\63\25\3\2\2\2\5\27")
        buf.write("\36!")
        return buf.getvalue()


class cflatParser ( Parser ):

    grammarFileName = "cflat.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'++'", "'-'", "'--'", "'*'", "'/'", 
                     "'%'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'case'", "'break'", "'continue'", "'default'", "'for'", 
                     "'while'", "'if'", "'else'", "'return'", "'switch'", 
                     "<INVALID>", "'int'", "'float'", "'string'", "'boolean'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'&'", "'&&'", 
                     "'|'", "'||'", "'^'", "'!'", "'=='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'='", "'.'", "':'", "';'", 
                     "','", "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Initialisation", "Assignment", "Declaration", "Value", 
                      "Valiable", "Val_int", "Val_float", "Val_string", 
                      "Val_boolean", "Val_void", "Digit", "Nondigit", "Case", 
                      "Break", "Continue", "Default", "For", "While", "If", 
                      "Else", "RETURN", "Switch", "Type", "Int", "Float", 
                      "String", "Boolean", "Void", "TRUE", "FALSE", "And", 
                      "Andand", "Or", "Oror", "Caret", "Not", "Equal", "Notequal", 
                      "Less", "Lessequal", "Greater", "Greaterequal", "Assign", 
                      "Dot", "Colon", "Semi", "Coma", "Leftparen", "Rightparen", 
                      "Leftbracket", "Rightbracket", "Leftbrace", "Rightbrace", 
                      "Whitespace", "Newline", "Block_comment", "Line_comment" ]

    RULE_run = 0
    RULE_line = 1
    RULE_action_end = 2
    RULE_plus = 3
    RULE_increase = 4
    RULE_minus = 5
    RULE_decrease = 6
    RULE_asterisk = 7
    RULE_div = 8
    RULE_percent = 9

    ruleNames =  [ "run", "line", "action_end", "plus", "increase", "minus", 
                   "decrease", "asterisk", "div", "percent" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    Initialisation=8
    Assignment=9
    Declaration=10
    Value=11
    Valiable=12
    Val_int=13
    Val_float=14
    Val_string=15
    Val_boolean=16
    Val_void=17
    Digit=18
    Nondigit=19
    Case=20
    Break=21
    Continue=22
    Default=23
    For=24
    While=25
    If=26
    Else=27
    RETURN=28
    Switch=29
    Type=30
    Int=31
    Float=32
    String=33
    Boolean=34
    Void=35
    TRUE=36
    FALSE=37
    And=38
    Andand=39
    Or=40
    Oror=41
    Caret=42
    Not=43
    Equal=44
    Notequal=45
    Less=46
    Lessequal=47
    Greater=48
    Greaterequal=49
    Assign=50
    Dot=51
    Colon=52
    Semi=53
    Coma=54
    Leftparen=55
    Rightparen=56
    Leftbracket=57
    Rightbracket=58
    Leftbrace=59
    Rightbrace=60
    Whitespace=61
    Newline=62
    Block_comment=63
    Line_comment=64

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
            self.state = 21
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cflatParser.Initialisation) | (1 << cflatParser.Assignment) | (1 << cflatParser.Declaration) | (1 << cflatParser.Value))) != 0):
                self.state = 20
                self.line()


            self.state = 23
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

        def action_end(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cflatParser.Action_endContext)
            else:
                return self.getTypedRuleContext(cflatParser.Action_endContext,i)


        def Newline(self):
            return self.getToken(cflatParser.Newline, 0)

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
            self.enterOuterAlt(localctx, 1)
            self.state = 26 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 25
                self.action_end()
                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cflatParser.Initialisation) | (1 << cflatParser.Assignment) | (1 << cflatParser.Declaration) | (1 << cflatParser.Value))) != 0)):
                    break

            self.state = 31
            _la = self._input.LA(1)
            if _la==cflatParser.Newline:
                self.state = 30
                self.match(cflatParser.Newline)


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

        def Initialisation(self):
            return self.getToken(cflatParser.Initialisation, 0)

        def Assignment(self):
            return self.getToken(cflatParser.Assignment, 0)

        def Declaration(self):
            return self.getToken(cflatParser.Declaration, 0)

        def Value(self):
            return self.getToken(cflatParser.Value, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cflatParser.Initialisation) | (1 << cflatParser.Assignment) | (1 << cflatParser.Declaration) | (1 << cflatParser.Value))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 34
            self.match(cflatParser.Semi)
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
        self.enterRule(localctx, 6, self.RULE_plus)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(cflatParser.T__0)
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
        self.enterRule(localctx, 8, self.RULE_increase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(cflatParser.T__1)
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
        self.enterRule(localctx, 10, self.RULE_minus)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(cflatParser.T__2)
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
        self.enterRule(localctx, 12, self.RULE_decrease)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(cflatParser.T__3)
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
        self.enterRule(localctx, 14, self.RULE_asterisk)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(cflatParser.T__4)
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
        self.enterRule(localctx, 16, self.RULE_div)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(cflatParser.T__5)
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
        self.enterRule(localctx, 18, self.RULE_percent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(cflatParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





