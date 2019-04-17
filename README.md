# Homework 4 autograder

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
    python autograder.py -t test_cases/q1/test_1
```
**Functions in question 1-13 are in `utils.py`, others are in `aes.py`**

## Question 1
Finish function `stateOf()`:
```sh
def stateOf(code):
    """
    Return the state of the code.

    :type code: int
    :rtype: list[int]
    """
```
Example input:
```sh
code = 0x3243f6a8885a308d313198a2e0370734
```
Example output:
```sh
[0x32, 0x43, 0xf6, 0xa8,
 0x88, 0x5a, 0x30, 0x8d,
 0x31, 0x31, 0x98, 0xa2,
 0xe0, 0x37, 0x07, 0x34]
```

## Question 2
Finish function `codeOf()`:
```sh
def codeOf(state):
    """
    Return the code of the state.

    :type state: list[int]
    :rtype: int
    """
```
Example input:
```sh
state = 
[0x32, 0x43, 0xf6, 0xa8,
 0x88, 0x5a, 0x30, 0x8d,
 0x31, 0x31, 0x98, 0xa2,
 0xe0, 0x37, 0x07, 0x34]
```
Example output:
```sh
0x3243f6a8885a308d313198a2e0370734
```

## Question 3
Finish function `RotWord()`:
```sh
def RotWord(word):
    """
    Function used in the Key Expansion routine that takes
    a four-byte word and performs a cyclic permutation.

    :type word: list[int]
    :rtype: list[int]
    """
```
Example input:
```sh
word = [0x86, 0x32, 0x18, 0x45]
```
Example output:
```sh
[0x32, 0x18, 0x45, 0x86]
```

## Question 4
Finish function `SubWord()`:
```sh
def SubWord(word):
    """
    Function used in the Key Expansion routine that takes 
    a four-byte input word and applies an S-box to each of 
    the four bytes to produce an output word.

    :type word: list[int]
    :rtype: list[int]
    """
```
Example input:
```sh
word = [0x86, 0x32, 0x18, 0x45]
```
Example output:
```sh
[0x44, 0x23, 0xad, 0x6e]
```

## Question 5
Finish function `XOR()`:
```sh
def XOR(item1, item2):
    """
    Return the XOR result list. For the ith item in the 
    result, it should be equal to item1[i] XOR item2[i].

    :type item1: list[int]
    :type item2: list[int]
    :rtype: list[int]
    """
```
Example input:
```sh
item1 = [138, 132, 235, 1]
item2 = [1, 0, 0, 0]
```
Example output:
```sh
[139, 132, 235, 1]
```
## Question 6
Finish function `keyExpansion()`:
```sh
def keyExpansion(key, Nk):
    """
    Routine used to generate a series of Round Keys from 
    the Cipher Key.

    :type key: int
    :type Nk: int
    :rtype: list[list[int]]
    """
```
Pseudocode:
```sh
begin
    word temp
    i = 0
    while (i < Nk)
        w[i] = word(key[4*i], key[4*i+1], key[4*i+2], key[4*i+3])
        i = i+1
    end while
    i = Nk
    while (i < Nb * (Nr+1)]
        temp = w[i-1]
        if (i mod Nk = 0)
            temp = SubWord(RotWord(temp)) xor Rcon[i/Nk]
        else if (Nk > 6 and i mod Nk = 4)
            temp = SubWord(temp)
        end if
        w[i] = w[i-Nk] xor temp
        i = i + 1
    end while
