from django import forms

# 書籍タイトルを検索するフォームの作成
class SearchForm(forms.Form):
    title = forms.CharField(label='タイトル', max_length=200, required=True)