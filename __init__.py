__version__ = "1.6.1"

import math
from .vector_math import (unit,
                          invert,
                          midVector3,
                          point3plane,
                          compareLines,
                          sumVector3,
                          multiplyVector3,
                          calcVector3,
                          addVector3,
                          dotProduct,
                          crossProduct
)

from .intersection import (unit_v,
                           vector_is_equal,
                           compare_dir_v,
                           intersection
)
from .Line import (Line,
                   ComplexLine
)

from .plane3 import (plane3)
from .plane3coord import (plane3coord)
from .plane3normal import (plane3normal)
from .plane3param import (plane3param)


"""
credits to Bastian Lipka
-
A lib for calculations with vectors (3d) 
"""