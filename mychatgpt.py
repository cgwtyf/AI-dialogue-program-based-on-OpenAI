import requests
import time
# import json

url = "https://openai.api2d.net/v1/chat/completions"

headers = {
  'Content-Type': 'application/json',
  'Authorization': '你自己的秘钥' 
}

data = {
  "model": "gpt-3.5-turbo",
  "messages": [{"role": "user", "content": ""}],
#   "stream": True,
}

while True:
    inp=input("\n用户：\n")
    if input != "exit":  
      data["messages"][0]["content"]=inp
      response = requests.post(url, headers=headers, json=data)
      # print(response.json())
      print("\nOpenAI：")
      # print(response)
      print(response.json()['choices'][0]['message']['content'])
      # for i in response.json()['choices'][0]['message']['content']:
      #   print(i,end="",flush=True)
      #   # time.sleep(0.01)
      #   if i==" ":
      #      continue
      #   else:
      #       time.sleep(0.01)
      # print()
    else:
       break