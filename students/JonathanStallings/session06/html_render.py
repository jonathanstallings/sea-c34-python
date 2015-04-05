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
        self.children = [content] if content else []

    def append(self, content):
        """Append content to element."""
        self.children.append(content)

    def render(self, file_out, ind=u""):
        """Render the element into HTML."""
        # output = (
        #     u"{indent}<{tag}>\n"
        #     u"{indent}{content}\n"
        #     u"{indent}</{tag}>"
        #     .format(
        #         indent=ind, tag=self.tag, content=self.content
        #     )
        # )
        # file_out.write(output)
        # print(output)
        file_out.write(
            u"{indent}<{tag}>\n".format(indent=ind, tag=self.tag)
        )
        for child in self.children:
            try:
                child.render(file_out, self.indent + ind)
            except AttributeError:
                file_out.write(
                    u"{indent}{child}\n"
                    .format(indent=self.indent + ind, child=unicode(child))
                )
        file_out.write(
            u"{indent}</{tag}>\n".format(indent=ind, tag=self.tag)
        )


class Html(Element):
    header = u"<!DOCTYPE html>\n"
    tag = u"html"

    def render(self, file_out, ind=u""):
        file_out.write(self.header)
        Element.render(self, file_out, ind)


class Body(Element):
    tag = u"body"


class P(Element):
    tag = u"p"
