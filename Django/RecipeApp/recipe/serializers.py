from rest_framework import serializers
from .models import CustomUser, Profile, Recipe, Save

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        # read_only_fields = ['username', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class RecipeSerializer(serializers.ModelSerializer):
    total_number_of_bookmarks = serializers.SerializerMethodField()
    class Meta:
        model = Recipe
        fields = ('title', 'chef', 'recipe_image', 'ingredients', 'servings', 'instructions')

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    bio = serializers.CharField(allow_blank=True, required=False)
    image = serializers.ImageField(required=False)
    class Meta:
        model = Profile
        fields = ('username', 'bio', 'image', 'created_at', 'updated_at')
        read_only_fields = ('username', )
    
    def get_image(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        return 'https://static.productionready.io/images/smiley-cyrus.jpg'

class SaveSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    recipe = serializers.PrimaryKeyRelatedField(queryset=Recipe.objects.all())
    class Meta:
        model = Save
        fields = ['id', 'user', 'recipe', 'created_at']
