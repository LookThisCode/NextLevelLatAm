<?php
	error_reporting(E_ERROR);
	
	function buscar($query){
		$query = str_replace(" ","%20",$query);
		$url = 'https://www.googleapis.com/plus/v1/people?query='.$query.'&key=AIzaSyBhLc1MHRVuTG8TdyGtEvjD8aBxvXnpR7w';
		$result = file_get_contents($url);
		$result = json_decode($result);
		//var_dump($result);

		foreach ($result->items as $persona){
			echo '<div class="persona">';
			echo '<img src="'.$persona->image->url.'"/>';
			echo '<a onclick="verPersona('. "'" .$persona->id. "'" . ')" href="javascript:void(0);">' . $persona->displayName . '</a>';
			echo '</div>';
		}
	}

	function verPersona($id){
		$url = 'https://www.googleapis.com/plus/v1/people/'.$id.'/?key=AIzaSyBhLc1MHRVuTG8TdyGtEvjD8aBxvXnpR7w';
		$result = file_get_contents($url);
		$result = json_decode($result);
		foreach ($result->placesLived as $lugares){
			$mapa = '<img src="http://maps.google.com/maps/api/staticmap?center='.$lugares->value.'&amp;zoom=16&amp;size=279x209&amp;maptype=roadmap%20&amp;markers='.$lugares->value.'&amp;sensor=false" alt=""> <br/> ' . $lugares->value;
			return $mapa;
		}

		$mapa = "El usuario no tiene visible su ubicación";
		return $mapa;
	}
?>