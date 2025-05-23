from PIL import Image
import numpy as np

ASCII_CHARS = "@#%BWM*oahkbdpqwmZO0QLCJUYXzcvunxrjft-:. "

def image_to_ascii(image_path, output_txt="ascii_image.txt", width=500):
    image = Image.open(image_path).convert("L")  # Convertir en niveaux de gris

    # Ajuster la taille pour moins de pixels par caractère
    aspect_ratio = image.height / image.width
    new_height = int(width * aspect_ratio)  # Facteur de correction vertical
    image = image.resize((width, new_height))

    pixels = np.array(image)

    # Conversion en ASCII
    ascii_art = "\n".join(
        "".join(ASCII_CHARS[min(pixel // (256 // len(ASCII_CHARS)), len(ASCII_CHARS) - 1)] for pixel in row)
        for row in pixels
    )

    # Sauvegarde
    with open(output_txt, "w") as f:
        f.write(ascii_art)

    print(f"✅ ASCII Art généré et stocké dans {output_txt} !")

# Test avec une largeur plus petite
image_to_ascii("findley.jpg", "ascii.txt")
