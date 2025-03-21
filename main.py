pip install pillow

from PIL import Image, ImageDraw, ImageFont


def create_meme(image_path, top_text, bottom_text, output_path="meme_output.jpg"):
    # Resmi aç
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)

    # Font yükle (Varsayılan font, eğer yoksa alternatife geç)
    try:
        font = ImageFont.truetype("impact.ttf", size=int(img.width / 10))
    except:
        font = ImageFont.load_default()

    # Metni çizme fonksiyonu
    def draw_text(draw, text, position):
        text_width, text_height = draw.textsize(text, font=font)
        x = (img.width - text_width) / 2
        y = position
        draw.text((x, y), text, font=font, fill="white", stroke_width=2, stroke_fill="black")

    # Üst ve alt metni ekleyelim
    draw_text(draw, top_text.upper(), 10)
    draw_text(draw, bottom_text.upper(), img.height - 60)

    # Görüntüyü kaydet
    img.save(output_path)
    print(f"✅ Meme oluşturuldu: {output_path}")
    img.show()  # Otomatik açar


# Kullanıcıdan giriş al
image_path = input("Meme için resim dosya adını gir: ")
top_text = input("Üst metni gir: ")
bottom_text = input("Alt metni gir: ")

# Meme oluştur
create_meme(image_path, top_text, bottom_text)
