<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Cosmetic Store</title>
<meta http-equiv="Content-Type" content="text/html; charset=windows-1252" />
<link rel="stylesheet" type="text/css" href="style.css" />
<!--[if IE 6]>
<link rel="stylesheet" type="text/css" href="iecss.css" />
<![endif]-->
<script type="text/javascript" src="js/boxOver.js"></script>
</head>
<body>
<div id="main_container">
  <div class="top_bar">
  
  
  <div id="form">
  
  <form method="get" action="results.php" enctype="multipart/form-data">
  
  
    <div class="top_search">
      <div class="search_text"><font color="black">Search comsmetic :)</font></div>
      <input type="text" class="search_input" name="user_query" placeholder="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Search your need"/>
      <input type="submit" value="Search" class="search_bt" name="search"/>
    </div>
</form>

  <div id="form">
  <form method="POST" action="logincheck.php" enctype="multipart/form-data">

    <div class="top_search">
      <div class="search_text1"><font color="black">Login</font></div>
      <input type="text" class="search_input1" name="text1" placeholder="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ID"/>
      <input type="text" class="search_input1" name="password1" placeholder="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;PWD"/>
      <input type="submit" value="Login" class="search_bt" name="login"/>
    <button><a href="join.php" style="text-decoration:none;color:black">Join</a></button>
    </div>
    
    </form>
    
    </div>
    
    
   
  <div id="header">
    <div id="logo"> <a href="index.php"><img src="images/logo.png" alt="" border="0" width="237" height="140" /></a> </div>
    <div class="oferte_content">
      <div class="top_divider"><img src="images/header_divider.png" alt="" width="1" height="164" /></div>
      <div class="oferta">
       
    <?php
    
    //sliderdata();



?>
      </div>

      <div class="top_divider"><img src="images/header_divider.png" alt="" width="1" height="164" /></div>
    </div>
    <!-- end of oferte_content-->
  </div>
  <div id="main_content">
    <div id="menu_tab">
      <div class="left_menu_corner"></div>
      <ul class="menu">
        <li><a href="index.php" class="nav1"><font color="white"> Home</a></li>
        <li class="divider"></li>
        <li><a href="allproducts.php" class="nav2"><font color="white">All Products</a></li>
        <li class="divider"></li>
     
        <li class="divider"></li>
        <li class="divider"></li>
        <li><a href="cart.php" class="nav5"><font color="white">Cart</a></li>
        <li class="divider"></li>
        <li class="divider"></li>
        
       
        
        
      </ul>
      <div class="right_menu_corner"></div>
    </div>
