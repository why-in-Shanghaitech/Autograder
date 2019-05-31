# autograder.py
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


import optparse
import os, sys
from grading import TestParser, TestClass

default_question_list = ['q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8']

def readCommand(argv):
    parser = optparse.OptionParser(description = 'Run public tests on student code')
    parser.set_defaults(muteResult=False, showFile=False, showInfo=False)
    parser.add_option('--test-directory',
                      dest = 'testRoot',
                      default = 'test_cases',
                      help = 'Root test directory which contains subdirectories corresponding to each question')
    parser.add_option('--code-directory',
                    dest = 'codeRoot',
                    default = "",
                    help = 'Root directory containing the student and testClass code')
    parser.add_option('--mute', '-m',
                    dest = 'muteResult',
                    action = 'store_true',
                    help = 'Mute the result printing.')
    parser.add_option('--show-file',
                    dest = 'showFile',
                    action = 'store_true',
                    help = 'Show the .test and .solution files if the answer is wrong.')
    parser.add_option('--show-info', '-s',
                    dest = 'showInfo',
                    action = 'store_true',
                    help = 'Show the input parameter and solution if the answer is wrong. Not conducted when --show-file is added.')
    parser.add_option('--test', '-t',
                      dest = 'runTest',
                      default = None,
                      help = 'Run one particular test.  Relative to test root.')
    parser.add_option('--question', '-q',
                    dest = 'gradeQuestion',
                    default = None,
                    help = 'Grade one particular question.')
    (options, args) = parser.parse_args(argv)
    return options


def readFile(path, root=""):
    "Read file from disk at specified path and return as string"
    with open(os.path.join(root, path), 'r') as handle:
        return handle.read()


def evaluate(test_dict, solution_dict):
    evaluation = TestClass(test_dict, solution_dict)
    return evaluation.getResult()    


if __name__ == '__main__':
    options = readCommand(sys.argv)
    sys.path.append(os.path.join(os.getcwd(), options.codeRoot))

    if options.gradeQuestion == None:
        questions = default_question_list
    else:
        questions = [options.gradeQuestion]

    if options.runTest != None:

        path = options.runTest

        # test = readFile(path)
        test_parser = TestParser(path)
        
        # solution = readFile(path.replace('.test', '.solution'))
        solution_parser = TestParser(path.replace('.test', '.solution'))
        
        passed, message = evaluate(test_parser.parse(), solution_parser.parse())
        
        if passed:
            message = '*** PASS: ' + path + '\n*** ' + message
        else:
            message = '*** FAIL: ' + path + '\n*** ' + message

        if not passed and options.showFile:

            test_file = '\n***     '.join(test_parser.parse()['__raw_lines__'])
            test_file = '\n***\n***     ==================\n***     Below is the test file (' +\
                            test_parser.parse()['path'] + '):\n*** \n***     ' +\
                            test_file + '\n***     ==================\n'

            solution_file = '\n***     '.join(solution_parser.parse()['__raw_lines__'])
            solution_file = '***     Below is the solution file (' +\
                                solution_parser.parse()['path'] +\
                                '):\n*** \n***     ' + solution_file + '\n***'
            
            message += test_file + solution_file
        
        elif not passed and options.showInfo:

            test_parsed = test_parser.parse()
            input_varibles = set(test_parsed.keys()).difference({'__raw_lines__', 'path', '__emit__', 'class', 'algorithm', 'trickyPart'})

            input_items = [varible + ': ' + test_parsed[varible] for varible in input_varibles]

            test_info = '\n***     '.join(input_items)
            test_info = '\n***\n***     ==================\n***     Below is the test varibles (' +\
                            test_parser.parse()['path'] + '):\n*** \n***     ' +\
                            test_info + '\n*** \n*** \n***     ==================\n'

            solution_info = '\n***     solution: ' + solution_parser.parse()['solution']
            solution_info = '***     Below is the solution (' +\
                                solution_parser.parse()['path'] +\
                                '):\n***     ' + solution_info + '\n***\n***'
        print(message)

    else:

        import time
        print (time.strftime("Starting on %m-%d at %H:%M:%S\n", time.localtime()))

        counter_t_pass, counter_t_total = {}, {}
        for question in questions:
            counter_pass, counter_total = 0, 0
            print("Question %s\n===========\n" % question)
            files = os.listdir(os.path.join(options.testRoot, question))
            test_names = []
            for file_name in files:
                if os.path.splitext(file_name)[1] == '.test':
                    test_names.append(os.path.splitext(file_name)[0])
            for test_name in test_names:
                path = os.path.join(options.testRoot, question, test_name + '.test').replace('\\\\', '\\')

                # test = readFile(test_name + '.test', os.path.join(options.testRoot, question))
                test_parser = TestParser(os.path.join(options.testRoot, question, test_name + '.test'))
                
                # solution = readFile(test_name + '.solution', os.path.join(options.testRoot, question))
                solution_parser = TestParser(os.path.join(options.testRoot, question, test_name + '.solution'))
                
                passed, message = evaluate(test_parser.parse(), solution_parser.parse())
                
                if passed:
                    counter_pass += 1
                    message = '*** PASS: ' + path + '\n*** ' + message
                else:
                    message = '*** FAIL: ' + path + '\n*** ' + message
                
                if not passed and options.showFile:

                    test_file = '\n***     '.join(test_parser.parse()['__raw_lines__'])
                    test_file = '\n***\n***     ==================\n***     Below is the test file (' +\
                                 test_parser.parse()['path'] + '):\n*** \n***     ' +\
                                 test_file + '\n***     ==================\n'

                    solution_file = '\n***     '.join(solution_parser.parse()['__raw_lines__'])
                    solution_file = '***     Below is the solution file (' +\
                                     solution_parser.parse()['path'] +\
                                     '):\n*** \n***     ' + solution_file + '\n***'
                    
                    message += test_file + solution_file
                
                elif not passed and options.showInfo:

                    test_parsed = test_parser.parse()
                    input_varibles = set(test_parsed.keys()).difference({'__raw_lines__', 'path', '__emit__', 'class', 'algorithm', 'trickyPart'})

                    input_items = [varible + ': ' + test_parsed[varible] for varible in input_varibles]

                    test_info = '\n***     '.join(input_items)
                    test_info = '\n***\n***     ==================\n***     Below is the test varibles (' +\
                                 test_parser.parse()['path'] + '):\n*** \n***     ' +\
                                 test_info + '\n*** \n*** \n***     ==================\n'

                    solution_info = '\n***     solution: ' + solution_parser.parse()['solution']
                    solution_info = '***     Below is the solution (' +\
                                     solution_parser.parse()['path'] +\
                                     '):\n***     ' + solution_info + '\n***\n***'
                    
                    message += test_info + solution_info

                counter_total += 1
                if not options.muteResult or not passed:
                    print(message)
            
            print('\n### Question %s: %d/%d ###\n\n' % (question, counter_pass, counter_total))
            counter_t_pass[question] = counter_pass
            counter_t_total[question] = counter_total
        
        print(time.strftime("Finished at %m-%d at %H:%M:%S\n", time.localtime()))
        print("Provisional grades\n==================")
        for question in questions:
            print("Question %s: %d/%d" % (question, counter_t_pass[question], counter_t_total[question]))
        print("------------------")
        print("Total: %d/%d" % (sum(list(counter_t_pass.values())), sum(list(counter_t_total.values()))))
        print ("""
Your grades are NOT yet registered.  To register your grades, make sure
to follow your instructor's guidelines to receive credit on your homework.
By the way, this is NOT the same test cases as those online! (which means 
you may fail in Q7's test cases even if you get the full score)
""")
    