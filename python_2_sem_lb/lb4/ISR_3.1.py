class Page:
    author = None
    info = None
    birth = None
    posts = 0

    def getFullInfo(self):
        return self._author + " " + self._info + " " + self._birth


class Post(Page):
    text = None
    like = 0
    dislike = 0
    comments = 0

    def сreatePost(self, text):
        self._posts += 1
        return "Автор:" + self._author + " Текст:" + text

    def getPostInfo(self):
        return "Комментариев:" + str(self._comments)


class Comment(Post):
    like = 0
    dislike = 0

    def createComment(self, author, text):
        self._comments += 1
        return "Комментарий: Автор: " + author + " Текст" + text


class Create(Comment):
    def __init__(self, author, info, birth):
        self.author = author
        self.info = info
        self.birth = birth

    def getPageInfo(self):
        return "Постов:" + str(self._posts)
