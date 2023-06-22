# pagination_tags.py

from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def paginate(context, adjacent_pages=3):
    current_page = context['company_list'].number
    total_pages = context['paginator'].num_pages
    page_range = context['paginator'].page_range

    if total_pages <= 2 * adjacent_pages + 1:
        return page_range

    left_range = page_range[:adjacent_pages]
    right_range = page_range[-adjacent_pages:]

    if current_page <= adjacent_pages + 1:
        return left_range + ['...'] + right_range

    if current_page >= total_pages - adjacent_pages:
        return left_range + ['...'] + right_range

    middle_range = page_range[
        current_page - adjacent_pages - 1:current_page + adjacent_pages
    ]

    return left_range + ['...'] + middle_range + ['...'] + right_range
