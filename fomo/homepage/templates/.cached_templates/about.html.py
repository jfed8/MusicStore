# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1490754229.8081088
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/homepage/templates/about.html'
_template_uri = 'about.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['title', 'body_center']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'app_base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def body_center():
            return render_body_center(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n<!--\r\nbase blocks\r\n    title\r\n    header\r\n    message\r\n    menu_items\r\n    body_main\r\n    body_above\r\n    body_left\r\n    body_center\r\n    body_right\r\napp_base blocks\r\n    more_menu_items\r\n-->\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_center'):
            context['self'].body_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n    About\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_center():
            return render_body_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="jumbotron">\r\n\r\n\r\n    <h1>About: FOMO Rentals</h1>\r\n\r\n</div>\r\n\r\n<div class="container-fluid">\r\n<div class="row">\r\n    <h2>Our Mission:</h2>\r\n    <p>To become the World\'s Favorite Music Store</p>\r\n    <h2>Our Story</h2>\r\n    <p>Visit any FOMO Music Store at any time and you’re guaranteed to see somebody making music. After all, making music is what we\'re all about.\r\n    Playing the incredible selection of instruments is not only allowed, it’s encouraged. You’ll find people of all ages, from novice to\r\n    pros playing trumpets, saxaphones, and other instruments. The huge inventory of musical instruments and accessories, sound and recording\r\n    equipment, sheet music and videos, computers and music software covers every musician’s needs no matter what his or her playing style or ability may be.</p>\r\n    <p>FOMO is currently a local rental store with locations throughout the state of Utah. Our current size doesn\'t prevent us from having big dreams.\r\n        We will one day become the world\'s favorite music store.</p>\r\n    <p>Come in and see us today!</p>\r\n    <h2>Accessibility</h2>\r\n    <p>FOMO is committed to providing a website that is accessible to the widest possible audience, regardless of technology or ability.\r\n        We are actively working to increase the accessibility and usability of our website and in doing so adhere to many of the available\r\n        standards and guidelines. Our recent improvements include:\r\n        <ul>\r\n            <li>Short and simple sentences to aid readability and engage a wider audience on About Us Page.</li>\r\n            <li>A keyboard alone accessibly homepage.</li>\r\n            <li>Hierarchical headings and markup on your homepage</li>\r\n            <li>Visible labels outside of text boxes on “Contact Us” form.</li>\r\n        </ul>\r\n    </p>\r\n</div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/homepage/templates/about.html", "uri": "about.html", "source_encoding": "utf-8", "line_map": {"28": 0, "37": 1, "42": 19, "47": 55, "53": 17, "59": 17, "65": 22, "71": 22, "77": 71}}
__M_END_METADATA
"""
