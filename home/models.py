from django.db import models
from wagtail.fields import RichTextField
from wagtail.models import Page


class HomePage(Page):
    subpage_types = ["notes.NotesContentsPage"]
    max_subpages = 1
    body = RichTextField(blank=True)

    def get_context(self, request):
        context = super().get_context(request)
        # Fetch all live NotePages that are children of this page
        context["linked_pages"] = self.get_children().live()#.order_by("sort_order")
        return context
