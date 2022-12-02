import uuid
from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
# Create your models here.

class HouseDetails(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    house_name = models.CharField(max_length=128)
    area = models.CharField(max_length=128)
    qr_code = models.ImageField(upload_to="qr_code", blank=True)

    class Meta:
        db_table = 'house'
        verbose_name = ('house')
        verbose_name_plural = ('house')

    def _str_(self):
        return f"{self.id} {self.house_name}"

    def save(self, *args, **kwargs):
        # qrcode_img = qrcode.make(self.id)
        # canvas = Image.new('RGB', (290, 290), 'white')
        # draw = ImageDraw.Draw(canvas)
        # canvas.paste(qrcode_img)
        # fname = f'qr_code-(self.id).png'
        # buffer = BytesIO()
        # canvas.save(buffer,'PNG')
        # self.qr_code.save(fname, File(buffer),save=False)
        # canvas.close()
        # super().save(*args, **kwargs)

        qr = qrcode.QRCode(version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,)
        qr.add_data(self.id)
        qr.make(fit=True)

        img = qr.make_image(fill_color="blue", back_color="white")
        fname = 'qr_code-'+str(self.id)+'.png'
        buffer = BytesIO()
        img.save(buffer,'PNG')
        self.qr_code.save(fname, File(buffer),save=False)
        img.close()
        super().save(*args, **kwargs)