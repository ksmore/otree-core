# -*- coding: utf-8 -*-
from __future__ import division
import otree.views
import {{ app_name }}.models as models
from {{ app_name }}._builtin import Page, WaitPage
from otree.common import Money, money_range

def variables_for_all_templates(self):
    return {
        # example:
        #'my_field': self.player.my_field,
    }

class MyPage(Page):

    form_model = models.Player
    form_fields = ['my_field']

    def participate_condition(self):
        return True

    template_name = '{{ app_name }}/MyPage.html'

    def variables_for_template(self):
        return {
            'my_variable_here': 1,
        }

class ResultsWaitPage(WaitPage):

    scope = models.Group

    def after_all_players_arrive(self):
        self.group.set_payoffs()

class Results(Page):

    template_name = '{{ app_name }}/Results.html'

def pages():
    return [
        MyPage,
        ResultsWaitPage,
        Results
    ]