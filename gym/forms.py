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
    ('Basketball', "Basket Ball"),
    ('Badminton', "Badminton"),
    ('Ping Pong', "Ping Pong")
)

OPTIONS2 = (
    ('EquipType', "Equipment Type"),
    ('EquipRate',"Equipment Rate"),
    ('EquipDamageFee',"Equipment Damage Fee")
)

class MyFormPage1(forms.Form):
    error_css_class = "error"
    EquipType = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage1Part1,label="Select one of the following equipment types:",error_messages={'required': ''})
    EquipType2 = forms.BooleanField(required=False, label="Click here to display: Equipment Type")
    EquipRate = forms.BooleanField(required=False, label="Click here to display: Equipment Rate")
    EquipDamageFee = forms.BooleanField(required=False, label="Click here to display: Equipment Damage Fee")

OptionsPage2 = (
    ("Option 11", "Get custID's and cusName's of customers who booked rooms"),
)

class MyFormPage2(forms.Form):
    JoinQuery = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage2, required=True, label="")

OptionsPage3 = (
    ("Option 10", "Get the customer ID's of customers who booked all the equipment"),
    ("Option 12", "Insert a Equipment and Resubmit")
)

class MyFormPage3(forms.Form):
    DivisionQuery = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage3, required=True, label="")

OptionsPage4 = (
    ("Option 41", "Number of rooms booked during the week for all customers"),
    ("Option 42", "Number of equipment booked during the week for all customers"),
)

class MyFormPage4(forms.Form):
    AggregationQuery = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage4, required=True, label="")

OptionsPage5 = (
    ("Option 31", "The most rented out equipment type [MAX(count(equipment type rented)]"),
    ("Option 32", "The least rented out equipment type [MIN(count(equipment type rented)]"),
)

class MyFormPage5(forms.Form):
    NestedAggregationQuery = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage5, required=True, label="")

OptionsPage6Part1 = (
    ('8147564912', "EmployeeID = 8147564912, EmployeeName = Amy Tang"),
)

OptionsPage6Part2 = (
    ("Option 6", "Stop this employee from cleaning the room:"),
)

class MyFormPage6(forms.Form):
    #CustomerToDelete = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage6Part1, label="")
    CustomerToDelete = forms.CharField(label="Insert the Employee ID")
    DeleteQuery = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage6Part2, label="Are you sure?")

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
    # ToUpdate = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage7Part1, label="")
    ToUpdateChar = forms.CharField(label="Insert The Value")
    UpdateQuery = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage7Part2, label="Are you sure?")

OptionsPage8 = (
    ('654321', "Member with CustomerID = 654321, CustomerName = Herb Derp"),
    ('392837', "Member with CustomerID = 392837, CustomerName = Tiffany Lin"),
    ('472839', "Athlete with CustomerID = 472839, CustomerName = Yoshi Yamamoto"),
)


OptionsPage8Part2 = (
    ("Option 12", "I want to delete the customer"),
)

class MyFormPage8(forms.Form):
    #CustomerToDelete2 = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage8, label="")
    CustomerToDelete2 = forms.CharField(label="Insert Customer ID:")
    DeleteOnCascadeQuery = forms.ChoiceField(widget=forms.RadioSelect, choices=OptionsPage8Part2, label="Are you sure?")