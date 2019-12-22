import os
import json

class TranslationLookup:
    lookup_dict = {}

    def __init__(self):
        glossory = json.load(open('state_legislature.json', 'r'))
        for glossory_item in glossory:
            self.lookup_dict.update({ k.strip().lower():v.strip().lower() for k, v in glossory_item.items()})

    def lookup_from_glossory(self, text):
        print(self.lookup_dict)
        return self.lookup_dict.get(text.strip().lower(), "not_found")

