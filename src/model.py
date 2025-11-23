import torch.nn as nn
from torchvision import models
import torch

"""
Note, 
 This model code is for loading the pretrained parameters in main file for inference
 this model that is trained on strawberry-plant-disease file.
 for clarrification take a look at the model code used in that file
 
 if you use this same code for training and inference you will get unmatched key error"""

class Model(nn.Module):
    def __init__(self,num_class,device,path_to_pretrained_weight=None):
        super().__init__()
        self.resnet = models.resnet34(weights=None).to(torch.float32)
        self.resnet.fc = nn.Sequential(
                        nn.Linear(in_features=self.resnet.fc.in_features,out_features=1024),
                        nn.Dropout(p=0.5),
                        nn.Linear(in_features=1024,out_features=num_class)
        )
        if path_to_pretrained_weight:
            pretrained_weight = torch.load(path_to_pretrained_weight,map_location=torch.device(device))
            print(f"Model is loaded\n{self.load_state_dict(pretrained_weight)}")

    def forward(self,x):
        return self.resnet(x)