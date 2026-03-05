# line 17
building strings with `+=` inside a loop is discouraged bcz strings are immutable
use a list or a list comprehension for better performance

# line 19
instead of adding a space for every non-alphanumeric char, use `re.sub()`
it's cleaner for replacing punctuation in one go

# line 24
btw, you can use `.get()` here to handle the dict lookup and the "else" case in one line

# line 24
this logic works for single digits, but `"10"` would stay `"10"` if it's not in your dict
