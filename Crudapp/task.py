from celery import Celery

app = Celery('image_tasks', broker='redis://localhost:6379/0')
# app.autodiscover_tasks(['path.to.your.tasks.module'], force=True)



from celery import Celery
import base64
import requests
from PIL import Image
from io import BytesIO

from celery import Celery
from celery import shared_task
app = Celery('image_tasks', broker='redis://localhost:6379/0')

@shared_task
def generate_image2(prompt, img_path):
    print("hello guys")
    def get_payload_dimensions():
        x, y = 512, 512
        tempx, tempy = 1024, 1024
        if x // y >= 2:
            tempx = 1536
            tempy = 640
        elif y // x >= 2:
            tempx = 640
            tempy = 1536
        return tempx, tempy

    def ttmgenerate_image(body):
        url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": "Bearer sk-aeH6MoVVaFgpEmUUPfxQTsSlyD5LIwzxTMbPpxYYAU6bGjvC",
        }
        response = requests.post(url, headers=headers, json=body)
        if response.status_code != 200:
            raise Exception("Non-200 response: " + response.text)
        return response.json()

    try:
        tempx, tempy = get_payload_dimensions()
        image_generation_body = {
            "steps": 40,
            "width": tempx,
            "height": tempy,
            "seed": 0,
            "cfg_scale": 7,
            "samples": 1,
            "style_preset": "pixel-art",
            "text_prompts": [
                {
                    "text": f"{prompt}",
                    "weight": 1
                },
                {
                    "text": "blurry, bad, extra elements, clutter",
                    "weight": -1
                }
            ],
        }
        generated_data = ttmgenerate_image(image_generation_body)
        if generated_data and "artifacts" in generated_data:
            for image in generated_data["artifacts"]:
                decoded_image = base64.b64decode(image["base64"])
                print("ki")
                img = Image.open(BytesIO(decoded_image))
                img.save(img_path)
        else:
            print("Generated data is invalid or does not contain artifacts.")
    except Exception as e:
        print(f"generate_image function Imagegen.py {e}")