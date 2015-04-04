#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):
    """An HTML element."""
    tag = u"html"
    indent = u"    "

    def __init__(self, content=None):
        self.content = self.indent + str(self.content) if content else ""

    def append(self, string):
        """Append string to content."""
        self.content += (
            u"{indent}{str}\n".format(indent=self.indent, str=str(string))
        )

    def render(self, file_out, ind=""):
        """Render the tag and strings in content."""
        output = (
            u"{indent}<{tag}>\n"
            "{indent}{content}"
            "{indent}</{tag}>"
            .format(indent=ind, tag=self.tag, content=self.content)
        )
        file_out.write(output)

