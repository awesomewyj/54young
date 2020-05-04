import json

import yaml
from jsonpath import jsonpath


class BaseApi:
    def format(self, r):
        # print(json.dump(r.json(), indent=2))
        print(json.dumps(json.loads(r.text), indent=2,ensure_ascii=False))


    def jsonpath(self,r,path):

        return jsonpath(r,path)






    #  todo 封装类似数据驱动步骤

    def steps(self, path):
        with open(path) as f:
            steps: list[dict] = yaml.safe_load(f)
            element: WebElement = None
            for step in steps:
                logging.info(steps)
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    action = step["action"]
                    if action == "find":
                        pass
                    elif action == "click":
                        element.click()
                    elif action == "text":
                        element.text
                    elif action == "attribute":
                        element.get_attribute(step["value"])
                    elif action in ["send", "input"]:
                        content: str = step["value"]
                        for key in self._params.keys():
                            content = content.replace("{%s}" % key, self._params[key])
                        element.send_keys(content)