import json

from django.views import View
from django.http import JsonResponse

from .models import Post
from user.models import Company

class PostView(View):
    def get(self, request):
        posts = Post.objects.all()

        res = [{
            'company_id' : post.company.id,
            'country' : post.country,
            'region' : post.region,
            'position' : post.position,
            'compensation' : post.compensation,
            'skill' : post.skill
        }for post in posts]
            
        return JsonResponse(res, status = 200, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body)

            company = Company.objects.get(id=data['company_id'])

            Post.objects.create(
                company = company,
                country = data['country'],
                region = data['region'],
                position = data['position'],
                compensation = data['compensation'],
                context = data['context'],
                skill = data['skill'],
            )

            return JsonResponse({'message' : 'success'}, status = 201)
        
        except KeyError:
            return JsonResponse({'messagae' : 'key_error'}, status = 400)

    def patch(self, request):
        try:
            data = json.loads(request.body)

            if not Post.objects.filter(id=data['post_id']):
                return JsonResponse({'message' : 'post_not_exist'}, status = 404)

            Post.objects.filter(id=data['post_id']).update(
                position = data['position'],
                compensation = data['compensation'],
                context = data['context'],
                skill = data['skill'],
            )

            return JsonResponse({'message': 'success'}, status = 201)

        except KeyError:
            return JsonResponse({'messagae' : 'key_error'}, status = 400)

    def delete(self, request):
        try:
            data = json.loads(request.body)

            Post.objects.get(id=data['post_id']).delete()

            return JsonResponse({'message': 'success'}, status = 200)

        except KeyError:
            return JsonResponse({'message' : 'key_error'}, status = 400)
        except Post.DoesNotExist:
            return JsonResponse({'message' : 'post_not_exist'}, status = 404)

class PostDetailView(View):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            related_posts = Post.objects.filter(company=post.company)
            other_posting = []

            for related_post in related_posts:
                other_posting.append(related_post.id)

            res = {
                'post_id' : post.id,
                'company' : post.company.name,
                'country' : post.country,
                'region' : post.region,
                'position' : post.position,
                'compensation' : post.compensation,
                'skill' : post.skill,
                'context' : post.context,
                'other_posting' : other_posting
            }

            return JsonResponse(res, status = 200, safe=False)

        except Post.DoesNotExist:
                return JsonResponse({'message' : 'post_not_exist'}, status = 404)