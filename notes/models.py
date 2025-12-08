from django.db import models
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.models import Page

from notes.blocks import BootstrapTableBlock


class NotesContentsPage(Page):
    """A page witha  simple text intro, followed by a auto generated list of children NotePages."""

    subpage_types = ["notes.NotePage", "notes.NotesContentsPage"]

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        # Fetch all live NotePages that are children of this page
        context["notes"] = self.get_children().live()  # .order_by("sort_order")
        return context


class NotePage(Page):
    """A page representing an individual note.

    Has updated date and a flexible content area.
    """

    parent_page_types = ["notes.NotesContentsPage"]
    # Note pages should not have any subpages
    subpage_types = []

    note_updated = models.DateField("Note Date", auto_now=True)

    # The main, flexible content area
    body = StreamField(
        [
            ("heading", blocks.CharBlock(form_classname="full title")),
            ("paragraph", blocks.RichTextBlock()),
            ("table", BootstrapTableBlock()),
        ],
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
