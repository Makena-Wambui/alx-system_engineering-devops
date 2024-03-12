What is a regular expression?
It is a pattern of characters
The pattern is used for searching and replacing characters in strings

SYNTAX
-------
/pattern/modifier(s)

Useful in extracting information from text such as code, log files, spreadsheets and docs
In regular expressions, everything is a character.
We are writing patterns to match a specific sequence of characters(string)

Metacharacters are special characters used to match any specific characters.
They are characters with a special meaning
/d used in place of any digit from 0 to 9

Dot(.)
represents the wildcard concept
To match any single character fom letters to digits to whitespaces, literally everything except line terminators

[abc] use square brackets to match specific characters -> will only match strings that specifically have a, b, or c

[^abc] to exclude specified characters

Character ranges use square brackets with dash(-)
[0-9] -> match any digit from 0 t0 9
[^n-p] -> exclude letters from n to p
\w to find a word character
\W non word character


Quantifiers/ Curly Braces Notation
w{} w exactly 3 times
a{1, 3} a no more than three times and no less than once
Can be used with any character or metacharacter
[w, x, y]{5}- any of these characters appearing  5 times
.{2, 6} -any character that appears at least twice and at most 6 times
hb{0,1}tn -> h, b appears 0 and at most once, t, n

Kleene plus: one or more of the characters it follows
Kleene star: 0 or more of the characters it follows

n+ : 1 or more ns
[abc]* 0 or more of a, or b or c

? METACHARACTER
----------------
Denotes optionality
Match either 0 or 1 of the preceding character or group
ab?c = abc, ac because b is optional
Escape it \? if you want it to match a normal ? in string

^n -match strings that start with n
n$ - those that end with n
