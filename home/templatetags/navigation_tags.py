from django import template
from wagtail.models import Page

register = template.Library()


@register.inclusion_tag("breadcrumbs.html", takes_context=True)
def breadcrumbs(context):
    self = context.get("self")

    # Exclude the root page (depth=1) and the home page (often depth=2)
    # The default Wagtail root page has depth=1, and the site's home page is often depth=2.
    # We use depth > 2 to exclude those, only getting ancestors of the current page.
    if self is None or self.depth <= 2:
        ancestors = ()
    else:
        # Get ancestors of the current page, inclusive=True includes the current page,
        # but we use .filter(depth__gt=2) to exclude the site root and immediate child (Home).
        # We also call .specific() to ensure we get the specific page model instance for titles/urls.
        ancestors = self.get_ancestors(inclusive=False).filter(depth__gt=2).specific()

    return {
        "ancestors": ancestors,
        "current_page": self,
        "request": context["request"],
    }
