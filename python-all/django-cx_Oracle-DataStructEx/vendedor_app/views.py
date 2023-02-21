from rest_framework.response import Response
from rest_framework import status, generics
from drf_yasg.utils import swagger_auto_schema

from .serializers import (
    VendedorSerializer,
    VendedorSearchSerializer,
    VendedorListSerializer,
    VendedorCreateSerializer,
    VendedorUpdateSerializer,
)
from empresa_app.serializers import GenericSelectDataSerializer
from .controllers import VendedorController
from .pagination import CustomPageNumberPagination


class ListVendedores(generics.ListAPIView):
    serializer_class = VendedorListSerializer
    http_method_names = ['get', 'head', 'options']
    
    def get(self, request, id_unn: int, id_emp: int):
        result = VendedorController.list_vendors(id_unn=id_unn, id_emp=id_emp)
        if result: 
            return Response(result)
            
        return Response({'message': 'Vendedores não encontrados.'}, status=status.HTTP_400_BAD_REQUEST)


class SearchVendedor(generics.CreateAPIView):
    serializer_class = VendedorSearchSerializer
    http_method_names = ['post', 'head', 'options']
    
    def post(self, request):
        serializer = VendedorSearchSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            result = VendedorController.search_ven(serialized_data=serializer.data)
        
        if result:
            return Response({'vendedor': result})
            
        return Response({'message': 'Vendedor não encontrado.'}, status=status.HTTP_400_BAD_REQUEST)


class SearchVendedoresPaginada(generics.ListAPIView):
    serializer_class = VendedorListSerializer
    pagination_class = CustomPageNumberPagination
    http_method_names = ['get', 'head', 'options']
    
    def get(self, request, id_unn: int, id_emp: int, id_ven: int):
        paginator = CustomPageNumberPagination()
        paginator.page_size = int(request.GET.get('count') or paginator.page_size)
        result = VendedorController.retrieve_many(id_unn=id_unn, id_emp=id_emp, id_ven=id_ven, limit=paginator.page_size)
        # paginator.page_query_param = page_query_param
        
        print(paginator.page_size)
        
        if result and len(result):
            paginator.paginate_queryset(queryset=result, request=request)
            return paginator.get_paginated_response(result)
            
        return Response({'message': 'Vendedores não encontrados.'}, status=status.HTTP_400_BAD_REQUEST)

    
class CreateVendedor(generics.CreateAPIView):
    serializer_class = VendedorCreateSerializer
    http_method_names = ['post', 'head', 'options']

    def post(self, request):
        serializer = VendedorCreateSerializer(data=request.data)
        print('serializer:', serializer)
        print('request.data:', request.data)

        if serializer.is_valid(raise_exception=True):
            try:
                created = VendedorController.create(serialized_data=serializer.data)
                print('created:', created)
            
                if created:
                    return Response(created, status=status.HTTP_201_CREATED)
            except Exception as e:
                mensagem = e.args[0]    
                return Response({"message": mensagem}, status=status.HTTP_400_BAD_REQUEST)
            if created:
                return Response(created, status=status.HTTP_201_CREATED)
        else:    
            return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        
        return Response({"message": "Erro desconhecido!"}, status=status.HTTP_400_BAD_REQUEST)


class UpdateVendedor(generics.UpdateAPIView):
    serializer_class = VendedorUpdateSerializer
    http_method_names = ['patch', 'head', 'options']

    def patch(self, request):
        serializer = VendedorUpdateSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            updated = VendedorController.update(serialized_data=serializer.data)
            
            if updated:
                return Response(updated, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response({"message": "Erro desconhecido."}, status=status.HTTP_400_BAD_REQUEST)


class DestroyVendedor(generics.DestroyAPIView):
    # serializer_class = 
    http_method_names = ['delete', 'head', 'options']
    
    def delete(self, request, id_unn: int, id_emp: int, id_ven: int):
        success = VendedorController.destroy(id_unn=id_unn, id_emp=id_emp, id_ven=id_ven)
        
        if success:
            return Response(status=status.HTTP_204_NO_CONTENT)
       
        return Response({"message": "Não foi possível apagar o registro."}, status=status.HTTP_400_BAD_REQUEST)


class ListTipoVendedor(generics.RetrieveAPIView):
    serializer_class = GenericSelectDataSerializer
    http_method_names = ['get', 'head', 'options']
    
    def get(self, request):
        result = VendedorController.list_vendor_type()
        
        if result:
            return Response(result)
            
        return Response({'message': 'Tipos de vendedor não encontrados.'}, status=status.HTTP_400_BAD_REQUEST)
    

class ListSupervisores(generics.RetrieveAPIView):
    serializer_class = GenericSelectDataSerializer
    http_method_names = ['get', 'head', 'options']
    
    def get(self, request, id_unn: int, id_emp: int):
        result = VendedorController.list_supervisors(id_unn=id_unn, id_emp=id_emp)
        
        if result:
            return Response(result)
            
        return Response({'message': 'Supervisores não encontrados.'}, status=status.HTTP_400_BAD_REQUEST)