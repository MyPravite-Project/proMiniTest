'''Autogenerated by get_gl_extensions script, do not edit!'''
from OpenGL import platform as _p
from OpenGL.GL import glget
EXTENSION_NAME = 'GL_NV_depth_clamp'
_p.unpack_constants( """GL_DEPTH_CLAMP_NV 0x864F""", globals())
glget.addGLGetConstant( GL_DEPTH_CLAMP_NV, (1,) )


def glInitDepthClampNV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( EXTENSION_NAME )