import os
from PIL import Image

def convert_and_rotate_images(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".tiff"):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, f"{os.path.splitext(filename)[0]}.png")

            # Read image, rotate 90 degrees, and save as PNG
            image = Image.open(input_path)
            rotated_image = image.rotate(-90, expand=True)
            rotated_image.save(output_path, format="PNG")


if __name__ == "__main__":
    input_dir = "../data/raw/dorothy-safranski"
    output_dir = "../data/processed"

    convert_and_rotate_images(input_dir=input_dir, output_dir=output_dir)