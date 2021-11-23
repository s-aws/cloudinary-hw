from django.forms import ModelForm

from cloudinary.forms import CloudinaryJsFileField, CloudinaryUnsignedJsFileField, CloudinaryFileField
# Next two lines are only used for generating the upload preset sample name
from cloudinary.compat import to_bytes
import cloudinary, hashlib

from .models import Photo

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
    
        ## modified
    image = CloudinaryFileField( # shamelessly stolen from https://cloudinary.com/documentation/django_image_and_video_upload#server_side_upload
        options = dict(
            tags='esayche_tag', # tag
            crop='limit', width=500, height=500# no more squish even though i liked squish
        ))
        ## end modification

class PhotoDirectForm(PhotoForm):
    image = CloudinaryJsFileField()

class PhotoUnsignedDirectForm(PhotoForm):
    upload_preset_name = "sample_" + hashlib.sha1(to_bytes(cloudinary.config().api_key + cloudinary.config().api_secret)).hexdigest()[0:10]
    image = CloudinaryUnsignedJsFileField(upload_preset_name)

