"""article.views."""
from django.core.cache import cache
from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework.views import APIView

from article.models import Article


class IndexPage(TemplateView):
    """博客首页"""

    template_name = 'account/index.html'
    view_name = 'index'

    # def get(self, request):
    #     # referer = request.META.get('HTTP_REFERER', None)
    #     # host = request.META['HTTP_HOST'].lower()
    #     # if (host.startswith('www') or host.startswith('syzljh.cn')) and not referer:
    #     #     url = SubSiteService.get_redirect_url(get_client_ip(request))
    #     #     if url:
    #     #         return HttpResponseRedirect(url)
    #
    #     # key = 'index:articlelist'
    #     # article_list = cache.get(key)
    #     # if not article_list:
    #     #     article_list = Article.objects.order_by('-create_time')
    #     #     cache.set(key, article_list, 3600 * 8)
    #     #
    #     # context = {
    #     #     'article_list': article_list,
    #     # }
    #     # return render(request, self.template_name, context)
    #     return render(request=request, template_name=self.template_name)
