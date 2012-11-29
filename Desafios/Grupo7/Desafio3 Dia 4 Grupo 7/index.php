<html>
	<head>
	    <script type="text/javascript" src="lib/js/jquery.js"></script>		
		<title>+NextLevel - Grupo 7</title>
		<style>
			.caja{ 
				margin:auto;
				width:350px;
			    background-color: #f7f7f7;  
			    border: 1px solid #cccccc;  
			    color: #333333;  
			    padding: 10px;  
			    font-size: 13px;  
			    font-weight: bold;  
			    text-align: center;
			}  		

			#btnBoton{
				margin-top:10px;
			}

			.persona{
				margin-left:15px;
				height:60px;
				font-size:14px;
				color:#333333;
				padding-top:10px;
				line-height:4em;
			}

			.persona img{
				float:left;
				padding-right:10px;
			}
		</style>

		<script>

		  function verPersona(id){
		      req = $.ajax({
		        type: 'POST',
		        url: 'ajax/ajax.php',
		        data: { 
					'id': id,
		          'action': 'verPersona'
		        },
		        success: function(data){
		          $("#resultados").html(data);
		        }
		      });     
		    }  

		  function buscarPersonas(){
		  	nombre = document.getElementById('txtNombre').value;
		  	$("#cargando").show();
		      req = $.ajax({
		        type: 'POST',
		        url: 'ajax/ajax.php',
		        data: { 
					'nombre': nombre,
		          'action': 'buscarPersonas'
		        },
		        success: function(data){
		          $("#resultados").html(data);
		        }
		      });     
		    }  

		</script>
	</head>

	<body>
		<div class="caja">
			Buscar en Google Plus: <input type="text" id="txtNombre" name="txtNombre" placeholder="nombre" /> <br/>
			<button onclick="buscarPersonas();" id="btnBoton">Buscar</button>
		</div>

		<div id="resultados">
		</div>
	</body>
</html>