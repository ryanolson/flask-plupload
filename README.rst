==============
Flask-Plupload
==============

Flask-Plupload packages `Plupload <http://http://www.plupload.com/>`_ 
into an extension that mostly consists of a blueprint named 'plupload'. 

In the future, the extension will serve Plupload from a CDN as a release
option.

Usage
-----

Here is an example::

  from flask.ext.plupload import Plupload

  [...]

  plupload = Plupload()
  plupload.init_app(app)

The url-endpoint ``plupload.static`` is available for refering to Plupload
resources.::

  url_for('plupload.static', filename='...')

There are two example templates that host an upload page, you can use these as
a guide when generating your own upload templates.  Eventually, this package will
provides some useful macros and possibly templates to ease intergration.

Make sure you set the following flask config variables prior to initializing the
extension.

* PLUPLOAD_TEMPLATE - The name of the template used for rendering your upload
landing page. Defaults to 'plupload/uploader.html'
* PLUPLOAD_PATH - The path in which uploaded files will be stored.  Ensure proper
permissions are set.

