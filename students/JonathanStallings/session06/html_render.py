#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):
    """An HTML element."""
    header = u""
    tag = u""
    indent = u"    "

    def __init__(self, content=None):
        self.content = self.indent + str(self.content) if content else ""

    def append(self, string):
        """Append string to content."""
        self.content += (
            u"{indent}{str}".format(indent=self.indent, str=str(string))
        )

    def render(self, file_out, ind=""):
        """Render the tag and strings in content."""
        output = (
            u"{indent}{header}\n"
            "{indent}<{tag}>\n"
            "{indent}{content}\n"
            "{indent}</{tag}>"
            .format(
                header=self.header, indent=ind,
                tag=self.tag, content=self.content
            )
        )
        file_out.write(output)


class HTML(Element):
    """The HTML element."""
    header = u"<!DOCTYPE html>"
    tag = u"html"

    def __init__(self, content=None):
        self.content = self.indent + str(self.content) if content else ""


class Body(Element):
    """The body element."""
    tag = u"body"

    def __init__(self, content=None):
        self.content = self.indent + str(self.content) if content else ""


class P(Element):
    """A paragraph element."""
    tag = u"p"

    def __init__(self, content=None):
        self.content = self.indent + str(self.content) if content else ""
