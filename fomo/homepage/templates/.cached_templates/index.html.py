# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1490207262.6776779
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['body_center']


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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<!--\r\nbase blocks\r\n    title\r\n    header\r\n    message\r\n    menu_items\r\n    body_main\r\n    body_above\r\n    body_left\r\n    body_center\r\n    body_right\r\napp_base blocks\r\n    more_menu_items\r\n-->\r\n\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_center'):
            context['self'].body_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_center():
            return render_body_center(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="row">\r\n    <div id="home-jumbo" class="jumbotron">\r\n        <h1 class="text-center">Family Oriented Music Organization</h1>\r\n        <h2 class="text-center">From our family to yours</h2>\r\n        <div class="text-center"><!--<button type="button" class="btn btn-default">--><a class="btn btn-default" href="/catalog/">Rent Now!</a></button></div>\r\n    </div>\r\n</div>\r\n<!-- <div class="container-fluid"> -->\r\n<div class="row">\r\n    <div class="col-md-6">\r\n        <div class="row">\r\n            <h3>New: Rent-To-Own</h3>\r\n            <p> <strong>0% Interest* </strong> <br>\r\n                No interest*, with payments as low as $19 per month. <br>\r\n                <strong>No Rental Fees</strong> <br>\r\n                Utah\'s only rental program completely free of rental fees & service charges</p>\r\n        </div>\r\n        <div class="row">\r\n            <img id="music_lessons"src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/music-lessons.png" alt="Music Lessons">\r\n        </div>\r\n    </div>\r\n    <div class="col-md-6">\r\n        <iframe id="video" width="590" height="315" src="https://www.youtube.com/embed/FRPDtXVblwI" frameborder="0" allowfullscreen></iframe>\r\n\r\n    </div>\r\n\r\n</div>\r\n<div class="row">\r\n    <div class="col-md-7">\r\n        <img id="music_park"src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/music_park.png" alt="Music in the Park">\r\n    </div>\r\n    <div class="col-md-5">\r\n        <div class="row">\r\n            <h3>Music in the Park</h3>\r\n            <p>Every Saturday at 4:00 PM, FOMO sponsors \'Music in the Park\' at Nielsen\'s Grove Park in Orem, Utah.\r\n                Musicians of all genres come each week to share music with us. We want you to come and enjoy the afternoon with us!</p>\r\n        </div>\r\n        <div class="row">\r\n            <iframe src="https://calendar.google.com/calendar/embed?src=8d1vssit41eq0mat064j6c1bc8%40group.calendar.google.com&ctz=America/Denver" style="border: 0" width="400" height="300" frameborder="0" scrolling="no"></iframe>\r\n        </div>\r\n    </div>\r\n</div>\r\n<!-- </div> -->\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"28": 0, "36": 1, "41": 64, "47": 19, "54": 19, "55": 38, "56": 38, "57": 49, "58": 49, "64": 58}}
__M_END_METADATA
"""
