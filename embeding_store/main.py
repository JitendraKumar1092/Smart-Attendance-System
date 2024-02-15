import face_recognition
himanshu_image = face_recognition.load_image_file("embeding_store/faces/himanshu.jpeg")
himanshu_face_encoding = face_recognition.face_encodings(himanshu_image)[0]

#2 Manu
manu_image = face_recognition.load_image_file("embeding_store/faces/manu.jpeg")
manu_face_encoding = face_recognition.face_encodings(manu_image)[0]


#3 chhari 
chhari_image = face_recognition.load_image_file("embeding_store/faces/chhari.jpeg")
chhari_face_encoding = face_recognition.face_encodings(chhari_image)[0]

#4 jitendra
jitendra_image = face_recognition.load_image_file("embeding_store/faces/jitendra.jpeg")
jitendra_face_encoding = face_recognition.face_encodings(jitendra_image)[0]

#5 hrishi
hrishi_image = face_recognition.load_image_file("embeding_store/faces/hrishi.jpeg")
hrishi_face_encoding = face_recognition.face_encodings(hrishi_image)[0]

# write down a list of known face encodings and their names
known_face_encoding = [
    himanshu_face_encoding,
    manu_face_encoding,
    chhari_face_encoding,
    jitendra_face_encoding,
    hrishi_face_encoding
]
print(known_face_encoding)
# write down a list of known face names 
known_face_names = [
    "Himanshu",
    "Manu",
    "Chhari",
    "Jitendra",
    "Hrishi"
]