# coding=utf-8
"""
#通过id检验验证码是否存在，通过goods查找商品
"""
import base64
coupon = {
    'id': '1231',
    'goods': '0001',
    'name': 'iphone',
}


def gen_coupon(coupon):

    raw = '/'.join([k+':'+v for k,v in coupon.items()])
    raw_64 = base64.urlsafe_b64encode(raw.encode('utf-8'))
    c_code = raw_64.decode()
    return c_code


def parse_coupon(c_code):
    de_coupon = base64.urlsafe_b64decode(c_code.encode('utf-8'))
    return de_coupon


print(gen_coupon(coupon))
print(parse_coupon('Z29vZHM6MDAwMS9pZDoxMjMxL25hbWU6aXBob25l'))
