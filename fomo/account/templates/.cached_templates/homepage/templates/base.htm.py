# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491588644.182838
_enable_loop = True
_template_filename = '/Users/JessClapier/IntexFOMO/fomo/homepage/templates/base.htm'
_template_uri = '/homepage/templates/base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
from decimal import Decimal
import django_mako_plus
_exports = ['title', 'header', 'message', 'menu_items', 'body_main', 'body_above', 'body_left', 'body_center', 'body_right']


from django_mako_plus import get_template_css, get_template_js 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        def body_right():
            return render_body_right(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def body_center():
            return render_body_center(context._locals(__M_locals))
        def body_above():
            return render_body_above(context._locals(__M_locals))
        def message():
            return render_message(context._locals(__M_locals))
        def body_main():
            return render_body_main(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def body_left():
            return render_body_left(context._locals(__M_locals))
        def menu_items():
            return render_menu_items(context._locals(__M_locals))
        def title():
            return render_title(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n\n<!--\nbase blocks\n    title\n    header\n    message\n    menu_items\n    body_main\n    body_above\n    body_left\n    body_center\n    body_right\n-->\n\n\n\n\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n\n\n\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.datetimepicker.full.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.loadmodal.js"></script>\n    <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.form.js"></script>\n    <link type="text/css" rel="stylesheet" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/styles/readable.css">\n    <link type="text/css" rel="stylesheet" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/styles/base.css">\n    <link type="text/css" rel="stylesheet" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery.datetimepicker.min.css">\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css">\n\n')
        __M_writer('    ')
        __M_writer(str( get_template_css(self, request, context) ))
        __M_writer('\n\n')
        __M_writer('    <link rel="icon" type="image/png" sizes="32x32"href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/FOMOLogo.ico">\n\n')
        __M_writer('    <title>')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer(' | Family Oriented Music Organization</title>\n\n  </head>\n  <body>\n\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n\n        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_main'):
            context['self'].body_main(**pageargs)
        

        __M_writer('\n\n<footer id="footer" class="footer">\n      <div class="container">\n\n            ')

        from datetime import datetime, date
        now = datetime.now()
                    
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['datetime','now','date'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n            <p class="text-muted"> &copy; ')
        __M_writer(str( now.year ))
        __M_writer('. All rights reserved. </p>\n      </div>\n</footer>\n\n\n')
        __M_writer('    ')
        __M_writer(str( get_template_js(self, request, context) ))
        __M_writer('\n\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('Home')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def message():
            return render_message(context)
        def menu_items():
            return render_menu_items(context)
        __M_writer = context.writer()
        __M_writer('\n      <header>\n          <div class="container-fluid">\n              <div class="row">\n                  <div id="message" >                                                                   <!--Can\'t get it to float right-->\n                      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'message'):
            context['self'].message(**pageargs)
        

        __M_writer('\n                  </div>\n              </div>\n          </div> <!--container-fluid, message-->\n\n\n          <div class="container-fluid">\n              <div class="row">\n                  <nav class="navbar navbar-default">\n                      <!-- Brand and toggle get grouped for better mobile display -->\n                      <div class="navbar-header">\n                          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\n                              <span class="sr-only">Toggle navigation</span>\n                              <span class="icon-bar"></span>\n                              <span class="icon-bar"></span>\n                              <span class="icon-bar"></span>\n                          </button>\n                          <a class="navbar-brand" id="logo" href="/"><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/FOMOLogo-03.png" alt="Family Oriented Music Organization"/></a>\n                      </div>\n\n        <!-- Collect the nav links, forms, and other content for toggling -->\n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n                <ul class="nav navbar-nav">\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu_items'):
            context['self'].menu_items(**pageargs)
        

        __M_writer('\n                </ul>\n\n                <ul class="nav navbar-nav navbar-right">\n')
        if request.user.is_authenticated:
            __M_writer('\n                    <li><span id=\'cart-count\' class="badge">')
            __M_writer(str(request.user.get_cart_count()))
            __M_writer('</span><a id="cart"  href="/checkout/cart"><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/cart.png" alt="Shopping Cart"></a></li>\n\n                        <li class="dropdown">\n\n                                <a href="#" class=" dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Hi ')
            __M_writer(str( request.user.first_name ))
            __M_writer('<span class="caret"></span></a>\n                                    <ul class="dropdown-menu">\n                                        <li><a href="/account/myaccount">My Account</a></li>\n                                        <li><a href="/account/logout">Log Out</a></li>\n\n                                    </ul>\n\n                        </li>\n')
        else:
            __M_writer('                        <li><a href="/account/signup">Signup</a></li>\n                        <li><a id=\'login-modal-button\' >Log In</a></li>\n')
        __M_writer('\n                </ul>\n            </div><!-- /.navbar-collapse -->\n                </nav>\n            </div>\n        </div> <!--container-fluid, navbar-->\n        </header>\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def message():
            return render_message(context)
        __M_writer = context.writer()
        __M_writer('\n\n                      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu_items(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def menu_items():
            return render_menu_items(context)
        __M_writer = context.writer()
        __M_writer('\n\n                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_main(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def body_right():
            return render_body_right(context)
        def body_center():
            return render_body_center(context)
        def body_above():
            return render_body_above(context)
        def body_main():
            return render_body_main(context)
        def body_left():
            return render_body_left(context)
        __M_writer = context.writer()
        __M_writer('\n            <div class="container-fluid">\n                <div id="row-above"class="row">\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_above'):
            context['self'].body_above(**pageargs)
        

        __M_writer('\n                </div>\n                <div id="body-row" class="row is-table-row">\n                    <div id="body-left" class="col-md-2">\n                        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_left'):
            context['self'].body_left(**pageargs)
        

        __M_writer('\n                    </div>\n\n                    <div id="body-center" class="col-md-8">\n\n\n                        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_center'):
            context['self'].body_center(**pageargs)
        

        __M_writer('\n                    </div>\n                    <div id="body-right" class="col-md-2">\n                        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_right'):
            context['self'].body_right(**pageargs)
        

        __M_writer('\n                    </div>\n                </div> <!--body-row-->\n            </div>\n        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_above(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_above():
            return render_body_above(context)
        __M_writer = context.writer()
        __M_writer('\n                        <br/>\n\n                        <br/>\n                    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_left(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_left():
            return render_body_left(context)
        __M_writer = context.writer()
        __M_writer('\n\n                        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_center():
            return render_body_center(context)
        __M_writer = context.writer()
        __M_writer('\n\n                        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_right(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def body_right():
            return render_body_right(context)
        __M_writer = context.writer()
        __M_writer('\n                            <ul class="nav nav-stacked panel">\n                                <li class="panel-title text-center">Recent Products:</li>\n')
        if request.user.is_authenticated:
            for prod in request.user.displayHistory():
                __M_writer('                                    <li><a href="/catalog/detail/')
                __M_writer(str( prod.id ))
                __M_writer('"> ')
                __M_writer(str( prod.name ))
                __M_writer(' </a></li>\n')
        else:
            __M_writer('                                    <p><a href="/account/login/">Sign in</a> to view your recent products.</p>\n')
        __M_writer('                            </ul>\n                        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JessClapier/IntexFOMO/fomo/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"19": 4, "21": 0, "47": 2, "48": 4, "49": 32, "50": 34, "51": 34, "52": 35, "53": 35, "54": 36, "55": 36, "56": 37, "57": 37, "58": 38, "59": 38, "60": 39, "61": 39, "62": 43, "63": 43, "64": 43, "65": 46, "66": 46, "67": 46, "68": 49, "73": 49, "78": 115, "83": 156, "84": 161, "91": 164, "92": 165, "93": 165, "94": 171, "95": 171, "96": 171, "102": 49, "108": 49, "114": 54, "126": 54, "131": 61, "132": 78, "133": 78, "138": 86, "139": 90, "140": 91, "141": 92, "142": 92, "143": 92, "144": 92, "145": 96, "146": 96, "147": 104, "148": 105, "149": 108, "155": 59, "161": 59, "167": 84, "173": 84, "179": 117, "194": 117, "199": 124, "204": 130, "209": 138, "214": 152, "220": 120, "226": 120, "232": 128, "238": 128, "244": 136, "250": 136, "256": 141, "263": 141, "264": 144, "265": 145, "266": 146, "267": 146, "268": 146, "269": 146, "270": 146, "271": 148, "272": 149, "273": 151, "279": 273}}
__M_END_METADATA
"""
