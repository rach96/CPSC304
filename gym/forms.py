# linking the query from the HTML and transform it into query we can use
from django import forms

OptionsPage1Part1 = (
    ("TennisRacket", "Tennis Racket"),
    ("TennisBall", "Tennis Ball"),
    ("BasketBall", "Basket Ball"),
    ("Badminton", "Badminton"),
    ("Ping Pong", "Ping Pong")
)

OPTIONS2 = (
    ("EquipType", "Equipment Type"),
    ("EquipRate","Equipment Rate"),
    ("EquipDamageFee","Equipment Damage Fee")
)

class MyFormPage1(forms.Form):
    EquipType = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage1Part1)
    EquipType2 = forms.BooleanField(required=False, label="Return Equipment Type");
    EquipRate = forms.BooleanField(required=False, label="Return Equipment Rate");
    EquipDamageFee = forms.BooleanField(required=False, label="Return Equipment Damage Fee");

OptionsPage2 = (
    ("Option 11","Get custID’s and cusName's of customers who booked equipment"),
)

class MyFormPage2(forms.Form):
    JoinQuery = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage2, required=True)

OptionsPage3 = (
    ("Option 10", "Get all customers who reserved every equipment")
)

class MyFormPage3(forms.Form):
    DivisionQuery = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage3, required=True)

OptionsPage4 = (
    ("Option 41", "Number of rooms booked during the week for all customers"),
    ("Option 42", "Number of equipment booked during the week for all customers"),
)

class MyFormPage4(forms.Form):
    AggregationQuery = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage4, required=True)

OptionsPage5 = (
    ("Option 31", "MAX(Average equipment rate for each equipment type)"),
    ("Option 32", "MIN(Average equipment rate for each equipment type)"),
)

class MyFormPage5(forms.Form):
    NestedAggregationQuery = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage5, required=True)