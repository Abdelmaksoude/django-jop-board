from .models import Jop
from .serializers import JopSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics

@api_view(['GET'])
def jop_list_api(request):
    all_jop = Jop.objects.all()
    data = JopSerializer(all_jop , many=True).data
    return Response({'data':data})

@api_view(['GET'])
def jop_detail_api(request , id):
    jop_detail = Jop.objects.get(id=id)
    data = JopSerializer(jop_detail).data
    return Response({'data':data})

# show for all jops and can add a new jop
class JopListApi(generics.ListCreateAPIView):
    queryset = Jop.objects.all()
    serializer_class = JopSerializer

# show one jop and you update and delete
class JopDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JopSerializer
    queryset = Jop.objects.all()
    lookup_field = 'id'