end
```
Note that Nk=4, 6, and 8 do not all have to be implemented;
they are all included in the conditional statement above for
conciseness. Specific implementation requirements for the
Cipher Key are presented in Sec. 6.1.

Example input:
```sh
key = 0x2b7e151628aed2a6abf7158809cf4f3c
Nk = 4
```
Example output:
```sh
[[43, 126, 21, 22],
 [40, 174, 210, 166],
 [171, 247, 21, 136],
 [9, 207, 79, 60], 
 [160, 250, 254, 23], 
 [136, 84, 44, 177], 
 [35, 163, 57, 57], 
 [42, 108, 118, 5], 
 [242, 194, 149, 242], 
 [122, 150, 185, 67], 
 [89, 53, 128, 122], 
 [115, 89, 246, 127], 
 [61, 128, 71, 125], 
 [71, 22, 254, 62], 
 [30, 35, 126, 68], 
 [109, 122, 136, 59], 
 [239, 68, 165, 65], 
 [168, 82, 91, 127], 
 [182, 113, 37, 59], 
 [219, 11, 173, 0], 
 [212, 209, 198, 248], 
 [124, 131, 157, 135], 
 [202, 242, 184, 188], 
 [17, 249, 21, 188], 
 [109, 136, 163, 122], 
 [17, 11, 62, 253], 
 [219, 249, 134, 65], 
 [202, 0, 147, 253], 
 [78, 84, 247, 14], 
 [95, 95, 201, 243], 
 [132, 166, 79, 178], 
 [78, 166, 220, 79], 
 [234, 210, 115, 33], 
 [181, 141, 186, 210], 
 [49, 43, 245, 96], 
 [127, 141, 41, 47], 
 [172, 119, 102, 243], 
 [25, 250, 220, 33], 
 [40, 209, 41, 65], 
 [87, 92, 0, 110], 
 [208, 20, 249, 168], 
 [201, 238, 37, 137], 
 [225, 63, 12, 200], 
 [182, 99, 12, 166]]
```
## Question 7
Finish function `SubBytes()`:

注意，这是原地算法（包括之后的问题8-13）。这意味着只能对`state`的元素的值进行修改，而且无需返回`return`。当然，也可以不按照本模板设计函数。
```sh
def SubBytes(state):
    """
    Transformation in the Cipher that processes the State using
    a nonlinear byte substitution table (S-box) that operates
    on each of the State bytes independently.

    :type state: list[int]
    :rtype: None
    """
```
Example input:
```sh
state = [25, 61, 227, 190, 160, 244, 226, 43, 154, 198, 141, 42, 233, 248, 72, 8]
```
Example output:
```sh
[212, 39, 17, 174, 224, 191, 152, 241, 184, 180, 93, 229, 30, 65, 82, 48]
```
## Question 8
Finish function `InvSubBytes()`:
```sh
def InvSubBytes(state):
    """
    Transformation in the Inverse Cipher that is the inverse of
    SubBytes().

    :type state: list[int]
    :rtype: None
    """
```
Example input:
```sh
state = [212, 39, 17, 174, 224, 191, 152, 241, 184, 180, 93, 229, 30, 65, 82, 48]
```
Example output:
```sh
[25, 61, 227, 190, 160, 244, 226, 43, 154, 198, 141, 42, 233, 248, 72, 8]
```
## Question 9
Finish function `ShiftRows()`:
```sh
def ShiftRows(state):
    """
    Transformation in the Cipher that processes the State by 
    cyclically shifting the last three rows of the State by 
    different offsets.

    :type state: list[int]
    :rtype: None
    """
```
Example input:
```sh
state = [25, 61, 227, 190, 160, 244, 226, 43, 154, 198, 141, 42, 233, 248, 72, 8]
```
Example output:
```sh
[25, 244, 141, 8, 160, 198, 72, 190, 154, 248, 227, 43, 233, 61, 226, 42]
```
## Question 10
Finish function `InvShiftRows()`:
```sh
def InvShiftRows(state):
    """
    Transformation in the Inverse Cipher that is the inverse
    of ShiftRows().

    :type state: list[int]
    :rtype: None
    """
```
Example input:
```sh
state = [25, 244, 141, 8, 160, 198, 72, 190, 154, 248, 227, 43, 233, 61, 226, 42]
```
Example output:
```sh
[25, 61, 227, 190, 160, 244, 226, 43, 154, 198, 141, 42, 233, 248, 72, 8]
```
## Question 11
Finish function `MixColumns()`:

矩阵乘法，可能会用到`MATRIX_MUL`
```sh
def MixColumns(state):
    """
    Transformation in the Cipher that takes all of the columns
    of the State and mixes their data (independently of one
    another) to produce new columns.

    :type state: list[int]
    :rtype: None
    """
