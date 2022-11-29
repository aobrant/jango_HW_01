from rest_framework import serializers

from logistic.models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id','title','description']


class ProductPositionSerializer(serializers.ModelSerializer):
    # настройте сериализатор для позиции продукта на складе
    class Meta:
        model = StockProduct
        fields = ['product','quantity','price']

    


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['id','adress','products','positions']

    def create(self, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # создаем склад по его параметрам
        stock = super().create(validated_data)

        # заполнить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for element in positions:
            StockProduct.objects.create(stock=stock,**element)

        return stock

    def update(self, instance, validated_data):
        # достаем связанные данные для других таблиц
        positions = validated_data.pop('positions')

        # обновляем склад по его параметрам
        stock = super().update(instance, validated_data)

        # здесь вам надо обновить связанные таблицы
        # в нашем случае: таблицу StockProduct
        # с помощью списка positions
        for element in positions:
            obj, created = StockProduct.objects.update_or_create(
                stock=stock,
                product=element.get('product'),
                defaults={
                'stock': stock, 
                'product': element.get('product'), 
                'quantity': element.get('quantity'), 
                'price': element.get('price')
                }
            )

        return stock
