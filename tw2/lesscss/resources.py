import tw2.core as twc
from base import less_js

class LessCSSLink(twc.Link):
    location = 'head'
    template = 'tw2.lesscss.templates.lesslink'
