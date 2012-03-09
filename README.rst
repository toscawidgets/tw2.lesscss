LessCSS for ToscaWidgets 2
==========================

This module adds the ability to link LessCSS based stylesheets.

More Information on LessCSS: `Less CSS <http://lesscss.org>`_.

Using TW2's LessCSS resource with TurboGears2
=============================================

Lets use LessCSS to define a simple box with rounded corners.

Create a file in the public folder TG2 project called 'simple.less'.
::
    .rounded-corners (@radius: 5px) {
        border-radius: @radius;
        padding: @radius;
        -webkit-border-radius: @radius;
        -moz-border-radius: @radius;
    }
    .shaded-rounded-corners {
        .rounded-corners;
        background-color: #333;
        color: #eee;
    }

Now we need to tell ToscaWidgets2 to add it to all of your requested pages. 
In the top of your TG2 base-controller (*projectname*/lib/base.py) add:
::
    from tg import url
    from tw2.lesscss import LessCSSLink

    class SimpleLess(LessCSSLink):
        link=url('simple.less')

Above the return in the `__call__` function of BaseController add:
::
    LessTest.inject()

This will inject the less file on every call to the controller.

Now you can use the lesscss class in your templates!
::
    <div class="shaded-rounded-corners">Hello!</div>

.. image:: http://github.com/toscawidgets/tw2.lesscss/raw/master/img/hello-div.png