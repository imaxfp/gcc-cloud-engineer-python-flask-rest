import logging
import os
from flask import Flask, render_template, request
import socket

logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s]: {} %(levelname)s %(message)s'.format(os.getpid()),
                    datefmt='%Y-%m-%d %H:%M:%S',
                    handlers=[logging.StreamHandler()])

logger = logging.getLogger()


def create_app():
    logger.info(f'Starting app in environment')
    app = Flask(__name__)
    # app.config.from_object('config')
    return app


app = create_app()


@app.route("/")
def index():
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        return render_template('index.html', hostname=host_name, ip=host_ip)
    except:
        return render_template('error.html')


@app.route("/upload")
def upload():
    try:
        return render_template('file_uploader.html')
    except:
        return render_template('error.html')


def upload_file_tmp(f):
    # Get a cgi.FieldStorage object
    upload = request.files.get('upload')

    # Get the data
    raw = upload.value

    # Write to file
    filename = upload.filename
    with open(filename, 'wb') as f:
        f.write(raw)

    return "You uploaded %s (%d bytes)." % (filename, len(raw))


@app.route('/pdf_file', methods=['GET', 'POST'])
def process_pdf_file():
    return '''
        <html>
        <body>
         Mock done! 
       </body>
       </html>
    '''


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
