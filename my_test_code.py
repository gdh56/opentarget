#!/usr/bin/python

from argparse import ArgumentParser
import requests
from scipy import stats
import json

class RequestProcessor(object):

    def __init__(self):
        self.endpoint_url = 'https://api.opentargets.io/v3/platform/public/evidence/filter'

    def make_target_id_request(self, target_id):
        raw_data = requests.post(self.endpoint_url, json={'target_id': [target_id]})
        score_list = []
        data = json.loads(raw_data.content)
        for data_point in data['data']:
            score_list.append(float(data_point['scores']['association_score']))
        print str(stats.describe(score_list))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-t', '--target-id', nargs='?')
    args = parser.parse_args()
    target_id = args.target_id
    processor = RequestProcessor()
    processor.make_target_id_request(target_id)


