# Copyright (C) 2019 H. Turgut Uyar <uyar@tekir.org>
#
# Derived from the sphinxjp.themes.revealjs project
# by tell-k <ffk2005@gmail.com>.

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.parsers.rst.roles import set_classes
from sphinx.util import logging


logger = logging.getLogger(__name__)


class Slide(nodes.General, nodes.Element):
    """Node for a slide."""


class SpeakerNotes(nodes.General, nodes.Element):
    """Node for speaker notes on a slide."""


class SlideDirective(Directive):
    """Directive for a slide."""

    has_content = True
    required_arguments = 0
    optional_arguments = 100
    final_argument_whitespace = False

    option_spec = {
        "id": directives.unchanged,
        "class": directives.class_option,
        "noheading": directives.flag,
        "title-heading": lambda t: directives.choice(t, ("h1", "h2", "h3", "h4", "h5", "h6")),
        "subtitle": directives.unchanged,
        "subtitle-heading": directives.unchanged,
        "data-autoslide": directives.unchanged,
        "data-transition": directives.unchanged,
        "data-transition-speed": directives.unchanged,
        "data-background": directives.unchanged,
        "data-background-repeat": directives.unchanged,
        "data-background-size": directives.unchanged,
        "data-background-transition": directives.unchanged,
        "data-state": directives.unchanged,
        "data-markdown": directives.unchanged,
        "data-separator": directives.unchanged,
        "data-separator-vertical": directives.unchanged,
        "data-separator-notes": directives.unchanged,
        "data-charset": directives.unchanged,
    }

    node_class = Slide

    def run(self):
        """Build slide node."""
        self.assert_has_content()

        set_classes(self.options)

        text = "\n".join(self.content)
        node = self.node_class(text, **self.options)
        self.add_name(node)

        if "data-markdown" not in self.options:
            self.state.nested_parse(self.content, self.content_offset, node)

        if self.arguments:
            node["title"] = " ".join(self.arguments)

        node["noheading"] = "noheading" in self.options

        return [node]


class SpeakerNotesDirective(Directive):
    """Directive for a speaker notes entry."""

    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = False

    option_spec = {"class": directives.class_option}

    node_class = SpeakerNotes

    def run(self):
        """Build speaker notes node."""
        self.assert_has_content()

        set_classes(self.options)

        text = "\n".join(self.content)
        node = self.node_class(text, **self.options)
        self.add_name(node)

        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


_MARKDOWN_HEADINGS = {
    "h1": "#",
    "h2": "##",
    "h3": "###",
    "h4": "####",
    "h5": "#####",
    "h6": "######",
}


def visit_slide(self, node):
    """Build start tag for a slide."""
    section_attrs = {}

    if node.get("id"):
        section_attrs.update({"ids": [node.get("id")]})

    data_attrs = [a for a in SlideDirective.option_spec if a.startswith("data-")]
    for attr in data_attrs:
        if node.get(attr) is not None:
            section_attrs.update({attr: node.get(attr)})

    title = None
    if node.get("title") and (not node.get("noheading")):
        title = node.get("title")
    title_heading = node.get("title-heading", "h2")

    subtitle = node.get("subtitle")
    subtitle_heading = node.get("subtitle-heading", "h3")

    if node.get("data-markdown") is not None:
        title_base = "%(heading)s %(title)s \n"
        title_text = None
        if title:
            title_text = title_base % {
                "heading": _MARKDOWN_HEADINGS.get(title_heading),
                "title": title,
            }

        subtitle_text = None
        if subtitle:
            subtitle_text = title_base % {
                "heading": _MARKDOWN_HEADINGS.get(subtitle_heading),
                "title": subtitle,
            }
    else:
        title_base = "<%(heading)s>%(title)s</%(heading)s>\n"
        title_text = None
        if title:
            title_text = title_base % {"title": title, "heading": title_heading}

        subtitle_text = None
        if subtitle:
            subtitle_text = title_base % {"title": subtitle, "heading": subtitle_heading}

    self.body.append(self.starttag(node, "section", **section_attrs))
    self.body.append('<div class="content">\n')
    if node.get("data-markdown") is not None:
        if node.get("data-markdown") == "":
            self.body.append("<script type='text/template'>\n")
            if title_text:
                self.body.append(title_text)
            if subtitle_text:
                self.body.append(subtitle_text)
            self.body.append(node.rawsource)
            self.body.append("</script>\n")
    else:
        if title_text:
            self.body.append(title_text)
        if subtitle_text:
            self.body.append(subtitle_text)
        self.set_first_last(node)


def depart_slide(self, node=None):
    """Build end tag for a slide."""
    self.body.append("</div>\n")
    self.body.append("</section>\n")


def visit_speaker_note(self, node):
    """Build start tag for a speaker note."""
    self.body.append(self.starttag(node, "aside", **{"class": "notes"}))
    self.set_first_last(node)


def depart_speaker_note(self, node=None):
    """Build end tag for a speaker note."""
    self.body.append("</aside>\n")


def setup(app):
    """Initialize the extension.

    :sig: (sphinx.application.Sphinx) -> None
    """
    logger.info("Initializing Kirlent directives")
    app.add_node(Slide, html=(visit_slide, depart_slide))
    app.add_node(SpeakerNotes, html=(visit_speaker_note, depart_speaker_note))
    app.add_directive("slide", SlideDirective)
    app.add_directive("speaker-notes", SpeakerNotesDirective)
