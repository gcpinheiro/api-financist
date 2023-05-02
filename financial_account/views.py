from django.shortcuts import render
from financial_account.serializers import FinancialAccountSerializer
from financial_account.models import FinancialAccount
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.response import Response

# Create your views here.

class FinancialAccountCreateView(CreateAPIView):
    serializer_class = FinancialAccountSerializer

class FinancialAccountList(ListCreateAPIView):
    queryset = FinancialAccount.objects.all()
    serializer_class = FinancialAccountSerializer

    def get_queryset(self):
        queryset = FinancialAccount.objects.all()
        # Obtém o valor do parâmetro de filtro 'type_purchase'
        type_purchase = self.request.query_params.get('type_purchase', None)
        # Filtra o queryset se o parâmetro de filtro estiver presente
        if type_purchase is not None:
            queryset = queryset.filter(type_purchase=type_purchase)

        if type_purchase == None:
            return Response({"error": "Filtro inválido"}, status=404)
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        total = sum([float(item['installment_amount']) for item in serializer.data])
        
        return Response({
            'total': total,
            'results': serializer.data
        })