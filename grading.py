# grading.py
# -------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


import re
import sys

class TestClass(object):

    def __init__(self, test_dict, solution_dict):

        self.test_dict = test_dict
        self.solution_dict = solution_dict
        self.class_ = test_dict['class']
        self.algorithm_ = test_dict['algorithm']

        self.algorithm_list = {
            "stateOf": lambda: self.stateOf(),
            "codeOf": lambda: self.codeOf(),
            "RotWord": lambda: self.RotWord(),
            "SubWord": lambda: self.SubWord(),
            "XOR": lambda: self.XOR(),
            "keyExpansion": lambda: self.keyExpansion(),
            "SubBytes": lambda: self.SubBytes(),
            "InvSubBytes": lambda: self.InvSubBytes(),
            "ShiftRows": lambda: self.ShiftRows(),
            "InvShiftRows": lambda: self.InvShiftRows(),
            "MixColumns": lambda: self.MixColumns(),
            "InvMixColumns": lambda: self.InvMixColumns(),
            "AddRoundKey": lambda: self.AddRoundKey(),
            "AES_init": lambda: self.AES_init(),
            "AES_enc": lambda: self.AES_enc(),
            "AES_dec": lambda: self.AES_dec(),
            "AESCBC_enc": lambda: self.AESCBC_enc(),
            "AESCBC_dec": lambda: self.AESCBC_dec()
        }
    
    def getResult(self):
        return self.algorithm_list[self.algorithm_]()

    def IOTest(self, ans, correctAns):
        if issubclass(type(ans), Exception):
            if issubclass(type(ans), ImportError):
                return False, '    ' + 'Code not found! Please check the path of your code.'
            elif issubclass(type(ans), InterruptedError):
                return False, '    ' + 'Have not been implemented!'
            else:
                return False, '    ' + 'Exception raised: ' + repr(ans) + ': ' + str(ans) + '\n*** ' +\
                              '    ' + '     Tricky part: ' + self.test_dict['trickyPart']
        elif ans != correctAns:
            return False, '    ' + 'Wrong answer!' + '\n*** ' +\
                           '    ' + '   Your answer: ' + str(ans) + '\n*** ' +\
                           '    ' + 'Correct answer: ' + str(correctAns) + '\n*** ' +\
                           '    ' + '   Tricky part: ' + self.test_dict['trickyPart']
        else:
            return True, '    ' + 'Test case passed!'
    
    def RandKeyTest(self, ans, correctAns):
        if issubclass(type(ans), Exception):
            if issubclass(type(ans), ImportError):
                return False, '    ' + 'Code not found! Please check the path of your code.'
            elif issubclass(type(ans), InterruptedError):
                return False, '    ' + 'Have not been implemented!'
            else:
                return False, '    ' + 'Exception raised: ' + repr(ans) + ': ' + str(ans) + '\n*** ' +\
                              '    ' + '     Tricky part: ' + self.test_dict['trickyPart']
        elif type(ans) != int or ans<0 or ans.bit_length() > correctAns:
            return False, '    ' + 'Wrong answer!' + '\n*** ' +\
                           '    ' + '   Your answer: ' + str(ans) + '\n*** ' +\
                           '    ' + 'Correct answer: bit length in ' + str(correctAns) + '\n*** ' +\
                           '    ' + '   Tricky part: ' + self.test_dict['trickyPart']
        else:
            return True, '    ' + 'Test case passed!'
    
    def ExceptionTest(self, ans, correctAns):
        if issubclass(type(ans), Exception):
            if issubclass(type(ans), ImportError):
                return False, '    ' + 'Code not found! Please check the path of your code.'
            elif issubclass(type(ans), InterruptedError):
                return False, '    ' + 'Have not been implemented!'
            elif type(ans) != type(correctAns):
                return False, '    ' + 'Exception raised: ' + repr(ans) + ': ' + str(ans) + '\n*** ' +\
                              '    ' + '  Correct answer: ' + repr(correctAns) + '\n*** ' +\
                              '    ' + '     Tricky part: ' + self.test_dict['trickyPart']
            else:
                return True, '    ' + 'Test case passed!'
        else:
            return False, '    ' + 'Wrong answer! Exception should be raised!' + '\n*** ' +\
                            '    ' + '   Your answer: ' + str(ans) + '\n*** ' +\
                            '    ' + 'Correct answer: ' + repr(correctAns) + '\n*** ' +\
                            '    ' + '   Tricky part: ' + self.test_dict['trickyPart']
            

    def stateOf(self):
        code = eval(self.test_dict['code'])
        correctAns = eval(self.solution_dict['solution'])
        try:
            import aes
            ans = aes.stateOf(code)
        except Exception as e:
            ans = e
        if self.test_dict['class'] == 'IOTest':
            return self.IOTest(ans, correctAns)
    
    def codeOf(self):
        state = eval(self.test_dict['state'])
        correctAns = eval(self.solution_dict['solution'])
        try:
            import aes
            ans = aes.codeOf(state)
        except Exception as e:
            ans = e
        if self.test_dict['class'] == 'IOTest':
            return self.IOTest(ans, correctAns)

    def RotWord(self):
        word = eval(self.test_dict['word'])
        correctAns = eval(self.solution_dict['solution'])
        try:
            import aes
            ans = aes.RotWord(word)
        except Exception as e:
            ans = e
        if self.test_dict['class'] == 'IOTest':
            return self.IOTest(ans, correctAns)
    
    def SubWord(self):
        word = eval(self.test_dict['word'])
        correctAns = eval(self.solution_dict['solution'])
        try:
            import aes
            ans = aes.SubWord(word)
        except Exception as e:
            ans = e
        if self.test_dict['class'] == 'IOTest':
            return self.IOTest(ans, correctAns)
    
    def XOR(self):
        item1, item2 = eval(self.test_dict['items'])
        correctAns = eval(self.solution_dict['solution'])
        try:
            import aes
            ans = aes.XOR(item1, item2)
        except Exception as e:
            ans = e
        if self.test_dict['class'] == 'IOTest':
            return self.IOTest(ans, correctAns)
    
    def keyExpansion(self):
        key = eval(self.test_dict['key'])
        Nk = eval(self.test_dict['Nk'])
        correctAns = eval(self.solution_dict['solution'])
        try:
            import aes
            ans = aes.keyExpansion(key, Nk)
        except Exception as e:
            ans = e
        if self.test_dict['class'] == 'IOTest':
            return self.IOTest(ans, correctAns)
    
    def SubBytes(self):
        state = eval(self.test_dict['state'])
        correctAns = eval(self.solution_dict['solution'])
        try:
            import aes
            aes.SubBytes(state)
            ans = state
        except Exception as e:
            ans = e
        if self.test_dict['class'] == 'IOTest':
            return self.IOTest(ans, correctAns)
    
    def InvSubBytes(self):
        state = eval(self.test_dict['state'])
        correctAns = eval(self.solution_dict['solution'])
        try:
            import aes
            aes.InvSubBytes(state)
            ans = state
        except Exception as e:
            ans = e
        if self.test_dict['class'] == 'IOTest':
            return self.IOTest(ans, correctAns)
    
    def ShiftRows(self):
        state = eval(self.test_dict['state'])
        correctAns = eval(self.solution_dict['solution'])
        try:
            import aes
            aes.ShiftRows(state)
            ans = state
        except Exception as e:
            ans = e
        if self.test_dict['class'] == 'IOTest':
            return self.IOTest(ans, correctAns)
    
    def InvShiftRows(self):
        state = eval(self.test_dict['state'])
        correctAns = eval(self.solution_dict['solution'])
        try:
            import aes
            aes.InvShiftRows(state)
            ans = state
        except Exception as e:
            ans = e
        if self.test_dict['class'] == 'IOTest':
            return self.IOTest(ans, correctAns)
    
    def MixColumns(self):
        state = eval(self.test_dict['state'])
        correctAns = eval(self.solution_dict['solution'])
        try:
            import aes
            aes.MixColumns(state)
            ans = state
        except Exception as e:
            ans = e
        if self.test_dict['class'] == 'IOTest':
            return self.IOTest(ans, correctAns)
    
    def InvMixColumns(self):
        state = eval(self.test_dict['state'])
        correctAns = eval(self.solution_dict['solution'])
        try:
            import aes
            aes.InvMixColumns(state)
            ans = state
        except Exception as e:
            ans = e
        if self.test_dict['class'] == 'IOTest':
            return self.IOTest(ans, correctAns)
    
    def AddRoundKey(self):
        state = eval(self.test_dict['state'])
        roundKey = eval(self.test_dict['roundKey'])
        correctAns = eval(self.solution_dict['solution'])
        try:
            import aes
            aes.AddRoundKey(state, roundKey)
            ans = state
        except Exception as e:
            ans = e
        if self.test_dict['class'] == 'IOTest':
            return self.IOTest(ans, correctAns)
    
    def AES_init(self):
        keylen = eval(self.test_dict['keylen'])
        key = eval(self.test_dict['key'])
        correctAns = None
        try:
            import aes
            correctAns = eval(self.solution_dict['solution'])
            t = aes.AES(keylen, key)
            ans = t.getkey()
        except Exception as e:
            ans = e
        if self.test_dict['class'] == 'IOTest':
            return self.IOTest(ans, correctAns)
        elif self.test_dict['class'] == 'RandKeyTest':
            return self.RandKeyTest(ans, correctAns)
        elif self.test_dict['class'] == 'ExceptionTest':
            return self.ExceptionTest(ans, correctAns)
    
    def AES_enc(self):
        keylen = eval(self.test_dict['keylen'])
        key = eval(self.test_dict['key'])
        msg = eval(self.test_dict['msg'])
        correctAns = None
        try:
            import aes
            correctAns = eval(self.solution_dict['solution'])
            t = aes.AES(keylen, key)
            ans = t.enc(msg)
        except Exception as e:
            ans = e
        if self.test_dict['class'] == 'IOTest':
            return self.IOTest(ans, correctAns)
        elif self.test_dict['class'] == 'RandKeyTest':
            return self.RandKeyTest(ans, correctAns)
        elif self.test_dict['class'] == 'ExceptionTest':
            return self.ExceptionTest(ans, correctAns)
    
    def AES_dec(self):
        keylen = eval(self.test_dict['keylen'])
        key = eval(self.test_dict['key'])
        ciph = eval(self.test_dict['ciph'])
        correctAns = None
        try:
            import aes
            correctAns = eval(self.solution_dict['solution'])
            t = aes.AES(keylen, key)
            ans = t.dec(ciph)
        except Exception as e:
            ans = e
        if self.test_dict['class'] == 'IOTest':
            return self.IOTest(ans, correctAns)
        elif self.test_dict['class'] == 'RandKeyTest':
            return self.RandKeyTest(ans, correctAns)
        elif self.test_dict['class'] == 'ExceptionTest':
            return self.ExceptionTest(ans, correctAns)
    
    def AESCBC_enc(self):
        keylen = eval(self.test_dict['keylen'])
        key = eval(self.test_dict['key'])
        msg = eval(self.test_dict['msg'])
        msglen = eval(self.test_dict['msglen'])
        iv = eval(self.test_dict['iv'])
        msg_file = eval(self.test_dict['msg_file'])
        ciph_file = eval(self.test_dict['ciph_file'])
        pad = eval(self.test_dict['pad'])
        correctAns = None
        try:
            import aes
            correctAns = eval(self.solution_dict['solution'])
            t = aes.AESCBC(keylen, key)
            if type(msg_file) == str:
                with open(msg_file, 'wb') as f:
                    f.write(msg.to_bytes(msglen, 'big'))
            t.encfile(msg_file, ciph_file, iv, pad)
            if type(ciph_file) == str:
                with open(ciph_file, 'rb') as f:
                    ciph = int.from_bytes(f.read(), 'big')
            ans = ciph
        except Exception as e:
            ans = e
        if self.test_dict['class'] == 'IOTest':
            return self.IOTest(ans, correctAns)
        elif self.test_dict['class'] == 'RandKeyTest':
            return self.RandKeyTest(ans, correctAns)
        elif self.test_dict['class'] == 'ExceptionTest':
            return self.ExceptionTest(ans, correctAns)
    
    def AESCBC_dec(self):
        keylen = eval(self.test_dict['keylen'])
        key = eval(self.test_dict['key'])
        ciph = eval(self.test_dict['ciph'])
        ciphlen = eval(self.test_dict['ciphlen'])
        iv = eval(self.test_dict['iv'])
        msg_file = eval(self.test_dict['msg_file'])
        ciph_file = eval(self.test_dict['ciph_file'])
        pad = eval(self.test_dict['pad'])
        correctAns = None
        try:
            import aes
            correctAns = eval(self.solution_dict['solution'])
            t = aes.AESCBC(keylen, key)
            if type(ciph_file) == str:
                with open(ciph_file, 'wb') as f:
                    f.write(ciph.to_bytes(ciphlen, 'big'))
            t.decfile(ciph_file, msg_file, iv, pad)
            if type(msg_file) == str:
                with open(msg_file, 'rb') as f:
                    msg = int.from_bytes(f.read(), 'big')
            ans = msg
        except Exception as e:
            ans = e
        if self.test_dict['class'] == 'IOTest':
            return self.IOTest(ans, correctAns)
        elif self.test_dict['class'] == 'RandKeyTest':
            return self.RandKeyTest(ans, correctAns)
        elif self.test_dict['class'] == 'ExceptionTest':
            return self.ExceptionTest(ans, correctAns)
    

