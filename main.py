from reactpy import component, web, html
from reactpy.backend.flask import configure
from flask import Flask
from datos import productos

mui = web.module_from_template("react", "@mui/material", fallback="⏳︎")
Container = web.export(mui, "Container")
Grid = web.export(mui, "Grid")
Paper = web.export(mui, "Paper")
Box = web.export(mui, "Box")
Typography = web.export(mui, "Typography")
Rating = web.export(mui, "Rating")

def tarjetas(productos):
  def tarjeta(producto):
     return Grid( 
       {"item": True, "sm": 6, "md": 3, "lg": 3},
       Paper(
         {"elevation": 4},
         html.img({
           "src": f"https://picsum.photos/id/{producto['id']}/400/100",
           "class_name": "img-fluid",
           "style": {"width": "100%", "height": "5rem"}
         }),
         Box(
            {"sx": {"bgcolor": "backgrond.paper"}},
            Typography({"variant": "h5"}, producto["nombre"]),
            Typography({"variant": "h5"}, producto["nombre"]),
             Rating({
                "readOnly": True, 
                "name": "half-rating",
                "precision": 0.5,
                "value": producto["rating"]
            }),  
            Typography({"variant": "body2"}, producto['descripcion']),
            Typography({"variant": "h5"}, producto['precio']),
         )
      )
   )

  """
  width: 100,
  height: 100,
  borderRadius: 1,
  bgcolor: 'primary.main',
  '&:hover': {
  gcolor: 'primary.dark',
 },
 """
  #return Grid(
   # {"container": True, "spacing": "8"},
  #  [ tarjeta(producto) for producto in productos ]
 #)
    
  return Grid( 
    {"container": True, "spacing": "3"},
    [tarjeta(producto) for producto in productos]
   )
  

    
       #     html.img({
        #      "src": f"https://picsum.photos/id/{producto['id']}/400/100",
         #     "class_name": "img-fluid",
          #    "style": {"width": "100%", "height": "5rem"}
           # }),
            
            
              #
              #Rating({
               # "readOnly": True, 
                #"name": "half-rating",
                #"precision": 0.5,
                #"value": producto["rating"]
            #}),  
            #Typography({"variant": "body2"}, producto['descripcion']),
            #Typography({"variant": "h5"}, producto['precio']),
         #)
      #)
   #)
      
  

@component
def App():
    return Container(
      { "maxWidth": "md" },
       tarjetas(productos) 
 )
    

app = Flask(__name__)
configure(app, App)
app.run(host='0.0.0.0', debug=True)