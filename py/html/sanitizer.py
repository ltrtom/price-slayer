import re


class Sanitizer():
    REG = r'(<%s.*?</%s>)'
    # REG_CONTAINS = r'(<%s.*</%s>)'

    USELESS_TAGS = ['noscript', 'svg', 'style', 'script', 'iframe']

    html = ''
    metas = []

    @staticmethod
    def find_tag(tag, html):

        if tag not in html:
            return None, None

        open_tag = '<%s' % tag
        index_open = html.index('>', html.index(open_tag)) + 1  # finding the next '>'
        index_close = html.index('</%s>' % tag)

        return index_open, index_close

    def _put_inline(self):
        self.html = self.html.replace('\n', '').replace('\r', '')

    def _remove_comments(self):
        self.html = re.sub(r'(<!--.*?-->)', '', self.html)

    def _remove_useless_tags(self):

        for tag in self.USELESS_TAGS:
            reg = re.compile(self.REG % (tag, tag))
            self.html = reg.sub('', self.html)

        self.html = re.sub(r'(<.*?>)', '', self.html)

    def sanitize(self, html, keep_meta=False):

        self.html = html
        self._put_inline()

        if keep_meta:
            self.extract_metas()

        # extract body
        open_tag, close = Sanitizer.find_tag('body', self.html)
        if open_tag and close:
            self.html = self.html[open_tag:close]

        # we need to remove all '\n' to make the regex works better
        self._put_inline()
        # remove script, comments
        self._remove_comments()

        self._remove_useless_tags()

        return self.html

    def extract_metas(self):
        pass

