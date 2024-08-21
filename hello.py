from PIL import Image
import cv2
import os

paths = "images"

mean_width = 0
mean_height = 0
num = len(os.listdir(paths))

for file in os.listdir(paths):
    img = Image.open(os.path.join(paths, file))
    width, height = img.size
    mean_height += height
    mean_width += width

mean_width //= num
mean_height //= num

for file in os.listdir(paths):
    if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".avif"):
        image = Image.open(os.path.join(paths, file))
        image_rsized = image.resize((mean_width, mean_height), image.ANTIALIAS)
        image_rsized.save(file, "JPEG", quality=95)


def vid_gen():
    video_name = "hi_there.avi"
    images = []
    for file in os.listdir(paths):
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".avif"):
            images.append(file)
    frame = cv2.imread(os.path.join(paths, images[0]))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, 0, 1, (width, height))
    for image in images:
        video.write(cv2.imread(os.path.join(paths, image)))
    cv2.destroyAllWindows()
    video.release()