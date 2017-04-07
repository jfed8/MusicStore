# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1490207316.5713718
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/catalog/templates/search.html'
_template_uri = 'search.html'
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
        products = context.get('products', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<!--\r\nbase blocks\r\n    title\r\n    header\r\n    message\r\n    menu_items\r\n    body_main\r\n    body_above\r\n    body_left\r\n    body_center\r\n    body_right\r\napp_base blocks\r\n    more_menu_items\r\n-->\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

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
        __M_writer('\r\n    Search Results\r\n')
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
        __M_writer('\r\n<table class="table table-striped">\r\n    <caption class="text-center"><strong>Search Results</strong></caption>\r\n    <tr>\r\n        <th></th>\r\n        <th>Name</th>\r\n        <th>Category</th>\r\n        <th>Price</th>\r\n        <th></th>\r\n    </tr>\r\n')
        for p in products:
            __M_writer('        <tr class="clickable-row" data-href=\'/catalog/detail/')
            __M_writer(str(p.id))
            __M_writer('\'>\r\n                <td><img class=\'graphic\' src="')
            __M_writer(str(STATIC_URL))
            __M_writer('catalog/media/prod_imgs/')
            __M_writer(str(p.graphic))
            __M_writer('" alt=""></td>\r\n                <td>')
            __M_writer(str(p.name))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(p.category.name))
            __M_writer('</td>\r\n                <td>')
            __M_writer(str(p.price))
            __M_writer('</td>\r\n                <td><a href="/catalog/detail/')
            __M_writer(str( p.id ))
            __M_writer('"class="btn btn-primary">View</a></td>\r\n        </tr>\r\n\r\n')
        __M_writer('</table>\r\n<p>Our customer support and account management teams provide the best service in the industry. We\'re passionate about our products\r\nas well as our customers and it shows in the level of service that we provide. We\'re always happy to help find the solution for\r\nyour needs. If a solution doesn\'t already exist, we\'ll create a new solution that resolves your issue. <a href="/homepage/contact" >Contact Us!</a></p>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/catalog/templates/search.html", "uri": "search.html", "source_encoding": "utf-8", "line_map": {"28": 0, "39": 1, "44": 19, "49": 45, "55": 17, "61": 17, "67": 21, "75": 21, "76": 31, "77": 32, "78": 32, "79": 32, "80": 33, "81": 33, "82": 33, "83": 33, "84": 34, "85": 34, "86": 35, "87": 35, "88": 36, "89": 36, "90": 37, "91": 37, "92": 41, "98": 92}}
__M_END_METADATA
"""
