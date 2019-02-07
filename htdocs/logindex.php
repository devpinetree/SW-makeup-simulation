
<?php

include("functions/logfunctions.php");
include("includes/db.php");

cart();
?>




<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<?php

include("logheader.php");

?>


    <!-- end of menu tab -->
<br>

    <?php
    if(isset($_GET['cat'])){
    $get_id = $_GET['cat'];
    $query = "select cat_title from categories where cat_id='$get_id'";
    $run_query = mysqli_query($con,$query);
  
    $row = mysqli_fetch_array($run_query);
    
    $cat = $row['cat_title'];
    
    echo"<span class=current>$cat</span>";
    
    }
    
    ?>


 </div>
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
      <div class="center_title_bar">Products</div>


<?php  

getpro();
get_pro_cat();
get_pro_brand();

 ?>



 <div class="center_none_bar"><br><br><br><br><br></div>
  
  


  </div>
  
 
  


 
    <!-- end of center content -->
<div class="right_content">
      <div class="shopping_cart">
        <div class="cart_title"><font color="white">Shopping cart</font></div>
        <div class="cart_details"><font color="skyblue"><?php total_items(); ?></font>&nbsp;item(s) <br />
          <span class="border_cart"></span> Total: <span class="price"><?php total_price(); ?> </span> </div>
        <div class="cart_icon"><a href="cart.php" title="header=[Checkout] body=[&nbsp;] fade=[on]"><img src="images/shoppingcart.png" alt="" width="48" height="48" border="0" /></a></div>
      </div>
      
       
       <br>
       <div class="right_content">
      <div class="shopping_cart">
        <div class="cart_title"><font color="white">Orderer Info</font></div>
        <div class="cart_details"><font color="skyblue">  
        <?php 
          global $con;
            $qry="select id from templogin";

            $resultid=mysqli_query($con,$qry);
            $row = mysqli_fetch_array($resultid);
            $id = $row['id'];
            echo $id;

            //$deleteqry="delete from templogin where id='$id'";
            //mysqli_query($con,$deleteqry);

          ?></font>&nbsp;!! <br />
          <span class="border_cart"></span>  Enjoy Your Shopping </div>
        <div class="cart_icon"><a href="mypage.php" title="header=[Checkout] body=[&nbsp;] fade=[on]"><img src="images/mypage.png" alt="" width="48" height="48" border="0" /></a></div>
      </div>


</div>

      
</div>
  <div class="footer">
    <div class="left_footer"> <img src="images/footer_logo.png" alt="" width="170" height="49"/> </div>
    <div class="center_footer"> All Rights Reserved 2018<br />
     </div>
</div>
</body>
</html>
