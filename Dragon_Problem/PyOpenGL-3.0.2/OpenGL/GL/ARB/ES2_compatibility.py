'''OpenGL extension ARB.ES2_compatibility

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.ES2_compatibility to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extension adds support for features of OpenGL ES 2.0 that are
	missing from OpenGL 3.x. Enabling these features will ease the process
	of porting applications from OpenGL ES 2.0 to OpenGL.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/ES2_compatibility.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.ES2_compatibility import *
### END AUTOGENERATED SECTION
from OpenGL import lazywrapper
from OpenGL.arrays import GLintArray
@lazywrapper.lazy( glGetShaderPrecisionFormat )
def glGetShaderPrecisionFormat(baseOperation, shadertype, precisiontype, range=None,precision=None ):
    """Provides range and precision if not provided, returns (range,precision)"""
    if range is None:
        range = GLintArray.zeros( (2,))
    if precision is None:
        precision = GLintArray.zeros((2,))
    baseOperation( shadertype, precisiontype, range, precision )
    return range, precision
