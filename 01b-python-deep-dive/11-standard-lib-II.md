# 11. Brief Tour of the Standard Library - Part II
## 11.1 Output Formatting
```py
# abbreviated display of large objects
import reprlib
reprlib.repr(set('supercalifragilisticexpialidocious'))
# "{'a', 'c', 'd', 'e', 'f', 'g', ...}"

# pretty print
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]
pprint.pprint(t, width=30)
# [[[['black', 'cyan'],
#    'white',
#    ['green', 'red']],
#   [['magenta', 'yellow'],
#    'blue']]]

# wrap text
import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc, width=40))
# The wrap() method is just like fill()
# except that it returns a list of strings
# instead of one big string with newlines
# to separate the wrapped lines.

# location/culture-specific data formatting
import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')
# 'English_United States.1252'
conv = locale.localeconv() # get a mapping of conventions
x = 1234567.8
locale.format_string("%d", x, grouping=True)
# '1,234,567'
locale.format_string("%s%.*f", (conv['currency_symbol'],
                     conv['frac_digits'], x), grouping=True)
# '$1,234,567.80'
```

## 11.2 Templating




## 11.3 Working with Binary Data Record Layouts




## 11.4 Multi-threading




## 11.5 Logging




## 11.6 Weak References




## 11.7 Tools for Working with Lists




## 11.8 Decimal Floating Point Arithmetic