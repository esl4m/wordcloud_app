from ..settings import settings
from collections import namedtuple


class Paginator(namedtuple('Paginator', ('queryset', 'page'))):
    def __str__(self):
        return 'page {} of {}'.format(self.page, self.num_pages())

    def results(self):
        """
        Paginate queryset and return results
        """
        return self.queryset.paginate(self.page, self.page_size())

    def num_pages(self):
        """
        Get number of pages
        """
        return (self.count() // self.page_size()) + 1

    def count(self):
        """
        Get number of records
        """
        return self.queryset.count()

    def page_size(self):
        """
        Get pagination page size
        """
        return settings['page_size']

    def pages(self):
        """
        Get pagination pages
        """
        return range(1, self.num_pages() + 1)

    def is_current(self, current_page):
        """
        Returns True is page is current_page
        """
        return self.page == current_page

    @property
    def next_page(self):
        if self.page != self.num_pages():
            return self.page + 1

    @property
    def prev_page(self):
        if self.page > 1:
            return self.page - 1

    @property
    def has_pages(self):
        return self.num_pages() > 1


__all__ = ['Paginator']
