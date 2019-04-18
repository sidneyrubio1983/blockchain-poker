# -*- coding: utf-8 -*-
import os
import django
import uuid
import string

from datetime import timedelta

from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "game.settings")
django.setup()

import logging
logger = logging.getLogger(__name__)

from utils.evalcards import card, deck

from game.models import Players, Decks, Wins, Jackpot
from random import choice

def home(request):

    try:
        player_session_key = request.COOKIES["player_session_key"]
    except:
        player_session_key = (''.join([choice(string.ascii_letters + string.digits) for i in range(28)]))

    player, created = Players.objects.get_or_create(session_key=player_session_key)
    print('player', player, 'is_new', created)

    hand = []
    cards_deck = deck()
    starting_nonreduced_cards_deck = cards_deck.copy()

    # Note: this would be an example how to work with cards individually
    # card1 = card('2','S')
    # card2 = card('Q','S')
    # card3 = card('J','S')
    # card4 = card('K','S')
    # card5 = card('A','D')
    # hand.insert(0, card1)
    # hand.insert(0, card2)
    # hand.insert(0, card3)
    # hand.insert(0, card4)
    # hand.insert(0, card5)

    hand = cards_deck.get_hand()
    evaluated_hand, numeral_dict, suit_dict = cards_deck.evaluate_hand(hand)
    sugested_hand = cards_deck.suggest_hand(player, hand, evaluated_hand, numeral_dict, suit_dict)

    # XXX TODO jackpot sa navysuje z kazdej prehranej hry

    deck_hash = (''.join([choice(string.ascii_letters + string.digits) for i in range(25)]) + \
                        ''.join([choice(string.digits) for i in range(10)])).upper()

    starting_nonreduced_cards_deck_ = ""
    for card in starting_nonreduced_cards_deck:
        starting_nonreduced_cards_deck_ += str(card) + "|"
    starting_cards_deck = starting_nonreduced_cards_deck_[:-1]

    player_cards_deck = Decks.objects.create(player=player, deck=starting_cards_deck, deck_hash=deck_hash)
    print('player_cards_deck', player_cards_deck)

    #########################################################################
    # XXX temporarily simulating credit
    if(player.credit == 0):
        player.credit = 30
        player.save()
    player.credit -= 5
    player.save()
    #########################################################################

    #########################################################################
    # XXX delete this shit it's for debug purposes only #####################
    XXX_DELETEME_TEMP_ONLY_DECKS = Decks.objects.all().order_by('-pk')[:100]
    #########################################################################

    response = render(
        request=request,
        template_name='index.html',
        context={
            'player_session_key': player_session_key,
            'hand': hand,
            'evaluated_hand': evaluated_hand,
            'sugested_hand': sugested_hand,
            'credit': player.credit,
            'bet_amount': player.bet_amount,
            'mini_bonus': player.mini_bonus,
            'DELETEME_TEMP_ONLY_DECKS': XXX_DELETEME_TEMP_ONLY_DECKS,
            },
    )
    response.set_cookie(key="player_session_key",value=player_session_key)

    return response


def about(request):

    try:
        player_session_key = request.COOKIES["player_session_key"]
    except:
        player_session_key = (''.join([choice(string.ascii_letters + string.digits) for i in range(28)]))

    player, created = Players.objects.get_or_create(session_key=player_session_key)
    print('player', player, 'is_new', created)

    response = render(
        request=request,
        template_name='about.html',
        context={
            'player_session_key': player_session_key,
            },
    )
    response.set_cookie(key="player_session_key",value=player_session_key)

    return response


def tmp_about_desired_look(request):

    response = render(
        request=request,
        template_name='tmp_about_desired_look.html',
    )

    return response


def tos(request):

    try:
        player_session_key = request.COOKIES["player_session_key"]
    except:
        player_session_key = (''.join([choice(string.ascii_letters + string.digits) for i in range(28)]))

    player, created = Players.objects.get_or_create(session_key=player_session_key)
    print('player', player, 'is_new', created)

    response = render(
        request=request,
        template_name='tos.html',
        context={
            'player_session_key': player_session_key,
            },
    )
    response.set_cookie(key="player_session_key",value=player_session_key)

    return response


