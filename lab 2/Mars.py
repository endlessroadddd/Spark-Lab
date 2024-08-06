import requests
import gradio as gr

# 定义函数
def fetch_mars_rover_photos(api_key, sol=1000, page=1, camera=None):
    base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    # 设置请求参数
    params = {
        'api_key': api_key,
        'sol': sol,
        'page': page
    }
    if camera:  # 提供相机类型，添加到参数中
        params['camera'] = camera #打印参数
    
    # 请求NASA API
    response = requests.get(base_url, params=params)
    
    # 检查响应状态码并返回相应的JSON数据或None
    if response.status_code == 200:
        return response.json()
    else:
        return None

# 设置Gradio界面的函数
def mars_rover_photo_interface(sol, page, camera):
    api_key = "qhGD6HG37RgzRWE23vyAf84n6diSL5qC7hzjc865"  #自己的API密钥
    data = fetch_mars_rover_photos(api_key, sol=sol, page=page, camera=camera)
    if data:
        photos = data.get('photos', [])                  #提取照片列表
        photo_urls = [photo['img_src'] for photo in photos] #提取照片url
        return photo_urls
    else:
        return []

# 创建Gradio输入组件，前端展示
sol_input = gr.Number(label="Martian Sol", value=1000) ## 火星太阳日
page_input = gr.Number(label="Page", value=1)          ##页码
camera_input = gr.Dropdown(choices=['FHAZ', 'RHAZ', 'MAST', 'CHEMCAM', 'MAHLI', 'MARDI', 'NAVCAM', 'PANCAM', 'MINITES'], label="Camera")

# 创建Gradio界面
gr.Interface(fn=mars_rover_photo_interface, 
             inputs=[sol_input, page_input, camera_input], 
             outputs=gr.Gallery(label="Mars Rover Photos")).launch()
