import json

import requests
import yaml
import json

from jsonpath import jsonpath


class BaseApi:

    params = {}

    @staticmethod
    def yaml_load(path):
        with open(path) as f:
            return yaml.safe_load(f)


    def json_path(self,path,r = None):
        if r is None:
            r = self.r.json()
        return jsonpath(r, path)




    @classmethod
    def format(cls,r):
        cls.r = r
        result = json.dumps(json.loads(r.text),indent=2,ensure_ascii=False)
        print(result)
        return result



    def api_send(self,data: dict):
        raw = yaml.dump(data)
        for k,v in self.params.items():
            raw = raw.replace(f"${{{k}}}",repr(v))
        data = yaml.safe_load(raw)
        result = requests.request(
            method=data['method'],
            url=data['url'],
            params=data['params'],
            json=data.get('json')
        )
        self.format(result)
        return result.json()










