from deepface import DeepFace

def getFaceAnalysis(image_path):
    res = DeepFace.analyze(image_path, actions = ['age', 'gender', 'race', 'emotion'])
    return res

def getSimilarityAnaysis(image1, image2):
    res = DeepFace.verify(image1,image2)
    return res

def getSimimlarFaces(image_path, database):
    res = DeepFace.find(img_path = image_path, db_path = database, enforce_detection=False)
    return res


print(getSimimlarFaces("img1.jpg","C:/Users/zengj/Desktop/Python/Deepface/myDb"))