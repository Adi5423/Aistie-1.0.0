import os
from google_images_download import google_images_download
from PIL import Image

# Set up Google Images search
prompt = "brown puppy with blue eyes"  # Set the prompt here
arguments = {"keywords": prompt, "format": "jpg", "limit": 50}
response = google_images_download.googleimagesdownload()
paths = response.download(arguments)

# Process images
if len(paths) > 0 and len(paths[0]) > 1:
    images = []
    for path in paths[0][1]:
        try:
            img = Image.open(path)
            img = img.resize((100, 100))  # Resize to 100x100 pixels
            images.append(img)
            if len(images) == 5:
                break
        except Exception as e:
            print(f"Error processing image: {e}")

    if len(images) > 0:
        # Create a new image
        new_img = Image.new('RGB', (500, 500), (255, 255, 255))  # Create a 500x500 white image

        # Place images in a grid
        x, y = 0, 0
        for img in images:
            new_img.paste(img, (x, y))
            x += 100
            if x >= 500:
                x = 0
                y += 100

        # Save the image
        new_img.save(f'generated_image_{prompt}.jpg')
    else:
        print("No images were downloaded for this search filter.")
else:
    print("No images were downloaded for this search filter.")