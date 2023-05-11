from flask import Flask, render_template, request, jsonify
import unix_utc_time as unix_utc_time

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/<string:date>', methods=['GET'])
def api(date):
    if request.method == 'GET':
        if date.isdigit():
            num = int(date)
            answer = unix_utc_time.unix_to_utc(num)
            json_answer = {
                "unix": num,
                "utc": answer,
            }
            return jsonify(json_answer)
        else:
            arr = date.split('-')
            if len(arr) == 3 and all(i.isdigit() for i in arr):
                answer = unix_utc_time.utc_to_unix(date)
                json_answer = {
                    "unix": answer[0],
                    "utc": answer[1],
                }
                return jsonify(json_answer)
            else:
                return jsonify({"error": "Invalid Date"})


if __name__ == '__main__':
    app.run()
