# co2018 - 2018-07-11
# display-csv-file project.
# Display a csv file in a web browser.

import sys         # System-specific parameters and functions
import csv         # CSV File Reading and Writing
import webbrowser  # Convenient Web-browser controller
# html framework from https://pypi.org/project/htmltag/
from htmltag import HTML, html, head, title, link, \
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
                myRow = myRow.append(td(HTML(row[col]), _class=col))
            mytbody = mytbody.append(myRow)
    return table(mytbody)


def getHtmlPageFromCsvFile(filePath, css, title):
    """ Prepare a html page including a table """
    myHtml = html(
        head(
            link(' ', rel='stylesheet', type='text/css', href=css),
            title=filePath
            )
        )
    myHtml = myHtml.append(
        body(
            h1(title),
            getHtmlTableFromCsvFile(filePath),
            )
        )
    return myHtml


# Main

if __name__ == '__main__':

    usage = 'Usage : python3 {} csv-file css-file title'.format(sys.argv[0])

    # Check parameters
    assert len(sys.argv) == 4, usage

    # Generate and display html file
    outfile = 'display-csv-file.html'
    with open(outfile, 'w') as f:
        f.write('<!DOCTYPE html>')
        f.write(getHtmlPageFromCsvFile(sys.argv[1], sys.argv[2], sys.argv[3]))
    webbrowser.open(outfile)

