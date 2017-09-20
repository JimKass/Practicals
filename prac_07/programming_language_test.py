"""
Will test the ProgrammingLanguage class
"""

from prac_07.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    get_dynamic_languages([ruby, python, visual_basic])


def get_dynamic_languages(languages):
    print("The dynamically typed langauges are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
