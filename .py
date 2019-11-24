from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [
    # Extension("chsv",  ["chsv.py"]),
    Extension("dem",  ["dem.py"]),
    # Extension("execute",  ["execute.py"]),
    # Extension("gih",  ["gih.py"]),
    # Extension("weth",  ["weth.py"]),
    # Extension("tsm",  ["tsm.py"]),
    # Extension("wk",  ["wk.py"]),
    # Extension("gser",["gser.py"]),
    Extension("st",["st.py"]),
    # Extension("gen",["generate_key.py"]),
    # Extension("cli",["client_key.py"]),
    
   
#   ... all your modules that need be compiled ...
]
setup(
    name = 'LBMINH CHATBOT',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
