import gviz_api
import urllib2
import json
from django.shortcuts import render_to_response

#response = urllib2.urlopen("https://fulfil_demo.fulfil.io/api/v1/model/sale.sale?field=reference&field=shipment_address.subdivision.code&field=shipment_address.country.code&filter=[[\"state\",\"=\",\"processing\"]]?api_key=c2ee00db1a75428981d49a5c74d24015")
#data = json.load(response)   
request_headers = {'x-api-key': 'c2ee00db1a75428981d49a5c74d24015'}
request = urllib2.Request("https://fulfil_demo.fulfil.io/api/v1/model/sale.sale?field=reference&field=shipment_address.subdivision.code&field=shipment_address.country.code&filter=[[\"state\",\"=\",\"processing\"]]", headers=request_headers)
opener = urllib2.build_opener()
f = opener.open(request)
json = json.loads(f.read())
#print json
#contents = urllib2.urlopen(request)
#data = json.load(contents)   
#print contents;
#print data
#def main():
  # Creating the data
description = {
                 
                 
                 "shipment_address.subdivision.code": ("string", "State"),
                 "id": ("number", "ID")}

data_table = gviz_api.DataTable(description)
data_table.LoadData(json) 
jsonData= data_table.ToJSon(columns_order=("shipment_address.subdivision.code","id"))             
#print jsonData

def my_view(request):
    #mylist = ['item 1', 'item 2', 'item 3']

    return render_to_response('test7.html', {'jd':jd})