```
Example input:
```sh
state = [25, 61, 227, 190, 160, 244, 226, 43, 154, 198, 141, 42, 233, 248, 72, 8]
```
Example output:
```sh
[40, 227, 32, 146, 149, 69, 246, 187, 217, 171, 35, 170, 154, 210, 153, 128]
```
## Question 12
Finish function `InvMixColumns()`:

矩阵乘法，可能会用到`INV_MATRIX_MUL`
```sh
def InvMixColumns(state):
    """
    Transformation in the Inverse Cipher that is the inverse
    of MixColumns().

    :type state: list[int]
    :rtype: None
    """
```
Example input:
```sh
state = [40, 227, 32, 146, 149, 69, 246, 187, 217, 171, 35, 170, 154, 210, 153, 128]
```
Example output:
```sh
[25, 61, 227, 190, 160, 244, 226, 43, 154, 198, 141, 42, 233, 248, 72, 8]
```
## Question 13
Finish function `AddRoundKey()`:
```sh
def AddRoundKey(state, roundKey):
    """
    Transformation in the Cipher and Inverse Cipher in which a
    Round Key is added to the State using an XOR operation. 
    The length of a Round Key equals the size of the State.

    :type state: list[int]
    :type roundKey: list[int]
    :rtype: None
    """
```
Example input:
```sh
state = [25, 61, 227, 190, 160, 244, 226, 43, 154, 198, 141, 42, 233, 248, 72, 8]
roundKey = [[43, 126, 20, 22], [40, 174, 210, 166], [171, 247, 21, 136], [9, 207, 79, 60]]
```
Example output:
```sh
[50, 67, 247, 168, 136, 90, 48, 141, 49, 49, 152, 162, 224, 55, 7, 52]
```
## Question 14
Finish function `AES.__init__()` and `AES.getkey()`:

注意：理解什么是**cannot be represented by keylen bits.**
```sh
class AES:
    def __init__(self, keylen, key=None):
        '''
        Input:
        - `keylen`: int type, the key length, with value 128, 192 or 256.
        - `key`: int type, the `keylen`-bit cipher key, encoded in big-endian;
          or None, generate the key randomly (None by default).

        Store the `key`, which is a cipher key provided by the user, as an
        attribute. If `key` is None, generate the cipher key randomly according
        to the length `keylen` with `random.randrange()`.

        Raise `AESInputError` if and only if either
        - `keylen` is not an int, or is a value other than 128, 192 and 256, or
        - `key` is not an int, is negative, or cannot be represented by
          `keylen` bits.
        '''
    
    def getkey(self):
        ''' Output: int type, the cipher key encoded in big-endian. '''
```
## Question 15
Finish function `AES.enc()`:
```sh
def enc(self, msg):
    '''
    Input: `msg`: int type, the 128-bit plaintext to be encrypted,
    encoded in big-endian.
    Output: int type, the 128-bit ciphertext encoded in big-endian.

    Encrypt the plaintext `msg` with AES algorithm, given the key provided
    or generated before. Return the ciphertext.

    Raise `AESInputError` if and only if `msg` is not an int, is negative,
    or cannot be represented by 128 bits.
    '''
```
Pseudocode:
```sh
Cipher(byte in[4*Nb], byte out[4*Nb], word w[Nb*(Nr+1)])
begin
    byte state[4,Nb]

    state = in

    AddRoundKey(state, w[0, Nb-1]) // See Sec. 5.1.4

    for round = 1 step 1 to Nr–1
        SubBytes(state) // See Sec. 5.1.1
        ShiftRows(state) // See Sec. 5.1.2
        MixColumns(state) // See Sec. 5.1.3
        AddRoundKey(state, w[round*Nb, (round+1)*Nb-1])
    end for

    SubBytes(state)
    ShiftRows(state)
    AddRoundKey(state, w[Nr*Nb, (Nr+1)*Nb-1])

    out = state
