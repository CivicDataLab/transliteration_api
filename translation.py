import os
import json

class TranslationLookup:
    lookup_dict = {}

    def __init__(self):
        self.lookup_dict = json.load(open('state_legislature.json', 'r'))[0]
        self.lookup_dict = { k.strip():v.strip() for k, v in self.lookup_dict.items()}

    def lookup_from_glossory(self, text):
        print(self.lookup_dict)
        return self.lookup_dict.get(text, "not_found")

