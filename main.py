from pathlib import Path
from PIL import Image
Image.MAX_IMAGE_PIXELS = None






def convert_to_webp(source):
   
    destination = source.with_suffix(".webp")
    image = Image.open(source)  
    image.save(destination, format="webp")  
    return destination


def get_all_files_in_dir(path):
    return [f for f in path.glob("*") if f.is_file()]


def filter_images(files):
    return [f for f in files if f.suffix in [".jpg", ".png"]]

def main():
    curr_dir = Path(__file__).parent
    all_files = get_all_files_in_dir(curr_dir)
    images = filter_images(all_files)
    print(images, "images")
    for image in images:
        try:
            convert_to_webp(image)  
        except Exception as e:
            print(image, "image path that caused error")
            print(e, "error")
            raise e



if __name__ == "__main__":
    main()
