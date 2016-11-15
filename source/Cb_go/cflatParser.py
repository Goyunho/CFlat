# Generated from cflat.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3H")
        buf.write("\63\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\4\t\t\t\3\2\5\2\24\n\2\3\2\3\2\3\3\6\3\31\n\3\r")
        buf.write("\3\16\3\32\3\3\5\3\36\n\3\3\4\3\4\3\4\3\5\3\5\3\5\7\5")
        buf.write("&\n\5\f\5\16\5)\13\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3")
        buf.write("\t\2\2\n\2\4\6\b\n\f\16\20\2\3\3\2\6\n.\2\23\3\2\2\2\4")
        buf.write("\30\3\2\2\2\6\37\3\2\2\2\b\"\3\2\2\2\n*\3\2\2\2\f,\3\2")
        buf.write("\2\2\16.\3\2\2\2\20\60\3\2\2\2\22\24\5\4\3\2\23\22\3\2")
        buf.write("\2\2\23\24\3\2\2\2\24\25\3\2\2\2\25\26\7\2\2\3\26\3\3")
        buf.write("\2\2\2\27\31\5\6\4\2\30\27\3\2\2\2\31\32\3\2\2\2\32\30")
        buf.write("\3\2\2\2\32\33\3\2\2\2\33\35\3\2\2\2\34\36\7F\2\2\35\34")
        buf.write("\3\2\2\2\35\36\3\2\2\2\36\5\3\2\2\2\37 \5\b\5\2 !\7=\2")
        buf.write("\2!\7\3\2\2\2\"\'\5\n\6\2#$\7>\2\2$&\5\n\6\2%#\3\2\2\2")
        buf.write("&)\3\2\2\2\'%\3\2\2\2\'(\3\2\2\2(\t\3\2\2\2)\'\3\2\2\2")
        buf.write("*+\t\2\2\2+\13\3\2\2\2,-\7\3\2\2-\r\3\2\2\2./\7\4\2\2")
        buf.write("/\17\3\2\2\2\60\61\7\5\2\2\61\21\3\2\2\2\6\23\32\35\'")
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
    RULE_actions = 3
    RULE_action = 4
    RULE_increase = 5
    RULE_decrease = 6
    RULE_percent = 7

    ruleNames =  [ "run", "line", "action_end", "actions", "action", "increase", 
                   "decrease", "percent" ]

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
            self.state = 17
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cflatParser.Initialisation) | (1 << cflatParser.Assignment) | (1 << cflatParser.Declaration) | (1 << cflatParser.Value) | (1 << cflatParser.Calculator))) != 0):
                self.state = 16
                self.line()


            self.state = 19
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
            self.state = 22 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 21
                self.action_end()
                self.state = 24 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cflatParser.Initialisation) | (1 << cflatParser.Assignment) | (1 << cflatParser.Declaration) | (1 << cflatParser.Value) | (1 << cflatParser.Calculator))) != 0)):
                    break

            self.state = 27
            _la = self._input.LA(1)
            if _la==cflatParser.Newline:
                self.state = 26
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

        def actions(self):
            return self.getTypedRuleContext(cflatParser.ActionsContext,0)


        def Semi(self):
            return self.getToken(cflatParser.Semi, 0)

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
            self.state = 29
            self.actions()
            self.state = 30
            self.match(cflatParser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ActionsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cflatParser.ActionContext)
            else:
                return self.getTypedRuleContext(cflatParser.ActionContext,i)


        def Coma(self, i:int=None):
            if i is None:
                return self.getTokens(cflatParser.Coma)
            else:
                return self.getToken(cflatParser.Coma, i)

        def getRuleIndex(self):
            return cflatParser.RULE_actions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActions" ):
                listener.enterActions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActions" ):
                listener.exitActions(self)




    def actions(self):

        localctx = cflatParser.ActionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_actions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.action()
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cflatParser.Coma:
                self.state = 33
                self.match(cflatParser.Coma)
                self.state = 34
                self.action()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ActionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

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
            return cflatParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)




    def action(self):

        localctx = cflatParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << cflatParser.Initialisation) | (1 << cflatParser.Assignment) | (1 << cflatParser.Declaration) | (1 << cflatParser.Value) | (1 << cflatParser.Calculator))) != 0)):
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
        self.enterRule(localctx, 10, self.RULE_increase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
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
        self.enterRule(localctx, 12, self.RULE_decrease)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
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
        self.enterRule(localctx, 14, self.RULE_percent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(cflatParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





