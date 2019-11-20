'''
Returns the length of a string in bytes.

Use s.encode('utf-8') to encode the given string and return its length.
'''
def byte_size(s):
    return len(s.encode('utf-8'))
print(byte_size('😀'))

'''
Converts a string to camelcase.

Break the string into words and combine them capitalizing the first letter of each word,
    using a regexp, title() and lower.
'''
import re

def camel(s):
    return re.sub(r"(\s|-|_)+", " ", s).title().replace(" ", "")
print(camel('Some label that needs to be camelized'))
print(camel('some_database_field_name'))

'''
Capitalizes the first letter of a string.

Capitalize the first letter of the string
    and then add it with rest of the string. 
Omit the lower_rest parameter to keep the rest of the string intact, or 
set it to True to convert to lowercase.
'''
def capitalize(s, lower_rest=False):
    return s[:1].upper() + (s[1:].lower() if lower_rest else s[1:])

def capitalize_every_word(s):
    return s.title()

def decapitalize(s, upper_rest=False):
    return s[:1].lower() + (s[1:].upper() if upper_rest else s[1:])

'''
Checks if a string is an anagram of another string (case-insensitive, ignores spaces, punctuation and special characters).

Use s.replace() to remove spaces from both strings. 
Compare the lengths of the two strings, return False if they are not equal. 
Use sorted() on both strings and compare the results.
'''
def is_anagram(s1, s2):
    _str1, _str2 = s1.replace(" ", ""), s2.replace(" ", "")

    if len(_str1) != len(_str2):
        return False
    else:
        return sorted(_str1.lower()) == sorted(_str2.lower())

def n_times_string(s, n):
    return (n * s)
print(n_times_string('py', 4))

'''
Returns True if the given string is a palindrome, False otherwise.

Use s.lower() and re.sub() to convert to lowercase and remove non-alphanumeric characters from the given string. Then, compare the new string with its reverse.
'''
from re import sub

def palindrome(s):
    s = sub('[\W_]', '', s.lower())
    return s == s[::-1]

print(palindrome('taco cat'))

def reverse_string(string):
    return string[::-1]

'''
Converts a string to kebab case.

Break the string into words and combine them adding - as a separator,
using a regexp.
'''
import re

def kebab(s):
    return re.sub(r"(\s|_|-)+","-",
    re.sub(r"[A-Z]{2,}(?=[A-Z][a-z]+[0-9]*|\b)|[A-Z]?[a-z]+[0-9]*|[A-Z]|[0-9]+",
    lambda mo: mo.group(0).lower(), s)
    )

kebab('camelCase'); # 'camel-case'
kebab('some text'); # 'some-text'
kebab('some-mixed_string With spaces_underscores-and-hyphens'); # 'some-mixed-string-with-spaces-underscores-and-hyphens'
kebab('AllThe-small Things'); # "all-the-small-things"

'''
Splits a multiline string into a list of lines.

Use s.split() and '\n' to match line breaks and create a list.
'''
def split_lines(s):
    return s.split('\n')


'''
Converts a string to snake case.

Break the string into words and combine them adding _ as a separator,
using a regexp.
'''
import re

def snake(s):
    return '_'.join(re.sub('([A-Z][a-z]+)', r' \1',
    re.sub('([A-Z]+)', r' \1',
    s.replace('-', ' '))).split()).lower()

snake('camelCase') # 'camel_case'
snake('some text') # 'some_text'
snake('some-mixed_string With spaces_underscores-and-hyphens') # 'some_mixed_string_with_spaces_underscores_and_hyphens'
snake('AllThe-small Things') # "all_the_smal_things"