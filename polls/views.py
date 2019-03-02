from django.shortcuts import render
from django.http import HttpResponse
from config import settings
from django.template import engines
from django.template.loader import render_to_string
from django.db.models import (
    F
)
from pprint import pprint

from django.shortcuts import (
render
)
from common.models.country import (
    Country
)
from common.models.money import (
    Currency,
    Money
)
from django.http import Http404
from common.utilities import *
from polls.forms import TitleForm

import logging
log = logging.getLogger('default')

"""
 Pep8 coding guide is here.
 @see http://pep8-ja.readthedocs.io/ja/latest/
"""
def index(request) :
    """
    agenda:
    1.user template.
        1-1.template was Used
        - 1-2.
        - 1-3. css, javascript
    2.use model and orm.
        2-1.make model package and add config_dir to INSTALLED_APP.
        2-2.edit money.py and add table definition.
        2-3.exec e.g.) python manage.py makemigrations <model_package> ...make latest migration(DB) definition file.
        2-4.python manage.py sqlmigrate common 0001 ...display sql of migration definition file.
        2-5.python manage.py migrate ...make tables by migration definition file.
        - 2-6 validation
    3.use session for web application.
    4.make autuenticate.
    5.switch to development setting.
    6.decolator
    
    :param request: 
    :return: 
    """
    # django_engine = engines['django']

    params = {
        'name': 'hello',
        'items': Money.objects.all(),
        'form' : TitleForm(),
    }
    pprint(settings.STATIC_ROOT)

    rendered = render(request, 'polls/index.html', params)
    return HttpResponse(rendered)
    # return HttpResponse("Hello this is index of poll")

def detail(request, money_id):
    """
    
    :param request: リクエスト
    :param question_id: 質問IDルーティングから受け取り
    :return: 
    """
    params = {
        'name': 'detail',
    }
    LOG_DEFAULT.debug(params)

    params['items'] = Money.objects.filter(pk=money_id) # キーを指定して、従属テーブル側を取得
    params['header'] = params['items'].first()
    # not exists
    if not params['header'] :
        raise Http404("Question does not exist")


    rendered = render(request, 'polls/detail.html', params)
    return HttpResponse(rendered)

def edit(request, money_id) :
    return HttpResponse('編集画面')

def delete(request, money_id) :
    return HttpResponse('編集画面')
