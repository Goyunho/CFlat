# Generated from cflat.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3I")
        buf.write("e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\3\3")
        buf.write("\3\3\6\3\36\n\3\r\3\16\3\37\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4\62\n\4\3\4")
        buf.write("\3\4\5\4\66\n\4\3\4\3\4\5\4:\n\4\3\4\3\4\5\4>\n\4\3\5")
        buf.write("\3\5\3\5\7\5C\n\5\f\5\16\5F\13\5\3\5\3\5\3\6\6\6K\n\6")
        buf.write("\r\6\16\6L\3\6\5\6P\n\6\3\7\3\7\3\7\3\b\3\b\3\b\7\bX\n")
        buf.write("\b\f\b\16\b[\13\b\3\t\3\t\3\n\3\n\3\13\3\13\3\f\3\f\3")
        buf.write("\f\2\2\r\2\4\6\b\n\f\16\20\22\24\26\2\4\4\2\b\b\16\16")
        buf.write("\3\2\7\13e\2\30\3\2\2\2\4\35\3\2\2\2\6=\3\2\2\2\b?\3\2")
        buf.write("\2\2\nJ\3\2\2\2\fQ\3\2\2\2\16T\3\2\2\2\20\\\3\2\2\2\22")
        buf.write("^\3\2\2\2\24`\3\2\2\2\26b\3\2\2\2\30\31\5\4\3\2\31\32")
        buf.write("\7\2\2\3\32\3\3\2\2\2\33\36\5\n\6\2\34\36\5\b\5\2\35\33")
        buf.write("\3\2\2\2\35\34\3\2\2\2\36\37\3\2\2\2\37\35\3\2\2\2\37")
        buf.write(" \3\2\2\2 \5\3\2\2\2!\"\7\34\2\2\"#\7@\2\2#$\7\16\2\2")
        buf.write("$%\7A\2\2%>\5\b\5\2&\'\7\3\2\2\'(\5\b\5\2()\7\34\2\2)")
        buf.write("*\7@\2\2*+\7\16\2\2+,\7A\2\2,-\7>\2\2->\3\2\2\2./\7\33")
        buf.write("\2\2/\61\7@\2\2\60\62\t\2\2\2\61\60\3\2\2\2\61\62\3\2")
        buf.write("\2\2\62\63\3\2\2\2\63\65\7>\2\2\64\66\7\16\2\2\65\64\3")
        buf.write("\2\2\2\65\66\3\2\2\2\66\67\3\2\2\2\679\7>\2\28:\t\2\2")
        buf.write("\298\3\2\2\29:\3\2\2\2:;\3\2\2\2;<\7A\2\2<>\5\b\5\2=!")
        buf.write("\3\2\2\2=&\3\2\2\2=.\3\2\2\2>\7\3\2\2\2?D\7D\2\2@C\5\n")
        buf.write("\6\2AC\5\b\5\2B@\3\2\2\2BA\3\2\2\2CF\3\2\2\2DB\3\2\2\2")
        buf.write("DE\3\2\2\2EG\3\2\2\2FD\3\2\2\2GH\7E\2\2H\t\3\2\2\2IK\5")
        buf.write("\f\7\2JI\3\2\2\2KL\3\2\2\2LJ\3\2\2\2LM\3\2\2\2MO\3\2\2")
        buf.write("\2NP\7G\2\2ON\3\2\2\2OP\3\2\2\2P\13\3\2\2\2QR\5\16\b\2")
        buf.write("RS\7>\2\2S\r\3\2\2\2TY\5\20\t\2UV\7?\2\2VX\5\20\t\2WU")
        buf.write("\3\2\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\17\3\2\2\2[Y\3")
        buf.write("\2\2\2\\]\t\3\2\2]\21\3\2\2\2^_\7\4\2\2_\23\3\2\2\2`a")
        buf.write("\7\5\2\2a\25\3\2\2\2bc\7\6\2\2c\27\3\2\2\2\r\35\37\61")
        buf.write("\659=BDLOY")
        return buf.getvalue()


