#!/usr/bin/env python3
import yaml

class SwaggerParser:
    def __init__(self, file_path):
        self.data = self.load(file_path)
       
    def load(self, file_path):
        with open(file_path, 'r') as stream:
                return yaml.load(stream)

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

