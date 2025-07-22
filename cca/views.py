from django.shortcuts import render
from .forms import CoverageForm
import google.generativeai as genai

# Create your views here.

# Api_key = 'AIzaSyBWIoT1qb-4mcM2ROhgwfhAU3vqGOm0Bow' 
# genai.configure(api_key=Api_key)

def get_health_cover_recommendation(name, age, city, income, dependents):
    prompt = (
        f"Suggest an appropriate health cover amount in INR for the following person:\n"
        f"Name: {name}\nAge: {age}\nCity: {city}\nAnnual Income: ₹{income}\n"
        f"Dependents: {dependents}\nReturn only the numeric amount, no explanation."
    )
    Api_key = 'AIzaSyBWIoT1qb-4mcM2ROhgwfhAU3vqGOm0Bow'    # API key disabled
    genai.configure(api_key=Api_key) 
    model = genai.GenerativeModel("gemini-2.0-flash")
    chat = model.start_chat()
    # user_input = str(input(prompt))
    response = chat.send_message(prompt)
    # print('Gemini:', response.text, 'lllllllllllllllllllll')
    return int(response.text)


def home(request):
    result = None
    if request.method == 'POST':
        form = CoverageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cover = get_health_cover_recommendation(**data)
            premium = int(0.009 * cover)
            result = {
                'cover': cover,
                'premium': premium
            }
    else:
        form = CoverageForm()
    return render(request, 'index.html', {'form': form, 'result': result})


