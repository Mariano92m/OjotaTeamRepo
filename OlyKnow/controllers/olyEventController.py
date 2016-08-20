# -*- coding: utf-8 -*-
# intente algo como
def olyEvent():
	    ##form = crud.crude( db.evento.nombre(request.args (0)),
      ##                  db.evento.descripcion(request.args (0)),
        ##                db.evento.categoria(request.args (0)),
          ##              db.evento.fecha_hora(request.args (0)),
            ##            db.evento.costo(request.args (0)),
              ##          db.evento.organizador(request.args (0))
                      ##  )
    #return dict (form=form)

    form = SQLFORM(db.evento)
    if form.accepts(request.vars, session):
        response.flash = 'form accepted'
    elif form.errors:
        response.flash = 'form has errors'
    else:
        response.flash = 'please fill out the form'
    return dict(form=form)