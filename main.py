from tag_class import Tag
"""
Конструктор класса в качестве аргументов принимает:
tag - название тэга
is_single - По-умолчанию False - тэг парный, при установке значения True - тэг одиночный
klass - класс тэга (при выводи изменится на class)
словарь других атрибутов
"""
from top_level_tag_class import TopLevelTag
"""
Конструктор класса в качестве аргументов принимает:
tag - название тэга
klass - класс тэга (при выводи изменится на class)
словарь других атрибутов
"""
from html_class import HTML
"""
Класс в качестве аргументов конструктора принимает путь к файлу для сохранения вывода (переменная output).
Если не указывать путь, по умолчанию значение переменной - None,
в данном случае вывод будет выполнен в консоль через print
Также констриктор принимает словарь атрибутов тега (например lang="ru")
"""


if __name__ == "__main__":
    with HTML(lang="en") as doc:
        with TopLevelTag("head") as head:
            with Tag("title") as title:
                title.text = "hello"
                head += title
            doc += head

        with TopLevelTag("body") as body:
            with Tag("h1", klass=("main-text",)) as h1:
                h1.text = "Test"
                body += h1

            with Tag("div", klass=("container", "container-fluid"), id="lead") as div:
                with Tag("p") as paragraph:
                    paragraph.text = "another test"
                    div += paragraph

                with Tag("img", is_single=True, src="/icon.png") as img:
                    div += img

                body += div

            doc += body

    html_file = open("test.html", "w", encoding="utf-8")
    html_file.write(str(doc))
    html_file.close()