from wagtail.contrib.table_block.blocks import TableBlock


class BootstrapTableBlock(TableBlock):
    class Meta:
        template = "blocks/table.html"  # your custom template
