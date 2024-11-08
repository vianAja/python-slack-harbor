#!/usr/bin/env python3

from flask import Flask, request, jsonify
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import datetime

app = Flask(__name__)


def scrapping(data):
    typeEvent = data.get('type')
    waktu = datetime.datetime.fromtimestamp(data['occur_at'])
    user = data['operator']
    image = data['event_data']['resources'][0]['resource_url']
    level_Vulnerability = data['event_data']['resources'][0]['scan_overview']['application/vnd.security.vulnerability.report; version=1.1']['severity']
    total_vulnerability = data['event_data']['resources'][0]['scan_overview']['application/vnd.security.vulnerability.report; version=1.1']['summary']['total']
    detail_vulnerability = data['event_data']['resources'][0]['scan_overview']['application/vnd.security.vulnerability.report; version=1.1']['summary']['summary']
    template_json = [
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': f'Event: *{typeEvent}*'
                    }
                },
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': f'Waktu: *{waktu}*'
                    }
                },
                                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': f'User: *{user}*'
                    }
                },
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': f'Nama Images: *{image}*'
                    }
                },
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': f'Level Vulnerability: *{level_Vulnerability}*'
                    }
                },
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': f'Jumlah Total Vulnerability: *{total_vulnerability}*'
                    }
                },
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': f'Jumlah Critical: *{detail_vulnerability["Critical"]}*'
                    }
                },
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': f'Jumlah High: *{detail_vulnerability["High"]}*'
                    }
                },
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': f'Jumlah Medium: *{detail_vulnerability["Medium"]}*'
                    }
                },
                {
                    'type': 'section',
                    'text': {
                        'type': 'mrkdwn',
                        'text': f'Jumlah Low: *{detail_vulnerability["Low"]}*'
                    }
                }
            ]
    return template_json

@app.route('/test', methods=['POST'])
def handle_request():
    data = request.get_json()
    hasil = scrapping(data)
    response_data = {
        "message": "Data berhasil diterima",
        "received_data": 'aman'
    }
    token_slack = "TOKEN_OAUTH"
    channel_id = "CHANNEL_ID_SLACK"
    name_bot = "NAME_BOT"
    client = WebClient(token=token_slack)
    try:
        response = client.chat_postMessage(
            channel=channel_id,
            blocks=hasil,
            username=name_bot
        )
        print("sukses")
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")

    # Mengembalikan respon JSON
    return jsonify(response_data), 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
