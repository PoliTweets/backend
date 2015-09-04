from django import forms
from models import *


from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

class ButtonRadioFieldRenderer(forms.widgets.RadioFieldRenderer):

    def render(self):
        # return  mark_safe(u'%s' % u'\n'.join([u'%s'  % force_unicode(w) for w in self]))
        return mark_safe(u'<div class="answersContainer">\n%s\n</div>' %
                         u'\n'.join([u'<div class="answerButtonContainer"><button class="btn btn-primary btn-lg" type="submit">%s</button></div>'
                                     % force_unicode(w) for w in self]))


class ResultCreateForm(forms.Form):
    answer = forms.ChoiceField(required=True, widget=forms.RadioSelect(renderer=ButtonRadioFieldRenderer))

    def __init__(self, choices=None, initial=None):
        super(ResultCreateForm, self).__init__()
        self.fields['answer'].choices = choices


