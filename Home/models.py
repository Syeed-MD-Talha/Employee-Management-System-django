from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
# Create your models here.
class Employee(models.Model):
    photo=models.ImageField(upload_to='images')
    full_name=models.CharField(max_length=30)
    email = models.EmailField(max_length=254, unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    date_of_birth=models.DateField()
    
    def __str__(self):
        return self.full_name
    
    
    def save(self, *args, **kwargs):
        # Open the image
        img = Image.open(self.photo)

        # Convert image to RGB if it has an alpha channel (RGBA)
        if img.mode == 'RGBA':
            img = img.convert('RGB')

        # Check if the image is larger than the desired size (e.g., 300x300)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)  # Resize to 300x300 pixels
            img.thumbnail(output_size)  # Resize the image

        # Save the resized image back to the model
        img_io = BytesIO()
        img.save(img_io, format='JPEG', quality=85)  # Save as JPEG with correct format 'JPEG'
        img_content = ContentFile(img_io.getvalue(), self.photo.name)
        self.photo.save(self.photo.name, img_content, save=False)

        # Save the rest of the model as normal
        super().save(*args, **kwargs)






    