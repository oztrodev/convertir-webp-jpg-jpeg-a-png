from PIL import Image
import imageio.v3 as iio
import os
import shutil

def convert_to_png(input_path, output_path):
    # Check the extension of the input file
    ext = os.path.splitext(input_path)[1].lower()
    
    if ext in ['.jpg', '.jpeg', '.webp']:
        # Open the image file with Pillow
        image = Image.open(input_path)
    elif ext == '.avif':
        # Open AVIF image using imageio
        image = iio.imread(input_path)
        image = Image.fromarray(image)
    else:
        raise ValueError(f"Unsupported file format: {ext}")
    
    # Convert the image to PNG format
    output_file = os.path.splitext(output_path)[0] + '.png'
    image.save(output_file, 'PNG')
    print(f"Converted {input_path} to {output_file}")

def process_images(all_folder, png_folder):
    # Ensure the output and ok folders exist
    ok_folder = os.path.join(all_folder, 'ok')
    os.makedirs(png_folder, exist_ok=True)
    os.makedirs(ok_folder, exist_ok=True)

    # Iterate over all files in the all folder
    for filename in os.listdir(all_folder):
        input_path = os.path.join(all_folder, filename)
        if os.path.isfile(input_path):
            try:
                output_path = os.path.join(png_folder, filename)
                convert_to_png(input_path, output_path)
                
                # Move the original file to the ok folder
                shutil.move(input_path, ok_folder)
            except ValueError as e:
                print(e)

if __name__ == "__main__":
    all_folder = "all"  # Reemplaza con la ruta a tu carpeta 'all'
    png_folder = "png"  # Reemplaza con la ruta a tu carpeta 'png'
    process_images(all_folder, png_folder)
