#!/usr/bin/env python3
import yaml
import itertools

class SwaggerParser:
    def __init__(self, file_path):
        self.data = self.load(file_path)
       
    def load(self, file_path):
        with open(file_path, 'r') as stream:
                return yaml.load(stream)

    def __flatten(self, list_of_lists):
        return list(itertools.chain(*list_of_lists))

    def info(self): 
        return self.data['info']
    
    def paths(self):
        paths = self.data['paths']
        results = []
        for path, operations in paths.items():
            for method, info in operations.items():
                data = info.copy()
                data.update({'path': path, 'method': method})
                results.append(data)
        return results    

    def operations(self):
        return self.paths()

