import datetime

import generateComponent

datetime = datetime.datetime.now().strftime('%m%d%y-%H%M%S')
resumetitle = "ResumeGenerated" + datetime
sources = generateComponent.generate_sources()
data = generateComponent.generate_file()
generateComponent.create_file(resumetitle)
generateComponent.append_file(resumetitle, sources)
bigdata = generateComponent.generate_header('config')
generateComponent.append_file(resumetitle, bigdata)
generateComponent.append_file(resumetitle, data)

generateComponent.make_pdf(resumetitle)
