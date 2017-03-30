# linking the query from the HTML and transform it into query we can use
from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CheckboxInput()

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError("This User Doesn't Exist")
        if not user.check_password(password):
            raise forms.ValidationError("Incorrect Password")
        if not user.is_active:
            raise forms.ValidationError("This user is no longer active")
        return super(UserLoginForm, self.clean(*args,**kwargs))

OptionsPage1Part1 = (
    ('TennisRacket', "Tennis Racket"),
    ('TennisBall', "Tennis Ball"),
    ('BasketBall', "Basket Ball"),
    ('Badminton', "Badminton"),
    ('Ping Pong', "Ping Pong")
)

OPTIONS2 = (
    ('EquipType', "Equipment Type"),
    ('EquipRate',"Equipment Rate"),
    ('EquipDamageFee',"Equipment Damage Fee")
)

class MyFormPage1(forms.Form):
    EquipType = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage1Part1,label="Select one of the following equipment types:")
    EquipType2 = forms.BooleanField(required=False, label="Return Equipment Type");
    EquipRate = forms.BooleanField(required=False, label="Return Equipment Rate");
    EquipDamageFee = forms.BooleanField(required=False, label="Return Equipment Damage Fee");

OptionsPage2 = (
    ("Option 11","Get custID’s and cusName's of customers who booked equipment"),
)

class MyFormPage2(forms.Form):
    JoinQuery = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage2, required=True)

OptionsPage3 = (
    ("Option 10", "Get all customers who reserved every equipment"),
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

OptionsPage6Part1 = (
    ('13948', "EmployeeID = 13948"),
    ('03948', "EmployeeID = 03948"),
    ('03993', "EmployeeID = 03993"),
)

OptionsPage6Part2 = (
    ("Option 6", "Stop this employee from cleaning the room:"),
)

class MyFormPage6(forms.Form):
    CustomerToDelete = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage6Part1)
    DeleteQuery = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage6Part2)

OptionsPage7Part1 = (
    (200.00, "$200"),
    (49.00, "$49"),
    (29.00, "$29"),
    (39.00, "$39"),
)

OptionsPage7Part2 = (
    ("Option 7", "I want to update"),
)

class MyFormPage7(forms.Form):
    ToUpdate = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage7Part1)
    UpdateQuery = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage7Part2)