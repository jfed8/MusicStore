# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1492099865.8137941
_enable_loop = True
_template_filename = '/Users/JessClapier/IntexFOMO/fomo/homepage/templates/faq.html'
_template_uri = 'faq.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
from decimal import Decimal
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
        __M_writer('\n<!--\nbase blocks\n    title\n    header\n    message\n    menu_items\n    body_main\n    body_above\n    body_left\n    body_center\n    body_right\napp_base blocks\n    more_menu_items\n-->\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_center'):
            context['self'].body_center(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\n    FAQ\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_center():
            return render_body_center(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content">\n      <h3 style="margin-top:0px;">Frequently Asked Questions</h3>\n      <!-- Question #1 -->\n      <br/>\n\n      <p><strong>What instruments do you have?</strong></p>\n      <p>We provide various instruments. Our most popular instrumenst are listed below:\n          <ul>\n              <li>Trumpet</li>\n              <li>Trombone</li>\n              <li>French Horn</li>\n              <li>Percussion Kit</li>\n              <li>Flute</li>\n              <li>Clarinet</li>\n              <li>Oboe</li>\n              <li>Saxaphone</li>\n              <li>Violin</li>\n              <li>Viola</li>\n              <li>Cello</li>\n          </ul>\n      If you don\'t see the instrument that you are looking for, <a href="/homepage/contact">contact us</a>. If we don\'t have it, we can get it!</p>\n      <br/>\n\n      <!-- Question #2 -->\n      <p><strong>If I am renting for educational purposes, will you give me the needed tax documents at the end of the year?</strong></p>\n      <p> We can provide the needed tax documents; however, you will be responsible for (1) informing us about this at the beginning of you rental agreement and (2) requesting the documents and the end of the year.</p>\n      <br/>\n\n      <p><strong>Can I rent even if I have bad credit?</strong></p>\n      <p>Yes. At the beginning of each rental agreement, we perform a credit check. If your credit does not meet our requirements, we are willing to work with you since the rental fees are a low monthly payment. </p>\n      <br/>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JessClapier/IntexFOMO/fomo/homepage/templates/faq.html", "uri": "faq.html", "source_encoding": "utf-8", "line_map": {"30": 0, "39": 1, "44": 19, "49": 54, "55": 17, "61": 17, "67": 21, "73": 21, "79": 73}}
__M_END_METADATA
"""
