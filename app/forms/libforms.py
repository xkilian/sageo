from flask.ext.wtf import Form
import wtforms.ext.i18n.form

class TranslatedForm(wtforms.ext.i18n.form.Form, Form):
    def __init__(self, **kwargs):
        super(TranslatedForm, self).__init__(**kwargs)

class TranslatedFormNoCsrf(wtforms.ext.i18n.form.Form, Form):
    def __init__(self, *args, **kwargs):
           kwargs['csrf_enabled'] = False
           super(TranslatedFormNoCsrf, self).__init__(*args, **kwargs)

