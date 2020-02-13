from django.shortcuts import get_object_or_404, render, redirect


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, slug):
        #   Вытащить из базы по slug'у
        obj = self.model.objects.get(slug__iexact=slug)
        #   Связываем форму с данными из базы
        bound_form = self.model_form(instance=obj)

        return render(
            request,
            # 'blog/tag_update_form.html',
            self.template,
            {'form': bound_form, self.model.__name__.lower(): obj}
        )

    def post(self, request, slug):
        #   Вытащить из базы по slug'у
        obj = self.model.objects.get(slug__iexact=slug)
        #   Связываем форму с данными из базы
        bound_form = self.model_form(request.POST)

        if bound_form.is_valid():
            return redirect(bound_form.save())

        return render(
            request,
            # 'blog/tag_update_form.html',
            self.template,
            {'form': bound_form, self.model.__name__.lower(): obj}
        )


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, {self.model.__name__.lower(): obj})


class ObjectCreateMixin:
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model()
        return render(request, self.template, {'form': form})

    def post(self, request):
        bound_form = self.form_model(request.POST)

        if bound_form.is_valid():
            return redirect(bound_form.save())

        return render(request, self.template, {'form': bound_form})
