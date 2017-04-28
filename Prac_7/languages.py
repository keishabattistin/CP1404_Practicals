from Prac_7.ProgrammingLanguage import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage('RUBY', 'Dynamic', True, 1995)
    python = ProgrammingLanguage('PYTHON', 'Dynamic', True, 1991)
    vb = ProgrammingLanguage('VISUAL BASIC', 'Static', False, 1991)

    print(ruby)
    print(python)
    print(vb)


main()
