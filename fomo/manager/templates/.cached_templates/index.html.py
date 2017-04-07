# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1488687419.620186
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/manager/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['title', 'more_breadcrumb', 'body_main']


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
        def more_breadcrumb():
            return render_more_breadcrumb(context._locals(__M_locals))
        def body_main():
            return render_body_main(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'more_breadcrumb'):
            context['self'].more_breadcrumb(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_main'):
            context['self'].body_main(**pageargs)
        

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


def render_more_breadcrumb(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def more_breadcrumb():
            return render_more_breadcrumb(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <span class="breadcrumb-item active">Index</span>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_main():
            return render_body_main(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n        <h3>Congratulations -- you\'ve successfully created a new django-mako-plus app!</h3>\r\n        <h4>Next Up: Go through the django-mako-plus tutorial and add Javascript, CSS, and urlparams to this page.</h4>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/manager/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"28": 0, "39": 1, "44": 6, "49": 10, "54": 17, "60": 4, "66": 4, "72": 8, "78": 8, "84": 12, "90": 12, "96": 90}}
__M_END_METADATA
"""
