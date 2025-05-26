# Магический метод __new__. Singleton

TYPE_OS = 1  # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    def __new__(cls, *args, **kwargs):
        obj = DialogWindows() if TYPE_OS == 1 else DialogLinux()
        setattr(obj, 'name', args[0])

        return obj


dlg1 = Dialog("диалог 1")
print(dlg1)
print(dlg1.name)
dlg2 = Dialog("диалог 2")
print(dlg2)
print(dlg2.name)