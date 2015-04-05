#!/usr/bin/env python

"""
Python class example.

"""

# The start of it all:
# Fill it all in here.


class Element(object):
    """A base HTML element."""
    tag = u"html"
    indent = u"    "

    def __init__(self, content=None, **kwargs):  # Can't pass 'class' attr
        self.children = [content] if content else []
        self.attributes = kwargs
        self.attr = u""
        for key, value in self.attributes.items():  # Consider alt method.
            self.attr += u' {k}="{v}"'.format(k=key, v=value)

    def append(self, content):
        """Append content to element."""
        self.children.append(content)

    def render(self, file_out, ind=u""):
        """Render the element and children into HTML."""
        file_out.write(
            u"{indent}<{tag}{attr}>\n"
            .format(indent=ind, tag=self.tag, attr=self.attr)
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


class OneLineTag(Element):
    def render(self, file_out, ind=u""):
        """Override default rendering in favor of one-line output."""
        file_out.write(
            u"{indent}<{tag}{attr}>"
            .format(indent=ind, tag=self.tag, attr=self.attr)
        )
        for child in self.children:
            try:
                child.render(file_out, "")
            except AttributeError:
                file_out.write(
                    u"{indent}{child}"
                    .format(indent="", child=unicode(child))
                )
        file_out.write(
            u"{indent}</{tag}>\n".format(indent="", tag=self.tag)
        )


class SelfClosingTag(Element):
    def render(self, file_out, ind=u""):
        """Override default rendering for self closing tags."""
        file_out.write(
            u"{indent}<{tag}{attr} />\n"
            .format(indent=ind, tag=self.tag, attr=self.attr)
        )


class Html(Element):
    header = u"<!DOCTYPE html>\n"
    tag = u"html"

    def render(self, file_out, ind=u""):
        file_out.write(self.header)
        Element.render(self, file_out, ind)


class Head(Element):
    tag = u"head"


class Title(OneLineTag):
    tag = u"title"


class Body(Element):
    tag = u"body"


class P(Element):
    tag = u"p"


class Hr(SelfClosingTag):
    tag = u"hr"


class Br(SelfClosingTag):
    tag = u"br"


class A(OneLineTag):
    tag = u"a"

    def __init__(self, link, content, **kwargs):
        self.link = link
        Element.__init__(self, content, href=link, **kwargs)

