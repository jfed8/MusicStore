# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1487015829.404133
_enable_loop = True
_template_filename = 'C:/Users/klynty/fomo/fomo/homepage/templates/sections.html'
_template_uri = 'sections.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['message', 'body_center']


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
        def message():
            return render_message(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n<!--\r\nbase blocks\r\n    title\r\n    header\r\n    message\r\n    menu_items\r\n    body_main\r\n    body_above\r\n    body_left\r\n    body_center\r\n    body_right\r\napp_base blocks\r\n    more_menu_items\r\n-->\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'message'):
            context['self'].message(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'body_center'):
            context['self'].body_center(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_message(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def message():
            return render_message(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <div class="alert alert-info alert-dismissible" role="alert">\r\n        <button type="button" class="close" data-dismiss="alert" aria-label="Close">\r\n            <span aria-hidden="true">&times;</span>\r\n        </button>\r\n        <strong>Holy guacamole!</strong> You have found the sections page.\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body_center(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def body_center():
            return render_body_center(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n    <div class="content">\r\n        <h2>Home Page</h2>\r\n        <h3>Naskah Lorem Ipsum standar yang digunakan sejak tahun 1500an</h3>\r\n\r\n        <p>"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\r\n            Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure\r\n            dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non\r\n            proident, sunt in culpa qui officia deserunt mollit anim id est laborum."</p>\r\n\r\n        <h3>Bagian 1.10.32 dari "de Finibus Bonorum et Malorum", ditulis oleh Cicero pada tahun 45 sebelum masehi</h3>\r\n\r\n        <p>"Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque\r\n            ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia\r\n            voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.\r\n            Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi\r\n            tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem\r\n            ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in\r\n            ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"</p>\r\n\r\n        <h3>Terjemahan tahun 1914 oleh H. Rackham</h3>\r\n\r\n        <p>"But I must explain to you how all this mistaken idea of denouncing pleasure and praising pain was born and I will give you\r\n            a complete account of the system, and expound the actual teachings of the great explorer of the truth, the master-builder of\r\n            human happiness. No one rejects, dislikes, or avoids pleasure itself, because it is pleasure, but because those who do not know\r\n            how to pursue pleasure rationally encounter consequences that are extremely painful. Nor again is there anyone who loves or\r\n            pursues or desires to obtain pain of itself, because it is pain, but because occasionally circumstances occur in which toil and\r\n            pain can procure him some great pleasure. To take a trivial example, which of us ever undertakes laborious physical exercise, except\r\n            to obtain some advantage from it? But who has any right to find fault with a man who chooses to enjoy a pleasure that has no annoying\r\n            consequences, or one who avoids a pain that produces no resultant pleasure?"</p>\r\n\r\n        <h3>Bagian 1.10.33 dari "de Finibus Bonorum et Malorum", ditulis oleh Cicero pada tahun 45 sebelum masehi</h3>\r\n\r\n        <p>"At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti quos dolores\r\n            et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id\r\n            est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam libero tempore, cum soluta nobis est eligendi\r\n            optio cumque nihil impedit quo minus id quod maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus.\r\n            Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet ut et voluptates repudiandae sint et molestiae\r\n            non recusandae. Itaque earum rerum hic tenetur a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis\r\n            doloribus asperiores repellat."</p>\r\n\r\n        <h3>Terjemahan tahun 1914 oleh H. Rackham</h3>\r\n\r\n        <p>"On the other hand, we denounce with righteous indignation and dislike men who are so beguiled and demoralized by the charms of pleasure of\r\n            the moment, so blinded by desire, that they cannot foresee the pain and trouble that are bound to ensue; and equal blame belongs to those who\r\n            fail in their duty through weakness of will, which is the same as saying through shrinking from toil and pain. These cases are perfectly simple\r\n            and easy to distinguish. In a free hour, when our power of choice is untrammelled and when nothing prevents our being able to do what we like best,\r\n            every pleasure is to be welcomed and every pain avoided. But in certain circumstances and owing to the claims of duty or the obligations of business\r\n            it will frequently occur that pleasures have to be repudiated and annoyances accepted. The wise man therefore always holds in these matters to this\r\n            principle of selection: he rejects pleasures to secure other greater pleasures, or else he endures pains to avoid worse pains."</p>\r\n    </div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/klynty/fomo/fomo/homepage/templates/sections.html", "uri": "sections.html", "source_encoding": "utf-8", "line_map": {"28": 0, "37": 1, "42": 25, "47": 81, "53": 18, "59": 18, "65": 28, "71": 28, "77": 71}}
__M_END_METADATA
"""
