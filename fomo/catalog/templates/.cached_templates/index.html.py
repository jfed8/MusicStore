# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1490207270.3390899
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/catalog/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['title', 'body_left', 'body_center']


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
        def body_left():
            return render_body_left(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        categories = context.get('categories', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<!--\r\nbase blocks\r\n    title\r\n    header\r\n    message\r\n    menu_items\r\n    body_main\r\n    body_above\r\n    body_left\r\n    body_center\r\n    body_right\r\napp_base blocks\r\n\r\n-->\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_left'):
            context['self'].body_left(**pageargs)
        

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
        __M_writer('\r\n    Catalog\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        categories = context.get('categories', UNDEFINED)
        def body_left():
            return render_body_left(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <ul class="nav nav-stacked panel">\r\n        <li class="panel-title text-center">Filter by Category:</li>\r\n')
        for c in categories:
            __M_writer('        <li><a href="/catalog/index.filter/')
            __M_writer(str(c.id))
            __M_writer('"> ')
            __M_writer(str( c.name ))
            __M_writer(' </a></li>\r\n')
        __M_writer('        <li><a href="/catalog/"> Clear Filter </a></li>\r\n    </ul>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_center():
            return render_body_center(context)
        products = context.get('products', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="body-outer">\r\n        <div class="tile-outer">\r\n')
        for p in products:
            __M_writer('            <a href="/catalog/detail/')
            __M_writer(str( p.id ))
            __M_writer('">\r\n                <div class="tile-container">\r\n\r\n                    <div class="tile-image">\r\n                        <img src="')
            __M_writer(str(STATIC_URL))
            __M_writer('catalog/media/prod_imgs/')
            __M_writer(str(p.graphic))
            __M_writer('" alt="">\r\n\r\n                    </div>\r\n                    <div class="tile-title">\r\n                        ')
            __M_writer(str( p.name ))
            __M_writer('\r\n\r\n                    </div>\r\n                </div>\r\n            </a>\r\n')
        __M_writer('        </div>\r\n    </div>\r\n\r\n    <br/>\r\n    <p>Our customer support and account management teams provide the best service in the industry. We\'re passionate about our products\r\n    as well as our customers and it shows in the level of service that we provide. We\'re always happy to help find the solution for\r\n    your needs. If a solution doesn\'t already exist, we\'ll create a new solution that resolves your issue. <a href="/homepage/contact" >Contact Us!</a></p>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/catalog/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"28": 0, "42": 1, "47": 18, "52": 29, "57": 57, "63": 16, "69": 16, "75": 20, "82": 20, "83": 23, "84": 24, "85": 24, "86": 24, "87": 24, "88": 24, "89": 26, "95": 31, "103": 31, "104": 34, "105": 35, "106": 35, "107": 35, "108": 39, "109": 39, "110": 39, "111": 39, "112": 43, "113": 43, "114": 49, "120": 114}}
__M_END_METADATA
"""
