from django.shortcuts import render, redirect
from .models import FinancialDocument
from .forms import DocumentForm

def upload_document(request, company_id):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.company_id = company_id
            document.save()
            return redirect('company_list')
    else:
        form = DocumentForm()
    return render(request, 'upload_document.html', {'form': form})
