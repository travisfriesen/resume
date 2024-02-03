from pdflatex import PDFLaTeX

import jsonExtracter

texdir = 'output/tex/'
pdfdir = 'output/pdf/'


def generate_sources():
    with open('resumecomponents/sources.tex', 'r') as file:
        sources = file.read().rstrip('\n')

    return sources


def generate_header(config_filename):
    data = get_header_data(config_filename)
    num_elements = jsonExtracter.get_num_elements(config_filename)
    data1 = "\n\n\n%----------HEADING----------\n\\begin{center}\n\\textbf{\\Huge \\scshape " + data[1] + "} \\\\ \\vspace{1pt}\n"
    for i in range(int(num_elements) - 1):
        if i != int(num_elements) - 2:
            if data[i*3 + 3] == 'text':
                data1 = data1 + "\\small " + data[i*3 + 4] + " $|$\n "
            elif data[i*3 + 3] == 'email' or data[i*3 + 3] == 'link':
                data1 = data1 + "\\href{ " + data[i*3 + 5] + "}{\\underline{" + data[i*3 + 4] + "}} $|$\n "
        else:
            if i == int(num_elements) - 2:
                if data[i*3 + 3] == 'text':
                    data1 = data1 + "\\small " + data[i*3 + 4] + "\n "
                elif data[i*3 + 3] == 'email' or data[i*3 + 3] == 'link':
                    data1 = data1 + "\\href{ " + data[i*3 + 5] + "}{\\underline{" + data[i*3 + 4] + "}} \n "

    data1 = data1 + "\\end{center}\n"
    return data1


def combine_header_array(a, b):
    a.extend(b)
    return a


def get_header_data(config_filename):
    num_elements = jsonExtracter.get_num_elements(config_filename)
    data = []
    for i in range(int(num_elements)):
        data = combine_header_array(data, jsonExtracter.get_header_element(i))

    return data


def generate_file():
    with open('test.tex', 'r') as file:
        data = file.read().rstrip('\n')

    return data


def create_file(resumetitle):
    open(texdir + resumetitle + ".tex", "x")


def append_file(resumetitle, passed_data):
    with open(texdir + resumetitle + ".tex", "r") as file:
        source_file = file.read().rstrip('\n')

    f = open(texdir + resumetitle + ".tex", "w")
    f.write(source_file)
    f.write(passed_data)


def make_pdf(resumetitle):
    pdfl = PDFLaTeX.from_texfile(texdir + resumetitle + '.tex')
    pdfl.set_output_directory(pdfdir)
    pdfl.create_pdf(keep_pdf_file=True, keep_log_file=False)
