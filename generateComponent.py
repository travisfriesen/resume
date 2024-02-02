from pdflatex import PDFLaTeX

import jsonExtracter

texdir = 'output/tex/'
pdfdir = 'output/pdf/'

def generate_sources():
    with open ('resumecomponents/sources.tex', 'r') as file:
        sources = file.read().rstrip('\n')

    return sources

def generate_header(config_filename):

    num_elements = jsonExtracter.getNumElements(config_filename)
    data1 = "\n\\begin{center}\n\\textbf{\Huge \scshape "
    #for i in range(num_elements):
        #print(i)
    return data1


def generateFile():
    with open('test.tex', 'r') as file:
        data = file.read().rstrip('\n')

    return data


def createFile(resumetitle):
    open(texdir + resumetitle + ".tex", "x")

def appendFile(resumetitle, passed_data):
    with open(texdir + resumetitle + ".tex", "r") as file:
        source_file = file.read().rstrip('\n')

    f = open(texdir + resumetitle + ".tex", "w")
    f.write(source_file)
    f.write(passed_data)


def make_pdf(resumetitle):
    pdfl = PDFLaTeX.from_texfile(texdir + resumetitle + '.tex')
    pdfl.set_output_directory(pdfdir)
    pdf, log, completed_process = pdfl.create_pdf(keep_pdf_file=True, keep_log_file=False)
