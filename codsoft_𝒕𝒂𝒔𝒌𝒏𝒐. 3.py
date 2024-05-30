import torch
import torchvision.models as models
import torchvision.transforms as transforms
from PIL import Image

# Load pre-trained VGG16 (or any other CNN) for feature extraction
vgg16 = models.vgg16(pretrained=True)
vgg16.eval()

# Preprocess the image
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def extract_image_features(image_path):
    image = Image.open(image_path)
    image = transform(image).unsqueeze(0)
    features = vgg16(image)
    return features

# Initialize RNN (LSTM or GRU) for caption generation
# Train the combined model on your dataset

# During inference:
image_features = extract_image_features('Snapchat-3180447.jpg')
# Generate captions using the trained RNN

# Remember to replace 'your_image.jpg' with your actual image path.

