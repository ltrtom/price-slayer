import unittest
import os
import requests

from py.html.sanitizer import Sanitizer
# https://regex101.com/r/lU8sM3/1


class SanitizerTest(unittest.TestCase):
    html = ''
    sanitizer = None
    body_sentence = 'Backshop'
    return_carriage = ('\n', '\r')

    def test_extract_body(self):
        self._sanitize()
        for tag in ('<body', '</body'):
            self.assertNotIn(tag, self.html)

    def test_remove_carriage(self):
        self._sanitize()
        for char in self.return_carriage:
            self.assertNotIn(char, self.html)

    def test_remove_comments(self):
        self._sanitize()
        for com_tag in ('<!--', '-->'):
            self.assertNotIn(com_tag, self.html)

    def test_remove_useless_tags(self):
        self._sanitize()
        for tag in self.sanitizer.USELESS_TAGS:
            self.assertNotIn('<%s' % tag, self.html)

        for t in ('<', '>'):
            self.assertNotIn(t, self.html)


    def _load_fixture(self):
        self.load_file('backshop.html')

    def _sanitize(self):
        self.html = self.sanitizer.sanitize(self.html)

    def _expect_has_body_sentence(self):
        self.assertIn(self.body_sentence, self.html)

    def tearDown(self):
        self._expect_has_body_sentence()

    def setUp(self):
        self._load_fixture()
        self.sanitizer = Sanitizer()
        self._expect_has_body_sentence()

    def load_file(self, name):
        self.assertTrue(os.path.isfile(name))
        with open(name, 'r') as f:
            self.html = f.read()


class ZalandoSanitizerTest(SanitizerTest):
    body_sentence = 'Ajouter au panier'

    def _load_fixture(self):
        self.load_file('fixture.html')


class LebrokeSanitizerTest(SanitizerTest):
    body_sentence = 'login'

    def _load_fixture(self):
        self.html = requests.get('http://cut.lebroke.fr/login').text


# class MixRadioTest(SanitizerTest):
#     body_sentence = 'Dance'
#
#     def _load_fixture(self):
#         self.html = requests.get('http://www.hotmixradio.fr/player/playerhtm/play-dance.html').text

