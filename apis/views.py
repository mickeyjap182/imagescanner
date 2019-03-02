from pprint import pprint
from django.http import JsonResponse
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.http import require_http_methods

from polls.forms import TitleForm

import logging
log = logging.getLogger('default')

"""
 Pep8 coding guide is here.
 @see http://pep8-ja.readthedocs.io/ja/latest/
"""

class SelectionView(View):

    # @require_http_methods("POST")
    def post(request) :
        """
        
        :param request: 
        :return: 
        """
        # django_engine = engines['django']
        if "query_param" in request.GET:
            # query_paramが指定されている場合の処理
            param_value = request.GET.get(key="query_param", default={})
            pprint(param_value)
        elif request.method == "POST":
            #form = Formtitle_frm
            param_value =request.POST
            pprint(dict(param_value))
            form = TitleForm(dict(param_value))
            if form.is_valid() :
                pprint('OK')
            else :
                pprint('NG')


        else:
            param_value ={}

        title = param_value['username'] if 'username' in param_value else 'Hello world'
        pprint(title)
        params = {
            'title': title
        }

        return JsonResponse(params)
        # return HttpResponse("Hello this is index of poll")

