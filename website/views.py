from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.utils.translation import activate
from django.utils.translation import LANGUAGE_SESSION_KEY

def intermediateView(request):
    context = {}
    return render(request, 'intermediateViewHTML.html', context)

def basetemplate(request):
    context = {}

    if "en" in request.path_info:
        context['current_lang'] = 'en'
        request.session[LANGUAGE_SESSION_KEY] = 'en'
        context['other_lang'] = 'de'
    else:
        context['current_lang'] = 'de'
        request.session[LANGUAGE_SESSION_KEY] = 'de'
        context['other_lang'] = 'en'

    prepareContext(context, 'services_menuitem',_('services_menuitem'))
    prepareContext(context, 'services_title', _('services_title'))
    prepareContext(context, 'team_menuitem', _('team_menuitem'))
    prepareContext(context, 'team_title', _('team_title'))
    prepareContext(context, 'contact_menuitem', _('contact_menuitem'))
    prepareContext(context, 'contact_title', _('contact_title'))

    prepareContext(context, 'intellineers_quote', _('intellineers_quote'))

    prepareContext(context, 'web_title', _('web_title'))
    prepareContext(context, 'web_content', _('web_content'))
    prepareContext(context, 'web_content_detailed', _('web_content_detailed'))

    print context['web_content_detailed']

    prepareContext(context, 'it_title', _('it_title'))
    prepareContext(context, 'it_content', _('it_content'))
    prepareContext(context, 'it_content_detailed', _('it_content_detailed'))
    prepareContext(context, 'ai_title', _('ai_title'))
    prepareContext(context, 'ai_content', _('ai_content'))
    prepareContext(context, 'ai_content_detailed', _('ai_content_detailed'))
    prepareContext(context, 'nlp_title', _('nlp_title'))
    prepareContext(context, 'nlp_content', _('nlp_content'))
    prepareContext(context, 'nlp_content_detailed', _('nlp_content_detailed'))
    prepareContext(context, 'back_text', _('back_text'))

    prepareContext(context, 'cw_content', _('cw_content'))
    prepareContext(context, 'cs_content', _('cs_content'))

    prepareContext(context, 'more', _('more'))

    return render(request, 'website_basetemplate.html', context)

def prepareContext(context, ct, key):
    context[ct] = key
