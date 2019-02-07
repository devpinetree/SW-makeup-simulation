
<?php
include("functions/functions.php");
?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">


<?php

include("header.php");

cart();


?>




    <!-- end of menu tab -->
<br><br>
<div class="left_content">
      <div class="title_box">Categories</div>
      <ul class="left_menu">
        
 <?php 
     getcats(); 
     

 ?>
        
      </ul>
     
<div class="title_box">Manufacturers</div>
      <ul class="left_menu">
        

    <?php  getbrands();  ?>


 
</ul>
 <br>
 <br>

     
    
      
           <br>
 <br>
 <br>
     
 
       

    </div>
    
    
    
    <!-- end of left content -->
    <div class="center_content">
     
      
<?php

details();

?>



 <div class="left_content">
   


     





   <br><br><br><br>

  


     
     <br><br><br><br>

 </div>
 

    


  <?php
  
  
  ?>
     
      
      
      
    </div>
    <!-- end of center content -->
    <div class="right_content">
      <div class="shopping_cart">
        <div class="cart_title"><font color="white">Shopping cart</div>
        <div class="cart_details"><font color="skyblue"><?php total_items(); ?></font>&nbsp;item(s)<br />
          <span class="border_cart"></span> Total: <span class="price"><?php total_price(); ?></span> </div>
        <div class="cart_icon"><a href="cart.php" title="header=[Checkout] body=[&nbsp;] fade=[on]"><img src="images/shoppingcart.png" alt="" width="48" height="48" border="0" /></a></div>
      </div>
      
      <br><br><br><br>
      
      
     

     
     
     <br /><br /><br /><br />
     
     
    </div>
    <!-- end of right content -->
  </div>
  <!-- end of main content -->
  <div class="footer">
    <div class="left_footer"> <img src="images/footer_logo.png" alt="" width="170" height="49"/> </div>
    <div class="center_footer"> All Rights Reserved 2018<br />
      
      <img src="images/payment.gif" alt="" /> </div>
    <div class="right_footer"> <a href="#">home</a> <a href="#">about</a> <a href="#">sitemap</a> <a href="#">rss</a> <a href="contact.html">contact us</a> </div>
  </div>
</div>
<!-- end of main_container -->
</body>
</html>
