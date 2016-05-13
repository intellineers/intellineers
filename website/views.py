# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.utils.translation import activate
from django.utils.translation import LANGUAGE_SESSION_KEY

from models import Article

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

    # NOTE: Loading the articles is hardcoded. It may be changed later.
    # if context['current_lang'] == 'en':
    #     context['article_1'] = Article.objects.get(title='Web-Solutions')
    #     context['article_2'] = Article.objects.get(title='IT-Consulting')
    #     context['article_3'] = Article.objects.get(title='NLP - Doculizer (TM)', language='en')
    #     context['article_4'] = Article.objects.get(title='Artificial Intelligence')
    #
    # if context['current_lang'] == 'de':
    #     context['article_1'] = Article.objects.get(slug='web-loesungen')
    #     context['article_2'] = Article.objects.get(title='IT-Beratung')
    #     context['article_3'] = Article.objects.get(title='NLP - Doculizer (TM)', language='de')
    #     context['article_4'] = Article.objects.get(slug='kuenstliche-intelligenz')

    if context['current_lang'] == 'en':
        context['article_1'] = {
            'title': 'Web-Solutions',
            'slug': 'web-solutions',
            'content': 'An individual websolution is key to utilize the new technologies that the Web 3.0 is about to offer. Web 3.0 describes the transition from the Web 2.0 (the current state) to a more intelligent web, and it makes reference to technologies like Data-Mining and Natural Language Processing used in combination with the web. Benefit from a digital office. We will help you to utilize the technologies that are available to you when using software solutions like ERP, DMS, etc. by combining them with your website / SaaS / webapp.',
            'language': 'en',
            'icon_1_url': '/static/img/icons/webservice.png',
            'icon_2_url': '/static/img/icons/webservice.png',
        }
        context['article_2'] = {
            'title': 'IT-Consulting',
            'slug': 'it-consulting',
            'content': 'Nowadays, there are many IT-Technologies that give you the edge over your competitors and provide you with tools to make sure that you are always a step ahead. In order to do so, several different software solutions must work together. We will help you to find the ideal solution that provides your business with the means to tackle the problems of tomorrow.',
            'language': 'en',
            'icon_1_url': '/static/img/icons/itsolutions.png',
            'icon_2_url': '/static/img/icons/itsolutions.png',
        }
        context['article_3'] = {
            'title': 'NLP - Doculizer (TM)',
            'slug': 'nlp-doculizer-tm',
            'content': 'The science of Natural Language Processing (NLP) is to extract information from text and process these information in order to visualize them. This improves the speed in which documents can be analyzed, because not all documents need to be read by human in order to retrieve information.This yields huge benefits, such as providing information of unread documents or E-Mails or help to maximize the efficiency of processes inside your company.The Doculizer (TM) framework utilizes NLP algorithms and can be incorporated in your existing IT-Portfolio given the software you use provides a certain API to do so.We will help you to plan the integration of the Doculizer framework and to determine, whether the software your company uses provides the above mentioned API.',
            'language': 'en',
            'icon_1_url': '/static/img/icons/nlp.png',
            'icon_2_url': '/static/img/icons/nlp.png',
        }
        context['article_4'] = {
            'title': 'Artificial Intelligence',
            'slug': 'artificial-intelligence',
            'content': 'Technologies of tomorrow are based on self-learning and self-evolving algorithms. Increasingly more business decisions are backed by artificial intelligence, which learns over time and improves itself. Data Mining algorithms extract information from large datasets. These information can be of great use to your company. Additionally, these information can be used to improve self-learning algorithms. We are experts in the field of Artificial Intelligence and are your partner when it comes to Data Mining or Machine Learning. We help you with technological means to catapult your company in the technological next century.',
            'language': 'en',
            'icon_1_url': '/static/img/icons/ai.png',
            'icon_2_url': '/static/img/icons/ai.png',
        }

    if context['current_lang'] == 'de':
        context['article_1'] = {
            'title': 'Web-Lösungen',
            'slug': 'web-loesungen',
            'content': 'Individuelle Web-Lösungen sind der Schlüssel zum Erschließen der Technologien, die das Web 3.0 bereitstellen wird. Web 3.0 beschreibt die Weiterentwicklung des Webs (2.0) und bezieht sich unter anderem auf die Verbreitung von Internet-basierten Diensten und Technologien wie Data-Mining und Natural Language Processing. Nutzen Sie die Vorteile, die z.B. die Digitalisierung des Büros mit sich bringt. Wir helfen Ihnen die neuen Technologien, die Ihnen mit Softwarelösungen wie ERP, DMS, und co. zur Verfügung stehen, mit Ihrem Webauftritt / SaaS / Webapp zu kombinieren und Ihnen den entscheidenden Vorteil zu verschaffen.',
            'language': 'de',
            'icon_1_url': '/static/img/icons/webservice.png',
            'icon_2_url': '/static/img/icons/webservice.png',
        }
        context['article_2'] = {
            'title': 'IT-Beratung',
            'slug': 'it-beratung',
            'content': 'Heutzutage bringen IT-Technologien den entschiedenen Vorteil und geben Ihnen Werkzeuge mit denen Sie der Konkurrenz einen Schritt voraus sein können. Damit dies gelingt, müssen verschiedene Technologien ineinander greifen und zusammenarbeiten. Wir helfen Ihnen, die richtigen Entscheidungen im technologischen Zeitalter zu treffen und auf die richtige, zukunftsorientierte IT-Strategie zu setzten.',
            'language': 'de',
            'icon_1_url': '/static/img/icons/itsolutions.png',
            'icon_2_url': '/static/img/icons/itsolutions.png',
        }
        context['article_3'] = {
            'title': 'NLP - Doculizer (TM)',
            'slug': 'nlp-doculizer-tm',
            'content': 'Natural Language Processing, kurz NLP, ist die Wissenschaft Informationen aus Texten zu extrahieren und den Inhalt zu visualisieren. Dabei kann ein großer Vorteil generiert werden, da nicht jedes Dokument von Menschen gelesen werden muss, um die darin enthaltenen Informationen zu erlangen. Unser Doculizer (TM) Framework hilft Ihnen Dokumente zu verschlagworten, E-Mails zu analysieren und Prozesse in Ihrem Unternehmen zu beschleunigen. Doculizer kann mit bereits bestehenden IT-Infrastrukturen genutzt werden, sofern entsprechende Schnittstellen vorliegen. Wir beraten Sie gerne und helfen Ihnen dabei herauszufinden, ob Ihre Software diese Schnittstellen zur Verfügung stellt.',
            'language': 'de',
            'icon_1_url': '/static/img/icons/nlp.png',
            'icon_2_url': '/static/img/icons/nlp.png',
        }
        context['article_4'] = {
            'title': 'Künstliche Intelligenz',
            'slug': 'kuenstliche-intelligenz',
            'content': 'Die Technologien von morgen basieren auf selbstlernenden Algorithmen. Zunehmend mehr Geschäftsentscheidungen werden durch künstliche Intelligenz unterstützt, welche mit der Zeit lernt und sich selbst verbessert. Data Mining Algorithmen extrahieren informationen aus großen Datensätzen, die für Ihr Unternehmen von Nutzen sein können. Zusätzlich können diese Informationen als Grundlage für die Verbesserung von selbstlernenden Algorithmen genutzt werden. Wir sind Experten in Machine Learning und Data Mining. Wir stehen Ihnen tatkräftig zur Seite, wenn es darum geht Ihr Unternehmen auf die technologischen Ansprüche von morgen vorzubereiten.',
            'language': 'de',
            'icon_1_url': '/static/img/icons/ai.png',
            'icon_2_url': '/static/img/icons/ai.png',
        }

    # prepareContext(context, 'web_title', _('web_title'))
    # prepareContext(context, 'web_content', _('web_content'))
    # prepareContext(context, 'web_content_detailed', _('web_content_detailed'))

    # prepareContext(context, 'it_title', _('it_title'))
    # prepareContext(context, 'it_content', _('it_content'))
    # prepareContext(context, 'it_content_detailed', _('it_content_detailed'))

    # prepareContext(context, 'ai_title', _('ai_title'))
    # prepareContext(context, 'ai_content', _('ai_content'))
    # prepareContext(context, 'ai_content_detailed', _('ai_content_detailed'))

    # prepareContext(context, 'nlp_title', _('nlp_title'))
    # prepareContext(context, 'nlp_content', _('nlp_content'))
    # prepareContext(context, 'nlp_content_detailed', _('nlp_content_detailed'))

    prepareContext(context, 'back_text', _('back_text'))


    prepareContext(context, 'cw_content', _('cw_content'))
    prepareContext(context, 'cs_content', _('cs_content'))

    prepareContext(context, 'more', _('more'))

    return render(request, 'website_basetemplate.html', context)

def prepareContext(context, ct, key):
    context[ct] = key
