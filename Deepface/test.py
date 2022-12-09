from deepface import DeepFace

result = DeepFace.verify(img1_path = "img1.jpg", img2_path = "img2.jpg")

print(result)

obj = DeepFace.analyze(img_path = "img3.jpg", 
        actions = ['age', 'gender', 'race', 'emotion']
)

print(obj)

obj2 = DeepFace.analyze(img_path = "img5.jpg", 
        actions = ['age', 'gender', 'race', 'emotion']
)

print(obj2)