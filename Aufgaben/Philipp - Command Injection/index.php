<!DOCTYPE html>
<html>
<head>

<!-- your webpage info goes here -->

    <title>Security</title>
	
	<meta name="author" content="Philipp Weitl" />
	<meta name="description" content="A Security Website" />

<!-- you should always add your stylesheet (css) in the head tag so that it starts loading before the page html is being displayed -->	
	<link rel="stylesheet" href="style.css" type="text/css" />
	
</head>
<body>

<!-- webpage content goes here in the body -->

	<div id="page">
		<div id="logo">
			<h1><a href="#/home" id="logoLink">Security</a></h1>
		</div>
		<div id="nav">
			<ul>
				<li><a href="index.php">Home</a></li>
				<li><a href="about.php">About</a></li>
				<li><a href="help.php">Help</a></li>
			</ul>	
		</div>
		<div id="content">
			<h2>Home</h2>
			<p>
				Auf dieser Seite k&ouml;nnt ihr euere F&auml;higkeiten testen.
			</p>
			<p> 
				Am besten schaut ihr euch mal ein wenig um! :) 
			</p>
			<p>
				Hier kannst du spielen:
			</p>
			<form action="#" method="post">
				<input type="text" name="domain">
				<input type="submit" value="submit" name="submit">
			</form>
			
		</div>
	</div>
<?php
if(isset($_POST['submit'])){
	$target = $_REQUEST[ 'domain' ];
	if (strpos($target,'files') !== false) {
    		echo '<pre>NOPE</pre>';
	}else{

	$cmd = shell_exec( 'cat  ' . $target );
	echo '<pre>'.$cmd.'</pre>';
	}
}
?>
</body>
</html>