end
```
## Question 16
Finish function `AES.dec()`:
```sh
def dec(self, ciph):
    '''
    Input: `msg`: int type, the 128-bit ciphertext to be decrypted,
    encoded in big-endian.
    Output: int type, the 128-bit plaintext encoded in big-endian.

    Decrypt the plaintext `ciph` with AES algorithm, given the key provided
    or generated before. Return the plaintext.

    Raise `AESInputError` if and only if `ciph` is not an int, is negative,
    or cannot be represented by 128 bits.
    '''
```
Pseudocode:
```sh
InvCipher(byte in[4*Nb], byte out[4*Nb], word w[Nb*(Nr+1)])
begin
    byte state[4,Nb]

    state = in

    AddRoundKey(state, w[Nr*Nb, (Nr+1)*Nb-1]) // See Sec. 5.1.4

    for round = Nr-1 step -1 downto 1
        InvShiftRows(state) // See Sec. 5.3.1
        InvSubBytes(state) // See Sec. 5.3.2
        AddRoundKey(state, w[round*Nb, (round+1)*Nb-1])
        InvMixColumns(state) // See Sec. 5.3.3
    end for

    InvShiftRows(state)
    InvSubBytes(state)
    AddRoundKey(state, w[0, Nb-1])

    out = state
end
```
## Question 17
Finish function `AESCBC.encfile()`:
```sh
def encfile(self, infile, outfile, iv=0, pad=True):
    '''
    Input:
    - `infile`: str type, the pathname of input file (plaintext).
    - `outfile`: str type, the pathname of output file (ciphertext).
    - `iv`: int type, the 128-bit initialization vector (IV) encoded in
        big-endian (0 by default).
    - `pad`: bool type, pad the file using PKCS#7 if True (True by
        default).

    Read the plaintext from file `infile`. Encrypt with AES-128/192/256-CBC
    and use `iv` as the initialization vector.
    If `pad` is True, pad the file using PKCS#7.
    If `pad` is False,
    - If the input is a multiple of 128 bits (16 bytes), do not pad.
    - Otherwise, raise `AESPaddingError`.
    Write the ciphertext to file `outfile`.
    It is NOT required to check the existence of `infile` or I/O errors.

    Raise `AESInputError` if and only if either
    - `infile` is not a str, or
    - `outfile` is not a str, or
    - `iv` is not an int, is negative, or cannot be represented by
        128 bits, or
    - `pad` is not a bool.

    Raise `AESPaddingError` if and only if `pad` is False, but the input is
    not a multiple of 128 bits (16 bytes).
    '''
```
## Question 18
Finish function `AESCBC.decfile()`:
```sh
def decfile(self, infile, outfile, iv=0, pad=True):
    '''
    - `infile`: str type, the pathname of input file (ciphertext).
    - `outfile`: str type, the pathname of output file (plaintext).
    - `iv`: int type, the 128-bit initialization vector (IV) encoded in
        big-endian (0 by default).
    - `pad`: bool type, remove the padding according to PKCS#7 if True
        (True by default).

    Read the ciphertext from file `infile`. Decrypt with AES-128/192/256-CBC
    and use `iv` as the initialization vector.
    If `pad` is True, remove the padding according to PKCS#7 before writing.
    Write the plaintext to file `outfile`.
    It is NOT required to check the existence of `infile` or I/O errors.

    Raise `AESInputError` if and only if either
    - `infile` is not a str, or
    - `outfile` is not a str, or
    - `iv` is not an int, is negative, or cannot be represented by
        128 bits, or
    - `pad` is not a bool.

    Raise `AESDataError` if and only if the input is not a multiple of
    128 bits.

    Raise `AESPaddingError` if and only if `pad` is True but the padding
    does not seem correct.
    '''
```"# Autograder" 
