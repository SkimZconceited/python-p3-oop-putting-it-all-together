#!/usr/bin/env python3

class Book:
    def __init__(self, title) -> None:
        self.title = title
        self._page_count = 0
        pass

    def get_page_count(self):
        return self._page_count
    
    def set_page_count(self, page_count):
        if type(page_count) == type(0) and page_count > 0:
            print('Changing the page_count')
            self._page_count = page_count
        else:
            print(f'Enter a valid nummber. {page_count} is less than 0')
        pass

    page_count = property(get_page_count, set_page_count,)

    def turn_page(self, page):
        # page = self._page_count
        if page <= self._page_count and page > 0:
            page += 1
            print(f'Flipping the page...wow, you read fast! On page {page}')
        elif page == self._page_count:
            print('Thank you for reading the book')
        return page

    pass
# book = Book("And Then There Were None", 272)

# book = Book('And Then There Were None', 272)
# book.title = "And Then There Were None"

# print(book.title)
# print(book.page_count)

# print(book.turn_page(25))

