x = "a"
y = "\n"
i = "\t"
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split %son a line." % (y)
backslash_cat = "I'm \\ %s \\ cat." % (x)

fat_cat = '''
I'll do a list:
%s* Cat food
%s* Fishies
%s* Catnip\n%s* Grass
''' % (i, i, i, i)

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
