<?php
error_reporting(E_ALL & ~E_NOTICE);
ini_set('display_errors', 1);


$w = 720; $h = 220;
$ctx = imagecreatetruecolor($w, $h); // makeCanvas(700, 220)

$red = imagecolorallocate($ctx, 90, 0, 0);
$white = imagecolorallocate($ctx, 255, 255, 255);

imagefilledrectangle($ctx, $w,$h,0,0,$white);

$rates = json_decode(file_get_contents('https://kodaktor.ru/j/rates'), true); 

$names = array_map(function($x) {return $x['name'];}, $rates); // const names = rates.map(({ name }) => name);
$rates = array_map(function($x) {return (float)$x['sell'];}, $rates); // rates = rates.map(({ sell }) => Number(sell)); 

$rates = array_map(function($x) use ($rates, $h) {return $x * $h / max($rates);}, $rates); // rates = rates.map(x => x * h / Math.max(...rates));
$wRect = $w / count($rates); //const wRect = Math.floor(w/rates.length);

$font_path = './arial.ttf';
$font_size = 10;
foreach($rates as $i => $rate){
	
	imagefilledrectangle($ctx, $x1 = $i * $wRect, $y1 = $h - $rate, $x1 + $wRect-5, $h, $red); //*/
	
	$size = imageftbbox($font_size, 0, $font_path, $names[$i])[2]; // берём длину текста
	$size /=2; // берём серидину текста
	
	imagettftext( $ctx, $font_size, 0, $x1 + ($wRect / 2 - $size), $h - 5, $white, $font_path, $names[$i]);
	
}

header('Content-type: image/jpeg');
imageJpeg($ctx);

