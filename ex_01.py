some_string = " Ми вчимо Java?  "
result = some_string.lstrip()
result = result.replace("Java", "Python")
result = result.removesuffix("?  ")
print(result)

# for i in result:
#     print(i, ord(i))


print("|{:*^12}|".format('123456'))