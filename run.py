from helpers import *
from flask import Flask, send_file
from constants import SERVER_PATH, PROJECT, COVER_HTML

app = Flask(__name__)

@app.route("/getconversion/bce-daily/<currencyTarget>")
def GetConversionBCE(currencyTarget):
    provider="BCE-daily"
    if not SERVER_PATH["temp"] == "":
        path=SERVER_PATH["temp"]
        filename= ZebraCLI.Convert(currencyTarget, provider)
        file_directory = f"{path}/{filename}"
    else:
        file_directory=ZebraCLI.Convert(currencyTarget, provider)

    return send_file(file_directory,as_attachment=True)


@app.route("/")
def Cover():
    cover= f"""
<b>Title: {PROJECT["name"]}</b><br>
<br>
Description: {PROJECT["description"]}<br>
<br>
{COVER_HTML["Logo"]}<br>
<br>
{COVER_HTML["copyright_text"]}<br>
<br>
{COVER_HTML["Guide"]}<br>
"""
    print(cover)

    return cover

if __name__ == "__main__":
    app.run()


    

