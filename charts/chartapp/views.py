from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
import json
from django.shortcuts import render_to_response
from .models import Response

from chartapp.models import Response
# Create your views here.

def index(request):
	request_headers = {'x-api-key': 'c2ee00db1a75428981d49a5c74d24015'}
	request = urllib2.Request("https://fulfil_demo.fulfil.io/api/v1/model/sale.sale?field=reference&field=shipment_address.subdivision.code&field=shipment_address.country.code&filter=[[\"state\",\"=\",\"processing\"]]", headers=request_headers)
	opener = urllib2.build_opener()
	f = opener.open(request)
	jsonf=json.loads(f.read())
	for resp in jsonf:
		r=Response()
		r.recname=resp["rec_name"]
		r.reference=resp["reference"]
		r.idf=resp["id"]
		r.state=resp["shipment_address.subdivision.code"]
		r.country=resp["shipment_address.country.code"]
		r.save()
	template=loader.get_template('chartapp/index.html') 
	return HttpResponse(template.render())