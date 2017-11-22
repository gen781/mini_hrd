from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

from karyawan.models import Karyawan
# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def profil(request):
	if request.session.has_key('karyawan_id'):
		karyawan = Karyawan.objects.get(id=request.session['karyawan_id'])
		return render(request, 'profil.html', {"karyawan": karyawan})
	else:
		return render(request, 'login.html', {})


