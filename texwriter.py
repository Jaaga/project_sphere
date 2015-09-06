#!/bin/python

import csv

# \definecolor{Gray}{gray}{0.90}

def main():

    preamble = r"""\documentclass[10pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{array, lmodern}
\usepackage[margin=2cm]{geometry}
\usepackage{ragged2e}
\usepackage{xcolor,colortbl}
\newcolumntype{M}[1]{>{\RaggedRight\hspace{0pt}}m{#1}}
\title{Jaaga Project Sphere - Interview Responses}
\author{Team Sphere}
\date{29 August 2015}

"""

    openTag = r"\begin{document}" + "\n"

    fileString = preamble + openTag

    tableTemplate = r"""\begin{tabular}{M{0.125in}M{2.75in}M{0.125in}}
\rule{0pt}{0.125in}  & & \\
\rule{0pt}{1in} &\_infobite& \\
\rule{0pt}{0.25in} &\_code& \\
\rule{0pt}{0.125in} & & \\
\end{tabular}
"""
    tables = ""

    data = []

    with open('greenopia.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    for row in data:
        section = row['Code']
        # sectionTag = r"\section*{"+section+'}'
        # fileString += sectionTag
        for key in row:
            if key != 'Code':
                subsection = key
                filtered = filter(None, row[key].split('\\'))
                # if len(filtered) > 0:
                #     subsectionTag = '\subsection*{'+subsection+'}'
                #     fileString += subsectionTag
                count = 1
                for byte in filtered:
                    byte = byte.strip()
                    if byte != '':
                        code = section+'-'+subsection+'-'+str(count)
                        byte = byte.replace('%', '\%').replace('&', '\&')
                        fileString += tableTemplate.replace("\_infobite", byte).replace("\_code", code)
                        count += 1
        #     fileString += r'\end{subsection}'
        # fileString += r'\end{section}'

    #
    # for b in a:
    #     tables += tableTemplate.replace("\_infobite", b).replace("\_code", code)

    closingTag = r"\end{document}"
    fileString += closingTag

    outputFile = "greenopia.tex"
    open(outputFile, 'w').write(fileString)


if __name__ == "__main__":
    main()
