
#For model_building file
dataset_path="Path to the dataset in .npz file with 'image' and 'label' array"
model_saving_path = "Path to save the model"
metrics_saving_path = "Path to save the metrics data"
pretrained_model_path ="Path to pretrained model in .pth"

#For page_3 in streamlit.app 
# endpoint_url="http://localhost:8000/predict" is default you can change this in that file,
# changing this in this file doesnt affect the variable in that file

#For inferencing pretrained model in main.py
inference_model_path = "resnet34-inference.pth"
