from django import forms 
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text')
        
        
        widgets = {
            'title':forms.TextInput(attrs={
                'class':'border border-gray-400 rounded-lg p-2 w-full text-lg mb-4',
                'placeholder':'Title',
            }),
            
            'text':forms.Textarea(attrs={
                'class':'border border-gray-400 rounded-lg p-3 w-full text-base h-40 ',
                'placeholder':'Write your text here....',
            })
        }