class Tag:
    """
    Конструктор класса в качестве аргументов принимает:
    tag - название тэга
    is_single - По-умолчанию False - тэг парный, при установке значения True - тэг одиночный
    klass - класс тэга (при выводи изменится на class)
    словарь других атрибутов
    """
    def __init__(self, tag, is_single=False, klass=None, **kwargs):
        self.tag = tag
        self.text = ""
        self.attributes = {}
        self.is_single = is_single
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
            opening = "<{tag}>\n".format(tag=self.tag) if len(attrs) == 0 \
                else "<{tag} {attrs}>\n".format(tag=self.tag, attrs=attrs)
            internal = "%s" % self.text
            for child in self.children:
                internal += str(child)
            ending = "</%s>\n" % self.tag
            return opening + internal + ending
        else:
            if self.is_single:
                return "<{tag} {attrs}/>\n".format(tag=self.tag, attrs=attrs)

            else:
                return "<{tag}>{text}</{tag}>\n".format(
                    tag=self.tag, text=self.text) if len(attrs) == 0 \
                    else "<{tag} {attrs}>{text}</{tag}>\n".format(
                    tag=self.tag, attrs=attrs, text=self.text)

    def __add__(self, other):
        self.children.append(other)
        return self

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

