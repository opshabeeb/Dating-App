from django.shortcuts import render
from django.views import View

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')

class SignupView(View):
    def get(self, request):
        return render(request, 'registration/signup.html')

class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html')

class MatchingView(View):
    def get(self, request):
        return render(request, 'matching_page.html')

class TestView(View):
    def get(self, request):
        return render(request, 'test.html')

class CreateProfileView(View):
    def get(self, request):
        return render(request, 'create_profile.html')

class ProfileView(View):
    def get(self, request):
        # Dummy profile data
        profile = {
            "firstName": "John",
            "email": "john.doe@example.com",
            "birthday": "1990-01-01",
            "gender": "Male",
            "bio": "A short introduction about John.",
            "height": "180 cm",
            "weight": "75 kg",
            "status": "Single",
            "designation": "Software Engineer",
            "qualification": "B.Sc in Computer Science",
            "location": "New York, USA",
            "hobbies": "Reading, Traveling, Coding",
            "profilepic": "static/images/dp.jpg",  # You should place a sample image in your static folder and refer to it here
            "additional_images": [
                "static/images/lad1.jpg",
                "static/images/lad2.jpg",
                "static/images/lad3.jpg"
            ]
        }

        return render(request, 'profile.html', {'profile': profile})

class PlansView(View):
    def get(self, request):
        return render(request, 'plans.html')
