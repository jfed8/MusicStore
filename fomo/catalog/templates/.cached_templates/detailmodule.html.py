# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1490209450.9763374
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/catalog/templates/detailmodule.html'
_template_uri = 'detailmodule.html'
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
    return runtime._inherit_from(context, '/homepage/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        pictures = context.get('pictures', UNDEFINED)
        def body_center():
            return render_body_center(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_center'):
            context['self'].body_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        pictures = context.get('pictures', UNDEFINED)
        def body_center():
            return render_body_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="text-center">\r\n        <button id="btn_previous" class="btn btn-default">Previous</button>\r\n        <button id="btn_next" class="btn btn-default">Next</button>\r\n\r\n\r\n')
        for pic in pictures:
            __M_writer('            <img class="product_picture" src="')
            __M_writer(str(STATIC_URL))
            __M_writer(str(pic.path))
            __M_writer('" alt="')
            __M_writer(str(pic.product.name))
            __M_writer('">\r\n')
        __M_writer('    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/catalog/templates/detailmodule.html", "uri": "detailmodule.html", "source_encoding": "utf-8", "line_map": {"28": 0, "37": 1, "42": 14, "48": 3, "56": 3, "57": 9, "58": 10, "59": 10, "60": 10, "61": 10, "62": 10, "63": 10, "64": 12, "70": 64}}
__M_END_METADATA
"""
