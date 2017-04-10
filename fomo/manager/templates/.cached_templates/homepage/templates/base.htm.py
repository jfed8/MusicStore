# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1491596263.118625
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
        def menu_items():
            return render_menu_items(context._locals(__M_locals))
        def body_center():
            return render_body_center(context._locals(__M_locals))
        def body_left():
            return render_body_left(context._locals(__M_locals))
        def body_above():
            return render_body_above(context._locals(__M_locals))
        def message():
            return render_message(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def body_main():
            return render_body_main(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def body_right():
            return render_body_right(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n<!--\nbase blocks\n    title\n    header\n    message\n    menu_items\n    body_main\n    body_above\n    body_left\n    body_center\n    body_right\n-->\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n\n')
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
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['date','datetime','now'] if __M_key in __M_locals_builtin_stored]))
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
        def menu_items():
            return render_menu_items(context)
        def message():
            return render_message(context)
        request = context.get('request', UNDEFINED)
        def header():
            return render_header(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n      <header>\n          <div class="container-fluid">\n              <div class="row">\n                  <div id="message" >                                                                   <!--Can\'t get it to float right-->\n                      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'message'):
            context['self'].message(**pageargs)
        

        __M_writer('\n                  </div>\n              </div>\n          </div> <!--container-fluid, message-->\n\n          <div class="container-fluid">\n              <div class="row">\n                  <nav class="navbar navbar-default navbar-static-top" style="margin-bottom: 0px;">\n                      <!-- Brand and toggle get grouped for better mobile display -->\n                      <div class="navbar-header">\n                          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\n                              <span class="sr-only">Toggle navigation</span>\n                              <span class="icon-bar"></span>\n                              <span class="icon-bar"></span>\n                              <span class="icon-bar"></span>\n                          </button>\n                          <a class="navbar-brand" id="logo" href="/"><img src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/FOMOLogo-03.png" alt="Family Oriented Music Organization"/></a>\n                      </div>\n\n        <!-- Collect the nav links, forms, and other content for toggling -->\n            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n                <ul class="nav navbar-nav">\n                    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'menu_items'):
            context['self'].menu_items(**pageargs)
        

        __M_writer('\n                </ul>\n\n                <ul class="nav navbar-nav navbar-right">\n')
        if request.user.is_authenticated:
            __M_writer('\n                    <!-- <li><span id=\'cart-count\' class="badge">')
            __M_writer(str(request.user.get_cart_count()))
            __M_writer('</span><a id="cart"  href="/checkout/cart/"><img src="')
            __M_writer(str( STATIC_URL ))
            __M_writer('homepage/media/cart.png" alt="Shopping Cart"></a></li> -->\n                    <li><a href="/checkout/cart/" class="fa fa-shopping-cart fa-6" id="cart-logo" aria-hidden="true"><span id="cart_count" class="badge">')
            __M_writer(str(request.user.get_cart_count()))
            __M_writer('</span></a></li>\n                        <li class="dropdown">\n\n                                <a href="#" class=" dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Hi ')
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
        def body_center():
            return render_body_center(context)
        def body_left():
            return render_body_left(context)
        def body_above():
            return render_body_above(context)
        request = context.get('request', UNDEFINED)
        def body_main():
            return render_body_main(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def body_right():
            return render_body_right(context)
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def body_right():
            return render_body_right(context)
        __M_writer = context.writer()
        __M_writer('\n\n                        <div class="panel panel-default">\n                            <div class="panel-heading">\n                                <h3 class="panel-title">Recently Viewed</h3>\n                              </div>\n                              <div class="panel-body">\n                                  <ul class="nav">\n')
        if request.user.is_authenticated:
            for prod in request.user.displayHistory():
                __M_writer('                                          <li><a href="/catalog/detail/')
                __M_writer(str( prod.id ))
                __M_writer('"><img class="product_picture" height="20" src="')
                __M_writer(str(STATIC_URL))
                __M_writer('catalog/media/prod_imgs/')
                __M_writer(str(prod.graphic))
                __M_writer('" />')
                __M_writer(str( prod.name ))
                __M_writer(' </a></li>\n')
        else:
            __M_writer('                                          <p><a href="/account/login/">Sign in</a> to view your recent products.</p>\n')
        __M_writer('                                  </ul>\n                              </div>\n                        </div>\n                        ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/JessClapier/IntexFOMO/fomo/homepage/templates/base.htm", "uri": "/homepage/templates/base.htm", "source_encoding": "utf-8", "line_map": {"19": 4, "21": 0, "47": 2, "48": 4, "49": 25, "50": 27, "51": 27, "52": 28, "53": 28, "54": 29, "55": 29, "56": 30, "57": 30, "58": 31, "59": 31, "60": 32, "61": 32, "62": 36, "63": 36, "64": 36, "65": 39, "66": 39, "67": 39, "68": 42, "73": 42, "78": 107, "83": 155, "84": 160, "91": 163, "92": 164, "93": 164, "94": 170, "95": 170, "96": 170, "102": 42, "108": 42, "114": 47, "126": 47, "131": 54, "132": 70, "133": 70, "138": 78, "139": 82, "140": 83, "141": 84, "142": 84, "143": 84, "144": 84, "145": 85, "146": 85, "147": 88, "148": 88, "149": 96, "150": 97, "151": 100, "157": 52, "163": 52, "169": 76, "175": 76, "181": 109, "197": 109, "202": 116, "207": 122, "212": 130, "217": 151, "223": 112, "229": 112, "235": 120, "241": 120, "247": 128, "253": 128, "259": 133, "267": 133, "268": 141, "269": 142, "270": 143, "271": 143, "272": 143, "273": 143, "274": 143, "275": 143, "276": 143, "277": 143, "278": 143, "279": 145, "280": 146, "281": 148, "287": 281}}
__M_END_METADATA
"""
