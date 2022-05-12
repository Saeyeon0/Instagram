from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os

for sy in os.listdir('.'):
    if sy.endswith('.jpg'):
        img = Image.open(sy)
        fn, flext = os.path.splitext(sy)

        rs = img.convert('L')
        rs1 = rs.filter(ImageFilter.DETAIL)
        rs2 = rs1.resize((1080, 1080))
        width, height = rs2.size

        draw = ImageDraw.Draw(rs2)
        text = "SAEYEON_0"
        title = "BLACK"
        font = ImageFont.truetype("arial.ttf", 80)
        textwidth, textheight = draw.textsize(text, font)

        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin

        draw.text((x, y), text, title, font=font)

        rs2.save('syeon/{}{}'.format(fn, flext))