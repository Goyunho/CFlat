# Generated from cflat.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3H")
        buf.write("%\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\5\2\20\n\2\3\2\3\2\3\3\6\3\25\n\3\r\3\16\3\26\3\3\5\3")
        buf.write("\32\n\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\2\2\b")
        buf.write("\2\4\6\b\n\f\2\3\3\2\6\n!\2\17\3\2\2\2\4\24\3\2\2\2\6")
        buf.write("\33\3\2\2\2\b\36\3\2\2\2\n \3\2\2\2\f\"\3\2\2\2\16\20")
        buf.write("\5\4\3\2\17\16\3\2\2\2\17\20\3\2\2\2\20\21\3\2\2\2\21")
        buf.write("\22\7\2\2\3\22\3\3\2\2\2\23\25\5\6\4\2\24\23\3\2\2\2\25")
        buf.write("\26\3\2\2\2\26\24\3\2\2\2\26\27\3\2\2\2\27\31\3\2\2\2")
        buf.write("\30\32\7F\2\2\31\30\3\2\2\2\31\32\3\2\2\2\32\5\3\2\2\2")
        buf.write("\33\34\t\2\2\2\34\35\7=\2\2\35\7\3\2\2\2\36\37\7\3\2\2")
        buf.write("\37\t\3\2\2\2 !\7\4\2\2!\13\3\2\2\2\"#\7\5\2\2#\r\3\2")
        buf.write("\2\2\5\17\26\31")
        return buf.getvalue()


class cflatParser ( Parser ):

    grammarFileName = "cflat.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'++'", "'--'", "'%'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'case'", "'break'", "'continue'", 
                     "'default'", "'for'", "'while'", "'if'", "'else'", 
                     "'return'", "'switch'", "<INVALID>", "'int'", "'float'", 
                     "'string'", "'boolean'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'&'", "'&&'", 
                     "'|'", "'||'", "'^'", "'!'", "'=='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'<<'", "'>>'", "'='", "'.'", 
                     "':'", "';'", "','", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Initialisation", "Assignment", "Declaration", "Value", 
                      "Calculator", "Calculator_pmad", "Calculator_bit", 
                      "Calculator_logic", "Valiable", "Val_int", "Val_float", 
                      "Val_string", "Val_boolean", "Val_void", "Digit", 
                      "Nondigit", "Case", "Break", "Continue", "Default", 
                      "For", "While", "If", "Else", "RETURN", "Switch", 
                      "Type", "Int", "Float", "String", "Boolean", "Void", 
                      "TRUE", "FALSE", "Plus", "Minus", "Asterisk", "Div", 
                      "And", "Andand", "Or", "Oror", "Caret", "Not", "Equal", 
                      "Notequal", "Less", "Lessequal", "Greater", "Greaterequal", 
                      "Leftshift", "Rightshift", "Assign", "Dot", "Colon", 
                      "Semi", "Coma", "Leftparen", "Rightparen", "Leftbracket", 
                      "Rightbracket", "Leftbrace", "Rightbrace", "Whitespace", 
                      "Newline", "Block_comment", "Line_comment" ]

    RULE_run = 0
    RULE_line = 1
    RULE_action_end = 2
    RULE_increase = 3
    RULE_decrease = 4
    RULE_percent = 5

    ruleNames =  [ "run", "line", "action_end", "increase", "decrease", 
                   "percent" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    Initialisation=4
    Assignment=5
    Declaration=6
    Value=7
    Calculator=8
    Calculator_pmad=9
    Calculator_bit=10
    Calculator_logic=11
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
    Plus=38
    Minus=39
    Asterisk=40
    Div=41
    And=42
    Andand=43
    Or=44
    Oror=45
    Caret=46
    Not=47
    Equal=48
    Notequal=49
    Less=50
    Lessequal=51
    Greater=52
    Greaterequal=53
    Leftshift=54
    Rightshift=55
    Assign=56
    Dot=57
    Colon=58
    Semi=59
    Coma=60
    Leftparen=61
    Rightparen=62
    Leftbracket=63
    Rightbracket=64
    Leftbrace=65
    Rightbrace=66
    Whitespace=67
    Newline=68
    Block_comment=69
    Line_comment=70

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
            self.state = 13
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cflatParser.Initialisation) | (1 << cflatParser.Assignment) | (1 << cflatParser.Declaration) | (1 << cflatParser.Value) | (1 << cflatParser.Calculator))) != 0):
                self.state = 12
                self.line()


            self.state = 15
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
            self.state = 18 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 17
                self.action_end()
                self.state = 20 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cflatParser.Initialisation) | (1 << cflatParser.Assignment) | (1 << cflatParser.Declaration) | (1 << cflatParser.Value) | (1 << cflatParser.Calculator))) != 0)):
                    break

            self.state = 23
            _la = self._input.LA(1)
            if _la==cflatParser.Newline:
                self.state = 22
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

        def Calculator(self):
            return self.getToken(cflatParser.Calculator, 0)

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
            self.state = 25
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cflatParser.Initialisation) | (1 << cflatParser.Assignment) | (1 << cflatParser.Declaration) | (1 << cflatParser.Value) | (1 << cflatParser.Calculator))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
            self.state = 26
            self.match(cflatParser.Semi)
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
        self.enterRule(localctx, 6, self.RULE_increase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(cflatParser.T__0)
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
        self.enterRule(localctx, 8, self.RULE_decrease)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(cflatParser.T__1)
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
        self.enterRule(localctx, 10, self.RULE_percent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(cflatParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





