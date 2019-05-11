# Homework 6 autograder

This autograder is modified from CS188 in Berkeley.

## Update
- May 11 (15 pm): Delete testcase with novels except the first one.
- May 11 (14 pm): Update testcase and hint. 
- May 10 (14 pm): Release.

## HINT

stoplist.txt 中的内容：

- 在Inverted Index中不作为key
- 在query中需要事先删去再作进一步处理

Select the larger one in Lexicographical order是指字典序较后的，即id数字较大的文件。

注意返回None.如果什么也不返回，也可以视作返回None.

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

Question i is exactly Task i (i = 1, 2, 3, 4, 5).

**Windows 可以通过在上方文件夹路径栏输入'cmd'打开命令提示符窗口**

# Homework 6: Poople Search Engine

- Author: [Hongze Shen](mailto:shenhz@shanghaitech.edu.cn)
- **Due: 23:59:59, May 16 (Thursday), 2019 UTC/GMT+08:00**

Search engine, is an information retrieval system designed to help find information stored on a computer system.

In this homework, you need to implement a mini search engine. Let's call it **Poople**.

# Getting Started
To get started, please simply fork this GitLab repository and follow the structure and submissions guidelines below.
Remember to **make your repository private** before any commits.

*Note*: Markdown text with file extension ***.md*** could be displayed properly using plug-ins in your browsers or IDEs.

# Repository Structure

```
|-homework-6
    |-Poople.py
    |-stoplist.txt
    |-docs
        |-doc1.txt
        |-doc2.txt
        |-...
```

# Submission

**You should check in `Poople.py` to GitLab.**

First, make a commit and push your files. From the root folder of this repo, run
```sh
git add Poople.py
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

# Regulations

- You may **not** use third-party libraries.
- No late submissions will be accepted.
- You have 30 chances of grading (i.e. `git tag`) in this homework. If you hand in more 30 times, each extra submission will lead to 10% deduction. In addition, you may require grading at most 10 times every 24 hours.
- We enforce academic integrity strictly. If you participate in any form of cheating, you will fail this course immediately. **DO NOT** try to hack gitlab in any way(include but not limited to **Hard Code**). You can view the full edition on [Piazza](https://piazza.com/class/jrykv8wi15m5dx?cid=7).
- If you have any questions on this homework, please ask on Piazza first.


# Update
- May 10: Add kindly reminder.
- May 6: Modify descriptions to eliminate ambiguity.
- May 5: Fix typos.
- May 4: Release.

# Description

Implement your class `Poople()`.

## Step 1: Loading

Load documents. Implement instance method `__init__(self, doc_path)` such that in `__init__`:

- get file names of all texts `doc_name` with suffix '.txt' in directory `doc_path`.
- order documents by file names in **Lexicographical order**.
- bind a `doc_id` to each document `doc_name` according to the sorting result. `doc_id` starts from 1.
- create an instance variable `self.id2name` of type dict whose keys are `doc_id` and values are `doc_name`.

For instance,
```
>>> from Poople import *
>>> p = Poople('docs')
>>> p.id2name[1]
'53296.txt'
```

## Step 2: Tokenizing

Tokenize documents. Implement instance method `tokenizer(self)`

Given a raw document you need to produce a sequence of tokens. For the purposes of this assignment, a token is any number of **continuous** letters and numbers.
Alphabetic characters should be converted to lowercase during tokenization, so `bob` and `Bob` and `BOB` are all tokenized into `bob`.

For instance, tokens in "Clearlove7 won't die!" are 'Clearlove7', 'won', 't', 'die'.

Return a tuple that contains
- the number of all tokens
- the number of distinct tokens

For instance,
```
>>> p.tokenizer()
(5015, 1545)
```

## Step 3: Indexing

Record tokens from all documents in an inverted index. Implement instance method `build_index(self)`.

### Stop words

In SEO(Search Engine Optimization) terminology, stop words are the most common words that most search engines **ignore**, saving space and time in processing large data during crawling or indexing. This helps search engines to save space in their databases and improve performance.

For this assignment, stop words are stored in the file **'stoplist.txt'**. You need ignore all stop words when building index.

In this assignment, you need **ignore all stopwords** in query.

### Inverted Index

An inverted index is a database index storing a mapping from terms to their locations in documents. The purpose of an inverted index is to allow fast full-text search.

- The index will contain all distinct words in the documents excluding stop words.
- Each word is associated with the list of its `position`s in all documents.
- `position`s are represented by tuples `(doc_id, line_number)`.
- Positions of a term are sorted in ascending order with `doc_id` as primary index and `line_number` as secondary index.

Create an instance variable `self.inverted_index` of dict type whose keys are `term` and values are list of `position`s.

For instance,
```
>>> p.build_index()
>>> p.inverted_index['death']
[(4, 32)]
```

## Step 4: Query

Searching is the main function of a search engine. Implement the instance method `Query(self, query, mode='AND')`.

`query` is a case-insensitive string which might contain one or more terms seperated by blanks. For instance, for the `query` 'Good LUCK ' you need search 'good' and 'luck' in documents. `Mode` is one of 'AND' and 'OR'.

Terms in `stoplist.txt` should be ignored.

Results for a query is the documents that
- contain any terms in `query` if `mode=='OR'`
- contain all terms in `query` if `mode=='AND'`

Return a list of `doc_id` which is sorted in ascending order.
If no document satisfies the `query` or `query` contains no meaningful word, return `None`.

For instance,
```
>>> p.Query('Ban GUN')
[1, 2]
```

## Step 5: Ranking

People tend to view the top results on the first page. The listings, which are on the first page are the most important ones, because those get 91% of the click through rates (CTR) from a particular search.

In this step, you need to implement an instance method `Rank(self, query, mode='AND')`.

The meaning of `mode` is the same as Step 4.

For a `query`, the rank of a document is calculated in following way:

![rank](https://latex.codecogs.com/gif.latex?\bg_white&space;Rank(query,&space;doc_k)&space;=&space;\sum_{term&space;\in&space;query}&space;\frac{Occur(term,&space;doc_k)}{\sum_{doc&space;\in&space;docs}Occur(term,&space;doc)})
where `Occur(term, doc)` is the number of occurrences of `term` in `doc`.

`first_target_line` in a document is the first line that contains any term in the query.

Return the tuple `(doc_name, first_target_line)` with highest rank. Select the larger one in Lexicographical order to break the tie. Ignore terms not in `inverted_index`. If no document satisfies the `query` or `query` contains no meaningful word, return `None`.

For instance,
```
>>> p.Rank('guns')
('53296.txt', 'Newsgroups: talk.politics.guns\n')
```
