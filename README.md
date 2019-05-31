# Homework 7 autograder

This autograder is modified from CS188 in Berkeley.

## Update
- May 31 (18 pm): Release.

## To get start with

If you want to get help, run
```sh
    python autograder.py -h
```

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

If you want to show the input parameter of your failed cases in question 1, run
```sh
    python autograder.py -q q1 -s
```

Question i is exactly Task i (i = 1, 2, 3, 4, 5, 6, 7, 8).

**Windows 可以通过在上方文件夹路径栏输入'cmd'打开命令提示符窗口**

# Homework 7.1: Digital Image Processing
Author: [Qifan Zhang](mailto:zhangqf@shanghaitech.edu.cn)

## Get Started

To get started, please simply fork this GitLab repository and follow the structure and submissions guidelines below. 
**Remember to change your repo to a private one before you commit to it.**

Kind Reminder:

- The following tasks are arranged from easy to hard. Arrange your coding plan well.
- This homework takes 15% of the programming part, so take it seriously and start as early as possible
- We have offered **a big bonus (up to 8% of the programming part)**, which is called Homework 7.2. Of course, the higher the bonus is, the more you need to pay. Start early and be "wealthy".


## Repository Structure

### 10_Huffman_coding.pdf/ppt

This is the slide file for Huffman coding, which could be a reference for Task 8

### 04_imgproc.pdf

