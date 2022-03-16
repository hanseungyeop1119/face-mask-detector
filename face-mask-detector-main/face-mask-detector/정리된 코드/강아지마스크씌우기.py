import face_recognition
from PIL import Image, ImageDraw

face_image_path = '../data/dog.png'
mask_image_path = '../data/mask.png'

face_image_np = face_recognition.load_image_file(face_image_path)
face_image = Image.fromarray((face_image_np))

mask_image = Image.open(mask_image_path)
mask_image = mask_image.resize((300, 260))

face_image.paste(mask_image, (160, 140), mask_image)
face_image.show()
