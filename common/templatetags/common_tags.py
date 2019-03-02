from django import template

"""
テンプレート側で {% load common_tag %} で使用

デコレータの例
@register.simple_tag ... シンプルタグ
@register.filter(name='cut') ... フィルター
https://docs.djangoproject.com/en/2.0/howto/custom-template-tags/

https://qiita.com/u_kan/items/fcea8bc7f338ab8770ee
{tag}
"""
# ライブラリ指定
register = template.Library()

@register.simple_tag
def summer(word:str) -> str:
    return word + '様へ'

class Date :
    def current(self, time:int) ->str:
        return  str(time) + '時'