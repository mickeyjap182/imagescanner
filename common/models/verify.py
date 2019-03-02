from django.db import models

class Verify(models.Model):
    """
    国マスタ

    @detail 国の言語や貨幣を定義
    """
    cd = models.CharField(primary_key=True, max_length=20,help_text="国コード")
    name = models.CharField(max_length=200, help_text="国名(英語表記)")
    detail = models.CharField(default="", max_length=200, help_text="詳細")
    memo = models.CharField(default="", max_length=500, help_text="メモ（内部用）")

    class Meta:
        db_table = "verify"
