# Regular Expressions aka regex
# Sequence Characters \d \D \w \W \s \S \b \A \Z
# Quantifires +, *, ?, {m}, {min,max}
# Special Characters \ . ^ $ [...] [^...] (...) (R | S)

import re


str = "Take up One idea.One idea at a time"
datum = "29-04-2021, 2-3-2020"
# re.search
# returns a substring of type class Instance <class re.Match> or
result = re.search(r'i\w+', str)
# so it needs a group method to print the results
print(type(result), result.group(), result)

# returns of type None
result = re.search(r'I\w+', str)
# so it doesn't need group method
print(type(result), result)

# Quantifiers demo using findall method
print("\n***************Quantifiers Demo****************\n")
# re.findall returns of type list
result = re.findall(r'a\w*', str)
print("asterik quantifier")
print(type(result), result)

result = re.findall(r'a\w+', str)
print("plus quantifier")
print(type(result), result)

result = re.findall(r'a\w?', str)
print("question mark quantifier")
print(type(result), result)

result = re.findall(r'a\w{2}', str)
print("paranthesis quantifier")
print(type(result), result)

result = re.findall(r'a\w{2, 5}', str)
print("min and max paranthesis quantifier")
print(type(result), result)

result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', datum)
print("finding date format")
print(result, "\n")

# re.match

# returns of type class Instance <class re.Match> or
result = re.match(r'T\w+', str)
# so it needs a group method to print the results
print(type(result), result.group(), result)

# returns of type None
result = re.match(r'i\w{4}', str)
# so it doesn't need group method
print(type(result), result)

# re.split returns of type list

# splitting based on white spaces "\s"
# + represents one or more spaces
result = re.split(r'\s+', str)
print(result)

# splitting based on special character : period - "\."
# + represents one or more periods
result = re.split(r'\.+', str)
print(result)

# splitting based on space "\s" and special character "\."
# + represents one or more spaces or periods
result = re.split(r'[\s.]+', str)
print(result)

# re.sub() returns of type string

# substituting one character at a time
result = re.sub(r'[\s.]+', '_', str)
print(type(result), result)

# substituting a word/string at a time
result = re.sub(r'idea', 'idea(s)', str)
print(result)


