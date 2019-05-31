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
import sys, traceback
import time_decorator

class TestClass(object):

    timeLimit = 2           # The time limit (in seconds) of each testcase

    def __init__(self, test_dict, solution_dict):

        self.test_dict = test_dict
        self.solution_dict = solution_dict
        self.class_ = test_dict['class']
        self.algorithm_ = test_dict['algorithm']

        self.algorithm_list = {      # The dict of all the algorithms that may be put into use
            "init": lambda: self.test(self.init),
            "addition": lambda: self.test(self.addition),
            "equalization": lambda: self.test(self.equalization),
            "reverse": lambda: self.test(self.reverse),
            "bitChange": lambda: self.test(self.bitChange),
            "getitem": lambda: self.test(self.getitem),
            "setitem": lambda: self.test(self.setitem),
            "his": lambda: self.test(self.his),
            "hiseq": lambda: self.test(self.hiseq),
            "kernel": lambda: self.test(self.kernel),
            "huffman": lambda: self.test(self.huffman),
            "consecutiveTest": lambda: self.test(self.consecutiveTest)
        }
    
    def getResult(self):
        return self.algorithm_list[self.algorithm_]()
    
    def test(self, my_algorithm, time = timeLimit):
        
        @time_decorator.time_limit(time)
        def excuteTask(my_algorithm):
            return my_algorithm()
        
        try:
            ans, correctAns = excuteTask(my_algorithm)
        except Exception as e:
            ans, correctAns = e, "Solution not accessable due to TimeOutError. Please find it in file."
        
        if self.test_dict['class'] == 'IOTest':
            return self.IOTest(ans, correctAns)
        elif self.test_dict['class'] == 'ExceptionTest':
            return self.ExceptionTest(ans, correctAns) 

    def IOTest(self, ans, correctAns):
        if isinstance(ans, BaseException):
            if isinstance(ans, ImportError):
                return False, '    ' + 'Code not found! Please check the path of your code.'
            elif isinstance(ans, NotImplementedError):
                return False, '    ' + 'Have not been implemented!'
            else:
                return False, '    ' + 'Exception raised: ' + type(ans).__name__ + \
                              ' (line %d)' % traceback.extract_tb(ans.__traceback__)[-1].lineno + ': ' + str(ans) + '\n*** ' + \
                              '    ' + '  Exception line: ' + str(traceback.extract_tb(ans.__traceback__)[-1].line) + '\n*** ' + \
                              '    ' + '     Tricky part: ' + self.test_dict['trickyPart']
        elif ans != correctAns:
            return False, '    ' + 'Wrong answer!' + '\n*** ' +\
                           '    ' + '   Your answer: ' + str(ans) + '\n*** ' +\
                           '    ' + 'Correct answer: ' + str(correctAns) + '\n*** ' +\
                           '    ' + '   Tricky part: ' + self.test_dict['trickyPart']
        else:
            return True, '    ' + 'Test case passed!'

    
    def ExceptionTest(self, ans, correctAns):
        if isinstance(ans, BaseException):
            if isinstance(ans, ImportError):
                return False, '    ' + 'Code not found! Please check the path of your code.'
            elif isinstance(ans, NotImplementedError):
                return False, '    ' + 'Have not been implemented!'
            elif not issubclass(type(ans), type(correctAns)):
                return False, '    ' + 'Exception raised: ' + type(ans).__name__ + \
                              ' (line %d)' % traceback.extract_tb(ans.__traceback__)[-1].lineno + ': ' + str(ans) + '\n*** ' + \
                              '    ' + '  Exception line: ' + str(traceback.extract_tb(ans.__traceback__)[-1].line) + '\n*** ' + \
                              '    ' + '  Correct answer: ' + repr(correctAns) + '\n*** ' +\
                              '    ' + '     Tricky part: ' + self.test_dict['trickyPart']
            else:
                return True, '    ' + 'Test case passed!'
        else:
            return False, '    ' + 'Wrong answer! Exception should be raised!' + '\n*** ' +\
                            '    ' + '   Your answer: ' + str(ans) + '\n*** ' +\
                            '    ' + 'Correct answer: ' + repr(correctAns) + '\n*** ' +\
                            '    ' + '   Tricky part: ' + self.test_dict['trickyPart']
            

    def init(self):
        try:
            import DIP
            correctAns = eval(self.solution_dict['solution'])

            imageInput = eval(self.test_dict['imageInput'])
            n = eval(self.test_dict['n'])

            img = DIP.Image(imageInput, n)
            ans = str(img)
        except BaseException as e:
            ans = e
        return ans, correctAns
    
    def addition(self):
        try:
            import DIP
            correctAns = eval(self.solution_dict['solution'])

            imageInput_1 = eval(self.test_dict['imageInput_1'])
            n_1 = eval(self.test_dict['n_1'])
            imageInput_2 = eval(self.test_dict['imageInput_2'])
            n_2 = eval(self.test_dict['n_2'])

            img1 = DIP.Image(imageInput_1, n_1)
            img2 = DIP.Image(imageInput_2, n_2)
            ans = str(img1 + img2)
        except BaseException as e:
            ans = e
        return ans, correctAns
    
    def equalization(self):
        try:
            import DIP
            correctAns = eval(self.solution_dict['solution'])

            imageInput_1 = eval(self.test_dict['imageInput_1'])
            n_1 = eval(self.test_dict['n_1'])
            imageInput_2 = eval(self.test_dict['imageInput_2'])
            n_2 = eval(self.test_dict['n_2'])

            img1 = DIP.Image(imageInput_1, n_1)
            img2 = DIP.Image(imageInput_2, n_2)
            ans = img1 == img2
        except BaseException as e:
            ans = e
        return ans, correctAns
    
    def reverse(self):
        try:
            import DIP
            correctAns = eval(self.solution_dict['solution'])

            imageInput = eval(self.test_dict['imageInput'])
            n = eval(self.test_dict['n'])

            img = DIP.Image(imageInput, n)
            ans = str(img.reverse())
        except BaseException as e:
            ans = e
        return ans, correctAns
    
    def bitChange(self):
        try:
            import DIP
            correctAns = eval(self.solution_dict['solution'])

            imageInput = eval(self.test_dict['imageInput'])
            n = eval(self.test_dict['n'])
            new_n = eval(self.test_dict['new_n'])

            img = DIP.Image(imageInput, n)
            ans = str(img.bitChange(new_n))
        except BaseException as e:
            ans = e
        return ans, correctAns
    
    def getitem(self):
        try:
            import DIP
            correctAns = eval(self.solution_dict['solution'])

            imageInput = eval(self.test_dict['imageInput'])
            n = eval(self.test_dict['n'])
            index = self.test_dict['index']

            img = DIP.Image(imageInput, n)
            ans = eval(index)
        except BaseException as e:
            ans = e
        return ans, correctAns
    
    def setitem(self):
        try:
            import DIP
            correctAns = eval(self.solution_dict['solution'])

            imageInput = eval(self.test_dict['imageInput'])
            n = eval(self.test_dict['n'])
            index = self.test_dict['index']
            target = eval(self.test_dict['target'])

            img = DIP.Image(imageInput, n)
            exec(index + ' = target')
            ans = str(img)
        except BaseException as e:
            ans = e
        return ans, correctAns
    
    def his(self):
        try:
            import DIP
            correctAns = eval(self.solution_dict['solution'])

            imageInput = eval(self.test_dict['imageInput'])
            n = eval(self.test_dict['n'])

            img = DIP.Image(imageInput, n)
            ans = img.his()
        except BaseException as e:
            ans = e
        return ans, correctAns
    
    def hiseq(self):
        try:
            import DIP
            correctAns = eval(self.solution_dict['solution'])

            imageInput = eval(self.test_dict['imageInput'])
            n = eval(self.test_dict['n'])

            img = DIP.Image(imageInput, n)
            ans = str(img.hiseq())
        except BaseException as e:
            ans = e
        return ans, correctAns
    
    def kernel(self):
        try:
            import DIP
            correctAns = eval(self.solution_dict['solution'])

            imageInput = eval(self.test_dict['imageInput'])
            n = eval(self.test_dict['n'])
            kernel = eval(self.test_dict['kernel'])

            img = DIP.Image(imageInput, n)
            ans = str(img * kernel)
        except BaseException as e:
            ans = e
        return ans, correctAns
    
    def huffman(self):
        try:
            import DIP
            correctAns = eval(self.solution_dict['solution'])

            imageInput = eval(self.test_dict['imageInput'])
            n = eval(self.test_dict['n'])

            img = DIP.Image(imageInput, n)
            ans = img.huffman()
        except BaseException as e:
            ans = e
        return ans, correctAns
    
    def consecutiveTest(self):
        try:
            import DIP
            correctAns = eval(self.solution_dict['solution'])

            exec(self.test_dict['code'])

            ans = eval(self.test_dict['ans'])
        except BaseException as e:
            ans = e
        return ans, correctAns

    

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
