import requests

def get_demo():
    url = "https://httpbin.org/get"
    resp = requests.get(url, timeout=10)
    print(f"状态码: {resp.status_code}")
    print(f"返回数据: {resp.json()}")

if __name__ == "__main__":
    get_demo()
