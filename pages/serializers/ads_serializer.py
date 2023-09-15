from rest_framework import serializers

from pages.models import Ads


class AdsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads
        fields = ('page_id', 'title', 'url',)
        # read_only_fields = ('user',)

    def create(self, validated_data):
        # user = self.context.get("request").user

        Ad = Ads.objects.create(
            title=validated_data['title'],
            page_id=validated_data['page_id'],
            url=validated_data['url'],
        )
        Ad.save()
        return Ad
