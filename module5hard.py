class User:

    users = []
    nickname = "None"
    password = "None"
    age = 0


    def __init__(self, nickname="None", password="None", age=0):
        self.nickname =  str(nickname)
        self.password = hash(password)
        self.age = int(age)
        self.users.append(self)

    def __str__(self):
        return self.nickname

    # def __eq__(self, other):
    #     return self.nickname == other.nickname

class Video:

    videos = []
    title = str
    duration = int
    time_now = int
    adult_mode = bool

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = int(time_now)
        self.adult_mode = bool(adult_mode)

    def __str__(self):
        return self.title

    def __eq__(self, other):
        return self.title == other.title



class UrTube:

    users = User.users
    videos = Video.videos
    current_user = User

    def watch_video(self, name_video):
        from time import sleep
        import sys
        name_video = str(name_video)
        for vdo in self.videos:
            if name_video == str(vdo):
                if self.current_user.nickname != "None":
                    if self.current_user.age >= 18 or vdo.adult_mode == False:
                        for time_ in range(vdo.time_now, vdo.duration):
                            sys.stdout.write(str(time_)+" ")
                            sleep(1)
                        print("Конец видео")
                    else:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                else:
                    print("Войдите в аккаунт, чтобы смотреть видео")
            else:
                pass

    def get_videos(self, search_word_):
        search_word = str(search_word_).lower()
        list_videos = []
        for video in self.videos:
            if search_word.lower() in str(video).lower():
                list_videos.append(str(video))
        if len(list_videos) > 0:
            return list_videos


    def add(self, *videos_: Video):
        for video_ in videos_:
            if video_ not in self.videos:
                self.videos.append(video_)
            else:
                pass


    def log_out(self):
        self.current_user = None

    def log_in(self, nickname, password):
        for usr in self.users:
            if usr.password == hash(password):
                self.current_user = usr

    def register(self, nickname_, password_,age_):
        user_in_list = 0
        if len(self.users) > 0:
            for usr in self.users:
                if str(usr) == nickname_:
                    user_in_list = 1
                    print(f"Пользователь {nickname_} уже существует")
            if user_in_list == 0:
                reg_user = User(nickname_, password_, age_)
        else:
            reg_user = User(nickname_, password_, age_)
        self.log_in(nickname=nickname_,password=password_)


if __name__ == "__main__":

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')