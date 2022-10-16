import json

from django.views import View
from django.http import JsonResponse

from .models import Resume, User, UserResume
from post.models import Post

class ApplyView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            post = data['post_id']
            user = data['user_id']

            if Resume.objects.filter(user=user, post=post):
                return JsonResponse({"message" : "already applied"}, status=400)

            resume = Resume.objects.create(
                post = Post.objects.get(id=post),
            )
            UserResume.objects.create(
                user = User.objects.get(id=user),
                resume = resume
            )

            return JsonResponse({"message" : "success"}, status=202)
        
        except KeyError:
            return JsonResponse({"message" : "key_error"}, status = 400)
        except Post.DoesNotExist:
            return JsonResponse({"message" : "post_not_exist"}, status = 400)
        except User.DoesNotExist:
            return JsonResponse({"message" : "user_not_exist"}, status = 400)