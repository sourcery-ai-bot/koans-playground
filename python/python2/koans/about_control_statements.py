#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutControlStatements(Koan):

    def test_if_then_else_statements(self):
        result = 'true value'
        self.assertEqual('true value', result)

    def test_if_then_statements(self):
        result = 'default value'
        result = 'true value'
        self.assertEqual('true value', result)

    def test_if_then_elif_else_statements(self):
        result = 'true value'
        self.assertEqual('true value', result)

    def test_while_statement(self):
        result = 1
        for i in range(1, 11):
            result *= i
        self.assertEqual(3628800, result)

    def test_break_statement(self):
        i = 1
        result = 1
        while True:
            if i > 10: break
            result *= i
            i += 1
        self.assertEqual(3628800, result)

    def test_continue_statement(self):
        i = 0
        result = []
        while i < 10:
            i += 1
            if (i % 2) == 0: continue
            result.append(i)
        self.assertEqual([1, 3, 5, 7, 9], result)

    def test_for_statement(self):
        phrase = ["fish", "and", "chips"]
        result = [item.upper() for item in phrase]
        self.assertEqual(["FISH", "AND", "CHIPS"], result)

    def test_for_statement_with_tuples(self):
        round_table = [
            ("Lancelot", "Blue"),
            ("Galahad", "I don't know!"),
            ("Robin", "Blue! I mean Green!"),
            ("Arthur", "Is that an African Swallow or Amazonian Swallow?")
        ]
        result = ["Contestant: '" + knight + \
            "'   Answer: '" + answer + "'" for knight, answer in round_table]
        text = "Contestant: 'Robin'   Answer: 'Blue! I mean Green!'"

        self.assertMatch(text, result[2])

        self.assertNoMatch(text, result[0])
        self.assertNoMatch(text, result[1])
        self.assertNoMatch(text, result[3])
