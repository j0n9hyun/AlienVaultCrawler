# -*- coding: utf-8 -*-
from modules import *

AuditLog.audit_log_start()
Service.EnableService()
for i in tqdm((GetApi.dbs), ncols=100):
    cprint('\nid: %s' % i['id'], 'red')
    cprint('\nName: %s' % i['name'], 'green')
    cprint('Desc: %s' % i['description'], 'yellow')
    cprint('Revision: %s' % i['revision'], 'cyan')
    cprint('Tags: %s\033[0m' % i['tags'], 'blue')
    cprint('-' * 100, 'magenta')
    for idx, j in enumerate(i['indicators'], 1):
        try:
            if (IndicatorService.reputation_indicator(j['type'])):
                cprint('PASS', 'green')
            else:
                cprint('새로운 타입 발견', 'white', 'on_red')
                ConnectionDB.cur.execute(
                    "INSERT INTO reputation_indicator (id, indicator_name) values (default, %s)",
                    (j['type'], ))
                ConnectionDB.conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        Date = datetime.now(timezone('Asia/Seoul')).strftime(DateFormat)
        print('ID: %d' % j['id'])
        cprint('Indicator: %s' % j['indicator'], 'red')
        cprint('Type: %s' % j['type'], 'red')
        print('Created: %s' % str(j['created'].replace('T', ' ')))
        print('Registed: %s' % Date)
        cprint('=' * 100, 'cyan')
        # time.sleep(0.5)
        ConnectionDB.cur.execute(
            "INSERT INTO reputation_data (id, tid, title, description, service, indicator_type, indicator, reg_date, cre_date) values (default, %s, %s, %s, %s, %s, %s, %s, %s)",
            (i['id'], i['name'], i['description'], Service.ServiceIdx('AlienVault'),
             IndicatorService.idx_exists(
                 j['type']), j['indicator'], Date, j['created']))
        ConnectionDB.conn.commit()
        Duplication.duplication_remove()
    AuditLog.audit_log_end()
    cprint('작업 종료', 'yellow')