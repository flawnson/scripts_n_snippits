# XXX: Date: November 6th, 2019
#      Ever find yourself needing to extract company names given only a list of e-mails?
#      Me neither, but my boss did, so I made this script that iterates over a list of strings to extract substrings.
#      This was my first time using regex.

import re


def email_extractor(codex):

    name_list = []

    if type(codex) == str:
        codex = re.split(',| |:', codex)

    for email in codex:
        name_list.append(email[email.find("@") + 1:email.rfind(".")])

    return name_list

