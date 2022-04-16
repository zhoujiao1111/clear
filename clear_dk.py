#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/3 11:16
# @Author  : zhoujiao
import pymysql


def Clear_Dk(mid):
    #打开数据库链接
    db = pymysql.connect(host='rm-2zeti0v9e6940n93p2o.mysql.rds.aliyuncs.com',
                         port=3306,
                         user='web_user',
                         passwd='l%meFN!Z88yRgrjz',
                         charset='utf8')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()

    # 删除创业家报名系统课相关信息
    sql_dk = [
        "delete from wm_order_center.t_order WHERE member_id=%s",
        "delete from wm_class.wm_order_landing WHERE uid=%s",
        "delete from wm_class.wm_user_property where user_id=%s",
        "delete from wm_class.wm_order_batch WHERE user_id=%s",
        "DELETE FROM wm_entrepreneur.e_orders WHERE mid=%s and type_order = 1",
        "DELETE FROM wm_entrepreneur.e_orders_big WHERE mid=%s",
    ]

    try:
        for i in sql_dk:
            print(i)
            cursor.execute(i,mid)
            rows = cursor.fetchall()
            print(rows)
        # 提交到数据库执行
        db.commit()
        print("删除数据成功")

    except Exception as e:
        print("删除数据失败：case%s" % e)
        # 发生错误时回滚
        db.rollback()
    finally:
        cursor.close()
        # 关闭数据库连接
        db.close()


def main():
    Clear_Dk(1631961689770050)


if __name__ == '__main__':
    main()