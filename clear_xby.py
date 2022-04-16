#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/3 11:16
# @Author  : zhoujiao
import pymysql


def Clear_Xby(mid):
    #打开数据库链接
    db = pymysql.connect(host='rm-2zeti0v9e6940n93p2o.mysql.rds.aliyuncs.com',
                           port=3306,
                           user='web_user',
                           passwd='l%meFN!Z88yRgrjz',
                           charset='utf8')
    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    # 删除创业家报名小白营课程相关信息
    sql_xby = [
        "delete from wm_material_center.wm_materials_mail where mid=%s",
        "delete from weimiao.mh_infoflow_order where mid=%s",
        "delete from weimiao.mh_wxorder where mid=%s",
        "delete from wm_order_center.t_order where member_id=%s",
        "DELETE FROM wm_entrepreneur.e_orders WHERE mid=%s and type_order = 0",
    ]
    try:
        for i in sql_xby:
            print(i)
            cur.execute(i,mid)
            rows = cur.fetchall()
            print(rows)
        db.commit()
        print("删除成功")
    except Exception as e:
        print("删除数据失败：case%s" % e)
    # 发生错误时回滚
        db.rollback()
    finally:
        cur.close()
        db.close()


def main():
    Clear_Xby(1625048238890429)


if __name__ == '__main__':
    main()