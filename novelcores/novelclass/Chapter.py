class Chapter:

    def __init__(self, title: str, text: list, identifier: int, text_html=True):
        self.__title = title
        self.__text = text
        self.__identifier = identifier
        self.__html = ""
        self.__is_text_html = text_html

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, value: str):
        if isinstance(value, str):
            if value == "":
                raise ValueError("Title cannot be empty")
            else:
                self.__title = value
        else:
            raise TypeError("Title must be type string.")

    @property
    def identifier(self) -> int:
        return self.__identifier

    @identifier.setter
    def identifier(self, value: int):
        if isinstance(value, int):
            if value >= 0:
                self.__identifier = value
            else:
                raise ValueError("Identifier must be bigger than or equal to 0")
        else:
            raise TypeError("Identifier must be an int.")

    def generate_html(self) -> str:
        self.__html = f"<h1>{self.__title}</h1>"
        if self.__is_text_html:
            self.__html += self.__text
            return self.__html
        else:
            for text in self.__text:
                self.__html += f"<p>{text}</p>"
            return self.__html

    @property
    def html(self) -> str:
        return self.__html