def reveal_deck(request, deck_hash):

    try:
        player_session_key = request.COOKIES["player_session_key"]
    except:
        player_session_key = (''.join([choice(string.ascii_letters + string.digits) for i in range(28)]))

    player, created = Players.objects.get_or_create(session_key=player_session_key)
    print('player', player, 'is_new', created)

    # XXX TODO reveal deck really shoul reveal player deck
    # XXX TODO for now we display just the deck since we're not yet recoding wins
    #player_deck = Decks.objects.get(deck_hash=deck_hash)
    #player_wins = Wins.objects.get(deck=player_deck)

    cards_deck = Decks.objects.get(deck_hash=deck_hash)
    tmp_cards_deck = cards_deck.deck
    tmp_cards_deck = tmp_cards_deck.split('|')

    response = render(
        request=request,
        template_name='deck.html',
        context={
            'deck_hash': deck_hash,
            'tmp_cards_deck': tmp_cards_deck,
            'deck_shuffled_at': cards_deck.shuffled_at,
            'player_session_key': player_session_key,
            },
    )
    response.set_cookie(key="player_session_key",value=player_session_key)

    return response


def credit(request):

    try:
        player_session_key = request.COOKIES["player_session_key"]
    except:
        player_session_key = (''.join([choice(string.ascii_letters + string.digits) for i in range(28)]))

    player, created = Players.objects.get_or_create(session_key=player_session_key)
    print('player', player, 'is_new', created)

    response = render(
        request=request,
        template_name='credit.html',
        context={
            'credit': player.credit,
            'player_session_key': player_session_key,
            },
    )
    response.set_cookie(key="player_session_key",value=player_session_key)

    return response


def ajax_bet(request):

    print(request.POST)

    bet_amount = request.POST['bet_amount']
    player_session_key = request.POST['player_session_key']

    player = Players.objects.get(session_key=player_session_key)
    player.bet_amount = int(bet_amount)
    player.save()

    print('player', player, 'bet_amount', bet_amount)

    return HttpResponse(bet_amount)


def ajax_draw_cards(request):

    # hold_cards = [1,3]
    # #hold_cards = request.POST.get('hold_cards')

    # player_session_key = "rncbZ2gRNSGIo6NCUrXEUAmqYZq7"
    # #player_session_key = request.POST['player_session_key']

    # player = Players.objects.get(session_key=player_session_key)

    # player_deck = Decks.objects.filter(player=player).order_by("-pk")[0]
    # print(player_deck.deck)

    # # XXX replace cards over here........
    # final_hand_ = ["10D","JD","QD","KD","AD"]

    # final_hand = []
    # for c_ in final_hand_:
    #     if(len(c_)==2):
    #         c = card(c_[0],c_[1])
    #     if(len(c_)==3):
    #         c = card(c_[0:2],c_[2])
    #     final_hand.insert(0, c)

    # evaluated_hand, numeral_dict, suit_dict = deck().evaluate_hand(final_hand)

    # final_hand_ = final_hand
    # final_hand = []

    # for c in final_hand_:
    #     final_hand.append(str(c))

    # congrats_you_won_flag = False
    # if(evaluated_hand!="Nothing."):
    #     congrats_you_won_flag = True

    # # XXX if winning hand, write the winning deck into the table...

    # # XXX increase credit in case of win....

    # response = {
    #     'credit': player.credit,
    #     'final_hand': final_hand,
    #     'evaluated_hand': evaluated_hand,
    #     'congrats_you_won_flag': congrats_you_won_flag,
    # }
    #     
    #return JsonResponse(response)
    return HttpResponse('{"credit": 25, "final_hand": ["AD", "KD", "QD", "JD", "10D"], "evaluated_hand": "Royal-flush.", "congrats_you_won_flag": true}')
