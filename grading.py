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
import time_decorator

class TestClass(object):

    timeLimit = 2           # The time limit (in seconds) of each testcase

    def __init__(self, test_dict, solution_dict):

        self.test_dict = test_dict
        self.solution_dict = solution_dict
        self.class_ = test_dict['class']
        self.algorithm_ = test_dict['algorithm']

        self.algorithm_list = {      # The dict of all the algorithms that may be put into use
            "fractionInit": lambda: self.test(self.fractionInit),
            "privateParameter": lambda: self.test(self.privateParameter)
        }
    
    def getResult(self):
        return self.algorithm_list[self.algorithm_]()
    
    @time_decorator.time_limit(timeLimit)
    def excuteTask(self, my_algorithm):
        return my_algorithm()
    
    def test(self, my_algorithm):
        
        try:
            ans, correctAns = self.excuteTask(my_algorithm)
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
                return False, '    ' + 'Exception raised: ' + type(ans).__name__ + ': ' + str(ans) + '\n*** ' +\
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
                return False, '    ' + 'Exception raised: ' + type(ans).__name__ + ': ' + str(ans) + '\n*** ' +\
                              '    ' + '  Correct answer: ' + repr(correctAns) + '\n*** ' +\
                              '    ' + '     Tricky part: ' + self.test_dict['trickyPart']
            else:
                return True, '    ' + 'Test case passed!'
        else:
            return False, '    ' + 'Wrong answer! Exception should be raised!' + '\n*** ' +\
                            '    ' + '   Your answer: ' + str(ans) + '\n*** ' +\
                            '    ' + 'Correct answer: ' + repr(correctAns) + '\n*** ' +\
                            '    ' + '   Tricky part: ' + self.test_dict['trickyPart']
            

    def fractionInit(self):
        try:
            import pyfraction
            correctAns = eval(self.solution_dict['solution'])

            numerator = eval(self.test_dict['numerator'])
            denominator = eval(self.test_dict['denominator'])
            sign = eval(self.test_dict['sign'])

            parameter = pyfraction.Fraction(numerator, denominator, sign)
            ans = (parameter.get_numerator(), parameter.get_denominator(), parameter.is_nonnegative())
        except BaseException as e:
            ans = e
        return ans, correctAns
    
    def privateParameter(self):
        try:
            import pyfraction
            correctAns = eval(self.solution_dict['solution'])

            numerator = eval(self.test_dict['numerator'])
            denominator = eval(self.test_dict['denominator'])
            sign = eval(self.test_dict['sign'])

            parameter = pyfraction.Fraction(numerator, denominator, sign)
            names = list(vars(parameter).keys())
            ans = correctAns
            for name in names:
                if not name.startswith(correctAns):
                    ans = 'There exists parameter name "' + name + '" whitch is not private.'
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
