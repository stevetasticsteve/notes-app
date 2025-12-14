from django.db import models
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page
from wagtail.search import index

from notes.blocks import BootstrapTableBlock


class NotesContentsPage(Page):
    """A page witha  simple text intro, followed by a auto generated list of children NotePages."""

    subpage_types = ["notes.NotePage", "notes.NotesContentsPage"]
    page_description = "A page that acts as a table of contents for all notes below it."

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        # Fetch all live NotePages that are children of this page
        context["notes"] = self.get_children().live()
        for note in context["notes"]:
            note.children = note.get_children().live()
            note.num_children = note.children.count()
        return context


class NotePage(Page):
    """A page representing an individual note.

    Has updated date and a flexible content area.
    """

    parent_page_types = ["notes.NotesContentsPage"]
    # Note pages should not have any subpages
    subpage_types = []
    page_description = "A page representing an individual note."

    note_updated = models.DateField("Note Date", auto_now=True)

    # The main, flexible content area
    body = StreamField(
        [
            ("paragraph", blocks.RichTextBlock()),
            ("table", BootstrapTableBlock()),
        ],
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

    search_fields = Page.search_fields + [  # Inherit search_fields from Page
        index.SearchField("body"),
    ]
