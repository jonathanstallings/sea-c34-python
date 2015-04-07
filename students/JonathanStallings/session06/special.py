# Can I use special methods on a class to allow primary colors to be
# simply added together to return a secondary color?


class PrimaryColor(object):
    """A simple representation of primary colors."""
    primaries = {'red': 1, 'blue': 2, 'yellow': 3}
    secondaries = {3: 'purple', 4: 'orange', 5: 'green'}

    def __init__(self, color):
        while color not in self.primaries:
            color = raw_input(
                "Please enter a primary color.\n\n"
                "> "
            ).lower()
        self.color = color

    def __add__(self, other):
        """Add two primary colors and return secondary."""
        if other.color == self.color:
            return self.color
        elif other.color in self.primaries:
            mixed_color = (
                self.primaries[self.color] + self.primaries[other.color]
            )
            return self.secondaries[mixed_color]
        else:
            print("Must add primary colors together.")


red = PrimaryColor('red')
blue = PrimaryColor('blue')
yellow = PrimaryColor('yellow')

print(red + blue)
print(red + red)
print(yellow + blue)


# result: Yes! Please forgive my silly, very impractical example.

