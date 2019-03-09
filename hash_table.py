class HashTable(object):
    def __init__(self, size=100):
        self.__size = size
        self.__array = [None] * self.__size

    def set(self, key, value):
        self.__array.insert(self.__hash(key), (key, value))

    def get(self, key):
        index = self.__hash(key)
        try:
            key, value = self.__array[index]
        except IndexError:
            raise KeyError('key not found')
        return value

    def values(self):
        """
        returns the values in the hash table
        as an array
        """
        values_array = []
        for item in self.__array:
            values_array.append(item[1])
        return values_array

    def keys(self):
        """
        returns the keys in the hash table
        as an array
        """
        keys_array = []
        for item in self.__array:
            keys_array.append(item[0])
        return keys_array

    def items(self):
        """
        returns key,value pairs.
        returns as a list of tuples
        """
        return self.__array

    def __hash(self, key):
        """
        returns a valid index in self.array
        to store the key's value
        """
        hash_value = 0
        for letter in key:
            hash_value += ord(letter)
        hash_value %= self.__size
        return hash_value
