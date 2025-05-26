# call + ф-ция filter
class ImageFileAcceptor:

    def __init__(self, extensions):
        self.extensions = extensions


    def __call__(self, filename):
        ext = filename.split('.')[1]
        return ext in extensions


extensions = ('jpg', 'bmp', 'jpeg', 'png')

acceptor = ImageFileAcceptor(extensions)

filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg", "eq_1.png", "eq_2.png",
             "my.html", "data.shtml"]

res1 = filter(acceptor, filenames)
print(*res1)

# def my_filter(filename):
#     ext = filename.split('.')[1]
#     return ext in extensions
#
#
# res2 = filter(my_filter, filenames)
#
# print(*res2)
