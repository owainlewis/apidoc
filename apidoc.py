#!/usr/bin/env python3
import yaml
import itertools

class SwaggerParser:
    def __init__(self, file_path):
        self.path = file_path

    def load(self):
        with open(self.path, 'r') as stream:
                return yaml.load(stream)

    def __flatten(self, list_of_lists):
        return list(itertools.chain(*list_of_lists))

    def paths(self):
        paths = self.load()['paths']
        results = []
        for path, operations in paths.items():
            for method, info in operations.items():
                data = info.copy()
                data.update({'path': path, 'method': method})
                results.append(data)
        return results    
            
parser = SwaggerParser("spec.yaml")

paths = parser.paths()
