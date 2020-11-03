#! /usr/bin/env python3
'''dict'''

TMPL = '''
<html>
    <title>{title}</title>
        <body>
            <div>{content}</div>
        </body>
</html>
'''

XIAOZHAO = {'name': 'xiaozhao', 'age': 23}
PEOPLE = dict([('name', 'jiujiu'), ('age', 34)])
PEOPLE2 = dict(name='lala', age=44)

print(XIAOZHAO)
print(PEOPLE, PEOPLE['name'])
PEOPLE['name'] = 'dajiaozhitou'
print(PEOPLE, PEOPLE['name'])
print(PEOPLE2)
print(len(PEOPLE2))
print("{name}".format_map(XIAOZHAO))
print(TMPL.format_map({'title': 'nihao', 'content': 'hahaha'}))
print(type(type(XIAOZHAO)))
# [8:12]
