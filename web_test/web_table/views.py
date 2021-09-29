from django.shortcuts import render
from web_table.models import ShowTable, ShowTableFilter
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from web_table.forms import ShowTableFilterForm


class TableListView(ListView):
    column_to_field = {
        'Название': 'title',
        'Количество': 'quantity',
        'Расстояние': 'distance_entity'
    }
    condition_to_cond = {
        'Равно': '__exact',
        'Содержит': '__contains',
        'Больше': '__gt',
        'Меньше': '__lt'
    }
    model = ShowTable, ShowTableFilter
    template_name = 'web_table/webtable_list.html'

    def post(self, request):
        form = ShowTableFilterForm(data=request.POST)
        context = {'form': form}
        col = request.POST['column']
        cond = request.POST['condition']
        val = request.POST['value_input']

        if 'clean_session' in request.POST:
            request.session['col'] = ''
            request.session['cond'] = ''
            request.session['val'] = ''
            col = ''
            cond = ''
            val = ''

        if len(col) and len(cond) and len(val):
            col = self.column_to_field[col]
            cond = self.condition_to_cond[cond]
            object_list = ShowTable.objects.filter(**{f'{col}{cond}': val})
            request.session['col'] = col
            request.session['cond'] = cond
            request.session['val'] = val
        else:
            object_list = ShowTable.objects.all()

        paginator = Paginator(object_list, 10)
        page = request.POST.get('page')
        try:
            object_list = paginator.page(page)
        except PageNotAnInteger:
            object_list = paginator.page(1)
        except EmptyPage:
            object_list = paginator.page(paginator.num_pages)
        context.update({'object_list': object_list})
        return render(request, self.template_name, context)

    def get_queryset(self):
        form = ShowTableFilterForm()
        col = self.request.session.get('col', '')
        cond = self.request.session.get('cond', '')
        val = self.request.session.get('val', '')
        if len(col) and len(cond) and len(val):
            object_list = ShowTable.objects.filter(**{f'{col}{cond}': val})
        else:
            object_list = ShowTable.objects.all()
        self.queryset = {'form': form, 'object_list': object_list}
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super(TableListView, self).get_context_data(**kwargs)
        if self.request.method == 'POST':
            form = context['form']
            object_list = context['object_list']
            context['object_list'] = object_list
            context['form'] = form
        else:
            form = self.queryset['form']
            object_list = self.queryset['object_list']
            context['form'] = form
            context['object_list'] = object_list

        paginator = Paginator(context['object_list'], 10)
        page = self.request.GET.get('page')
        try:
            context['object_list'] = paginator.page(page)
        except PageNotAnInteger:
            context['object_list'] = paginator.page(1)
        except EmptyPage:
            context['object_list'] = paginator.page(paginator.num_pages)
        return context
