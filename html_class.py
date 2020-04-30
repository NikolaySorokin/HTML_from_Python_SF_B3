from tag_class import Tag


class HTML(Tag):
    """
    Класс в качестве аргументов конструктора принимает путь к файлу для сохранения вывода (переменная output).
    Если не указывать путь, по умолчанию значение переменной - None,
    в данном случае вывод будет выполнен в консоль через print
    Также констриктор принимает словарь атрибутов тега (например lang="ru")
    """
    def __init__(self, output=None, **kwargs):
        self.tag = "html"
        self.text = ""
        self.attributes = {}
        self.children = []
        self.output = output

        for attr, value in kwargs.items():
            if "_" in attr:
                attr = attr.replace("_", "-")
            self.attributes[attr] = value

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.output is not None:
            with open(self.output, "w") as html_file:
                html_file.write(str(self))
        else:
            print(str(self))