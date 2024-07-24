from django.shortcuts import render
from .models import Post, Category , Comment
from .forms import CommentForm
from django.core.paginator import Paginator


# Create your views here.

def post_list(request):
	post_list = Post.objects.all()
	paginator = Paginator(post_list, 12)

	page = request.GET.get('page')
	post_list = paginator.get_page(page)


	context = {

		'post_list': post_list ,


	}


	return render(request , 'Post/post_list.html', context)




def post_detail(request, id):
	post_detail = Post.objects.get(id=id)
	categories = Category.objects.all()
	comments = Comment.objects.filter(post=post_detail)

	if request.method =='POST' :
		comment_form = CommentForm(request.POST)
		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.user = request.user
			new_comment.post = post_detail
			new_comment.save()

	else:
		comment_form = CommentForm()





	context = {
		'post_detail':post_detail , 'categories' : categories , 'comments': comments , 'comment_form':comment_form

	}

	return render(request , 'Post/post_detail.html', context)









def post_by_category(request, category):
	post_by_category = Post.objects.filter(category__category_name__in=[category])

	context = {
		'post_list':post_by_category


	}

	return render(request , 'Post/post_list.html', context)