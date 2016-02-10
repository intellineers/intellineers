from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.utils import translation

def intermediateView(request):
    context = {}
    return render(request, 'intermediateViewHTML.html', context)

def basetemplate(request):
    context = {}

    prepareContext(context, 'services_menuitem',_('services_menuitem'))
    prepareContext(context, 'services_title', _('services_title'))
    prepareContext(context, 'team_menuitem', _('team_menuitem'))
    prepareContext(context, 'team_title', _('team_title'))
    prepareContext(context, 'contact_menuitem', _('contact_menuitem'))
    prepareContext(context, 'contact_title', _('contact_title'))

    prepareContext(context, 'intellineers_quote', _('intellineers_quote'))

    prepareContext(context, 'web_title', _('web_title'))
    prepareContext(context, 'web_content', _('web_content'))
    prepareContext(context, 'it_title', _('it_title'))
    prepareContext(context, 'it_content', _('it_content'))
    prepareContext(context, 'ai_title', _('ai_title'))
    prepareContext(context, 'ai_content', _('ai_content'))
    prepareContext(context, 'nlp_title', _('nlp_title'))
    prepareContext(context, 'nlp_content', _('nlp_content'))

    prepareContext(context, 'cw_content', _('cw_content'))
    prepareContext(context, 'cs_content', _('cs_content'))

    return render(request, 'website_basetemplate.html', context)

def prepareContext(context, ct, key):
    context[ct] = key
