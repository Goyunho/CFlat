# Generated from cflat.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3@")
        buf.write("\65\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\5\2\30\n\2\3\2\3")
        buf.write("\2\3\3\6\3\35\n\3\r\3\16\3\36\3\3\5\3\"\n\3\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\2-\2\27\3\2")
        buf.write("\2\2\4\34\3\2\2\2\6#\3\2\2\2\b&\3\2\2\2\n(\3\2\2\2\f*")
        buf.write("\3\2\2\2\16,\3\2\2\2\20.\3\2\2\2\22\60\3\2\2\2\24\62\3")
        buf.write("\2\2\2\26\30\5\4\3\2\27\26\3\2\2\2\27\30\3\2\2\2\30\31")
        buf.write("\3\2\2\2\31\32\7\2\2\3\32\3\3\2\2\2\33\35\5\6\4\2\34\33")
        buf.write("\3\2\2\2\35\36\3\2\2\2\36\34\3\2\2\2\36\37\3\2\2\2\37")
        buf.write("!\3\2\2\2 \"\7>\2\2! \3\2\2\2!\"\3\2\2\2\"\5\3\2\2\2#")
        buf.write("$\7\13\2\2$%\7\65\2\2%\7\3\2\2\2&\'\7\3\2\2\'\t\3\2\2")
        buf.write("\2()\7\4\2\2)\13\3\2\2\2*+\7\5\2\2+\r\3\2\2\2,-\7\6\2")
        buf.write("\2-\17\3\2\2\2./\7\7\2\2/\21\3\2\2\2\60\61\7\b\2\2\61")
        buf.write("\23\3\2\2\2\62\63\7\t\2\2\63\25\3\2\2\2\5\27\36!")
        return buf.getvalue()


class cflatParser ( Parser ):

    grammarFileName = "cflat.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'++'", "'-'", "'--'", "'*'", "'/'", 
                     "'%'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'case'", "'break'", 
                     "'continue'", "'default'", "'for'", "'while'", "'if'", 
                     "'else'", "'return'", "'switch'", "'int'", "'float'", 
                     "'string'", "'boolean'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'&'", "'&&'", "'|'", "'||'", "'^'", "'!'", 
                     "'=='", "'!='", "'<'", "'<='", "'>'", "'>='", "'='", 
                     "'.'", "':'", "';'", "','", "'('", "')'", "'['", "']'", 
                     "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "Declaration", "Value", "Type", "Valiable", "Val_int", 
                      "Val_float", "Val_string", "Val_boolean", "Val_void", 
                      "Digit", "Nondigit", "Case", "Break", "Continue", 
                      "Default", "For", "While", "If", "Else", "RETURN", 
                      "Switch", "Int", "Float", "String", "Boolean", "Void", 
                      "TRUE", "FALSE", "And", "Andand", "Or", "Oror", "Caret", 
                      "Not", "Equal", "Notequal", "Less", "Lessequal", "Greater", 
                      "Greaterequal", "Assign", "Dot", "Colon", "Semi", 
                      "Coma", "Leftparen", "Rightparen", "Leftbracket", 
                      "Rightbracket", "Leftbrace", "Rightbrace", "Whitespace", 
                      "Newline", "Block_comment", "Line_comment" ]

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
    Declaration=8
    Value=9
    Type=10
    Valiable=11
    Val_int=12
    Val_float=13
    Val_string=14
    Val_boolean=15
    Val_void=16
    Digit=17
    Nondigit=18
    Case=19
    Break=20
    Continue=21
    Default=22
    For=23
    While=24
    If=25
    Else=26
    RETURN=27
    Switch=28
    Int=29
    Float=30
    String=31
    Boolean=32
    Void=33
    TRUE=34
    FALSE=35
    And=36
    Andand=37
    Or=38
    Oror=39
    Caret=40
    Not=41
    Equal=42
    Notequal=43
    Less=44
    Lessequal=45
    Greater=46
    Greaterequal=47
    Assign=48
    Dot=49
    Colon=50
    Semi=51
    Coma=52
    Leftparen=53
    Rightparen=54
    Leftbracket=55
    Rightbracket=56
    Leftbrace=57
    Rightbrace=58
    Whitespace=59
    Newline=60
    Block_comment=61
    Line_comment=62

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
            if _la==cflatParser.Value:
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
                if not (_la==cflatParser.Value):
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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(cflatParser.Value)
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





