import pandas as pd

from flask import Flask,Response,request
import webbrowser
import threading
import requests
import time

file_csv = []

app = Flask(__name__)

@app.route('/shutdown', methods=['GET'])
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func:
        func()
    return "Server shutting down..."

@app.route('/')
def download_csv():
    
    global file_csv
    
    file_csv = pd.DataFrame(
        file_csv, # Hotel list
        columns=[
        'Name',
        'Room',
        'Log'
        ]
                        )
    
    threading.Timer(0.1,lambda: requests.get("http://127.0.0.1:5000/shutdown")).start()

    return Response(
            iter([file_csv.to_csv(index=False)]),
            mimetype="text/csv",
            headers={"Content-Disposition": "attachment; filename=Hotel_Room.csv"}
        )


def auto_open_browser():
    time.sleep(0.2) 
    webbrowser.open("http://127.0.0.1:5000/")

def run_flask():
    app.run(port=5000, debug=True, use_reloader=False)
def auto_download(data):
    global file_csv
    file_csv = data

    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread    .start()
   
    threading.Thread(target=auto_open_browser, daemon=True).start()
    
    start_time = time.time()
    while flask_thread.is_alive():
        if time.time() - start_time > 10:  # กันเผื่อกรณี error
            break
        time.sleep(0.5)


#------------------------------------------------------------------


# def auto_download(data):
#     df =  pd.DataFrame(
#         data, # Hotel list
#         columns=[
#         'Name',
#         'Room',
#         'Log'
#         ])
#     df.to_csv("Hotel_Room.csv", index=False, encoding='utf-8-sig')
    

if __name__ == "__main__":
    sample_data = [
        ["Alice", 101, "2025-10-99"],
        ["Bob", 102, "2025-10-08"],
        ["Charlie", 103, "2025-10-09"]
    ]
    auto_download(sample_data)