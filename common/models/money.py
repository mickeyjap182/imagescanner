from django.db import models
from common.models.country import *
"""
・マイグレーションを含む。完全にモデルのファイルから作る。
"""


class Currency(models.Model) :
    """
    貨幣
    """
    # リファクタリングでドメイン定義

    # データが存在しない。
    # groups = ManyToManyField(Group,
    #                          related_name="%(class)ss",
    #                          related_query_name="%(class)s",
    #                          blank=True)

    country = models.ForeignKey(Country, on_delete=models.CASCADE, help_text="国")
    cd = models.CharField(max_length=20,  help_text="貨幣コード")
    name = models.CharField(max_length=20,  help_text="貨幣の名称")
    detail = models.CharField(null=True, max_length=200, help_text="詳細情報")
    est_date = models.DateTimeField(help_text="施行日")

    class Meta:
        db_table = "currency"
        # 多言語対応目的の複合主キー
        unique_together = ('country', 'cd', 'name')


class MoneyType(models.Model):
    """
    貨幣種別マスタ

    @detail 貨幣の種類を定義
    """
    country = models.ForeignKey(Currency, on_delete=models.CASCADE, help_text="言語別の貨幣タイプ")
    cd = models.CharField(primary_key=True, max_length=20, help_text="貨幣コード")
    name = models.CharField(max_length=20, help_text="貨幣名称")
    alias = models.CharField(null=True, max_length=20, help_text="貨幣名称の別名（カナ表記など）")
    prefix = models.CharField(max_length=20, help_text="金額の前表記")
    suffix = models.CharField(max_length=20, help_text="金額の後表記")
    detail = models.CharField(null=True, max_length=200, help_text="詳細情報")

    class Meta:
        db_table = "money_type"


class Money(models.Model) :
    """
    お金
    """

    # on_delete : 削除時の動作設定をする
    # models.PROTECT 保護する。デフォルト動作で、参照されていたら削除できなくする。
    # models.CASCADE デフォルト動作で一緒に削除される
    # models.SET_NULL, null=trueも合わせて設定 null許可。結合なしを許容。
    # models.SET_DEFALUT, default=somethingも合わせて設定 デフォルト値を設定
    # models.SET(function) functionのコール結果を設定。
    # models.DO_NOTHING 何もしない
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, help_text="貨幣情報")
    pub_date = models.DateTimeField(verbose_name="発行日時")
    name = models.CharField(max_length=50)
    alias = models.CharField(null=True, max_length=20, help_text="貨幣名称の別名（カナ表記など）")
    price = models.IntegerField(default=1)
    image = models.CharField(max_length=200, help_text="選択肢名")
    detail = models.CharField(default="", max_length=200, help_text="選択肢名")

    class Meta:
        db_table = "money"

# その他ORMのこと
# データがあれば返し、なければ作った結果を返す
# Category.objects.get_or_create(name="New")[0]


