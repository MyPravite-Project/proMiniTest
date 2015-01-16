'''OpenGL extension VERSION.GL_1_4

This module customises the behaviour of the 
OpenGL.raw.GL.VERSION.GL_1_4 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/VERSION/GL_1_4.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.VERSION.GL_1_4 import *
### END AUTOGENERATED SECTION
GL_CURRENT_FOG_COORD = GL_CURRENT_FOG_COORDINATE # alias
GL_FOG_COORD = GL_FOG_COORDINATE # alias
GL_FOG_COORD_ARRAY = GL_FOG_COORDINATE_ARRAY # alias
GL_FOG_COORD_ARRAY_POINTER = GL_FOG_COORDINATE_ARRAY_POINTER # alias
GL_FOG_COORD_ARRAY_STRIDE = GL_FOG_COORDINATE_ARRAY_STRIDE # alias
GL_FOG_COORD_ARRAY_TYPE = GL_FOG_COORDINATE_ARRAY_TYPE # alias
GL_FOG_COORD_SRC = GL_FOG_COORDINATE_SOURCE # alias