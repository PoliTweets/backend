# coding=utf-8

from django import forms
from models import *


from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe

class ButtonRadioFieldRenderer(forms.widgets.RadioFieldRenderer):

    def render(self):
        # return  mark_safe(u'%s' % u'\n'.join([u'%s'  % force_unicode(w) for w in self]))
        return mark_safe(u'<div class="answersContainer">\n%s\n</div>' %
                         u'\n'.join([u'<div class="answerButtonContainer">%s</div>'
                                     % force_unicode(w) for w in self]))


class ResultCreateForm(forms.Form):
    answer = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        answer = kwargs.pop('answer', None)
        super(ResultCreateForm, self).__init__(*args, **kwargs)
        self.fields['answer'] = forms.ChoiceField(choices=answer,
                                                  required=True,
                                                  widget=forms.RadioSelect(renderer=ButtonRadioFieldRenderer),
                                                  label=u"Votre réponse")
