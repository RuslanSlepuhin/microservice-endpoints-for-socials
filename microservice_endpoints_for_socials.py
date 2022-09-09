import ast

from flask import Flask, request, Response, render_template, jsonify
import os

server = Flask(__name__)

@server.route('/', methods=['GET'])
def get_message():
    return f'MicroService is working\n' \
           f'End-points:\n' \
           f'/auth\n' \
           f'/auth-callback\n' \
           f'signin-linkedin', 200


@server.route('/auth', methods=['POST', 'GET'])
def auth_tiktok():
    global data
    if request.method == 'POST':
        data = ast.literal_eval(request.data.decode('utf-8'))
        print('auth/(TikTok) = ', data)
        return jsonify(data)

    if request.method == 'GET':
        return data


@server.route('/auth-callback', methods=['POST', 'GET'])
def auth_callback_tiktok():
    global data
    if request.method == 'POST':
        data = ast.literal_eval(request.data.decode('utf-8'))
        print('auth/(TikTok) = ', data)
        return jsonify(data)

    if request.method == 'GET':
        return data


@server.route('/signin-linkedin', methods=['POST', 'GET'])
def signin_linkedin_linkedin():
    global data
    if request.method == 'POST':
        data = ast.literal_eval(request.data.decode('utf-8'))
        print('auth/(TikTok) = ', data)
        return jsonify(data)

    if request.method == 'GET':
        return data


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

