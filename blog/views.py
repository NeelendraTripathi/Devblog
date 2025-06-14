from django.shortcuts import render, get_object_or_404,redirect
from .models import post
from .form import ContactForm
# Create your views here.


def post_list(request):
    
    all_posts = post.objects.all()
    
    context ={
        'posts':all_posts
    }
    
    return render(request, 'blog/post_list.html',context)


def post_detail(request, slug):
    posts = get_object_or_404(post, slug=slug)
    context = {
        'post': posts,
    }
    return render(request, 'blog/post_detail.html',context)



def contact(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request
        form = ContactForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            # For now, we just print the cleaned data to the terminal.
            print(form.cleaned_data)
            # Redirect to a new 'success' URL after submission.
            return redirect('contact_success')
    else:
        # If it's a GET request, create a blank, unbound form.
        form = ContactForm()

    # Render the contact page template with the form object.
    return render(request, 'blog/contact.html', {'form': form})

# This view just displays the success page.
def contact_success(request):
    return render(request, 'blog/contact_success.html')