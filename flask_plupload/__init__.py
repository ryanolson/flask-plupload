# -*- coding: utf-8 -*-
import os

from flask import Blueprint, request, url_for, render_template, jsonify
from werkzeug import secure_filename

__version__ = "2.1.1-1"

class Plupload(object):
    def __init__(self, app=None, **kwargs):
        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app, **kwargs):
        blueprint = Blueprint(
            'plupload',
            __name__,
            template_folder='templates',
            static_folder='static',
            static_url_path=app.static_url_path + '/plupload'
        )
        self.upload_tmpl = app.config.get("PLUPLOAD_TEMPLATE", 'plupload/uploader.html')
        self.upload_path = app.config.get("PLUPLOAD_PATH", None)
        self.allowed_exts = app.config.get("PLUPLOAD_ALLOWED_EXTS", set([]))

        @blueprint.route('/', methods=['GET', 'POST'])
        def upload():
            if request.method == 'POST':
                saved_file_urls = []
                for key, file in request.files.iteritems():
                    if file: # and allowed_file(fie.filename):
                        filename = secure_filename(file.filename)
                        file.save(os.path.join(self.upload_path, filename))
                        saved_file_urls.append(url_for('.files', filename=filename))
                return jsonify(dict(saved_file_urls=saved_file_urls))
            return render_template(self.upload_tmpl)

        @blueprint.route('/files/<filename>')
        def files(filename):
            return send_from_directory(self.upload_path, filename)

        app.register_blueprint(blueprint, **kwargs)

