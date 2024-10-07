<h1><br />Actividad 4 arquitectura basada-cliente</h1>
<p>En el presente trabajo se presenta un ejemplo de un aplicativo web que emplea el modelo de cliente-servidor.</p>
<p><br />La p&aacute;gina consiste de dos secciones, la primera secci&oacute;n es de miscel&aacute;nea, consiste en varias secciones experimentales como una manera de probar las funcionalidades de una p&aacute;gina web mediate Python, y la segunda secci&oacute;n es de un chat en donde cada usuario puede crear su propia sala y unirse a ellas, o permitir que otros usuarios se unan tambi&eacute;n, en dicha secci&oacute;n del aplicativo web, los usuarios se pueden comunicar entre s&iacute;.</p>
<p>Las herramientas utlilizadas fueron:</p>
<ul>
<li>Visual Studio Code para el proceso de la codificaci&oacute;n.</li>
<li>Bootstrap para brindar una interfaz gr&aacute;fica m&aacute;s personalizada y (hasta cierto punto) limpia por medio de sus formatos propios.</li>
<li>CSS Online Editor de W3 Schools para experimentar con los distintos formatos y etiquetas de CSS.</li>
<li>HTML Online Editor de W3 Schools para experimentar con las distintas etiquetas manejadas en CSS.</li>
<li>Flask para el dise&ntilde;o del entorno de trabajo y del establecimiento de las redirecciones y los enlaces entre cada p&aacute;gina con el ejecutable de Python.</li>
</ul>
<p>Se emplearon los siguientes lenguajes de programaci&oacute;n:</p>
<ul>
<li>Python para la codificaci&oacute;n de programa principal (el ejecutable) que posee todos los procedimientos y las conexiones de los <em>sockets</em>.</li>
<li>Javascript para la funci&oacute;n de los mensajes dentro de la secci&oacute;n de "sala".</li>
</ul>
<p>Se emplearon los siguientes <strong>no</strong> lenguajes de programaci&oacute;n:</p>
<ul>
<li>HTML para la creaci&oacute;n de las distintas secciones de la p&aacute;gina web.</li>
<li>CSS para el dise&ntilde;o de la p&aacute;gina web, brindando un aspecto m&aacute;s &uacute;nico y personalizado en lo posible.</li>
</ul>
<p>Se emplearon las siguientes librer&iacute;as:</p>
<ul>
<li>Random para el m&eacute;todo choice() que permite otorgar una numeraci&oacute;n de sala aleatoria para cada usuario quen desee crear una nueva sala.</li>
<li>Flask-SocketIO para establecer la comunicaci&oacute;n entre los clientes y el servidor.</li>
</ul>

<p>En el presente c&oacute;digo se presenta una aplicaci&oacute;n web realizada a trav&eacute;s de Flask empleando Socket.IO para las comunicaciones entre los clientes.</p>
<p>Las funciones que realiza el programa se clasifican de la siguiente manera:</p>
<ol>
<li>Importaciones y ajustes:
<ul>
<li>Importa los m&oacute;dulos necesarios.</li>
<li>Inicia el&nbsp;<em>framework</em> de Flask y el Socket.IO.</li>
<li>Configura un diccionario para almacenar informaci&oacute;n.</li>
</ul>
</li>
<li>Home:
<ul>
<li>Borra las sesiones.</li>
<li>Maneja las peticiones POST para unirse o crear una sala de chat.</li>
<li>Valida el c&oacute;digo de grupo y redirecciona al usuario a la sala de chat.</li>
</ul>
</li>
<li>Sala:
<ul>
<li>Revisa si la sesi&oacute;n es v&aacute;lida y renderiza la sala de chat.</li>
</ul>
</li>
<li>Funcionalidades de Socket.IO:
<ul>
<li>Gestiona los mensajes, conexiones y desconexiones.</li>
<li>Gestiona las membres&iacute;as de las salas y la emisi&oacute;n de los mensaje.</li>
</ul>
</li>
</ol>
<p>Se tiene la expectativa que una vez se abra la p&aacute;gina principal, el usuario podr&aacute; explorar el contenido de la pagina web, y cuando se vaya a dirigir a la secci&oacute;n de la sala de chat, tenga que ingresar su nombre y crear una sala, o unirse a ella. Una vez dentro, puede interactuar con otros usuarios.</p>
