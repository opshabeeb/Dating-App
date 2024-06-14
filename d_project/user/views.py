from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def signup(request):
    return render(request,'registration/signup.html')
def login(request):
    return render(request,'registration/login.html')
def matching(request):
    return render(request,'matching_page.html')
def test(request):
    return render(request,'test.html')
def create_profile(request):
    return render(request,'create_profile.html')
def profile_view(request):
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

def plans(request):
    return render (request,'plans.html')