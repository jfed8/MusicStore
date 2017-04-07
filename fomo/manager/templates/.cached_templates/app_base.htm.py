# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1490749278.6054013
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/manager/templates/app_base.htm'
_template_uri = 'app_base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['menu_items', 'more_menu_items']


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
    return runtime._inherit_from(context, '/homepage/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def menu_items():
            return render_menu_items(context._locals(__M_locals))
        def more_menu_items():
            return render_more_menu_items(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<!--\r\nbase blocks\r\n    title\r\n    header\r\n    message\r\n    menu_items\r\n    body_main\r\n    body_above\r\n    body_left\r\n    body_center\r\n    body_right\r\napp_base blocks\r\n    more_menu_items\r\n-->\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu_items'):
            context['self'].menu_items(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu_items():
            return render_menu_items(context)
        def more_menu_items():
            return render_more_menu_items(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n    <li class="')
        __M_writer(str( 'active' if(request.dmp_router_page == 'products') else ''))
        __M_writer('"><a href="/manager/products">Products</a></li>\r\n    <li class="')
        __M_writer(str( 'active' if(request.dmp_router_page == 'users') else ''))
        __M_writer('"><a href="/manager/users">Users</a></li>\r\n    <li ><a href="/catalog/">Catalog</a></li>\r\n    <li><a href="/">Customer Portal<span class="sr-only">(current)</span></a></li>\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'more_menu_items'):
            context['self'].more_menu_items(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_more_menu_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def more_menu_items():
            return render_more_menu_items(context)
        __M_writer = context.writer()
        __M_writer('\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/manager/templates/app_base.htm", "uri": "app_base.htm", "source_encoding": "utf-8", "line_map": {"28": 0, "38": 1, "43": 24, "49": 17, "58": 17, "59": 18, "60": 18, "61": 19, "62": 19, "67": 23, "73": 22, "79": 22, "85": 79}}
__M_END_METADATA
"""
