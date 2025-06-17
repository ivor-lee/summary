import requests
import json
from PIL import Image
from io import BytesIO

url = 'https://api-inference.modelscope.cn/v1/images/generations'

payload = {
    'model': 'MusePublic/489_ckpt_FLUX_1',#ModelScope Model-Id,required
    'prompt': 'A golden cat'# required
}
headers = {
    'Authorization': 'Bearer bfbd15ff-ce1b-42a1-a779-f9def8f13c28',
    'Content-Type': 'application/json'
}

response = requests.post(url, data=json.dumps(payload, ensure_ascii=False).encode('utf-8'), headers=headers)

response_data = response.json()
image = Image.open(BytesIO(requests.get(response_data['images'][0]['url']).content))
image.save('result_image.jpg')