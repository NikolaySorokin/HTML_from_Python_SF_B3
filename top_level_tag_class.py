from tag_class import Tag


class TopLevelTag(Tag):
    """
    Конструктор класса в качестве аргументов принимает:
    tag - название тэга
    klass - класс тэга (при выводи изменится на class)
    словарь других атрибутов
    """

    def __init__(self, tag, klass=None, **kwargs):
        self.tag = tag
        self.text = ""
        self.attributes = {}
        self.children = []

        if klass is not None:
            if type(klass) == str:
                self.attributes["class"] = klass
            else:
                self.attributes["class"] = " ".join(klass)

        for attr, value in kwargs.items():
            if "_" in attr:
                attr = attr.replace("_", "-")
            self.attributes[attr] = value

    def __str__(self):
        attrs = []
        for attribute, value in self.attributes.items():
            attrs.append('%s="%s"' % (attribute, value))
        attrs = " ".join(attrs)

        if self.children:
            opening = "<{tag}>\n".format(tag=self.tag) if len(attrs)==0 \
                else "<{tag} {attrs}>\n".format(tag=self.tag, attrs=attrs)
            internal = "%s" % self.text
            if self.text:
                internal = "%s\n" % self.text
            for child in self.children:
                internal += str(child)
            ending = "</%s>\n" % self.tag
            return opening + internal + ending
        else:
            return "<{tag} {attrs}>{text}</{tag}>\n".format(
                tag=self.tag, attrs=attrs, text=self.text)