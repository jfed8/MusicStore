# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491245400.434728
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/formlib/templates/form.htm'
_template_uri = 'form.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        csrf_input = context.get('csrf_input', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(str( django_mako_plus.link_css(self) ))
        __M_writer('\r\n\r\n<form id="')
        __M_writer(str( form.form_id ))
        __M_writer('" class="')
        __M_writer(str( ' '.join(form.form_classes) ))
        __M_writer('" action="')
        __M_writer(str( form.form_action or '' ))
        __M_writer('" method="')
        __M_writer(str( form.form_method ))
        __M_writer('">\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( csrf_input ))
        __M_writer('\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( form.as_p() ))
        __M_writer('\r\n\r\n')
        __M_writer('    <p class="text-center"><button type="submit" class="btn btn-primary">')
        __M_writer(filters.html_escape(str( form.form_submit )))
        __M_writer('</button></p>\r\n\r\n</form>\r\n\r\n\r\n')
        __M_writer(str( django_mako_plus.link_js(self) ))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/formlib/templates/form.htm", "uri": "form.htm", "source_encoding": "utf-8", "line_map": {"17": 0, "25": 2, "26": 2, "27": 4, "28": 4, "29": 4, "30": 4, "31": 4, "32": 4, "33": 4, "34": 4, "35": 7, "36": 7, "37": 7, "38": 10, "39": 10, "40": 10, "41": 13, "42": 13, "43": 13, "44": 19, "45": 19, "51": 45}}
__M_END_METADATA
"""
