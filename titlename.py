# -*- coding: utf-8 -*-
from modules import *
import time

while 1:
    # AuditLog.audit_log_start()
    # Service.EnableService()
    for i in tqdm((GetApi.dbs), ncols=100):
        cprint('\nid: %s\033[0m' % i['id'], 'red')
        cprint('Name: %s' % i['name'], 'green')
        cprint('Desc: %s' % i['description'], 'yellow')
        cprint('Revision: %s' % i['revision'], 'cyan')
        cprint('Tags: %s\033[0m' % i['tags'], 'blue')
        cprint('-' * 100, 'magenta')
        time.sleep(1)
        ConnectionDB.cur.execute(
            "INSERT INTO reputation_info (id, id_value, name, description) values (default, %s, %s, %s)",
            (i['id'], i['name'], i['description']))
        ConnectionDB.conn.commit()
    Test()