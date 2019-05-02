# Homework 5 autograder

This autograder is modified from CS188 in Berkeley.

If you want to test your code, run
```sh
    python autograder.py
```

If you want to test your code for specified question, for example, question 1, run
```sh
    python autograder.py -q q1
```

If you want to mute passed cases, run
```sh
    python autograder.py -m
```

If you want to test your code for specified testcase, for example, q1/test_1.test, run
```sh
    python autograder.py -t test_cases/q1/test_1.test
```

Question i is exactly Task i (i = 1, 2, 3, 4).

第二题可能只需要处理Fraction(int, int, sign)的情况，所以如果第一题不会做也不要气馁，可以先做第二题！

对第4题，推荐[领扣-逆波兰表达式](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/)上面有可用的大量优质testcase和知识点解析。

# SI 100B Homework 5: pyFraction

* Author: [Diao Zihao](mailto:diaozh@shanghaitech.edu.cn)
* Last modified: Apr. 12, 2019
* Deadline: 23:59:59, May 2nd, 2019 China Standard Time (UTC+8:00)

## Introduction

A common way to represent a real number in Python and many other programming language is using float point number. It is straightforward, even for Python beginners, to represent the fraction $`\frac{1}{2}`$ using $`0.5`$. Those two representation are equivalent in the sence of mathematic. Float point arithmetic stores number in a way similar to the scientific notation. For example, the number $`1.234`$ is represented in a way like $`1234 \times 10^{-3}`$ (the $`-3`$ is called base, it controls the postion of the *point* in the number, actually, this is how the point in *float point* comes from. the detail of how float point number is actually stored is way more complicated, refer to [Wikipedia](https://en.wikipedia.org/wiki/Floating-point_arithmetic) for more information if you are interested in this topic). You could not represent some real numbers persiscely using float point. For instance, $`1/3`$ and $`\pi`$ will be the case. They could barely not be represented percisely as a float point number. Another example is when you are trying to get the value of `0.1 + 0.2` using some programming language (include python3 :-)), you will get `0.30000000000000004`, a quite counterintuitive answer (visit [this website](https://0.30000000000000004.com/) for more details). In fact, floating point arithmetic is one of the famous examples in Computer Science about the tradeoff between range and precision.

Those problems shall not happen in some scenario where the presicion is considered very important. For rational number, a subset of real number, a way to achieve higher precision is to represent them as fraction. Python has [its own `fraction` module](https://docs.python.org/3.1/library/fractions.html#fractions.Fraction) which gives support for rational number arithmetic. **But in this homework you are required to implement your own version of this module called `pyFraction` and try to solve simple equations using your fraction modules.**

Hope this homework will help you practice your knowledge about class, exception and error handling. Good luck and let's get started!

## Getting Started

To get started, please simply fork this GitLab repository and follow the structure and submissions guidelines below.
Remember to **make your repository private** before any commits.

*Note*: Markdown text with file extension ***.md*** could be displayed properly using plug-ins in your browsers, IDEs or specialized markdown editors (like [typora](<https://typora.io/>)).

## Repository Structure

### README.md

Homework description and requirements.

### pyfraction.py

A basic template for this homework, contains all the code you needs to fill in.

### test.py

Some facilities and simple testcases for tesing the correctness of your program.

## Submission

**You should check in pyfraction.py to GitLab.**

First, make a commit and push your files. From the root folder of this repo, run

```sh
git add pyfraction.py
git commit -m '{your commit message}'
git push
```

Then add a tag to create a submission.

```sh
git tag {tagname} && git push origin {tagname}
```

You need to define your own submission tag by changing `{tagname}`, e.g.

```sh
git tag first_trial && git push origin first_trial
```

**Please use a new tag for every new submission.**

Every submission will create a new GitLab issue, where you can track the progress.

## Regulations

- You may **not** use third-party libraries or the built-in Python Standard Library [fraction](<https://docs.python.org/3.1/library/fractions.html>).
- No late submissions will be accepted.
- You have 30 chances of grading (i.e. `git tag`) in this homework. If you hand in more 30 times, each extra submission will lead to 10% deduction. In addition, you are able to require grading at most 10 times every 24 hours.
- We enforce academic integrity strictly. If you participate in any form of cheating, you will fail this course immediately. **DO NOT** try to hack GitLab in any way. You can view the full version of the code of conduct on [Piazza](https://piazza.com/class/jrykv8wi15m5dx?cid=7).
- If you have any questions about this homework, please ask it on Piazza first so that everyone else could benefit from your question and the answer.

## Specification

### Task 1: Build your Fraction class

In this task, you need to finish four methods of the `Fraction` class provided to you in `pyfraction.py`.

1. `__init__(self, numerator, denominator, sign='+')`: the initializer of `Fraction`. In this method you should initizalize your `Fraction` instance according to the three parameters given. `numerator`/`denominator` gives you the numerator and denominator of this fraction, respectively. ` numerator`/`denominator` could be any integer or another `Fraction` instance (That means `Fraction` should support nested expressions. You may find the built-in function [`isinstance`](<https://docs.python.org/3/library/functions.html#isinstance>) helpful). `sign` is a single character indicating an extra sign bit of your fraction. The value could be `+` or `-`. If the numerator is 0, the sign should be ignored. You could choose your own way of storing those information inside your implementation as far as your `Fraction` satisfy the following two rules:

   * Your internal storage shall not be accessed directly outside the class (think about why!);

   * Your fraction initizalized shall be normalized as defined in Appendix A.

   **Error handling**: To improve the robustness of your implementation, you may deal with illegal inputs (an example of illegal inputs is the user give you a float `0.333` as the denominator) correctly by raising the exceptions to inform your user that their input is illegal. Some exceptions has been provided for you in `pyfraction.py` but feel free to define your own exception classes as far as your exceptions are inherited from the given `BaseFractionError`.

2. `get_denominator(self)`, `get_numerator(self)` and `is_nonnegative(self)`: since you are designing your own internal sturcture for your `Fraction` class, there is no simple way for others (e.g. the auto-grader) to know where you stored them and then access them. The solution is to provide a public read-only (it is read-only beacuse nobody wants his/her data being modified by an outsider! ) interface for getting the value of denominator, numerator and sign.

   In `get_denominator(self)`, return the denominator of your normalized  `Fraction` instance as an integer. In `get_numerator(self)`, return the numerator of your normalized `Fraction` instance as an integer. In `is_nonnegative(self)`, return `True` if this this fraction is non-negative (i.e. if $`\text{fraction instance} = |\text{fraction instance}|`$) and return `False` otherwise.

Now you can test your implementation using the following code snippet.

```python
>>> from pyfraction import Fraction
>>> my_fraction = Fraction(1,2)
>>> print(my_fraction)
```

If your implementation is correct, you may see the following in your console.

```latex
\frac{1}{2}
```

### Task 2: Arithmetic operations for `Fraction`

See also: [the Python documentation on data models](<https://docs.python.org/3/reference/datamodel.html#special-method-names>)

A fraction without arithmetic operations could not be a real fraction. In this task, you are required to implement serval so called *magic methods* to give your `Fraction` instances abilities to be compared through operators like `>`, `<` and `==` or do arithmetic operations through the `+`, `-`, `*` and `\` operators and built-in functions like `abs()`.

The methods that you are required to implement is pre-defined in the framework. See the comments in each methods for the implementation details. You may find the official guide (see the link above) helpful. Feel free to define extra ones to make your `Fraction` acts more like a built-in Python datatype but we will not have testcase on them.

All the parameters passed to your method should be `Fraction` instance. If an input violates this rule, raise a proper exception inherited from `BaseFractionError` to inform the user.

### Task 3: More Fraction conversions

You need to finish three mothods in this task for convertion between different  representation of rational numbers.

1.  `to_float(self)`: returns the closest approximate floating point representation in Python of this `Fraction` instance.
2. `from_integer(integer)`: construct a `Fraction` instance from the given integer. In this method, you needs to check the validity of the instance. If the user gives you an invalid input, raise an exception inherited from `BaseFractionError`.
3. `from_string(string)`: construct a `Fraction` instance from a string. The syntax of representaion is similar to the fraction representaion (see below for formal defination of the syntax) in a $`\LaTeX`$ typesetted documentaion (the format is also used in the `__str__(self)` method of the framework which you may have seen when you `print` a `Fraction` instance). For simplicity, unlike in `__init__()`,  you are not required to deal with nested expression (that means all fields in the expression should be integer). Instead, raise an exception inherited from `BaseFractionError` if the expression in the string is invalid or requires you to evaluate it as a nested expression.

To get rid of ambiguity, the string expression the fraction is defined using [EBNF](https://en.wikipedia.org/wiki/EBNF) (Extended Backus–Naur form) as below.

```ebnf
expression   = {blank}, fraction, {blank};
fraction     = [sign], {blank},"\frac{", int, "}{", int, "}" ;
int          = {blank}, [sign], digit-excluding-zero, {digit}, {blank} | {blank}, "0", {blank};
digit        = "0" | digit-excluding-zero ;
digit-exlucding-zero = "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;
sign         = "+" | "-" ;
blank        = " " | "\n" | "\t" | "\r";
```

### Task 4: Calculator!

In this task we are getting down to evaluate an expression with your `Fraction` class.

You are requried to create a simple postfix calculator in the function `evaluate_postfix_expr(expr)`.

Your postfix calculator will read in postfix expressions. You may be familiar with infix notation, where the operators are placed inside operands (e.g. `(1 + 2) * 3`). Postfix notation places the operator after the operands (e.g. `1 2 + 3 *`). With postfix notations, you do not need to deal with priorities and also parentheses. You may find the simple data structure [stack](<https://en.wikipedia.org/wiki/Stack_(abstract_data_type)>) helpful in your implementaion.

Your caculator shall support operators `+` (add), `-` (subtract), `*` (multiply) and `\`  (division).

#### Input & Output

* Your function takes in a string `expr` as the input. The input string contains a series of operators and operands separated by white spaces. There will be no testcase that the expression consists of characters other than we mentioned below.
* The operators includes `+` (add), `-` (subtract), `*` (multiply) and `\`  (division) ;
* The operands are integers represented in the string form;
* Whitespace is defined as consists of a sequence of the following: `‘’ `(space), `‘\t’`(tab), `‘\n’` (newline) and `‘\r’` (carraige return);
* Your function should return a valid `Fraction` instance as output. In case  of error, return `None` to indicate the expression is invalid instead of crash.

Once you finish your implementation, test it in console by

```python
>>> from pyfraction import evaluate_postfix_expr
>>> expr = "1 2 * 3 +"
>>> print(evaluate_postfix_expr(expr))
```

You will see

```latex
\frac{5}{1}
```

if your implementation is correct.

## Testing and Grading

`test.py` provided in the repository gives you some simple testcases for you to examine the correctness of your code. Those tests are pretty simple and naïve. Passing them does not guarantee that you will pass testcases in the auto-grader on your submission. **So read carefully about the specification and create your own reasonable testcase, do not use GitLab and the auto-grader as your debugging tool**.

The auto-grader will test your code by importing your module and test it in a similar manner to `test.py` once you tagged a commit on GitLab.

There will be 10 testcases in the auto-grader. Each of them is composed with multiple operations. Only results of the testcases in the auto-grader will be considered valid and will count for your final score.

To help your find out which part of your code may be wrong in hope to reduce the time consumption of you on this homework, each testcase will have a label indicating which task the testcase is foucusing on. The label will be in the form of  `m-n`. For example, the label `2-1` means this testcase is the 1st testcase aiming to test your implementation in task 2. But since the testcaes are compositional and latter tasks may depends on your implementation of former tasks, **you may also needs to check your code in tasks other than the one the grading label gives if your module failed any of the testcaes**.

Good luck!

## Appendix A: Normalized `Fraction`

A `Fraction` instance is normalized if and only if it follows the following constraints through equivalent mathematical transformation.

* Its denominator and numerator are positive integer;
* The greatest common divider (<abbr>g.c.d</abbr>) of the denominator & numerator is $`1`$;
* The representation of number $`0`$ is in the form of $`+\frac{0}{1}`$.

## Feedbacks

* If you believe you find any mistake in this homework, please contact with me ([Diao Zihao](mailto:diao.zihao@icloud.com)) directly. Any mistake and typo will be corrected ASAP. 
* Comments on this homework is always welcomed so that we could do better. You are also welcome to send us feedback anonymously if you like.