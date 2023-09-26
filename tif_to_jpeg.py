import os
from PIL import Image

def convert_tif_and_bmp_to_jpeg(src_folder):
    for filename in os.listdir(src_folder):
        if filename.endswith(".tif") or filename.endswith(".bmp"):
            base_name = os.path.splitext(filename)[0]
            outfile = os.path.join(src_folder, base_name + ".jpeg")
            
            try:
                # Open the image file
                image_path = os.path.join(src_folder, filename)
                im = Image.open(image_path)
                
                # Convert to RGB format
                out = im.convert("RGB")
                
                # Save as JPEG with quality 90
                out.save(outfile, "JPEG", quality=90)
                
                print(f"Converted: {filename} -> {base_name}.jpeg")
                
            except Exception as e:
                print(f"Error converting {filename}: {str(e)}")

if __name__ == "__main__":
    src_folder = "tif_File_Directory_File_Path"
    convert_tif_and_bmp_to_jpeg(src_folder)