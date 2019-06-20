class Page:
    _author = None
    _info = None
    _birth = None
    _posts = 0

    @property
    def posts(self):
        return self._posts

    @posts.setter
    def posts(self, value):
        self._posts = value

    @property
    def author(self):
        return self._info

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, value):
        self._info = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    def getFullInfo(self):
        return self._author + " " + self._info + " " + self._birth


class Post(Page):
    _text = None
    _like = 0
    _dislike = 0
    _comments = 0

    @property
    def author(self):
        return self._info

    @author.setter
    def author(self, value):
        self._author = value

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value

    @property
    def like(self):
        return self._like

    @like.setter
    def like(self, value):
        self._like = value

    @property
    def dislike(self):
        return self._dislike

    @dislike.setter
    def dislike(self, value):
        self._dislike = value

    @property
    def comments(self):
        return self._comments

    @comments.setter
    def comments(self, value):
        self._comments = value

    def сreatePost(self, text):
        self._posts += 1
        return "Автор:" + self._author + " Текст:" + text

    def getPostInfo(self):
        return "Комментариев:" + str(self._comments)


class Comment(Post):
    _like = 0
    _dislike = 0

    def createComment(self, author, text):
        self._comments += 1
        return "Комментарий: Автор: " + author + " Текст" + text


class Create(Comment):
    def __init__(self, author, info, birth):
        self._author = author
        self._info = info
        self._birth = birth

    def getPageInfo(self):
        return "Постов:" + str(self._posts)


ivan = Create("Ivan", "Programmer", "19.12.1999")
grage = Create("Grage", "Programmer", "19.12.1999")
print(ivan.getFullInfo())
print(grage.getFullInfo())
print(grage.сreatePost("Я программитс, ищу работу в компании, опыт работы в Googlr 5 лет"))
print(grage.getPostInfo())
print(grage.createComment("Иван", "похожая ситуация"))
print(grage.getPostInfo())
print(grage.getPageInfo())
print(ivan.getPageInfo())

