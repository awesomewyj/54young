import json
from pprint import pprint
from jsonpath import jsonpath
# import jsonpath as jsonpath
import requests
from requests import Session, Response

proxies = {
    "http": "http://127.0.0.1:8998",
    "https": "http://127.0.0.1:8998"
}

url_get = "https://httpbin.testing-studio.com/get"

def test_requests():
    r = requests.get("https://home.testing-studio.com/categories.json")
    pprint(r)
    print(r.json())
    assert r.status_code == 200


def test_get():
    r = requests.get("https://httpbin.testing-studio.com/get",\
                     params={
                         "a":1,
                         "b":2,
                         "c":'ccccc'
                     },
                     # proxies=proxies,
                     # verify=False
                     )

    print(r.json())
    assert r.status_code == 200


def test_post():
    r = requests.post("https://httpbin.testing-studio.com/post",\
                     params={
                         "a":1,
                         "b":2,
                         "c":'ccccc'
                     },
                      data={
                          "a": 3,
                          "b": 4,
                          "c": 'dddd'
                      },
    headers={"h": "hearders_demo"},
                      proxies=proxies,
                      verify=False
                      )

    print(r.json())
    assert r.status_code == 200
    assert r.json()["headers"]["H"] == "hearders_demo"


def test_upload():
    # todo: upload fix

    r = requests.post(
        "https://httpbin.testing-studio.com/post",
        files={"file": open("__init__.py", 'rb')},
        proxies=proxies,
        verify=False
    )
    print(r.json())
    assert r.status_code == 200


def test_session():
    s = Session()
    s.proxies = proxies
    s.verify = False
    r =s.get("https://httpbin.testing-studio.com/get",\
                     params={
                         "a":1,
                         "b":2,
                         "c":'ccccc'
                     },headers={"headers":"aasd"})
    print(r.text)
    r.status_code == 200


def test_get_hook():
    def modify_response(r: Response, *args, **kwargs):
        r.decode_content = "demo content"
        # r.content = "OK HOOK SUCCESS"
        # r.demo = "demo"
        # rn=Response()

        return r

    r = requests.get(
        "https://httpbin.testing-studio.com/get",
        params={
            "a": 1,
            "b": 2,
            "c": "cccc"
        },
        hooks={"response": [modify_response]}
    )

    print(r.json())
    # print(r.decode_content)
    # r.text
    assert r.decode_content == "demo content"
    # print(r.demo)
    assert r.status_code == 200

def test_jsonpath():
  r = requests.get("https://home.testing-studio.com/categories.json")
  # print(json.dumps(r.json(), indent=2))
  # print(json.dumps(json.loads(r.text), indent=2,ensure_ascii=False))
  assert r.status_code == 200

  for item in r.json()["category_list"]["categories"]:
      if item["name"] == "开源项目":
        break

  # print(item)
  assert jsonpath(r.json(), "$..categories[?(@.name=='开源项目')")[0]['description'] == '开源项目交流与维护'
  assert item["description"]  == "开源项目交流与维护"

