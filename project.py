import qrcode
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.colormasks import ImageColorMask


qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data("AY DATA")

#qr.make(fit=True)
qr.make_image(fill_color="black", back_color="white")


bg = Image.open("./download.jpeg")
bg = bg.resize((qr.modules_count * qr.box_size, qr.modules_count * qr.box_size))


qr_img = qr.make_image(
    image_factory=StyledPilImage, 
    color_mask=ImageColorMask(back_color=(25, 25, 25), color_mask_image=bg), fill_color="black"
)


qr_img.save("qr_code_with_bg.png")