from django.db import models
"""
・マイグレーションを含む。完全にモデルのファイルから作る。
・削除時のタスク（応急処置）
  common/migration のマイグレーションファイル削除
- # テーブル削除
  mysql -u appuser images_scanner --password=apppass 

  delete from money;
  drop table money cascade;
  delete from money_type;
  drop table money_type cascade;
  delete from currency;
  drop table currency cascade; 
  delete from country;
  drop table country cascade;
  delete from auth_group;
  delete from auth_group_permissions;
  delete from auth_permission;
  delete from auth_user;
  delete from auth_user_groups;
  delete from auth_user_user_permissions;
  delete from django_content_type;
  delete from django_migrations;
  drop table auth_group_permissions cascade;
  drop table auth_user_groups cascade;
  drop table auth_user_user_permissions cascade;
  drop table django_migrations cascade;
  drop table auth_group cascade;
  drop table auth_permission cascade;
  drop table auth_user cascade;
  drop table django_content_type cascade;

- # Mygration
  python manage.py makemigrations # マイグレーションファイル作成
  python manage.py migrate # マイグレーション
"""

class Country(models.Model):
    """
    国マスタ

    @detail 国の言語や貨幣を定義
    """
    cd = models.CharField(primary_key=True, max_length=20,help_text="国コード")
    name = models.CharField(max_length=200, help_text="国名(英語表記)")
    detail = models.CharField(default="", max_length=200, help_text="詳細")
    memo = models.CharField(default="", max_length=500, help_text="メモ（内部用）")

    class Meta:
        db_table = "country"
