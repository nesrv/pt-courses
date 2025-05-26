
class ImageFileAcceptor:

    def __init__(self, extensions):
        self.extensions = extensions


    def __call__(self, name):
        ext = name.split('.')[-1]
        return ext in  self.extensions





extensions = ('jpg', 'bmp', 'jpeg', 'doc')
filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg", "eq_1.png", "eq_2.png", "my.html", "data.shtml"]

acceptor = ImageFileAcceptor(extensions)

image_filenames = filter(acceptor, filenames)


print(*image_filenames)
