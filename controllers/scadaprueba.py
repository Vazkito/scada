def verscada():
    
    
   
    verscada=FORM('Tu nombre:', INPUT(_name='nombre', requires=IS_NOT_EMPTY()), INPUT(_type='submit'))
    
    if verscada.accepts(request,session):
        response.flash = 'formulario aceptado'
    elif verscada.errors:
        response.flash = 'el formulario tiene errores'
    else:
        response.flash = 'por favor complete el formulario'
    
      
    return dict(verscada=verscada)
    
  