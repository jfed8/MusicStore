# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1490754234.8522115
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/homepage/templates/faq.html'
_template_uri = 'faq.html'
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
        __M_writer('\r\n    FAQ\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_center():
            return render_body_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="content">\r\n      <h3>Frequently Asked Questions</h3>\r\n      <!-- Question #1 -->\r\n      <br/>\r\n\r\n      <p><strong>What instruments do you have?</strong></p>\r\n      <p>We provide various instruments. Our most popular instrumenst are listed below:\r\n          <ul>\r\n              <li>Trumpet</li>\r\n              <li>Trombone</li>\r\n              <li>French Horn</li>\r\n              <li>Percussion Kit</li>\r\n              <li>Flute</li>\r\n              <li>Clarinet</li>\r\n              <li>Oboe</li>\r\n              <li>Saxaphone</li>\r\n              <li>Violin</li>\r\n              <li>Viola</li>\r\n              <li>Cello</li>\r\n          </ul>\r\n      If you don\'t see the instrument that you are looking for, <a href="/homepage/contact">contact us</a>. If we don\'t have it, we can get it!</p>\r\n      <br/>\r\n\r\n      <!-- Question #2 -->\r\n      <p><strong>If I am renting for educational purposes, will you give me the needed tax documents at the end of the year?</strong></p>\r\n      <p> We can provide the needed tax documents; however, you will be responsible for (1) informing us about this at the beginning of you rental agreement and (2) requesting the documents and the end of the year.</p>\r\n      <br/>\r\n\r\n      <p><strong>Can I rent even if I have bad credit?</strong></p>\r\n      <p>Yes. At the beginning of each rental agreement, we perform a credit check. If your credit does not meet our requirements, we are willing to work with you since the rental fees are a low monthly payment. </p>\r\n      <br/>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/homepage/templates/faq.html", "uri": "faq.html", "source_encoding": "utf-8", "line_map": {"28": 0, "37": 1, "42": 19, "47": 54, "53": 17, "59": 17, "65": 21, "71": 21, "77": 71}}
__M_END_METADATA
"""
