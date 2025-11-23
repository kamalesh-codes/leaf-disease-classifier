import torch
from model import Model
from fastapi import FastAPI,UploadFile,File
import io
import numpy as np
from PIL import Image
from torchvision import transforms
from config import *

device="cuda" if torch.cuda.is_available() else "cpu"

class_decode = {0:"healthy",1:"angular_leafspot",
                2:"Calciumdeficiency",3:"Leaf_scorch",4:"leaf_spot"}

transform = transforms.Compose([transforms.ToTensor(),
                                transforms.Normalize(
                                std=[75.640,92.417, 91.233, ],
                                mean=[  20.912,2.458, -22.453])])

model=Model(num_class=5,path_to_pretrained_weight=inference_model_path,device=torch.device(device))
model.eval()
def preprocess_image(img:Image)->torch.Tensor:
    img = img.resize(size=(224,224),resample=Image.Resampling.BICUBIC)
    img = np.array(img,dtype=np.uint8)
    img = transform(img).unsqueeze(dim=0)
    return img

app=FastAPI()


@app.post("/predict")
async def predict(file:UploadFile=File(...))->dict:

    content = await file.read()
    img = Image.open(io.BytesIO(content)).convert("RGB")
    with torch.no_grad():
        output = model(preprocess_image(img))
    prob = output.squeeze().softmax(dim=0)
    class_idx = prob.argmax().item()
    pred_class = class_decode[class_idx]
    class_prob = {key:value for key,value in zip(class_decode.values(),list(map(lambda x:round(float(x)*100,3),prob)))}
    return {"predicted_class":pred_class,"pred_prob":round(prob.max().item()*100,3),"class_prob":class_prob}