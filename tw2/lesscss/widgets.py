import tw2.core as twc


class Lesscss(twc.Widget):
    template = "genshi:tw2.lesscss.templates.lesscss"

    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [
        twc.JSLink(modname=__name__, filename='static/lesscss.js'),
        twc.CSSLink(modname=__name__, filename='static/lesscss.css'),
    ]

    @classmethod
    def post_define(cls):
        pass
        # put custom initialisation code here

    def prepare(self):
        super(Lesscss, self).prepare()
        # put code here to run just before the widget is displayed
