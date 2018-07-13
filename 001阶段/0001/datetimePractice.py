# coding=utf-8

# time & datetime 练习
'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''

'''
------------------------------------------------------------------------------------
From                       |To                        |Use                         |
seconds since the epoch    |struct_time in UTC        |gmtime(([secs])             |
seconds since the epoch    |struct_time in local time |localtime(([secs])          |
struct_time in UTC         |seconds since the epoch   |calendar.timegm()           |
struct_time in local time  |seconds since the epoch   |mktime()                    |
struct_time                |Formatting time           |strftime([9-item sequence]) |
------------------------------------------------------------------------------------
'''

import time

#获取时间戳
now_timestamp = time.time()
#获取结构化时间
now_time = time.localtime()
#格式化时间
now_ftime = time.strftime('%Y-%m-%d %H:%M:%S', now_time)
#now_ftime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

print("当前时间戳:\t", now_timestamp)
print("当前时间:\t", now_time)
print("格式化时间:\t", now_ftime)


