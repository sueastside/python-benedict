# -*- coding: utf-8 -*-

from benedict import benedict

import unittest


class github_issue_0027_test_case(unittest.TestCase):

    """
    https://github.com/fabiocaccamo/python-benedict/issues/27

    To run this specific test:
    - Run python -m unittest tests.github.test_issue_0027
    """

    def test_append_to_list_with_empty_index(self):
        d = benedict({
            'results': [
                {
                    'locations': [
                        'Torino',
                        'Milano',
                        'Napoli',
                    ]
                },
            ]
        })
        d['results[0].locations'].append('Roma')
        self.assertEqual(d['results[0].locations'], ['Torino', 'Milano', 'Napoli', 'Roma'])
        return d