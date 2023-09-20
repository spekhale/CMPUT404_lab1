# https://github.com/spekhale/CMPUT404_lab1/blob/main/test2.py
# https://raw.githubusercontent.com/spekhale/CMPUT404_lab1/main/test2.py?token=GHSAT0AAAAAACH2BZFPKWMGFN3GQMFP5JWWZIKLZ3Q


import requests

print(requests.__version__)

res = requests.get("https://raw.githubusercontent.com/spekhale/CMPUT404_lab1/main/main.py?token=GHSAT0AAAAAACH2BZFOSJI3IHEJB3JE75DQZIKMB2A")

print(res.text)

