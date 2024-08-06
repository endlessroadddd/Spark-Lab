import requests

# 创建包含API参数的字典
api_params = {
    'city': 'New York',
    'apikey': 'your_api_key_here'
}

# 发送GET请求，并使用字典传递参数
response = requests.get('http://api.weatherapi.com/v1/current.json', params=api_params)

# 打印API返回的数据
print(response.json())
