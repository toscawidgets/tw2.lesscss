LessCSS for ToscaWidgets 2
==========================

This module adds the ability to link LessCSS based stylesheets.

More Information on LessCSS: `Less CSS <http://lesscss.org>`_.

Using TW2's LessCSS resource with TurboGears2
=============================================

Lets use LessCSS to define a simple box with rounded corners and a drop-shadow.

Create a file in the public folder TG2 project called 'simple.less'.

    .rounded-corners (@radius: 5px) {
      border-radius: @radius;
      padding: @radius;
      -webkit-border-radius: @radius;
      -moz-border-radius: @radius;
    }

    .round-corners {
        .rounded-corners;
    }


In your TG2 base-controller (projectname/lib/base.py):

    from tg import url
    from tw2.lesscss import LessCSSLink

    class SimpleLess(LessCSSLink):
        link=url('simple.less')

in the `__call__` function of BaseController add:

    LessTest.inject()

above the return statement.
