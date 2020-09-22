from .constants import PAGE_LIMIT


def get_page_details(page_id, count):
    page_details = {'remaining': count - (PAGE_LIMIT * page_id)}
    if page_id == 1:
        page_details['previous'] = 0
        page_details['next'] = 2

    elif page_id > 1:
        page_details['previous'] = page_id - 1
        page_details['next'] = page_id + 1

    return page_details