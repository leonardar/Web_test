from django import forms
from web_table.models import ShowTableFilter


class ShowTableFilterForm(forms.ModelForm):
    class Meta:
        model = ShowTableFilter
        fields = ('column', 'condition', 'value_input')

    def __init__(self, *args, **kwargs):
        super(ShowTableFilterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = ''
