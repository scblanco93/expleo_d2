from rest_framework import serializers
from entries.models import EntryModel


class EntrySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    concept = serializers.CharField()
    amount = serializers.FloatField()
    datetime = serializers.CharField()

    def create(self, validated_data):
        #voy a salvar a validated dataclass
        instance=EntryModel(
            datetime = validated_data.get("datetime"),
            concept = validated_data.get("concept"),
            amount = validated_data.get("amount")
        )
        
        instance.save()
        return instance
        
    def update(self, instance, validated_data):
        
        instance.datetime=validated_data.get("datetime")
        instance.concept = validated_data.get('concept')
        instance.amount = validated_data.get("amount")
        
        instance.save()
        return instance