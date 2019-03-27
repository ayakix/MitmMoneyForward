#!/usr/bin/env python3

from mitmproxy import ctx
import json

def configure(updated):
    ctx.log.info('Loaded')

def response(flow):
    if flow.request.url.find('moneyforward.com/sp2') == -1:
        return

    if flow.request.url.find('home_summary') > -1:
        content = json.loads(flow.response.content.decode(encoding='utf-8'))
        content['user_asset']['total'] = 14395737542
        content['user_asset']['vs_last_day'] = 1582367
        content['sum_by_category'][0]['income'] = 9485783
        content['sum_by_category'][0]['expense'] = 384573
        content['sum_by_category'][0]['balance'] = 9101210
        flow.response.text = json.dumps(content)

#     if flow.request.url.find('account_summaries') > -1:
#         with open('./account_summaries.json', "r") as file:
#             flow.response.text = file.read()

