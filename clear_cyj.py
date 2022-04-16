#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/2 14:49
# @Author  : zhoujiao
import pymysql


def clear(mid,role):
    conn = pymysql.connect(host='rm-2zeti0v9e6940n93p2o.mysql.rds.aliyuncs.com',
                           port=3306,
                           user='web_user',
                           passwd='l%meFN!Z88yRgrjz',
                           charset='utf8')
    cur = conn.cursor()  # 使用cursor()方法获取操作游标
    # 清除大课订单
    dk_live = [
        "delete from wm_order_center.t_order WHERE member_id=%s",
        "delete from wm_class.wm_order_landing WHERE uid=%s",
        "delete from wm_class.wm_user_property where user_id=%s",
        "delete from wm_class.wm_order_batch WHERE user_id=%s",
    ]
    # 清除小白营订单
    xby_live = [
        "delete from wm_material_center.wm_materials_mail where mid=%s",
        "delete from weimiao.mh_infoflow_order where mid=%s",
        "delete from weimiao.mh_wxorder where mid=%s",
        "delete from wm_order_center.t_order where member_id=%s",
    ]
    # 清除创业家数据
    cyj = [
        "delete from wm_entrepreneur.e_orders WHERE mid =%s",
        "delete from wm_entrepreneur.e_orders_big WHERE mid =%s",
        "delete from wm_entrepreneur.e_reward_log WHERE invitee_mid =%s",
        "delete from wm_entrepreneur.e_reward_detail_log WHERE invitee_mid =%s",
        "delete from wm_order_center.t_order WHERE member_id =%s",
        "delete from `wm-pay-center`.t_trade_items where member_id =%s",
        "delete from wm_entrepreneur.e_wechat_transferinfo WHERE mid =%s",
        "delete from wm_entrepreneur.e_exchange_code_record WHERE mid =%s",
        "delete from wm_entrepreneur.e_exchange_code WHERE mid =%s",
        "delete from wm_entrepreneur.e_members WHERE mid=%s",
    ]
    if role == 'all':
        all = dk_live + xby_live + cyj
    for i in role:
        print("delete role %s" % i)
        for j in locals()[i]:
            print("sql: ",j)
            result = cur.execute(j, mid)
            if result == 1:
                print("affact line: ", result)
            conn.commit()  # 提交请求

    result = cur.fetchall()
    print("result:",result)
    # 关闭数据库连接
    cur.close()
    conn.close()


clear('1634873958998435',['dk_live','xby_live','cyj'])

