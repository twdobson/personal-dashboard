import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
import django
django.setup()
from django.urls import get_resolver

resolver = get_resolver('core.urls')
url_patterns = resolver.url_patterns

for pattern in url_patterns:
    print(pattern)

# V1 results
# <URLResolver <URLPattern list> (admin:admin) 'admin/'>
# <URLResolver <module 'apps.authentication.urls' from '/Users/tdobson/Documents/repos/personal/personal-dashboard/apps/authentication/urls.py'> (None:None) ''>
# <URLResolver <module 'debug_toolbar.urls' from '/Users/tdobson/miniconda3/envs/personal-dashboard/lib/python3.9/site-packages/debug_toolbar/urls.py'> (djdt:djdt) '__debug__/'>
# <URLResolver <module 'apps.polls.urls' from '/Users/tdobson/Documents/repos/personal/personal-dashboard/apps/polls/urls.py'> (polls:polls) 'polls/'>
# <URLResolver <module 'apps.pastebin.urls' from '/Users/tdobson/Documents/repos/personal/personal-dashboard/apps/pastebin/urls.py'> (pastebin:pastebin) 'pastebin/'>
# <URLResolver <URLPattern list> (None:None) 'api/'>
# <URLResolver <module 'rest_framework.urls' from '/Users/tdobson/miniconda3/envs/personal-dashboard/lib/python3.9/site-packages/rest_framework/urls.py'> (rest_framework:rest_framework) 'api/api-auth/'>
# <URLResolver <module 'apps.accounts.urls' from '/Users/tdobson/Documents/repos/personal/personal-dashboard/apps/accounts/urls.py'> (None:None) ''>
# <URLResolver <module 'apps.home.urls' from '/Users/tdobson/Documents/repos/personal/personal-dashboard/apps/home/urls.py'> (None:None) ''>


resolver = get_resolver('apps.pastebin.urls')
url_patterns = resolver.url_patterns

for pattern in url_patterns:
    print(pattern)

# V1 results 
# <URLPattern 'snippets/'>
# <URLPattern 'snippets/<int:pk>/'>    

# V2 - adding api_view decorator + format 
# <URLPattern 'snippets/'>
# <URLPattern 'snippets<drf_format_suffix:format>'>
# <URLPattern 'snippets/<int:pk>/'> 
# <URLPattern 'snippets/<int:pk><drf_format_suffix:format>'>


# V3 - no difference
# <URLPattern 'snippets/'>
# <URLPattern 'snippets<drf_format_suffix_json_html_csv:format>'>
# <URLPattern 'snippets/<int:pk>/'>
# <URLPattern 'snippets/<int:pk><drf_format_suffix_json_html_csv:format>'>


