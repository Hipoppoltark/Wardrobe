from main import *
import shutil


class MainCapWidget(QMainWindow):
    def __init__(self, user_id: int):
        self.user_id = user_id
        super().__init__()
        uic.loadUi('main.ui', self)
        self.main = MainWidget(self)

        self.setWindowTitle('My Wardrobe')

        self.pixmap = QPixmap("img/wardrobe.png")
        self.pixmap = self.pixmap.scaled(40, 40)
        # Если картинки нет, то QPixmap будет пустым,
        # а исключения не будет
        self.image = QLabel(self)
        self.image.move(20, 10)
        self.image.resize(40, 40)
        # Отображаем содержимое QPixmap в объекте QLabel
        self.image.setPixmap(self.pixmap)

        self.pixmap_user = QPixmap("img/user.png")
        self.pixmap_user = self.pixmap_user.scaled(31, 31)
        # Если картинки нет, то QPixmap будет пустым,
        # а исключения не будет
        # Отображаем содержимое QPixmap в объекте QLabel
        self.label_profile_img.setPixmap(self.pixmap_user)


        self.btn_clothes.setStyleSheet(ANIMATION_BTN)
        self.btn_profile.setStyleSheet(ANIMATION_BTN)

        self.btn_exit.clicked.connect(self.exit_from_programm)

    def exit_from_programm(self):
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), PATH_FOLDER_PHOTO)
        shutil.rmtree(path)
        path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'user_id.txt')
        os.remove(path)
        self.close()