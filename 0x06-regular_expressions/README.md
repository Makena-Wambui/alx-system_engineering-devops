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



