from hash_table import HashTable
from unittest import TestCase

class Tests(TestCase):
    def test_can_set_and_get_a_key(self):
        ht = HashTable()
        value = [1, 2, 3]
        ht.set('key', value)
        self.assertEqual(ht.get('key'), value)

    def test_can_set_many_keys_and_get(self):
        ht = HashTable()
        ht.set('key1', 1)
        ht.set('key2', 2)
        self.assertEqual(ht.get('key1'), 1)
        self.assertEqual(ht.get('key2'), 2)
