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



class TbBlacklist(models.Model):
    date = models.DateTimeField(db_column='DATE')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', primary_key=True, max_length=6)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=60, blank=True, null=True)  # Field name made lowercase.
    reason = models.TextField(db_column='REASON', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_blacklist'

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

class TbJingzhi2019(models.Model):
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    assert_field = models.FloatField(db_column='Assert', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    netvalue = models.FloatField(db_column='NetValue', blank=True, null=True)  # Field name made lowercase.
    profit = models.FloatField(db_column='Profit', blank=True, null=True)  # Field name made lowercase.
    hs300 = models.FloatField(db_column='HS300', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_jingzhi_gj_2019'

class TbJingzhi2020(models.Model):
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    assert_field = models.FloatField(db_column='Assert', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    netvalue = models.FloatField(db_column='NetValue', blank=True, null=True)  # Field name made lowercase.
    profit = models.FloatField(db_column='Profit', blank=True, null=True)  # Field name made lowercase.
    hs300 = models.FloatField(db_column='HS300', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_jingzhi_gj_2020'

class TbJingzhiHB2020(models.Model):
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    assert_field = models.FloatField(db_column='Assert', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    netvalue = models.FloatField(db_column='NetValue', blank=True, null=True)  # Field name made lowercase.
    profit = models.FloatField(db_column='Profit', blank=True, null=True)  # Field name made lowercase.
    hs300 = models.FloatField(db_column='HS300', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'tb_jingzhi_hb_2020'

class TbJingzhiHB2021(models.Model):
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    assert_field = models.FloatField(db_column='Assert', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.


    netvalue = models.FloatField(db_column='NetValue', blank=True, null=True)  # Field name made lowercase.
    profit = models.FloatField(db_column='Profit', blank=True, null=True)  # Field name made lowercase.
    hs300 = models.FloatField(db_column='HS300', blank=True, null=True)  # Field name made lowercase.
    cash = models.FloatField(db_column='Cash', blank=True, null=True)  # Field name made lowercase.
    position = models.FloatField(db_column='Position', blank=True, null=True )  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_jingzhi_hb_2021'

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

class TbDeliveryHbDjango(models.Model):
    成交日期 = models.DateTimeField(blank=True, null=True)
    证券代码 = models.TextField(blank=True, null=True)
    证券名称 = models.TextField(blank=True, null=True)
    委托类别 = models.TextField(blank=True, null=True)
    成交数量 = models.FloatField(blank=True, null=True)
    成交价格 = models.FloatField(blank=True, null=True)
    成交金额 = models.FloatField(blank=True, null=True)
    发生金额 = models.FloatField(blank=True, null=True)
    佣金 = models.FloatField(blank=True, null=True)
    印花税 = models.FloatField(blank=True, null=True)
    过户费 = models.FloatField(blank=True, null=True)
    本次金额 = models.TextField(blank=True, null=True)
    其他费 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tb_delivery_hb_django'




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


