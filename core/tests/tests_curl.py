import json
from subprocess import PIPE, Popen
from django.test import TestCase
from core.tests._aux import get_curl, MARK, EXISTS, SARAH, HAYS



class PersonTestCase(TestCase):


    def test_post_exists_delete(self):
        # Insert Zuckerberg
        p = json.loads(Popen([get_curl('post',4)], shell=True, stdout=PIPE).communicate()[0])
        person = MARK if p==MARK else EXISTS
        self.assertEqual(person, p)

        # Delete Zuckerberg
        p = Popen([get_curl('delete',4)], shell=True, stdout=PIPE)

    def test_list(self):

        # Database Empty
        p = Popen([get_curl('empty')], shell=True, stdout=PIPE)

        # Insert Zuckerberg
        p = json.loads(Popen([get_curl('post', 4)], shell=True, stdout=PIPE).communicate()[0])
        person = MARK if p==MARK else EXISTS
        self.assertEqual(person, p)


        # Insert SARAH
        p = json.loads(Popen([get_curl('post', 1399)], shell=True, stdout=PIPE).communicate()[0])
        person = SARAH if p==SARAH else EXISTS
        self.assertEqual(person, p)

        # Insert Hays
        p = json.loads(Popen([get_curl('post', 1399)], shell=True, stdout=PIPE).communicate()[0])
        person = HAYS if p==HAYS else EXISTS
        self.assertEqual(person, p)

