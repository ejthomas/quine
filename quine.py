quine = '''print("quine = {}".format("".join(["'", "'", "'"]))+quine+"".join(["'", "'", "'"]))
print(quine)'''
print("quine = {}".format("".join(["'", "'", "'"]))+quine+"".join(["'", "'", "'"]))
print(quine)
