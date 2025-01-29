from rest_framework import serializers
from .models import Listing

class ListingSerializer(serializers.ModelSerializer):
    photo_main = serializers.SerializerMethodField()

    class Meta:
        model = Listing
        fields = ('title', 'address', 'city', 'state', 'price', 'sale_type', 'home_type', 'bedrooms', 'bathrooms', 'sqft', 'photo_main', 'slug', 'list_date')

    def get_photo_main(self, obj):
        if obj.photo_main:
            request = self.context.get('request')  # Needed for full URL generation
            return request.build_absolute_uri(obj.photo_main.url) if request else obj.photo_main.url
        return None

class listingDetailSerializer(serializers.ModelSerializer):
    photo_main = serializers.SerializerMethodField()
    photo_1 = serializers.SerializerMethodField()
    photo_2 = serializers.SerializerMethodField()
    photo_3 = serializers.SerializerMethodField()
    photo_4 = serializers.SerializerMethodField()
    photo_5 = serializers.SerializerMethodField()
    photo_6 = serializers.SerializerMethodField()
    photo_7 = serializers.SerializerMethodField()
    photo_8 = serializers.SerializerMethodField()
    photo_9 = serializers.SerializerMethodField()
    photo_10 = serializers.SerializerMethodField()
    photo_11 = serializers.SerializerMethodField()
    photo_12 = serializers.SerializerMethodField()
    photo_13 = serializers.SerializerMethodField()
    photo_14 = serializers.SerializerMethodField()
    photo_15 = serializers.SerializerMethodField()
    photo_16 = serializers.SerializerMethodField()
    photo_17 = serializers.SerializerMethodField()
    photo_18 = serializers.SerializerMethodField()
    photo_19 = serializers.SerializerMethodField()
    photo_20 = serializers.SerializerMethodField()

    class Meta:
        model = Listing
        fields = '__all__'
        lookup_field = 'slug'

    def get_photo_main(self, obj):
        return obj.photo_main.url if obj.photo_main else None

    def get_photo_1(self, obj):
        return obj.photo_1.url if obj.photo_1 else None

    def get_photo_2(self, obj):
        return obj.photo_2.url if obj.photo_2 else None

    def get_photo_3(self, obj):
        return obj.photo_3.url if obj.photo_3 else None

    def get_photo_4(self, obj):
        return obj.photo_4.url if obj.photo_4 else None

    def get_photo_5(self, obj):
        return obj.photo_5.url if obj.photo_5 else None

    def get_photo_6(self, obj):
        return obj.photo_6.url if obj.photo_6 else None

    def get_photo_7(self, obj):
        return obj.photo_7.url if obj.photo_7 else None

    def get_photo_8(self, obj):
        return obj.photo_8.url if obj.photo_8 else None

    def get_photo_9(self, obj):
        return obj.photo_9.url if obj.photo_9 else None

    def get_photo_10(self, obj):
        return obj.photo_10.url if obj.photo_10 else None

    def get_photo_11(self, obj):
        return obj.photo_11.url if obj.photo_11 else None

    def get_photo_12(self, obj):
        return obj.photo_12.url if obj.photo_12 else None

    def get_photo_13(self, obj):
        return obj.photo_13.url if obj.photo_13 else None

    def get_photo_14(self, obj):
        return obj.photo_14.url if obj.photo_14 else None

    def get_photo_15(self, obj):
        return obj.photo_15.url if obj.photo_15 else None

    def get_photo_16(self, obj):
        return obj.photo_16.url if obj.photo_16 else None

    def get_photo_17(self, obj):
        return obj.photo_17.url if obj.photo_17 else None

    def get_photo_18(self, obj):
        return obj.photo_18.url if obj.photo_18 else None

    def get_photo_19(self, obj):
        return obj.photo_19.url if obj.photo_19 else None

    def get_photo_20(self, obj):
        return obj.photo_20.url if obj.photo_20 else None

