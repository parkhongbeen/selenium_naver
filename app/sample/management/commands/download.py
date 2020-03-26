import mimetypes
import os
import magic
from django.core.files.temp import NamedTemporaryFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.management import BaseCommand
import requests
from sample.models import SampleImageModel


class Commend(BaseCommand):
    def handle(self, *args, **options):
        url = 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.ytimg.com%2Fvi%2FzX0ovzu6Ujc%2Fmaxresdefault.jpg&imgrefurl=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DzX0ovzu6Ujc&tbnid=WiDFxaHJimi1RM&vet=12ahUKEwjB8pi06rfoAhXtxIsBHdwKC68QMygBegUIARDkAQ..i&docid=mJVGNZinNcByxM&w=1280&h=720&q=%ED%8E%91%ED%8B%B0%EB%AA%A8&ved=2ahUKEwjB8pi06rfoAhXtxIsBHdwKC68QMygBegUIARDkAQ'
        basename = os.path.basename(url)

        response = requests.get(url)
        binary_data = response.content

        mime_type = magic.from_buffer(binary_data, mime=True)

        ext = mimetypes.quess_extension(mime_type)

        file = SimpleUploadedFile(basename, binary_data)
        instance = SampleImageModel.objects.create(image=file)
