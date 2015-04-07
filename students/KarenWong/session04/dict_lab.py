# item 1
my_dict = {"name": "Chris", "city": "Seattle", "cake": "Chocolate"}
for k, v in my_dict.items():
    print("%s: %s" % (k, v))
my_dict.pop("cake")
for k, v in my_dict.items():
    print("%s: %s" % (k, v))
my_dict["fruit"] = "Mango"
for k, v in my_dict.items():
    print("%s: %s" % (k, v))
print my_dict.keys()
print my_dict.values()
print "cake" in my_dict
print "Mango" in my_dict.values()


# item 2
d = {}
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
hexadecimal = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C",
               "D", "E", "F"]
for number, hexadecimal in zip(num, hexadecimal):
    d[number] = hexadecimal
print d


# item 3
a_counts = {}
for key, value in my_dict.items():
    a_counts[key] = value.count("a")
print a_counts

# item 4
S2 = set()
S3 = set()
S4 = set()
S2.update([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20])
S3.update([0, 3, 6, 9, 12, 15, 18])
S4.update([0, 4, 8, 12, 16, 20])
print S2
print S3
print S4
print S3.issubset(S2)
print S4.issubset(S2)


# item 5
SLetter = set(list("Python"))
SLetter.update(["i"])
fs = frozenset(list("marathon"))
print SLetter.union(fs)
print SLetter.intersection(fs)
