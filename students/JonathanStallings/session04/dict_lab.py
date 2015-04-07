from __future__ import print_function

# Section 1
a = {
    "name": "Chris",
    "city": "Seattle",
    "cake": "Chocolate"
}

print(a)

del a["cake"]

print(a)

a["fruit"] = "Mango"

print(a.keys())
print(a.values())
print("cake" in a.keys())  # OR "cake" in d
print("Mango" in a.values())

# Section 2
key_num = []
val_hex = []
# b = {}

for x in range(16):
    key_num.append(x)
    val_hex.append(hex(x))

b = dict([(k, v) for k, v in zip(key_num, val_hex)])

print(b)

# Section 3
c = {k: v.count('a') for k, v in a.items()}
print(c)

# Section 4


def divisible_set(r, div):
    """
    Return set of numbers evenly divisble by given number in given range.

    Args:
        r: range of numbers from zero to natural counting end of range
        div: divisor

    Returns: set of divisible numbers in range
    """
    set_list = []
    for x in range(r + 1):
        if not x % div:
            set_list.append(x)
    return set(set_list)


s2 = divisible_set(20, 2)
s3 = divisible_set(20, 3)
s4 = divisible_set(20, 4)
print(s2)
print(s3)
print(s4)

print(s3.issubset(s2))
print(s4.issubset(s2))

# Section 5
s_py = set(list('Python'))
s_py.add('i')
s_ma = frozenset(list('marathon'))
print(s_py.union(s_ma))
print(s_py.intersection(s_ma))

