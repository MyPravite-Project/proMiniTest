'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p, constants as _cs, arrays
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_vertex_attrib_64bit'
def _f( function ):
    return _p.createFunction( function,_p.GL,'GL_ARB_vertex_attrib_64bit',False)

@_f
@_p.types(None,_cs.GLuint,_cs.GLdouble)
def glVertexAttribL1d( index,x ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLdouble,_cs.GLdouble)
def glVertexAttribL2d( index,x,y ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glVertexAttribL3d( index,x,y,z ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble,_cs.GLdouble)
def glVertexAttribL4d( index,x,y,z,w ):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLdoubleArray)
def glVertexAttribL1dv( index,v ):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLdoubleArray)
def glVertexAttribL2dv( index,v ):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLdoubleArray)
def glVertexAttribL3dv( index,v ):pass
@_f
@_p.types(None,_cs.GLuint,arrays.GLdoubleArray)
def glVertexAttribL4dv( index,v ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLint,_cs.GLenum,_cs.GLsizei,ctypes.c_void_p)
def glVertexAttribLPointer( index,size,type,stride,pointer ):pass
@_f
@_p.types(None,_cs.GLuint,_cs.GLenum,arrays.GLdoubleArray)
def glGetVertexAttribLdv( index,pname,params ):pass


def glInitVertexAttrib64BitARB():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )
