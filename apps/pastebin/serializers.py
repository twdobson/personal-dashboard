from rest_framework import serializers
from apps.pastebin.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


from .. authentication.models import CustomUser

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='pastebin:snippet-highlight', format='html')
    

    class Meta:
        model = Snippet
        fields = ['id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='pastebin:snippet-detail', read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'snippets']


#  -----------------------------------
# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(
#         many=True,
#         queryset=Snippet.objects.all()
#     )

#     class Meta:
#         model = CustomUser
#         fields = ['id', 'username', 'snippets']

        
# class SnippetSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')

#     class Meta:
#         model = Snippet
#         fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']        

#  -----------------------------------

# class SnippetSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#     owner = serializers.ReadOnlyField(source='owner.username')

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance

   

# -------------------------------------------------------------------------------------------
# ------------------------------------ Playing with serializers in shell --------------------
# -------------------------------------------------------------------------------------------

# testing serializers
# from snippets.models import Snippet
# from apps.pastebin.serializers import SnippetSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser

# snippet = Snippet(code='foo = "bar"\n')
# snippet.save()

# snippet = Snippet(code='print("hello, world")\n')
# # snippet.save()    
# serializer = SnippetSerializer(snippet)
# serializer.data
# # {'id': 2, 'title': '', 'code': 'print("hello, world")\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}
# content = JSONRenderer().render(serializer.data)
# content
# # b'{"id": 2, "title": "", "code": "print(\\"hello, world\\")\\n", "linenos": false, "language": "python", "style": "friendly"}'
# import io

# stream = io.BytesIO(content)
# data = JSONParser().parse(stream)
# serializer = SnippetSerializer(data=data)
# serializer.is_valid()
# # True
# serializer.validated_data
# # OrderedDict([('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
# serializer.save()
# # <Snippet: Snippet object>
# serializer = SnippetSerializer(Snippet.objects.all(), many=True)
# serializer.data
# # [OrderedDict([('id', 1), ('title', ''), ('code', 'foo = "bar"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 2), ('title', ''), ('code', 'print("hello, world")\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 3), ('title', ''), ('code', 'print("hello, world")'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])]
# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Snippet
#         fields = ['id', 'title', 'code', 'linenos', 'language', 'style']

# -------------------------------------------------------------------------------------------
# # Using a model serializer
# from snippets.serializers import SnippetSerializer
# serializer = SnippetSerializer()
# print(repr(serializer))
# # SnippetSerializer():
# #    id = IntegerField(label='ID', read_only=True)
# #    title = CharField(allow_blank=True, max_length=100, required=False)
# #    code = CharField(style={'base_template': 'textarea.html'})
# #    linenos = BooleanField(required=False)
# #    language = ChoiceField(choices=[('Clipper', 'FoxPro'), ('Cucumber', 'Gherkin'), ('RobotFramework', 'RobotFramework'), ('abap', 'ABAP'), ('ada', 'Ada')...
# #    style = ChoiceField(choices=[('autumn', 'autumn'), ('borland', 'borland'), ('bw', 'bw'), ('colorful', 'colorful')...