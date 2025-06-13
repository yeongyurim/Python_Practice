class Book :
    def __init__(self, title, author) :
        self.title = title
        self.author = author
    def info(self) :
        print("{0} - 저자 : {1}".format(self.title,self.author))
        
class EBook(Book) :
    def __init__(self, title, author, file_size):
        self.title = title
        self.author = author
        self.file_size = file_size
    
    def info(self) :
        print("{0} - 저자 : {1} (파일 크기: {2:.1f}MB)".format(self.title,self.author,self.file_size))

book1 = Book("어린 왕자", "생텍쥐페리")
ebook1 = EBook("파이썬 기초", "홍길동", 3.5)

book1.info()
ebook1.info()