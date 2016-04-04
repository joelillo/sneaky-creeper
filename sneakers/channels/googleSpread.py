# Authors: Gabriel Butterick and Bonnie Ishiguro


import time
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

from sneakers.modules import Channel

class Googlespread(Channel):
    description = """\
        Posts data to Google Spreadsheets.
    """

    requiredParams = {
        'sending': {
            'keyfile': '',
            'google_sheet': ''},
        'receiving': {
            'keyfile': '',
            'google_sheet': ''
        }
    }

    # Courtesy Limit: 10,000,000 queries/day

    def send(self, data):

        send_params = self.params['sending']

        KEYFILE = send_params['keyfile']
        GOOGLE_SPREAD = send_params['google_sheet']

        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(KEYFILE, scope)
        gc = gspread.authorize(credentials)
        sheet = gc.open(GOOGLE_SPREAD).sheet1

        WRITE_COL = 'A'
        row = 1
        if sheet.acell(WRITE_COL+str(row)).value:
            row += 1
        cell = WRITE_COL + str(row)

        sheet.update_acell(cell, data)
        return

    def receive(self):

        rec_params = self.params['receiving']

        KEYFILE = rec_params['keyfile']
        GOOGLE_SPREAD = rec_params['google_sheet']

        scope = ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(KEYFILE, scope)
        gc = gspread.authorize(credentials)
        sheet = gc.open(GOOGLE_SPREAD).sheet1

        READ_COL = 'A'
        
        cells = []
        row = 1

        while sheet.acell(READ_COL+str(row)).value:
            cells.append(sheet.acell(READ_COL+str(row)).value)
            row += 1

        return cells