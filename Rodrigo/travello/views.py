from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

	dest1 = Destination()
	dest1.name='Arequipa'
	dest1.desc='The city'
	dest1.img = 'destination_1.jpg'
	dest1.price=700

	dest2 = Destination()
	dest2.name='Lima'
	dest2.desc='The city'
	dest2.img = 'destination_2.jpg'
	dest2.price=650

	dest3 = Destination()
	dest3.name='Trujillo'
	dest3.desc='The city'
	dest3.img = 'destination_3.jpg'
	dest3.price=750

	dests = [dest1,dest2,dest3]

	return render(request, 'index.html',{'dests': 	dests})