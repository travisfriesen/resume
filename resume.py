from pylatex import Document, Package, Command, Section
from pylatex.utils import italic

# Create a PyLaTeX document
doc = Document(documentclass=['article'], document_options=['letterpaper', '11pt'])

# Set Up Document



# Import necessary packages
doc.preamble.append(Package('latexsym'))
doc.preamble.append(Package('fullpage', options=['empty']))
doc.preamble.append(Package('titlesec'))
doc.preamble.append(Package('marvosym'))
doc.preamble.append(Package('color', options=['usenames','dvipsnames']))
# doc.preamble.append(Package('verbatim'))
doc.preamble.append(Package('enumitem'))
doc.preamble.append(Package('hyperref', options=['hidelinks']))
doc.preamble.append(Package('fancyhdr'))
doc.preamble.append(Package('babel', options=['english']))
doc.preamble.append(Package('tabularx'))
doc.preamble.append(Package('fontawesome5'))
doc.preamble.append(Package('multicol'))

doc.append(Command('setlength', arguments=['multicolsep', "-3.0pt"]))
doc.append(Command('setlength', arguments=['columnsep', "-1.0pt"]))
# doc.preamble.append(Command('input', options=['glyphtounicode']))

with doc.create(Section('A section')):
    doc.append('Some regular text and some ')
    doc.append(italic('italic text. '))

# Save to PDF
doc.generate_pdf('resume', clean_tex=False)
