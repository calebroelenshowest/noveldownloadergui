from ebooklib import epub
from json import dump, load


class Novel(epub.EpubBook):

    def __init__(self, title, author, chapters, image, location):
        super().__init__()
        self.set_title(title)
        self.add_author(author)
        self.set_language("en")
        self.__chapters = chapters
        self.__add_chapter_list()
        self.__novel_chapters = []
        self.__style()
        self.__toc()
        self.__spine()
        self.__location = location
        self.__image_loc = image
        self.__image()

    def __add_chapter(self, title, text, identifier):
        chapter = epub.EpubHtml()
        chapter.title = title
        chapter.content = text
        chapter.id = identifier
        chapter.file_name = f"chapter_{identifier}.xhtml"
        self.__novel_chapters.append(chapter)
        self.add_item(chapter)

    def __add_chapter_list(self):
        for index, chapter in enumerate(self.__chapters):
            self.__add_chapter(chapter["title"], chapter["content"], index+1)

    def __style(self):
        style = 'body { font-family: Times, Times New Roman, serif; }'

        nav_css = epub.EpubItem(uid="style_nav",
                                file_name="style/nav.css",
                                media_type="text/css",
                                content=style)
        self.add_item(nav_css)

    def __spine(self):
        self.spine = self.__novel_chapters

    def __toc(self):
        self.toc = self.__novel_chapters

    def __image(self):
        self.set_cover("cover.jpg", open(self.__image_loc, 'rb').read())

    def save(self):
        self.add_item(epub.EpubNcx())
        self.add_item(epub.EpubNav())
        epub.write_epub(self.__location, self)
