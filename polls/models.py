# from django.db import models
#
# """
# ・マイグレーションを含む。完全にモデルのファイルから作る。
# """
#
# class Question(models.Model) :
#     """
#     投票項目
#     """
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#
# class Choice(models.Model) :
#     """
#     選択肢
#     """
#     # on_delete : 削除時の動作設定をする
#     # models.PROTECT 保護する。デフォルト動作で、参照されていたら削除できなくする。
#     # models.CASCADE デフォルト動作で一緒に削除される
#     # models.SET_NULL, null=trueも合わせて設定 null許可。結合なしを許容。
#     # models.SET_DEFALUT, default=somethingも合わせて設定 デフォルト値を設定
#     # models.SET(function) functionのコール結果を設定。
#     # models.DO_NOTHING 何もしない
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, help_text="投票項目の外部キー")
#     choice_text = models.CharField(max_length=200, help_text="選択肢名")
#     votes = models.IntegerField(defalut=0)
#
# # その他ORMのこと
# # データがあれば返し、なければ作った結果を返す
# # Category.objects.get_or_create(name="New")[0]