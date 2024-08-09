import requests
import gradio as gr
import re
# 定义函数
def fetch_mars_rover_photos(api_key, sol=1000, page=1, camera=None):
    base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    params = {
        'api_key': api_key,
        'sol': sol,
        'page': page
    }
    if camera:
        params['camera'] = camera
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# 解析文本输入函数
def parse_input(text):
    sol = int(re.search(r"\d+", text).group())  
    camera = re.search(r"(FHAZ|RHAZ|MAST|CHEMCAM|MAHLI|MARDI|NAVCAM|PANCAM|MINITES)", text, re.IGNORECASE)
    if camera:
        camera = camera.group().upper()
    return sol, 1, camera  

# 设置Gradio界面的函数
def mars_rover_photo_interface(text):
    sol, page, camera = parse_input(text)
    api_key = "qhGD6HG37RgzRWE23vyAf84n6diSL5qC7hzjc865"
    data = fetch_mars_rover_photos(api_key, sol=sol, page=page, camera=camera)
    if data:
        photos = data.get('photos', [])
        photo_urls = [photo['img_src'] for photo in photos]
        return photo_urls
    else:
        return []

# 创建Gradio界面
iface = gr.Interface(fn=mars_rover_photo_interface, 
                     inputs="text", 
                     outputs=gr.Gallery(label="Mars Rover Photos"),
                     title="获取火星车照片",
                     description="输入例如：'我想获取NASA火星车在火星上第1000天的照片'")
iface.launch()

