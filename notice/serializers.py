from rest_framework import serializers

from notice.models import Notice, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ["image"]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        image = {
            "url": representation.pop("image"),
            "size": instance.image.size,
            "name": instance.image.name,
        }
        representation["image"] = image
        return representation


class NoticeDetailSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = Notice
        fields = [
            "title",
            "content",
            "created_at",
        ]

class NoticeSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True, required=False)

    class Meta:
        model = Notice
        fields = [
            "id",
            "title",
            "content",
            "image",
            "created_at",
        ]

    def create(self, validated_data):
        files = validated_data.pop("files", [])
        instance = Notice.objects.create(**validated_data)

        images = []
        pic = ["png", "jpg", "jpeg"]
        for file in files:
            if file.name.split(".")[-1].lower() in pic:
                images.append(Image(image=file, board_id=instance.id))
            else:
                raise serializers.ValidationError("이미지 파일 확장자는 png, jpg, jpeg만 가능합니다.")
        Image.objects.bulk_create(images)
        return instance