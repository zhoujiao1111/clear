#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/11/2 15:48
# @Author  : zhoujiao
import pymysql


def clear_imid(imid):
    db = pymysql.connect(
        host='rm-2zeti0v9e6940n93p2o.mysql.rds.aliyuncs.com',
        port=3306,
        user='web_user',
        passwd='l%meFN!Z88yRgrjz',
        charset='utf8'
    )
    cur = db.cursor()
    # 删除被邀请人订单
    sql_imid = [
        "DELETE FROM wm_entrepreneur.e_orders_big WHERE mid=%s",
        "DELETE FROM wm_entrepreneur.e_reward_log WHERE mid=%s",
        "DELETE FROM wm_entrepreneur.e_reward_detail_log WHERE mid=%s",
        "DELETE FROM wm_entrepreneur.e_wechat_transferinfo WHERE mid=%s",
        "DELETE FROM wm_entrepreneur.e_exchange_code WHERE mid=%s",
        "DELETE FROM wm_entrepreneur.e_exchange_code_record WHERE mid=%s",
        "DELETE FROM wm_order_center.t_order WHERE member_id=%s",
        "DELETE FROM `wm-pay-center`.t_trade_items WHERE member_id=%s",
    ]

    try:
        for i in sql_imid:
            print(i)
            cur.execute(i, imid)
            rows = cur.fetchall()
            print(rows)
        # 提交到数据库执行
        db.commit()
        print("删除数据成功")
    except Exception as e:
        print("删除数据失败：case%s" % e)
        # 发生错误时回滚
        db.rollback()
    finally:
        # 关闭游标连接
        cur.close()
        # 关闭数据库连接
        db.close()


def main():
    clear_imid(1631961689770050)


if __name__ == '__main__':
    main()

