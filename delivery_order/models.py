#-*- coding=utf8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django import forms
class NameForms(forms.Form):
    name = forms.CharField(max_length=20)

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class TbBasicInfo(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    industry = models.TextField(blank=True, null=True)
    area = models.TextField(blank=True, null=True)
    pe = models.FloatField(blank=True, null=True)
    outstanding = models.FloatField(blank=True, null=True)
    totals = models.FloatField(blank=True, null=True)
    totalassets = models.FloatField(db_column='totalAssets', blank=True, null=True)  # Field name made lowercase.
    liquidassets = models.FloatField(db_column='liquidAssets', blank=True, null=True)  # Field name made lowercase.
    fixedassets = models.FloatField(db_column='fixedAssets', blank=True, null=True)  # Field name made lowercase.
    reserved = models.FloatField(blank=True, null=True)
    reservedpershare = models.FloatField(db_column='reservedPerShare', blank=True, null=True)  # Field name made lowercase.
    esp = models.FloatField(blank=True, null=True)
    bvps = models.FloatField(blank=True, null=True)
    pb = models.FloatField(blank=True, null=True)
    timetomarket = models.BigIntegerField(db_column='timeToMarket', blank=True, null=True)  # Field name made lowercase.
    undp = models.FloatField(blank=True, null=True)
    perundp = models.FloatField(blank=True, null=True)
    rev = models.FloatField(blank=True, null=True)
    profit = models.FloatField(blank=True, null=True)
    gpr = models.FloatField(blank=True, null=True)
    npr = models.FloatField(blank=True, null=True)
    holders = models.FloatField(blank=True, null=True)
    更新日期 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_basic_info'


class TbBlacklist(models.Model):
    date = models.DateTimeField(db_column='DATE')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', primary_key=True, max_length=6)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=60, blank=True, null=True)  # Field name made lowercase.
    reason = models.TextField(db_column='REASON', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_blacklist'


class TbBondJisilu(models.Model):
    可转债代码 = models.CharField(max_length=10, blank=True, null=True)
    可转债名称 = models.TextField(blank=True, null=True)
    可转债价格 = models.FloatField(blank=True, null=True)
    正股名称 = models.TextField(blank=True, null=True)
    正股代码 = models.TextField(blank=True, null=True)
    正股现价 = models.FloatField(blank=True, null=True)
    正股涨跌幅 = models.TextField(blank=True, null=True)
    最新转股价 = models.FloatField(blank=True, null=True)
    溢价率 = models.FloatField(blank=True, null=True)
    可转债涨幅 = models.TextField(blank=True, null=True)
    回售触发价 = models.FloatField(blank=True, null=True)
    转股起始日 = models.TextField(blank=True, null=True)
    到期时间 = models.TextField(blank=True, null=True)
    成交额_万元_field = models.FloatField(db_column='成交额(万元)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    强赎价格 = models.FloatField(blank=True, null=True)
    剩余时间 = models.TextField(blank=True, null=True)
    回售起始日 = models.TextField(blank=True, null=True)
    评级 = models.TextField(blank=True, null=True)
    发行时间 = models.TextField(blank=True, null=True)
    强制赎回条款 = models.TextField(blank=True, null=True)
    下修条件 = models.TextField(blank=True, null=True)
    下修提示 = models.TextField(blank=True, null=True)
    回售 = models.TextField(blank=True, null=True)
    下调次数 = models.BigIntegerField(blank=True, null=True)
    转债剩余占总市值比 = models.FloatField(blank=True, null=True)
    剩余规模 = models.TextField(blank=True, null=True)
    发行规模 = models.TextField(blank=True, null=True)
    股东配售率 = models.FloatField(blank=True, null=True)
    更新日期 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_bond_jisilu'


class TbBondJisiluModifyPrice(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    可转债代码 = models.TextField(blank=True, null=True)
    可转债名称 = models.TextField(blank=True, null=True)
    正股名称 = models.TextField(blank=True, null=True)
    正股代码 = models.TextField(blank=True, null=True)
    最新转股价 = models.FloatField(blank=True, null=True)
    转股起始日 = models.TextField(blank=True, null=True)
    剩余时间 = models.TextField(blank=True, null=True)
    更新日期 = models.TextField(blank=True, null=True)
    modified_date = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_bond_jisilu_modify_price'


class TbBondKindInfo(models.Model):
    可转债名称 = models.CharField(max_length=20, blank=True, null=True)
    可转债代码 = models.CharField(primary_key=True, max_length=10)
    正股名称 = models.CharField(max_length=20, blank=True, null=True)
    正股代码 = models.CharField(max_length=10, blank=True, null=True)
    地区 = models.CharField(max_length=10, blank=True, null=True)
    评级 = models.CharField(max_length=10, blank=True, null=True)
    板块概念 = models.CharField(max_length=400, blank=True, null=True)
    更新时间 = models.CharField(max_length=50, blank=True, null=True)
    最小值 = models.FloatField(blank=True, null=True)
    最小值_发生时间 = models.CharField(db_column='最小值-发生时间', max_length=16, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'tb_bond_kind_info'


class TbBondLowDownPrice(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    可转债代码 = models.TextField(blank=True, null=True)
    可转债名称 = models.TextField(blank=True, null=True)
    可转债价格 = models.FloatField(blank=True, null=True)
    正股名称 = models.TextField(blank=True, null=True)
    正股代码 = models.TextField(blank=True, null=True)
    正股现价 = models.FloatField(blank=True, null=True)
    正股涨跌幅 = models.TextField(blank=True, null=True)
    最新转股价 = models.FloatField(blank=True, null=True)
    溢价率 = models.FloatField(blank=True, null=True)
    可转债涨幅 = models.TextField(blank=True, null=True)
    回售触发价 = models.FloatField(blank=True, null=True)
    转股起始日 = models.TextField(blank=True, null=True)
    到期时间 = models.TextField(blank=True, null=True)
    成交额_万元_field = models.FloatField(db_column='成交额(万元)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    强赎价格 = models.FloatField(blank=True, null=True)
    剩余时间 = models.TextField(blank=True, null=True)
    回售起始日 = models.TextField(blank=True, null=True)
    评级 = models.TextField(blank=True, null=True)
    发行时间 = models.TextField(blank=True, null=True)
    强制赎回条款 = models.TextField(blank=True, null=True)
    下修条件 = models.TextField(blank=True, null=True)
    下修提示 = models.TextField(blank=True, null=True)
    回售 = models.TextField(blank=True, null=True)
    下调次数 = models.BigIntegerField(blank=True, null=True)
    转债剩余占总市值比 = models.FloatField(blank=True, null=True)
    剩余规模 = models.TextField(blank=True, null=True)
    发行规模 = models.TextField(blank=True, null=True)
    股东配售率 = models.FloatField(blank=True, null=True)
    更新日期 = models.TextField(blank=True, null=True)
    多少天内 = models.TextField(blank=True, null=True)
    维持 = models.TextField(blank=True, null=True)
    低于比例 = models.TextField(blank=True, null=True)
    当前比例 = models.FloatField(blank=True, null=True)
    how_many_day = models.TextField(blank=True, null=True)
    need_keep = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_bond_low_down_price'


class TbBondLowDownPrice20190102(models.Model):
    可转债代码 = models.TextField(blank=True, null=True)
    可转债名称 = models.TextField(blank=True, null=True)
    可转债价格 = models.FloatField(blank=True, null=True)
    正股名称 = models.TextField(blank=True, null=True)
    正股代码 = models.TextField(blank=True, null=True)
    最新转股价 = models.FloatField(blank=True, null=True)
    溢价率 = models.FloatField(blank=True, null=True)
    回售触发价 = models.FloatField(blank=True, null=True)
    转股起始日 = models.TextField(blank=True, null=True)
    到期时间 = models.TextField(blank=True, null=True)
    强赎价格 = models.FloatField(blank=True, null=True)
    剩余时间 = models.TextField(blank=True, null=True)
    回售起始日 = models.TextField(blank=True, null=True)
    评级 = models.TextField(blank=True, null=True)
    发行时间 = models.TextField(blank=True, null=True)
    转债剩余占总市值比 = models.FloatField(blank=True, null=True)
    股东配售率 = models.FloatField(blank=True, null=True)
    更新日期 = models.TextField(blank=True, null=True)
    需要的天数内 = models.TextField(blank=True, null=True)
    维持天数 = models.TextField(blank=True, null=True)
    低于比例 = models.TextField(blank=True, null=True)
    当前比例 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_bond_low_down_price_2019-01-02'


class TbBondLowDownPrice20190104(models.Model):
    可转债代码 = models.TextField(blank=True, null=True)
    可转债名称 = models.TextField(blank=True, null=True)
    可转债价格 = models.FloatField(blank=True, null=True)
    正股名称 = models.TextField(blank=True, null=True)
    正股代码 = models.TextField(blank=True, null=True)
    最新转股价 = models.FloatField(blank=True, null=True)
    溢价率 = models.FloatField(blank=True, null=True)
    回售触发价 = models.FloatField(blank=True, null=True)
    转股起始日 = models.TextField(blank=True, null=True)
    到期时间 = models.TextField(blank=True, null=True)
    强赎价格 = models.FloatField(blank=True, null=True)
    剩余时间 = models.TextField(blank=True, null=True)
    回售起始日 = models.TextField(blank=True, null=True)
    评级 = models.TextField(blank=True, null=True)
    发行时间 = models.TextField(blank=True, null=True)
    转债剩余占总市值比 = models.FloatField(blank=True, null=True)
    股东配售率 = models.FloatField(blank=True, null=True)
    更新日期 = models.TextField(blank=True, null=True)
    需要的天数内 = models.TextField(blank=True, null=True)
    维持天数 = models.TextField(blank=True, null=True)
    低于比例 = models.TextField(blank=True, null=True)
    当前比例 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_bond_low_down_price_2019-01-04'


class TbBondLowDownPrice20190108(models.Model):
    可转债代码 = models.TextField(blank=True, null=True)
    可转债名称 = models.TextField(blank=True, null=True)
    可转债价格 = models.FloatField(blank=True, null=True)
    正股名称 = models.TextField(blank=True, null=True)
    正股代码 = models.TextField(blank=True, null=True)
    最新转股价 = models.FloatField(blank=True, null=True)
    溢价率 = models.FloatField(blank=True, null=True)
    回售触发价 = models.FloatField(blank=True, null=True)
    转股起始日 = models.TextField(blank=True, null=True)
    到期时间 = models.TextField(blank=True, null=True)
    强赎价格 = models.FloatField(blank=True, null=True)
    剩余时间 = models.TextField(blank=True, null=True)
    回售起始日 = models.TextField(blank=True, null=True)
    评级 = models.TextField(blank=True, null=True)
    发行时间 = models.TextField(blank=True, null=True)
    转债剩余占总市值比 = models.FloatField(blank=True, null=True)
    股东配售率 = models.FloatField(blank=True, null=True)
    更新日期 = models.TextField(blank=True, null=True)
    需要的天数内 = models.TextField(blank=True, null=True)
    维持天数 = models.TextField(blank=True, null=True)
    低于比例 = models.TextField(blank=True, null=True)
    当前比例 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_bond_low_down_price_2019-01-08'


class TbBondRelease(models.Model):
    可转债代码 = models.CharField(max_length=10, blank=True, null=True)
    可转债名称 = models.CharField(max_length=10, blank=True, null=True)
    集思录建议 = models.CharField(max_length=500, blank=True, null=True)
    包销比例 = models.FloatField(blank=True, null=True)
    中签率 = models.FloatField(blank=True, null=True)
    上市日期 = models.CharField(max_length=20, blank=True, null=True)
    申购户数_万户_field = models.FloatField(db_column='申购户数（万户）', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    单账户中签_顶格_field = models.FloatField(db_column='单账户中签（顶格）', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    股东配售率 = models.FloatField(blank=True, null=True)
    评级 = models.CharField(max_length=8, blank=True, null=True)
    现价比转股价 = models.FloatField(blank=True, null=True)
    抓取时间 = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_bond_release'


class TbChinaclear(models.Model):
    crawl_time = models.TextField(blank=True, null=True)
    publish_date = models.TextField(blank=True, null=True)
    已开立a股账户投资者_自然人 = models.TextField(db_column='已开立A股账户投资者-自然人', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    已开立a股账户投资者_非自然人 = models.TextField(db_column='已开立A股账户投资者-非自然人', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    已开立b股账户投资者_自然人 = models.TextField(db_column='已开立B股账户投资者-自然人', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    已开立b股账户投资者_非自然人 = models.TextField(db_column='已开立B股账户投资者-非自然人', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    新增投资者数量 = models.TextField(blank=True, null=True)
    新增投资者数量_自然人 = models.TextField(db_column='新增投资者数量-自然人', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    新增投资者数量_非自然人 = models.TextField(db_column='新增投资者数量-非自然人', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    期末投资者数量 = models.TextField(blank=True, null=True)
    期末投资者数量_自然人 = models.TextField(db_column='期末投资者数量-自然人', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    期末投资者数量_非自然人 = models.TextField(db_column='期末投资者数量-非自然人', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    期末持仓投资者数量 = models.TextField(blank=True, null=True)
    期末持仓投资者数量_a股 = models.TextField(db_column='期末持仓投资者数量-A股', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    期末持仓投资者数量_b股 = models.TextField(db_column='期末持仓投资者数量-B股', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    期间参与交易的投资者数量 = models.TextField(blank=True, null=True)
    期间参与交易的投资者数量_a股 = models.TextField(db_column='期间参与交易的投资者数量-A股', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    期间参与交易的投资者数量_b股 = models.TextField(db_column='期间参与交易的投资者数量-B股', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'tb_chinaclear'


class TbChinaclear01(models.Model):
    publish_date = models.TextField(blank=True, null=True)
    新增投资者数量 = models.TextField(blank=True, null=True)
    新增投资者数量_自然人 = models.TextField(db_column='新增投资者数量-自然人', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    新增投资者数量_非自然人 = models.TextField(db_column='新增投资者数量-非自然人', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    期末投资者数量 = models.TextField(blank=True, null=True)
    期末投资者数量_自然人 = models.TextField(db_column='期末投资者数量-自然人', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    已开立a股账户投资者_自然人 = models.TextField(db_column='已开立A股账户投资者-自然人', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    已开立b股账户投资者_自然人 = models.TextField(db_column='已开立B股账户投资者-自然人', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    期末投资者数量_非自然人 = models.TextField(db_column='期末投资者数量-非自然人', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    已开立a股账户投资者_非自然人 = models.TextField(db_column='已开立A股账户投资者-非自然人', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    已开立b股账户投资者_非自然人 = models.TextField(db_column='已开立B股账户投资者-非自然人', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    期末持仓投资者数量 = models.BigIntegerField(blank=True, null=True)
    期末持仓投资者数量_a股 = models.BigIntegerField(db_column='期末持仓投资者数量-A股', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    crawl_time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_chinaclear01'


class TbChinaclearCopy1(models.Model):
    crawl_time = models.TextField(blank=True, null=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    已开立a股账户投资者_自然人 = models.TextField(db_column='已开立A股账户投资者-自然人', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    已开立a股账户投资者_非自然人 = models.TextField(db_column='已开立A股账户投资者-非自然人', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    已开立b股账户投资者_自然人 = models.TextField(db_column='已开立B股账户投资者-自然人', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    已开立b股账户投资者_非自然人 = models.TextField(db_column='已开立B股账户投资者-非自然人', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    新增投资者数量 = models.TextField(blank=True, null=True)
    新增投资者数量_自然人 = models.TextField(db_column='新增投资者数量-自然人', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    新增投资者数量_非自然人 = models.TextField(db_column='新增投资者数量-非自然人', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    期末投资者数量 = models.TextField(blank=True, null=True)
    期末投资者数量_自然人 = models.TextField(db_column='期末投资者数量-自然人', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    期末投资者数量_非自然人 = models.TextField(db_column='期末投资者数量-非自然人', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    期末持仓投资者数量 = models.TextField(blank=True, null=True)
    期末持仓投资者数量_a股 = models.TextField(db_column='期末持仓投资者数量-A股', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    期末持仓投资者数量_b股 = models.TextField(db_column='期末持仓投资者数量-B股', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    期间参与交易的投资者数量 = models.TextField(blank=True, null=True)
    期间参与交易的投资者数量_a股 = models.TextField(db_column='期间参与交易的投资者数量-A股', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    期间参与交易的投资者数量_b股 = models.TextField(db_column='期间参与交易的投资者数量-B股', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'tb_chinaclear_copy1'


class TbCnstock(models.Model):
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=3000, blank=True, null=True)  # Field name made lowercase.
    url = models.TextField(db_column='URL')  # Field name made lowercase.
    content = models.TextField(db_column='Content', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_cnstock'


class TbCurrentHold(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    当前日期 = models.TextField(blank=True, null=True)
    买入日期 = models.TextField(blank=True, null=True)
    代码 = models.TextField(blank=True, null=True)
    名字 = models.TextField(blank=True, null=True)
    买入价格 = models.FloatField(blank=True, null=True)
    当前价格 = models.FloatField(blank=True, null=True)
    今日涨幅 = models.FloatField(blank=True, null=True)
    目前盈亏 = models.FloatField(blank=True, null=True)
    买入原因 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_current_hold'

class TbJingzhi(models.Model):
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    assert_field = models.FloatField(db_column='Assert', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    netvalue = models.FloatField(db_column='NetValue', blank=True, null=True)  # Field name made lowercase.
    profit = models.FloatField(db_column='Profit', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_jingzhi'

class TbDeliveryGjDjango(models.Model):
    成交日期 = models.DateTimeField(blank=True, null=True)
    证券代码 = models.TextField(blank=True, null=True)
    证券名称 = models.TextField(blank=True, null=True)
    操作 = models.TextField(blank=True, null=True)
    成交数量 = models.FloatField(blank=True, null=True)
    成交均价 = models.FloatField(blank=True, null=True)
    成交金额 = models.FloatField(blank=True, null=True)
    余额 = models.FloatField(blank=True, null=True)
    发生金额 = models.FloatField(blank=True, null=True)
    手续费 = models.FloatField(blank=True, null=True)
    印花税 = models.FloatField(blank=True, null=True)
    过户费 = models.FloatField(blank=True, null=True)
    本次金额 = models.TextField(blank=True, null=True)
    其他费用 = models.TextField(blank=True, null=True)
    交易市场 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_delivery_gj_django'


class TbNewStockBond(models.Model):
    level_0 = models.BigIntegerField(blank=True, null=True)
    index = models.BigIntegerField(blank=True, null=True)
    可转债代码 = models.TextField(blank=True, null=True)
    可转债名称 = models.TextField(blank=True, null=True)
    可转债涨幅 = models.TextField(blank=True, null=True)
    可转债价格 = models.FloatField(blank=True, null=True)
    正股名称 = models.TextField(blank=True, null=True)
    正股代码 = models.TextField(blank=True, null=True)
    正股涨跌幅 = models.TextField(blank=True, null=True)
    正股现价 = models.FloatField(blank=True, null=True)
    最新转股价 = models.FloatField(blank=True, null=True)
    溢价率 = models.FloatField(blank=True, null=True)
    评级 = models.TextField(blank=True, null=True)
    转股起始日 = models.TextField(blank=True, null=True)
    回售起始日 = models.TextField(blank=True, null=True)
    回售触发价 = models.FloatField(blank=True, null=True)
    剩余时间 = models.TextField(blank=True, null=True)
    更新日期 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_new_stock_bond'


class TbSimulation(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    当前日期 = models.TextField(blank=True, null=True)
    买入日期 = models.TextField(blank=True, null=True)
    代码 = models.TextField(blank=True, null=True)
    名字 = models.TextField(blank=True, null=True)
    买入价格 = models.FloatField(blank=True, null=True)
    当前价格 = models.FloatField(blank=True, null=True)
    今日涨幅 = models.FloatField(blank=True, null=True)
    目前盈亏 = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_simulation'


class TbWinsertBond(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ce = models.TextField(blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    alias = models.TextField(db_column='Alias', blank=True, null=True)  # Field name made lowercase.
    code = models.TextField(db_column='Code', blank=True, null=True)  # Field name made lowercase.
    zgcode = models.TextField(blank=True, null=True)
    prefix = models.TextField(db_column='Prefix', blank=True, null=True)  # Field name made lowercase.
    position = models.BigIntegerField(blank=True, null=True)
    avg = models.FloatField(db_column='AVG', blank=True, null=True)  # Field name made lowercase.
    hprice = models.BigIntegerField(db_column='HPrice', blank=True, null=True)  # Field name made lowercase.
    lprice = models.BigIntegerField(db_column='LPrice', blank=True, null=True)  # Field name made lowercase.
    jian = models.FloatField(blank=True, null=True)
    jia = models.FloatField(blank=True, null=True)
    zhong = models.FloatField(blank=True, null=True)
    note = models.TextField(db_column='Note', blank=True, null=True)  # Field name made lowercase.
    zgdm = models.TextField(blank=True, null=True)
    zgqsr = models.TextField(blank=True, null=True)
    zgj = models.FloatField(blank=True, null=True)
    hsqsr = models.TextField(blank=True, null=True)
    hsj = models.FloatField(blank=True, null=True)
    dqr = models.TextField(blank=True, null=True)
    shj = models.FloatField(blank=True, null=True)
    zgjxt = models.TextField(blank=True, null=True)
    qzsh = models.TextField(blank=True, null=True)
    hs = models.TextField(blank=True, null=True)
    ll = models.TextField(blank=True, null=True)
    qs = models.BigIntegerField(blank=True, null=True)
    qss = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_winsert_bond'


class UsdRatio(models.Model):
    price = models.FloatField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usd_ratio'
