import logging
import os
from flask import Flask, request

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
def hello():
    return '''
    <html>
    <body>
      <form action = "/pdf_file" method = "POST" 
         enctype = "multipart/form-data">
         <input type = "file" name = "file" />
         <input type = "submit"/>
      </form>   
   </body>
   </html>
'''


def upload_file_tmp(f):
    # Get a cgi.FieldStorage object
    upload = request.files.get('upload')

    # Get the data
    raw = upload.value;

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
    port = int(os.environ.get("PORT", 5005))
    app.run(debug=True, host='0.0.0.0', port=port)
