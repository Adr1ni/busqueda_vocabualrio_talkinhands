lista = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r',
    's','t','u','v','w','x','y','z','olanda','cristhian','cesar','claudio','tecsup'
    'abril','agosto','ahora','amanecer','año','antes','atardecer','ayer','bobadilla','cumpleaños','día','vargas'
    'diciembre','domingo','enero','estaciones','febrero','feriado','futuro','hora','hoy','invierno',
    'jueves','julio','junio','lunes','mañana','martes','marzo','mayo','mes','miércoles','minuto',
    'navidad','noche','nunca','octubre','otoño','pasado','primavera','próximo','sabado','semana',
    'septiembre','temprano','vacaciones','verano','viernes','amarillo','anaranjado','arte','audífono','azul','blanco','borrador','celeste','ciencia','clase',
    'colegio','colores','computadora','cuaderno','diccionario','diploma','examen','fólder','geografía',
    'goma','historia','inicial','lapicero','lápiz','lenguaje','libreta','libro','marrón','matemática',
    'mochila','morado','mota','negro','nota','papel','pizarra','plomo','plumones','primaria','regla',
    'rojo','rosado','secundaria','tajador','tarea','tiza','universidad','verde','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15', 
    '20','21','26','30','31','40','50','60','61','100','1000','abuela','abuelo','adulto','amigo','bebé','cuñado','esposa','esposo',
    'estudiante','familia','hermana','hija','hijo','hombre','joven','mamá',
    'mujer','nieto','niños','papá','persona','primo','sobrina','sobrino',
    'soltera','soltero','tía','tío','vecino','aceitunas','antiuchos','arroz','azucar','caramelo','carne_de_pescado','carne','causa',
    'ceviche','chorizo','ensalada','frijoles','galleta','gelatina','hamburguesa','helado',
    'hotdog','huevo','jamón','ketchup','mantequilla','mayonesa','pan','papa','parrillada',
    'queso','sal','sandwich','sopa','tallarines','tamal','torta','tortilla','anillo','aretes','blusa','calzon','calzoncillo','camisa','cartera','chaleco','chalina',
    'chompa','chullo','collar','corbata','correa','falda','gorro','guantes','maleta','mandil',
    'medias','pantalon','pañuelo','parguas','pijama','polo','poncho','reloj','saco','short',
    'sombrero','sosten','uniforme','vestido','vincha','zapatilla','zapatos','ciruela','coco','durazno','fresas','limón','mandarina','mango','manzana','naranja','palta',
    'papaya','pera','piña','platano', 'ajedrez','arbito','atletismo','automovilismo','avión','básquet','boxeo','capitán','ciclismo',
    'cubo','dados','estadio','fútbol','jugador','motociclismo','muñeca','pelota','pesca','ping'
    ,'pistola','reglamento','soga','soldado','tambor','tenis','tren','trompo','voleybol','yases',
    'adorar','aleluya','alma','altar','amen','amor','ángel','apóstol','arrepentida','ascensión',
    'bautizo','bendecir','biblia','capítulo','católica','cielo','confirmación','creer','cruz',
    'diablo','dios','evangélica','fe','gloria','gracia','imagen','infierno','jesús','judío',
    'mandamiento','matrimonio','milagro','misa','misionero','obispo','ofrenda','papa','pastor',
    'pecado','religión','resurrección','rezar','sacerdote','sacramento','salvación','tentación',
    'abandonar','abrazar','abrigar','acariciar','aceptar','acompañar','acostumbrar','adelgazar',
    'afeitar','agarrar','agradecer','aguantar','amarrar','apagar','aplaudir','aprender','apurar',
    'arruinar','aterrizar','aumentar','avergonzar','ayudar','bailar','bañar','barrer','beber','besar',
    'borrar','botar','buscar','caer','calcular','callar','calmar','cambiar','caminar','cantar','castigar',
    'cerrar','chocar','clavar','cobrar','cocinar','coger','colgar','comer','comprar','comprender','confesar',
    'continuar','copiar','cortar','coser','crecer','creer','cruzar','curiosear','dar','decir','dejar',
    'despertar','dialogar','dibujar','doler','dormir','empezar','empujar','enseñar','entrar','envolver',
    'equibocar','escoger','escribir','escuchar','esperar','explicar','firmar','fumar','ganar','gastar',
    'golpear','guardar','gustar','intercambiar','inventar','jugar','lavar','leer','limpiar','llegar',
    'llevar','llorar','llover','mandar','manejar','marearse','medir','memorizar','montar','morder','morir',
    'multiplicar','nacer','necesitar','obedecer','obligar','observar','olvidar','operar','ordernar','pensar',
    'perder','perdonar','perseguir','pintar','planchar','practicar','querer','quitar','recodar','rebalar',
    'respetar','respirar','rezar','robar','romper','saber','salir','saltar','saludar','sentarse','sentir',
    'significar','soñar','sonreir','subir','telefonear','terminar','tirar','visitar','vivir','volar','adinerado','ágil','alegre','alto','amargo','antipático','asustado',
    'bajo','bien','blando','bonita','brillo','bueno','callado','cansado','caro','celoso','cerrado','chismoso','claro',
    'cobarde','contento','corto','cuadrado','cualquier','despacio','diferente','divertido','dulce','egoísta','enamorado'
    ,'enfermo','estudioso','fácil','falso','falta','feliz','feo','flaco','fresco','frío','fuerte','fumador','gordo',
    'gracioso','grande','gritón','húmedo','igual','importante','largo','limpio','lleno','loco','malo','mejor','mentiroso',
    'mío','molesto','nervioso','oscuro','otro','paciencia','pequeño','pesado','pobre','preocupado','rápido','redondo',
    'rico','seco','sediento','sorprendido','suave','sucio','tacaño','tonto','torpe','tranquilo','triste','vergonzoso'
    ,'viejo','cerca','con','de','delante','dentro','detras','encima','entre','ese','hacia','junto','mucho',
    'nada','por','si','siempre','solamente','solo','tampoco','verdad','y','áfrica','alemania','américa','argentina','bolivia','brasil','canadá','chile','china','colombia',
    'cuba','ecuardor','egipto','españa','europa','francia','holanda','india','inglaterra','italia','méxico',
    'oceanía','país','paraguay','perú','rusia','uruguay','venezuela','araña','bombero','búho','burro','caballo','chancho','chofer','cocodrilo','cóndor','conejo','culebra',
    'elefante','gallina','gallo','gato','gusano','jirafa','león','llama','loro','mariposa','mono','mosca','niñera',
    'oso','oveja','pájaro','pato','pavo','perro','pescado','pollo','sapo','toro','tortuga','vaca','zancudo','zorro','abogado','albañil','carpintero','ingeniero','jardinero','juez','dentista','dibujante','director','doctor',
    'electricista','ingeniero','jardinero','juez','mecánico','presidente','profesora','sacerdote',
    'sastre','secretaria','aeropuerto','amazonas','ancash','ate','avenida','ayacucho',
    'cajamarca','callao','cárcel','casa','cementerio','chiclayo','chorrillos','chosica','colegio','comas','comisaría','correos',
    'cusco','edificio','estadio','fábrica','hospital','huancavelica','huancayo','huánuco','ica','iglesia','iquitos','lima',
    'miraflores','municipalidad','puno','restaurant','rimac','surco','tacna','trujillo','tumbes','ucayali',
     'el','él','ella','ellas','ellos','guión','la','lo','los','mi','nosotros','paréntesis','punto',
    'subrayado','tú','un','una','ustedes','yo','almohada','baño','basura','botella','caja','cama','casa','cepillo','champu','clóset','cocina','colcha','colchón','comedor','cuchara','cucharón','cuchillo','desodorante','dormitorio','ducha','escoba','espejo',
    'frazada','funda','horno','jabón','jardín','lámpara','lavandería','licuado','llave','mantel','mesa','olla','pared','peine',
    'plato','puerta','radio','refrigeradora','reja','sábana','sala','sartén','servilleta','silla','sofá','talco','techo','teléfono','televisor',
    'tenedor','timbre','toalla','vaso','aire','árbol','calor','fresco','lluvia','luz','mar','montaña','mundo','neblina','nieve','nube','ola',
    'piedra','rayo','río','sol','terremoto','tierra','universo','abrir','access','aceptar','alineacion','archivo','autoformato','calculadora','cancelar','cerrar','columna',
    'comando','comentario','computación','configuración','contraseña','correo','cortar','cursiva',
    'cursor','diskettera','encabezado','escape','estilo','excel','filas','filtro','flecha','formato',
    'formulario','fuente','guardar','hardware','hipervinculo','icono','impresora','inicio','internet',
    'justificado','línea','margen','maximizar','máximo','mayuscula','microsoft','mínimo','minúscula','monitor',
    'mouse','negrita','nuevo','ordenar','página','paint','pantalla','programa','promedio','puntero','red','regleta',
    'regresar','sangría','seleccionar','software','sombreado','tabular','tamaño','teclado','texto','ventana',
    'vocabulario','windows',
]

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def create_binary_search_tree(sorted_list, start, end):
    if start > end:
        return None
    middle_index = (start + end) // 2
    root = Node(sorted_list[middle_index])
    root.left = create_binary_search_tree(sorted_list, start, middle_index - 1)
    root.right = create_binary_search_tree(sorted_list, middle_index + 1, end)
    return root

orden = sorted(lista)
raiz = create_binary_search_tree(orden, 0, len(orden) - 1)

def preorder_traversal(root):
    result = []
    stack = []
    node = root
    while node or stack:
        if node:
            result.append(node.data)
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            node = node.right
    return result

result = preorder_traversal(raiz)