class cflatParser ( Parser ):

    grammarFileName = "cflat.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'do'", "'++'", "'--'", "'%'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'case'", "'break'", 
                     "'continue'", "'default'", "'for'", "'while'", "'if'", 
                     "'else'", "'return'", "'switch'", "<INVALID>", "'int'", 
                     "'float'", "'string'", "'boolean'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'&'", "'&&'", 
                     "'|'", "'||'", "'^'", "'!'", "'=='", "'!='", "'<'", 
                     "'<='", "'>'", "'>='", "'<<'", "'>>'", "'='", "'.'", 
                     "':'", "';'", "','", "'('", "')'", "'['", "']'", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "Initialisation", "Assignment", "Declaration", 
                      "Value", "Calculator", "Calculator_pmad", "Calculator_bit", 
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
    RULE_frame = 1
    RULE_iterationStatement = 2
    RULE_brace_group = 3
    RULE_line = 4
    RULE_action_end = 5
    RULE_actions = 6
    RULE_action = 7
    RULE_increase = 8
    RULE_decrease = 9
    RULE_percent = 10

    ruleNames =  [ "run", "frame", "iterationStatement", "brace_group", 
                   "line", "action_end", "actions", "action", "increase", 
                   "decrease", "percent" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    Initialisation=5
    Assignment=6
    Declaration=7
    Value=8
    Calculator=9
    Calculator_pmad=10
    Calculator_bit=11
    Calculator_logic=12
    Valiable=13
    Val_int=14
    Val_float=15
    Val_string=16
    Val_boolean=17
    Val_void=18
    Digit=19
    Nondigit=20
    Case=21
    Break=22
    Continue=23
    Default=24
    For=25
    While=26
    If=27
    Else=28
    RETURN=29
    Switch=30
    Type=31
    Int=32
    Float=33
    String=34
    Boolean=35
    Void=36
    TRUE=37
    FALSE=38
    Plus=39
    Minus=40
    Asterisk=41
    Div=42
    And=43
    Andand=44
    Or=45
    Oror=46
    Caret=47
    Not=48
    Equal=49
    Notequal=50
    Less=51
    Lessequal=52
    Greater=53
    Greaterequal=54
    Leftshift=55
    Rightshift=56
    Assign=57
    Dot=58
    Colon=59
    Semi=60
    Coma=61
    Leftparen=62
    Rightparen=63
    Leftbracket=64
    Rightbracket=65
    Leftbrace=66
    Rightbrace=67
    Whitespace=68
    Newline=69
    Block_comment=70
    Line_comment=71

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RunContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def frame(self):
            return self.getTypedRuleContext(cflatParser.FrameContext,0)


        def EOF(self):
            return self.getToken(cflatParser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.frame()
            self.state = 23
            self.match(cflatParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FrameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cflatParser.LineContext)
            else:
                return self.getTypedRuleContext(cflatParser.LineContext,i)


        def brace_group(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cflatParser.Brace_groupContext)
            else:
                return self.getTypedRuleContext(cflatParser.Brace_groupContext,i)


        def getRuleIndex(self):
            return cflatParser.RULE_frame

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrame" ):
                listener.enterFrame(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrame" ):
                listener.exitFrame(self)




    def frame(self):

        localctx = cflatParser.FrameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_frame)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 27
                token = self._input.LA(1)
                if token in [cflatParser.Initialisation, cflatParser.Assignment, cflatParser.Declaration, cflatParser.Value, cflatParser.Calculator]:
                    self.state = 25
                    self.line()

                elif token in [cflatParser.Leftbrace]:
                    self.state = 26
                    self.brace_group()

                else:
                    raise NoViableAltException(self)

                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((((_la - 5)) & ~0x3f) == 0 and ((1 << (_la - 5)) & ((1 << (cflatParser.Initialisation - 5)) | (1 << (cflatParser.Assignment - 5)) | (1 << (cflatParser.Declaration - 5)) | (1 << (cflatParser.Value - 5)) | (1 << (cflatParser.Calculator - 5)) | (1 << (cflatParser.Leftbrace - 5)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IterationStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Calculator_logic(self, i:int=None):
            if i is None:
                return self.getTokens(cflatParser.Calculator_logic)
            else:
                return self.getToken(cflatParser.Calculator_logic, i)

        def brace_group(self):
            return self.getTypedRuleContext(cflatParser.Brace_groupContext,0)


        def Assignment(self, i:int=None):
            if i is None:
                return self.getTokens(cflatParser.Assignment)
            else:
                return self.getToken(cflatParser.Assignment, i)

        def getRuleIndex(self):
            return cflatParser.RULE_iterationStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterationStatement" ):
                listener.enterIterationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterationStatement" ):
                listener.exitIterationStatement(self)




    def iterationStatement(self):

        localctx = cflatParser.IterationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_iterationStatement)
        self._la = 0 # Token type
        try:
            self.state = 59
            token = self._input.LA(1)
            if token in [cflatParser.While]:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.match(cflatParser.While)
                self.state = 32
                self.match(cflatParser.Leftparen)
                self.state = 33
                self.match(cflatParser.Calculator_logic)
                self.state = 34
                self.match(cflatParser.Rightparen)
                self.state = 35
                self.brace_group()

            elif token in [cflatParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.match(cflatParser.T__0)
                self.state = 37
                self.brace_group()
                self.state = 38
                self.match(cflatParser.While)
                self.state = 39
                self.match(cflatParser.Leftparen)
                self.state = 40
                self.match(cflatParser.Calculator_logic)
                self.state = 41
                self.match(cflatParser.Rightparen)
                self.state = 42
                self.match(cflatParser.Semi)

            elif token in [cflatParser.For]:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
                self.match(cflatParser.For)
                self.state = 45
                self.match(cflatParser.Leftparen)
                self.state = 47
                _la = self._input.LA(1)
                if _la==cflatParser.Assignment or _la==cflatParser.Calculator_logic:
                    self.state = 46
                    _la = self._input.LA(1)
                    if not(_la==cflatParser.Assignment or _la==cflatParser.Calculator_logic):
                        self._errHandler.recoverInline(self)
                    else:
                        self.consume()


                self.state = 49
                self.match(cflatParser.Semi)
                self.state = 51
                _la = self._input.LA(1)
                if _la==cflatParser.Calculator_logic:
                    self.state = 50
                    self.match(cflatParser.Calculator_logic)


                self.state = 53
                self.match(cflatParser.Semi)
                self.state = 55
                _la = self._input.LA(1)
                if _la==cflatParser.Assignment or _la==cflatParser.Calculator_logic:
                    self.state = 54
                    _la = self._input.LA(1)
                    if not(_la==cflatParser.Assignment or _la==cflatParser.Calculator_logic):
                        self._errHandler.recoverInline(self)
                    else:
                        self.consume()


                self.state = 57
                self.match(cflatParser.Rightparen)
                self.state = 58
                self.brace_group()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Brace_groupContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Leftbrace(self):
            return self.getToken(cflatParser.Leftbrace, 0)

        def Rightbrace(self):
            return self.getToken(cflatParser.Rightbrace, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cflatParser.LineContext)
            else:
                return self.getTypedRuleContext(cflatParser.LineContext,i)


        def brace_group(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(cflatParser.Brace_groupContext)
            else:
                return self.getTypedRuleContext(cflatParser.Brace_groupContext,i)


        def getRuleIndex(self):
            return cflatParser.RULE_brace_group

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBrace_group" ):
                listener.enterBrace_group(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBrace_group" ):
                listener.exitBrace_group(self)




    def brace_group(self):

        localctx = cflatParser.Brace_groupContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_brace_group)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(cflatParser.Leftbrace)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 5)) & ~0x3f) == 0 and ((1 << (_la - 5)) & ((1 << (cflatParser.Initialisation - 5)) | (1 << (cflatParser.Assignment - 5)) | (1 << (cflatParser.Declaration - 5)) | (1 << (cflatParser.Value - 5)) | (1 << (cflatParser.Calculator - 5)) | (1 << (cflatParser.Leftbrace - 5)))) != 0):
                self.state = 64
                token = self._input.LA(1)
                if token in [cflatParser.Initialisation, cflatParser.Assignment, cflatParser.Declaration, cflatParser.Value, cflatParser.Calculator]:
                    self.state = 62
                    self.line()

                elif token in [cflatParser.Leftbrace]:
                    self.state = 63
                    self.brace_group()

                else:
                    raise NoViableAltException(self)

                self.state = 68
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
            self.match(cflatParser.Rightbrace)
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
        self.enterRule(localctx, 8, self.RULE_line)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 71
                    self.action_end()

                else:
                    raise NoViableAltException(self)
                self.state = 74 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 77
            _la = self._input.LA(1)
            if _la==cflatParser.Newline:
                self.state = 76
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
        self.enterRule(localctx, 10, self.RULE_action_end)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.actions()
            self.state = 80
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
        self.enterRule(localctx, 12, self.RULE_actions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.action()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cflatParser.Coma:
                self.state = 83
                self.match(cflatParser.Coma)
                self.state = 84
                self.action()
                self.state = 89
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
        self.enterRule(localctx, 14, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
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
        self.enterRule(localctx, 16, self.RULE_increase)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(cflatParser.T__1)
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
        self.enterRule(localctx, 18, self.RULE_decrease)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.match(cflatParser.T__2)
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
        self.enterRule(localctx, 20, self.RULE_percent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(cflatParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





