import pandas as pd
# from flask import Flask,Response
# import webbrowser
# import threading

# file_csv = []

# app = Flask(__name__)

# @app.route('/')
# def download_csv():
    
#     global file_csv

#     file_csv = pd.DataFrame(
#         file_csv, # Hotel list
#         columns=[
#         'Name',
#         'Room',
#         'Log'
#         ]
#                         )

#     return Response(
#             iter([file_csv.to_csv(index=False)]),
#             mimetype="text/csv",
#             headers={"Content-Disposition": "attachment; filename=Hotel_Room.csv"}
#         )

def auto_download(data):
    df =  pd.DataFrame(
        data, # Hotel list
        columns=[
        'Name',
        'Room',
        'Log'
        ])
    df.to_csv("Hotel_Room.csv", index=False, encoding='utf-8-sig')
    

if __name__ == "__main__":
    sample_data = [
        ["Alice", 101, "2025-10-99"],
        ["Bob", 102, "2025-10-08"],
        ["Charlie", 103, "2025-10-09"]
    ]
    auto_download(sample_data)