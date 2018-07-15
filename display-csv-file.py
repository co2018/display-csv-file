# co2018 - 2018-07-11
# display-csv-file project.
# Display a csv file in a web browser.

import sys  # System-specific parameters and functions
import csv  # CSV File Reading and Writing
# html framework from https://pypi.org/project/htmltag/
from htmltag import HTML, html, head, title, \
    body, h1, table, tbody, tr, th, td


class ExcelFR(csv.excel):
    "French specific csv constants"
    delimiter = ";"
    lineterminator = "\n"
    quotechar = ""
    quoting = csv.QUOTE_NONE


def getHtmlTableFromCsvFile(filePath):
    """ Prepare a html table from a csv file """
    mytbody = tbody()
    with open(filePath, 'r') as f:
        fReader = csv.DictReader(f, dialect=ExcelFR())
        myRow = tr()
        for col in fReader.fieldnames:
            myRow = myRow.append(th(col))
        mytbody = mytbody.append(myRow)
        for row in fReader:
            myRow = tr()
            for col in fReader.fieldnames:
                myRow = myRow.append(td(HTML(row[col])))
            mytbody = mytbody.append(myRow)
    return table(mytbody)


def getHtmlPageFromCsvFile(filePath):
    """ Prepare a html page including a table """
    myHtml = html(
        head(
            title=filePath
            )
        )
    myHtml = myHtml.append(
        body(
            h1(filePath),
            getHtmlTableFromCsvFile(filePath),
            )
        )

    with open('display-csv-file.html', 'w') as f:
        f.write('<!DOCTYPE html>')
        f.write(myHtml)


# Main

if __name__ == '__main__':

    usage = 'Usage : python3 {} csv-file'.format(sys.argv[0])

    # Check parameters
    assert len(sys.argv) == 2, usage

    # Generate html file
    getHtmlPageFromCsvFile(sys.argv[1])

