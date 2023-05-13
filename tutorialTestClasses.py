# tutorialTestClasses.py
# -------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to ShanghaiTech University, including a link 
# to https://i-techx.github.io/iTechX/courses?course_code=CS274A
# 
# Attribution Information: The NLP projects were developed at ShanghaiTech University.
# The core projects and autograders were adapted by Haoyi Wu (wuhy1@shanghaitech.edu.cn)

# tutorialTestClasses.py
# ----------------------
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


import testClasses
import util


# Simple test case which evals an arbitrary piece of python code.
# The test is correct if the output of the code given the student's
# solution matches that of the instructor's.
class EvalTest(testClasses.TestCase):

    def __init__(self, name, question, testDict):
        super(EvalTest, self).__init__(name, question, testDict)
        self.preamble = compile(testDict.get('preamble', ""), "%s.preamble" % self.getPath(), 'exec')
        self.test = compile(testDict['test'], "%s.test" % self.getPath(), 'eval')
        self.success = testDict['success']
        self.failure = testDict['failure']

    def evalCode(self, moduleDict):
        bindings = dict(moduleDict)
        # exec self.preamble in bindings
        exec(self.preamble, bindings)
        return str(eval(self.test, bindings))

    def execute(self, grades, moduleDict, solutionDict):
        result = self.evalCode(moduleDict)
        if result == solutionDict['result']:
            grades.addMessage('PASS: %s' % self.path)
            grades.addMessage('\t%s' % self.success)
            return True
        else:
            grades.addMessage('FAIL: %s' % self.path)
            grades.addMessage('\t%s' % self.failure)
            grades.addMessage('\tstudent result: "%s"' % result)
            grades.addMessage('\tcorrect result: "%s"' % solutionDict['result'])

        return False

    def writeSolution(self, moduleDict, filePath):
        with open(filePath, 'w') as handle:
            handle.write('# This is the solution file for %s.\n' % self.path)
            handle.write('# The result of evaluating the test must equal the below when cast to a string.\n')

            handle.write('result: "%s"\n' % self.evalCode(moduleDict))
        return True


# Hidden test case checks the md5 of the result. Student can view
# the test case but not the plain text of the solution.
class HiddenTest(EvalTest):

    def evalCode(self, moduleDict):
        bindings = dict(moduleDict)
        # exec self.preamble in bindings
        exec(self.preamble, bindings)
        return util.md5(eval(self.test, bindings))

    def writeSolution(self, moduleDict, filePath):
        with open(filePath, 'w') as handle:
            handle.write('# This is the solution file for %s.\n' % self.path)
            handle.write('# The hash of the result of evaluating the test must equal the below.\n')

            handle.write('result: "%s"\n' % self.evalCode(moduleDict))
        return True


# Test case that requires student to raise an exception.
class ExceptionTest(EvalTest):

    def execute(self, grades, moduleDict, solutionDict):
        try:
            result = self.evalCode(moduleDict)
        except Exception as inst:
            if str(type(inst)) == solutionDict['result']:
                grades.addMessage('PASS: %s' % self.path)
                grades.addMessage('\t%s' % self.success)
                return True
            raise inst
        
        grades.addMessage('FAIL: %s' % self.path)
        grades.addMessage('\t%s' % self.failure)
        grades.addMessage('\tstudent result: "%s"' % result)
        grades.addMessage('\tcorrect result: "%s"' % solutionDict['result'])

        return False

    def writeSolution(self, moduleDict, filePath):
        with open(filePath, 'w') as handle:
            handle.write('# This is the solution file for %s.\n' % self.path)
            handle.write('# The result of evaluating the test must raise the following exception.\n')

            try:
                result = self.evalCode(moduleDict)
            except Exception as inst:
                result = str(type(inst))
            else:
                raise RuntimeError('Use ExceptionTest but no exception raised.')

            handle.write('result: "%s"\n' % result)
        return True