# unit_generator provide the advanced information based on the raw information provided by processors
# e.g.
# Wanted -1 -1 -1 {"tf": 1, "oh": 1} \test\-Km-gkgaAJAx37yEHIERDg 1
# give -1 -1 -1 {"tf": 1, "oh": 1} \test\-Km-gkgaAJAx37yEHIERDg 1
# place -1 -1 -1 {"tf": 1, "oh": 1} \test\-Km-gkgaAJAx37yEHIERDg 1

from . import Unit_generator as ug
Unit_generator = ug.Unit_generator # simplify the importing of class