This is the slide file of [Lecture 4 of CS148](<http://graphics.stanford.edu/courses/cs148-10-summer/docs/04_imgproc.pdf>) in Stanford, which will help you understand the concept of convolution in Task 7.

### README.md/pdf

Problem description and requirements.

### DIP.py

A basic template for this homework. It also includes some simple testing codes.


## Submit

You should check in `DIP.py` to Gitlab.

First, make a commit and push your own `DIP.py`. From the root of this repo, run:

```shell
git add DIP.py
git commit -m"{Your commit message}"
git push origin master
```

Then add a tag to request grading on your current submission:

```shell
git tag {tagname} && git push origin {tagname}
```

Beware that all of your tag names should be distinguished among one homework repo. Therefore, remember to use **a new tag name** `{tagname}` in each submission.

Every submission will create a new Gitlab issue, where you can track the progress.

## Regulations

- Due: **23:59:59, June 1 (Saturday), 2019, CST**
- No late submission will be accepted.
- You could only import and use built-in modules.
- You have 30 chances of grading (i.e. `git tag`) in this homework (i.e. Homework 7.1. Homework 7.1 and 7.2 will separately be counted). You are able to require grading at most 10 times every 24 hours. If you hand in more 30 times, each extra submission will lead to 10% deduction.
- **Hard code is strictly forbidden.** Once found, your score of this homework will be set as 0.
- We enforce academic integrity strictly. If you participate in any from of cheating, you will fail this course immediately. You can view full edition on [Piazza](https://piazza.com/class/jrykv8wi15m5dx?cid=7).
- If you have any question about this homework, please ask on Piazza first.

## Overall Description

Alice and Bob are good friends. They have classes together, do homework together, study cryptology together and so on. Once, they shared their Gitlab accounts and then both got punished, which made them very angry, especially at a TA called Mr. Sailboat.

In order to relax themselves and forget that awkward incident, during Labor Day holiday, they went out for sightseeing and got some raw pictures (i.e. without being processed by image processing algorithms). However, raw images are always far from satisfaction. Mr. Sailboat now invites you to help them finish this job by performing some 'magic' on some images.

All images provided by Mr. Sailboat are gray scale images.

## Task 1.1: Load in an Image

In order to process an image, you first need to load it in.

The basic element for an image is `pixel`, which is stored by a non-negative integer. In computer, an integer is stored by several `bits`. When we call an image "`an n-bit image`", `n` tells us how many bits will be used to store one pixel. In the other word, given $n$, a valid pixel value will be an integer in the range of $[0,2^n-1]$. Of course, $n$ should be a positive integer or it will be meaningless.

Mr. Sailboat will now give you an $n$-bit image in the form of a matrix expression. The expression is defined using [EBNF]([https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form](https://en.wikipedia.org/wiki/Extended_Backus–Naur_form)) form below. 

```ebnf
Matrix = "[", {blank}, Rows, {blank}, "]" | "[", {blank}, "]";
Rows = {blank}, Row, {blank} | {blank}, Row ,{blank}, ";", {blank}, Rows, {blank};
Row = {blank}, pixel, {blank} | {blank}, pixel, {blank}, ",", {blank}, Row, {blank};
pixel = int | float | complex;
blank = " " | "\n" | "\r" | "\t";
```

However, Mr. Sailboat is such a careless guy. As you have observed above, Mr Sailboat may give an invalid image matrix. If you meet an mistake, you need raise an exception. All possible exceptions are listed below:

### PixelSyntaxError

As stated above, a valid syntax should be an integer in the range of $[0,2^n-1]$ ($n$ is 8 by default if it is not given).

Once you found this property is not held in the given image matrix, you should raise `PixelSyntaxError`.

### MatrixSizeError

Each row of the given matrix must have the same number of columns. In the other word, the number of elements in each row of the matrix should be the same.

Once you found this property is not held in the given image matrix, you should raise `MatrixSizeError`.

### PixelBitError

As stated above, $n$ should be a positive integer or it will be meaningless.

Once you found this property is not held in the given $n$, you should raise `PixelBitError`.



All the given matrices will have **at most one** of the above 3 exceptions. 

**Note**: You should first judge whether $n$ is valid before handling other exceptions. Once $n$ is invalid, you should directly raise `PixelBitError` and do not care about other possible exceptions.



Once you finish your implementation, test it in console by:

```python
>>> imageInput = '[1,2,3,4;5,6,7,8;9,10,11,12]'
>>> n = 8
>>> img = Image(ImageInput, n)
>>> # or
>>> img = Image(ImageInput) # n is not given, then see the image as 8-bit image by default
```

## Task 1.2: Print out the Image

In this task, you should implement your class `Image()` in order to make it possible to print the image matrix out via function `print()`.

The printing format is quite similar with the input one. The only difference is that there should be no redundant characters in your output. The output is defined using [EBNF]([https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form](https://en.wikipedia.org/wiki/Extended_Backus–Naur_form)) form below. 

```enbf
Matrix = "[" Rows "]" | "[" "]" ;
Rows = Row | Row ";" Rows ;
Row = pixel | pixel "," Row ;
pixel = int | float | complex;
```



Once you finish your implementation, test it in console by:

```python
>>> x = Image("[1,2,3; 4,5,6; 7,8,9]")
>>> print(x)
[1,2,3;4,5,6;7,8,9]
```

## Task 2: Image Addition and Equalization

Sometimes, you may need to synthesize two (or even more) images together in order to get a better one. Also, you need to know whether it is the 2 images are the same.

In this task you need to realize this feature.



For addition, there are 2 images which has the same number of rows and columns. You need add values of 2 pixels with the same coordinates in 2 images.You may meet the following 3 errors:

### PixelSyntaxError

When adding two images together, there may be one or a few pixels exceeding the storage range of the given bits. When you meet this error, you should raise `PixelSyntaxError`.

### BitUnmatchedError

Two images should have the same $n$. If they are not the same, you should raise `BitUnmatchedError`.

### ImageSizeUnmatchedError

Two images that is added together should has the same number of rows and columns. Otherwise



All the given test cases will have **at most one** of the above 3 exceptions.



For equalization, you should return `True` while the images are the same. If not, return `False`.

Notice that if $n$s of two images are not the same, they are definitely **not** the same.



Once you finish your implementation, test it in console by:

```python
>>> a = '[1,2,3,4;5,6,7,8;9,10,11,12]'
>>> b = '[5,6,4,7;1,2,3,4;10,10,10,10]'
>>> img1 = Image(a)
>>> img2 = Image(b)
>>> img3 = img1 + img2
>>> img3 == Image('[6,8,7,11;6,8,10,12;19,20,21,22]')
True
>>> img3 == Image('[0,0,0,0]')
False
```

## Task 3: Gray Scale Reversion

In this task, you will need to reverse their color into its opposite one in gray scale. To be more explicit, for each pixel $p_{i,j}$, it should be transferred into $p^{'}_{i,j}$ with the relationship:

$$p^{'}_{i,j}=2^n-1-p_{i,j}$$

The task should be implemented as a method of `Image` named `reverse()`.

There will be no possible exception.



Once you finish your implementation, test it in console by:

```python
>>> a = Image('[1,2,3,4;5,6,7,8]')
>>> b = a.reverse()
>>> b == Image('[254,253,252,251;250,249,248,247]')
True
```

## Task 4: Bit Extension and Compression

Storage space is also a big issue for an image. Sometimes we need to allocate more bits (i.e. extension) for each pixel in order to store an image with higher quality while sometimes we need to shrink the current bits (i.e. compression) into fewer bits. In this task, you should implement it in method `bitChange()`.

To be more explicit, for each pixel $p_{i,j}$, it should be transferred into $p^{'}_{i,j}$ with the relationship:

$$p^{'}_{i,j}=\left\lfloor p_{i,j}\times\cfrac{n'}{n_0} \right\rfloor$$

$n'$ is the new given $n$ while $n_0$ is the initial $n$. If $n'$ is not given, set it as 8 by default.

Just like Task 1,  you may meet `PixelBitError`. The property of the new given $n$ is the same as what has been stated in Task 1. Once you found this property is not held in the given $n$, you should raise `PixelBitError`. 



Once you finish your implementation, test it in console by:

```python
>>> a = Image('[4,8,12,16;20,24,28,32]', 16)
>>> a1 = a.bitChange()
>>> b = Image('[1,2,3,4;5,6,7,8]', 4)
>>> b1 = b.bitChange(8)
>>> a1 == b1
True
>>> b2 = b.bitChange(7)
>>> a1 == b2
False
```

## Task 5: Image Indexing

During processing, you may want to get part of the image or a particular pixel. Also, you may want to replace a particular pixel or part of the image with a new one. In this task, you need to finish this task in order to index the image just like using a list.

The following are tasks you need to do (`x` is a given `Image()` class):

- `x[i]` returns the `i`-th row (starting at `0`) which also is a matrix
  - If `i` is invalid, raise `IndexSyntaxError`
- `x[i,j]` returns the element at the `i`-th row and `j`-th column
  - If `i` or `j`  or both are invalid, raise `IndexSyntaxError`.
- `x[i,j] = k` replaces the element `x[i,j]` by `k` in `x`
  - If `i` or `j`  or both are invalid, raise `IndexSyntaxError`.
  - If `k` is invalid, raise `PixelSyntaxError`.
- `x[i] = Image(..)` replaces the row `x[i]` by the row `Image(..)` in `x` if the lengths of the row `x[i]` and the row `Image(..)` are identical, otherwise raise the exception `IndexSyntaxError`
  - If `i` is invalid, raise `IndexSyntaxError`
  - If the `Image()` which replaces the original one does not have the same `n` with the original one, raise `BitUnmatchedError`.
- `x[start1:stop1:step1,start2:stop2:step2]` returns the image `y`, such that `y[i,j]` is the element `x[start1+i*step1,start2+j*step2]` if it exists and `start1+i*step1<stop1`, `start2+i*step2<stop2`
  - If `start1:stop1:step1,start2:stop2:step2` is invalid, raise `IndexSyntaxError`
- `x[start1:stop1:step1,start2:stop2:step2] = Image(..)` replaces the matrix `x[start1+i*step1,start2+j*step2]` by `Image(..)` in `x` if the number of rows (as well as columns) of `x[start1+i*step1,start2+j*step2]` are `Image(..)` are identical, otherwise raise the exception `ImagexSyntaxError` 
  - If `start1:stop1:step1,start2:stop2:step2` is invalid, raise `IndexSyntaxError`
  - If the `Image()` which replaces the original one does not have the same `n` with the original one, raise `BitUnmatchedError`.



Once you finish your implementation, test it in console by:

```python
>>> x = Image("[1,2,3; 4,5,6; 7,8,9]")
>>> y = Image("[0,1,2; 3,4,5; 6,7,8]")
>>> z = x[2]
>>> print(z)
[7,8,9]

>>> x[2,1]
8

>>> z = x[1:3:1,0:3:2]
>>> print(z)
[4,6;7,9]

>>> x[2] = Image("[17,18,19]")
>>> print(x)
[1,2,3;4,5,6;17,18,19]

>>> x[1,2] = 0
>>> print(x)
[1,2,3;4,5,0;17,18,19]

>>> x[1:3:1,0:3:2] = Image("[14,16;7,9]")
>>> print(x)
[1,2,3;14,5,16;7,18,9]
```

## Task 6.1: Histogram

First, if you do not know a histogram, you could go to [Histogram](<https://en.wikipedia.org/wiki/Histogram>) for details.

In this task, you need to calculate the distribution of pixel values of the given image. To replace an image version of histogram, you need to store your result in a list $l$, where $l[value]=num$. $value$ is an integer in the range of $[0,2^n-1]$ which represents value of pixel, $num$ should be the times of the related pixel value appearing in the given image matrix.

This task is implemented in the method `his()`.

There should be no exception in task.



Once you finish implementation, test it in console by:

```python
>>> x = Image("[1,2,3; 4,5,6; 7,8,9]", 4)
>>> h = x.his()
>>> h == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
True
```

## Task 6.2: Histogram Equalization

Histogram equalization usually increases the global [contrast](https://en.wikipedia.org/wiki/Contrast_(vision)) of many images, especially when the usable data of the image is represented by close contrast values. Through this adjustment, the [intensities](https://en.wikipedia.org/wiki/Luminous_intensity) can be better distributed on the histogram. This allows for areas of lower local contrast to gain a higher contrast. Histogram equalization accomplishes this by effectively spreading out the most frequent intensity values.

For more information, you could go to [Wikipedia](<https://en.wikipedia.org/wiki/Histogram_equalization>).

In this task, you need to implement a method `hiseq()` to do histogram equalization on an image `i`.

### Algorithm

Here is the algorithm for this task:

1. Calculate `i_his = i_1.his()`

2. Calculate probability of occurrence for each valid value.  $p_r(r_k)$ using `i_his`, while $p_r(r_k)$ is:

   $p_r(r_k)=\cfrac{i\_his[r_k]}{MN}$

   where $r_k\in[0,2^n-1]$, $MN$ is the total number of all the pixels.

   Notice that here you should keep 4 decimals for each $p_r(r_k)$. If there are more than 4 decimals, you should round it using function `round(x,4)` ($x=p_r(r_k)$).

3. Calculate *Cumulative Probability Density* function (a.k.a. CDF) for each $r_k$. You can get CDF by the formula:

   $$CDF(r_k)=\sum_{i=0}^{r_k}p_r(r_k)$$

   where $r_k\in[0,2^n-1]$

4. Get the new value of the pixel. After calculating CDF out, each value was transformed from initial value $v$ into new value $v'$ with transformation:

   $$v'=\left\lfloor CDF(v) \times (2^n-1) \right\rfloor$$



Once you finish implementation, test it in console by:

```python
>>> x = Image("[1,1,3; 4,4,5; 7,7,7]", 4)
>>> x_hiseq = x.hiseq()
>>> print(x_hiseq)
[3,3,4;8,8,9;14,14,14]
```



# Homework 7.2 (Bonus): Advanced Digital Image Processing

## Get Started

To get started, please simply fork this GitLab repository and follow the structure and submissions guidelines below. 
**Remember to change your repo to a private one before you commit to it.**

Kind Reminder: Please do not try to do this homework without Homework 7.2 is accepted. Tough there are only 2 tasks, they are much more difficult than Task 1-6 since you need to spend some time learning some basic linear algebra (Task 7) and some data structure (Task 8) first.

## Repository Structure

### 10_Huffman_coding.pdf/ppt

This is the slide file for Huffman coding, which could be a reference for Task 8

### 04_imgproc.pdf

This is the slide file of [Lecture 4 of CS148](<http://graphics.stanford.edu/courses/cs148-10-summer/docs/04_imgproc.pdf>) in Stanford, which will help you understand the concept of convolution in Task 7.

### README.md

Problem description and requirements.

### DIP.py

A basic template for this homework. It also includes some simple testing codes.

## Submit

You should check in `DIP.py` to Gitlab.

First, make a commit and push your own `DIP.py`. From the root of this repo, run:

```shell
git add DIP.py
git commit -m"{Your commit message}"
git push origin master
```

Then add a tag to request grading on your current submission:

```shell
git tag {tagname} && git push origin {tagname}
```

Beware that all of your tag names should be distinguished among one homework repo. Therefore, remember to use **a new tag name** `{tagname}` in each submission.

Every submission will create a new Gitlab issue, where you can track the progress.

## Regulations

- Due: **23:59:59, June 3 (Monday), 2019, CST**
- No late submission will be accepted.
- You could only import and use built-in modules.
- You have 30 chances of grading (i.e. `git tag`) in this homework. You are able to require grading at most 10 times every 24 hours. If you hand in more 30 times, each extra submission will lead to 10% deduction.
- **Hard code is strictly forbidden.** Once found, your score of this homework will be set as 0.
- We enforce academic integrity strictly. If you participate in any from of cheating, you will fail this course immediately. You can view full edition on [Piazza](https://piazza.com/class/jrykv8wi15m5dx?cid=7).
- If you have any question about this homework, please ask on Piazza first.

## Overall Description

Alice and Bob are good friends. They have classes together, do homework together, study cryptology together and so on. Once, they shared their Gitlab accounts and then both got punished, which made them very angry, especially at a TA called Mr. Sailboat.

In order to relax themselves and forget that awkward incident, during Labor Day holiday, they went out for sightseeing and got some raw pictures (i.e. without being processed by image processing algorithms). However, raw images are always far from satisfaction. Mr. Sailboat now invites you to help them finish this job by performing some 'magic' on some images.

All images provided by Mr. Sailboat are gray scale images.

## Task 7: Convolution Between Image and Kernel

Convolution is a very important operation in Signal Processing domain. For digital image processing, it is often used in spatial filtering, which will optimize the image in a fast and easy way but still get good results. In Task 7 you need to implement an operation `*`, i.e. method `__mul__()` to utilize this operation.

### Kernel

Suppose we do convolution on Matrix $A$ with Matrix $B$, denoted as `A*B`, then `B` is called a `kenerel`. A kernel $B$ is a matrix which holds following properties:

1. It is a squared matrix, i.e. $B$ is an $n\times n$ matrix
2. $n$ is an odd number
3. To make it simple, all valid elements in $B$ should be integers

Of course, when one of the properties is not held, an exception should be raised. There are 3 possible exceptions:

#### MatrixSizeError

If property 1 or/and 2 is not held, raise this error

#### KenelElementError

If property 3 is not held, raise this error.

#### PixelNegError

If any pixel has a negative value after convolution, then raise this error.

##### Notes:

Notice that $A[i-m,j-n]$ does not always exist, so you have 2 options:

- Zero-padding
  - Extend A into a larger size with 0
- Do a check whether $A[i-m,j-n]$ exists for each $m$ and $n$

### How to Calculate

For detailed introduction to 2D convolution, you could see [CS148 Lecture 4 Slides](<http://graphics.stanford.edu/courses/cs148-10-summer/docs/04_imgproc.pdf>), which has been included in this repo as `04_imgproc.pdf`. It will also be covered in discussion of Week 14.

### Input and Output

You need to implement `Image.__mul__(self, kernel)` method

To simplify your task, the `kernel` $B$ is given in the form of a matrix in string same as the form in Task 1.1. The expression is defined using [EBNF]([https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form](https://en.wikipedia.org/wiki/Extended_Backus–Naur_form)) form below. 

```ebnf
Matrix = "[", {blank}, Rows, {blank}, "]" | "[", {blank}, "]";
Rows = {blank}, Row, {blank} | {blank}, Row ,{blank}, ";", {blank}, Rows, {blank};
Row = {blank}, pixel, {blank} | {blank}, pixel, {blank}, ",", {blank}, Row, {blank};
pixel = int | float | complex;
blank = " " | "\n" | "\r" | "\t";
```

You should return an `Image` class which has been convolved with the kernel.



## Task 8: Advanced Image Compression - Huffman Coding

In Task 4, we have implemented a naive image compression method using bit changing. However, it will damage quality of the image too much. In this task, you will implement another compression algorithm, which compresses the image a lot but without loss of image quality. The algorithm is `Huffman Coding`.

For Huffman Coding, you could see the slides `10_Huffman_coding.pdf/ppt` attached in this repository (also available on Piazza. Link: [here](<https://piazza-resources.s3.amazonaws.com/jrykv8wi15m5dx/jvduezzkopo1zv/10_Huffman_coding.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAR6AWVCBXU6C3NHTQ%2F20190519%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20190519T152200Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Security-Token=AgoJb3JpZ2luX2VjEFMaCXVzLWVhc3QtMSJHMEUCIQD9yV%2B5npXmY2iBL%2BT1ulgV44F53WKxNgXZKTterU%2FBmQIgMj9DP30ie8X3YuvfR11nDO5jhKvrAkFnB76OYnDV%2F7sq2gMIXBAAGgwxMzMxOTE1MDM5ODMiDIUGUmFNGUbuxxuF1Sq3A2RNOmE252AxKXz9YDgTwor%2BzgBQ1zEJaT0GE0YAgtdaCzJLkBhoxcCnMaKjZMjquRkzXL4AT2gFsVhAzT8ZwFak1izFqP2MIdXfGuNdYlpEb4KC21JOUjV57hhr5mrx1R2BSZGTbWmphiQ7%2Fs27Ew1ALHxl7eXAf723obljgAORnEl9rnf76bqIUHs9dIJp6llsj6NX8jv1pnKyLfrIZ3TyebOKJKghzlwlZrpmULAfaxoL161bDZzaq5gWpztUWUfIbYP9LoUPaC9zFaIe7P6QmNtH%2FFrtP2Kax3KFbOumpeyvms4xc6I7xEq1gqCAkErxBxEq%2FMa2Mq9DF%2FyUNjulFxJBhQw0i7CleXRt1kwWSZCU%2BbZgySF3NvCX1IUsYit9VF8Bk9ZH%2BkmQP3lQoUZ%2BphxTiiroNq8lCAS2eaJESoMF1AEvooBfp4nRSS6XAw7rtZyTi%2FWpxxjcDjjdOH2JDMr0cyFORyJRZzIRsakHxE9%2FUnn5YrD%2Brk4Ev6s0uHDeaUC6wBGEmN5S9xkEXxYo0iJIAqeojy1b2hlGuYT86stdnKXjOj%2BoMuIBT5KGiqwCLHJ1mQ0wmu2E5wU6tAEbpc%2FIjy98Nz3P0d4aGI8HZRmt4Vd%2B7sfS%2BnaQGOEdmlNUb6HAhv%2B5LTzNX%2BfkPRb2V4pVl8bEglZZTI8NUtj6IIiCvXc813x5DrQEI2bpa6lNnjvWbgSCPW2NfN%2BJYWtiz83robTx%2Brp6CczGrSdvfkkuaPGMW0iHVbkmw%2BsVgiggm4I9rB0vAjhXVARvhsNhdn7GeRKblZDM7eAZAqiUNTmFXD%2FNfo%2Fmx2D7Ep8ruFWZZns%3D&X-Amz-Signature=bbbf45ef19905ca75c811e6fff5ef2a0b5f30a5e536d894a5dd61ac7d4d932a5>)) to have a detailed view. This will also be covered in the discussion on Week 14.

In this task, you need to generate Huffman Codes for pixel values and finally encode them with Huffman Codes you have gotten.

### Specification

Priority will not be the main topic in this task. So Mr. Sailboat will carefully construct test cases in order to avoid same priority when sorting in priority queue. Therefore, feel free to use built-in sorting function such as `sort()` when dealing with sorting issue.

#### Input and Output

You need to implement `Image.huffman()`

There is no input.

You should return a string `s` which stores Huffman-coded pixels row by row and column by column. Suppose $A$ is an $m\times n $ matrix. If written in formula, it is:

$\tt s=\ ''$

$\tt s = \sum_{i=1}^{m}\sum_{j=1}^{n}huffman\_code(str(A[i,j]))$

(P.S. the `+` for `s` is the same with the `+` for type `str` in Python)

Example:

```python
>>> img1 = Image('[1,2,2,3,5,3;3,3,4,4,5,3;4,4,5,5,5,3]')
>>> print(img1.huffman())
000001001111011111101011011010110101011
```



