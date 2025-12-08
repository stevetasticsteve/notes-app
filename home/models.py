from django.db import models
from wagtail import blocks
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.models import Page


class HomePage(Page):
    subpage_types = ["notes.NotesContentsPage"]
    max_subpages = 1
    body = RichTextField(blank=True)

    # Define a StreamField for the linked pages/cards
    linked_pages = StreamField(
        [
            (
                "card",
                blocks.StructBlock(
                    [
                        (
                            "page",
                            blocks.PageChooserBlock(
                                required=True,
                                page_type=[
                                    "notes.NotesContentsPage", "notes.NotePage"
                                ],
                            ),
                        ),
                        (
                            "custom_title",
                            blocks.CharBlock(
                                required=False, help_text="Override the page's title."
                            ),
                        ),
                        ("card_image", ImageChooserBlock(required=False)),
                    ],
                    label="Link Card",
                ),
            )
        ],
        use_json_field=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("linked_pages"),
    ]
