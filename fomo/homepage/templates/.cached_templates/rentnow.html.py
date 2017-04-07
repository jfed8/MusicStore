# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1488684280.7364552
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/homepage/templates/rentnow.html'
_template_uri = 'rentnow.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['title', 'menu_items', 'body_center']


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
        def menu_items():
            return render_menu_items(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n<!--\r\nbase blocks\r\n    title\r\n    header\r\n    message\r\n    menu_items\r\n    body_main\r\n    body_above\r\n    body_left\r\n    body_center\r\n    body_right\r\napp_base blocks\r\n    more_menu_items\r\n-->\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu_items'):
            context['self'].menu_items(**pageargs)
        

        __M_writer('\r\n\r\n')
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
        __M_writer('\r\n    Rent Now\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu_items():
            return render_menu_items(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_center():
            return render_body_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="text-center">\r\n        <img class=\'landing_img\' src="https://static1.squarespace.com/static/52cc44d6e4b057654fef89f6/t/52d57f6ce4b01276a21d88a0/1389723501310/" alt="">\r\n\r\n    </div>\r\n    <div class="text-center"><h1>Rent Affordable Instruments</h1></div>\r\n        <div class="row">\r\n        <div class="col-md-9">\r\n            <h2>Cheap Quality Instruments</h2>\r\n                <p> Whether you are an aspiring musician or a high school student, FOMO has the instrument for you.\r\n                    Our wide collection of instruments include woodwind, brass, and string instruments as well as percussion kits.\r\n                    FOMO is home to the biggest instrument brands, including Fender, Yamaha, Casio, Gibson, Gretsch, Ibanez, PRS,\r\n                    Novation, Roland, Pure Tone, Tanglewood, Squier. We provide you with big store quality at a price that anyone in the neighborhood could afford!\r\n                </p>\r\n                    <p><strong>High School Instrument Rentals:</strong> Our student rental package provides a variety of services ideal for High School students.</p>\r\n        </div>\r\n        <div class="col-md-3" id="promotion_body">\r\n            <div class="row">\r\n                <h2 class="text-center" id="promotion">Special Promotion</h2>\r\n            </div>\r\n            <div class="row text-center" >\r\n                <p>Sign up today and get your rental for $10.99/month!<br>\r\n                    <a class=\'btn btn-primary\' href="#">Rent Now!</a>\r\n                </p>\r\n            </div>\r\n        </div>\r\n    </div>\r\n\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/homepage/templates/rentnow.html", "uri": "rentnow.html", "source_encoding": "utf-8", "line_map": {"28": 0, "39": 1, "44": 19, "49": 23, "54": 56, "60": 17, "66": 17, "72": 21, "78": 21, "84": 25, "90": 25, "96": 90}}
__M_END_METADATA
"""
