from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [
    Extension("amlich",  ["amlich.py"]),
    Extension("begin",  ["begin.py"]),
    Extension("checkser",  ["checkser.py"]),
    Extension("dem",  ["dem.py"]),
    Extension("execute",["execute.py"]),
    Extension("fun",["fun.py"]),
    Extension("gih",["gih.py"]),
    Extension("helper",["helper.py"]),
    Extension("legal",["legal.py"]),
#    Extension("loto",["loto.py"]),
    Extension("lun",["lun.py"]),
#    Extension("news",["news.py"]),
    Extension("ngayle",["ngayle.py"]),
    Extension("onoff",["onoff.py"]),
    Extension("processss",["processss.py"]),
    Extension("ptz",["ptz.py"]),
    Extension("radio",["radio.py"]),
    Extension("speaking",["speaking.py"]),
    Extension("st",["st.py"]),	
    Extension("thu",["thu.py"]),
    Extension("tintuc",["tintuc.py"]),
    Extension("tsm",["tsm.py"]),
    Extension("weth",["weth.py"]),
    Extension("wk",["wk.py"]),
#    Extension("",[".py"]),
#    Extension("",[".py"]),
#    Extension("",[".py"]),	
#    Extension("",[".py"]),
   
#   ... all your modules that need be compiled ...
]
setup(
    name = 'LBMINH CHATBOT',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
