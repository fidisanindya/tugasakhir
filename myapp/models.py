from django.db import models
import numpy as np
from tensorflow.keras.preprocessing import image

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class Detection(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    result = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
    
def predict_image(file_path, model):
    img = image.load_img(file_path, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])
    classes = model.predict(images, batch_size=8)
    return classes
