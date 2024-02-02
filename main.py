import datetime

import generateComponent

datetime = datetime.datetime.now().strftime('%m%d%y-%H%M%S')
resumetitle = "ResumeGenerated" + datetime
sources = generateComponent.generate_sources()
data = generateComponent.generateFile()
generateComponent.createFile(resumetitle)
generateComponent.appendFile(resumetitle, sources)
#bigdata = generateComponent.generate_header('config')
#generateComponent.appendFile(resumetitle, bigdata)
generateComponent.appendFile(resumetitle, data)

generateComponent.make_pdf(resumetitle)
