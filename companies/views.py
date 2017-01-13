from django.shortcuts import render, get_object_or_404
from .models import Companies

def get_company_id(request, company_id):
	company = get_object_or_404(Companies, company_id=company_id)
	return render(request, 'company.html', {'company_id': company})