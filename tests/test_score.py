import pytest

from score import split_note, parse_step, parse_note, parse_score

def test_split_note():
    assert split_note("1") == ("1",0,1) 
    assert split_note("1#") == ("1",1,1) 
    assert split_note("1b") == ("1",-1,1) 
    assert split_note("1/1") == ("1",0,1) 
    assert split_note("1#/1") == ("1",1,1) 
    assert split_note("1b/1") == ("1",-1,1) 
    assert split_note("1/2") == ("1",0,2) 
    assert split_note("1#/2") == ("1",1,2) 
    assert split_note("1b/2") == ("1",-1,2)  
    assert split_note("3/2") == ("3",0,2) 
    assert split_note("3#/2") == ("3",1,2) 
    assert split_note("3b/2") == ("3",-1,2) 
    assert split_note("b/2") == ("b",0,2) 
    assert split_note("b#/2") == ("b",1,2) 
    assert split_note("bb/2") == ("b",-1,2) 


def test_parse_step():
    assert parse_step("1") == 0
    assert parse_step("1b") == -1
    assert parse_step("1#") == 1
    assert parse_step("1/1") == 0
    assert parse_step("1b/1") == -1
    assert parse_step("1#/1") == 1
    assert parse_step("7") == 11
    assert parse_step("7b") == 10
    assert parse_step("7#") == 12
    assert parse_step("1/2") == 12
    assert parse_step("1b/2") == 11
    assert parse_step("1#/2") == 13
    # assert parse_step("8") == 12 not allowed at now
    assert parse_step("7#/2") == 24

def test_parse_note():
    assert parse_note("c") == 0
    assert parse_note("cb") == -1
    assert parse_note("c#") == 1
    assert parse_note("c/1") == 0
    assert parse_note("cb/1") == -1
    assert parse_note("c#/1") == 1
    assert parse_note("d") == 2
    assert parse_note("b") == 11
    assert parse_note("bb") == 10
    assert parse_note("b#") == 12
    assert parse_note("c/2") == 12
    assert parse_note("cb/2") == 11
    assert parse_note("c#/2") == 13
    assert parse_note("b#/2") == 24
    assert parse_note("B#/2") == 24


def test_parse_score():
    assert parse_score("c,d,e,f,g,a,b", "c") == [0, 2, 4, 5, 7, 9, 11]
    assert parse_score("c,d,e,f,g,a,b", "a") == [3, 5, 7, 8, 10, 12, 14]
    assert parse_score("c,a,a/2", "a/2") == [3, 12, 24]


