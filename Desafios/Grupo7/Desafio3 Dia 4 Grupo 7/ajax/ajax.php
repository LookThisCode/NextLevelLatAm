<?php
	include_once("../lib/php/common.php");

	if (isset($_POST['action'])){
		$action = $_POST['action'];
	}

	switch ($action) {
		case 'buscarPersonas':
			$nombre = $_POST['nombre'];
			echo buscar($nombre);
			break;
		case 'verPersona':
			$id = $_POST['id'];
			echo verPersona($id);
			break;
	}
?>