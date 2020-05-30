from functools import partial

def func(a,b):
    print(a,b)

res = partial(func, 'request')

# app.template_filter()
# def fit(a)
'''
{{ 123 | fit }}
'''

res(888)