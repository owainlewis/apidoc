#!/usr/bin/env python3
import yaml

class SwaggerParser:

    def __init__(self, file_path):
        self.spec = self.__load(file_path)

    def __load(self, file_path):
        with open(file_path, 'r') as stream:
                return yaml.load(stream)

    def info(self):
        return self.spec.get('info', {})

    def version(self):
        return self.info().get('version')

    def title(self):
        return self.info().get('title')

    def host(self):
        return self.spec.get('host')

    def basePath(self):
        return self.spec.get('basePath')

    def consumes(self):
        return self.spec.get('consumes')

    def produces(self):
        return self.spec.get('produces')

    def paths(self):
        paths = self.spec.get('paths', {})
        results = []
        for path, operations in paths.items():
            for method, info in operations.items():
                data = info.copy()
                data.update({'path': path, 'method': method})
                results.append(data)
        return results
