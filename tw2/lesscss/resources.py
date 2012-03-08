import tw2.core as twc
from base import less_js

class LessCSSLink(twc.Link):
    resources = [less_js]
    location = 'head'
    template = 'tw2.lesscss.templates.lesslink'
