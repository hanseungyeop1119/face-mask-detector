import face_recognition
from PIL import Image, ImageDraw
import glob
import os
from PIL import Image

face_image_path = '다운로드.jpg'
mask_image_path = 'data/mask.png'

def combineImage(full_width,full_height,image_key,image_list,index):
    canvas = Image.new('RGB', (full_width, full_height), 'white')
    output_height = 0

for im in image_list:
    width, height = im.size
    canvas.paste(im, (0, output_height))
    output_height += height

face_image_np = face_recognition.load_image_file(face_image_path)
face_locations = face_recognition.face_locations(face_image_np)

face_image = Image.fromarray(face_image_np)
draw = ImageDraw.Draw(face_image)

for face_location in face_locations:
    top = face_location[0]
    right = face_location[1]
    bottom = face_location[2]
    left = face_location[3]
    draw.rectangle(((left, top), (right, bottom)), outline=(255, 255, 0), width=2)

    mask_image = Image.open(mask_image_path)
    mask_width = right - left
    mask_height = bottom - top
    mask_image = mask_image.resize((mask_width, int(mask_height * 0.8)))

    face_image.paste(mask_image, (left+15, int(top * 1.49)), mask_image)

    face_image_np = face_recognition.load_image_file(face_image_path)
face_locations = face_recognition.face_locations(face_image_np)
face_landmarks = face_recognition.face_landmarks(face_image_np, face_locations)

face_landmarks_image = Image.fromarray(face_image_np)
draw = ImageDraw.Draw(face_landmarks_image)

for face_landmark in face_landmarks:
    for feature_name, points in face_landmark.items():
        print(feature_name, points)
        for point in points:
            draw.point(point)

face_landmarks_image.show()

face_image.show()
