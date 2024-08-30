from mango_test_framework import mangostart, mangoend, summary

mangostart()
code = """
a = 1
b = 2
assert a + b == 3
"""
mangoend(code)

mangostart()
code = """
"""
mangoend(code)

# Print the summary
summary()