class TestParser(object):

    def __init__(self, path):
        # save the path to the test file
        self.path = path

    def removeComments(self, rawlines):
        # remove any portion of a line following a '#' symbol
        fixed_lines = []
        for l in rawlines:
            idx = l.find('#')
            if idx == -1:
                fixed_lines.append(l)
            else:
                fixed_lines.append(l[0:idx])
        return '\n'.join(fixed_lines)

    def parse(self):
        # read in the test case and remove comments
        test = {}
        with open(self.path) as handle:
            raw_lines = handle.read().split('\n')

        test_text = self.removeComments(raw_lines)
        test['__raw_lines__'] = raw_lines
        test['path'] = self.path
        test['__emit__'] = []
        lines = test_text.split('\n')
        i = 0
        # read a property in each loop cycle
        while(i < len(lines)):
            # skip blank lines
            if re.match('\A\s*\Z', lines[i]):
                test['__emit__'].append(("raw", raw_lines[i]))
                i += 1
                continue
            m = re.match('\A([^"]*?):\s*"([^"]*)"\s*\Z', lines[i])
            if m:
                test[m.group(1)] = m.group(2)
                test['__emit__'].append(("oneline", m.group(1)))
                i += 1
                continue
            m = re.match('\A([^"]*?):\s*"""\s*\Z', lines[i])
            if m:
                msg = []
                i += 1
                while(not re.match('\A\s*"""\s*\Z', lines[i])):
                    msg.append(raw_lines[i])
                    i += 1
                test[m.group(1)] = '\n'.join(msg)
                test['__emit__'].append(("multiline", m.group(1)))
                i += 1
                continue
            print ('error parsing test file: %s' % self.path)
            sys.exit(1)
        return test


def emitTestDict(testDict, handle):
    for kind, data in testDict['__emit__']:
        if kind == "raw":
            handle.write(data + "\n")
        elif kind == "oneline":
            handle.write('%s: "%s"\n' % (data, testDict[data]))
        elif kind == "multiline":
            handle.write('%s: """\n%s\n"""\n' % (data, testDict[data]))
        else:
            raise Exception("Bad __emit__")
