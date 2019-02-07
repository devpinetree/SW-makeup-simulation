
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
  <br><br>
    

    <?php
    
    if(isset($_GET['cat'])){
    
    $get_id = $_GET['cat'];
    
    $query = "select cat_title from categories where cat_id='$get_id'";
    $run_query = mysqli_query($con,$query);
    
    $row = mysqli_fetch_array($run_query);
    
    $cat = $row['cat_title'];
    
    echo"<span class=current>>$cat</span>";
    
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
      <div class="center_title_bar">Latest Products</div>
  
 <form action="" enctype="multipart/form-data" method="post">
 
 <table align="center" width="500" border="0">
 

<tr align="center" >


  <th><font color="black">Remove</font></th>
  <th><font color="black">Product(s)</font></th>
  <th><font color="black">Quantity</font></th>
  <th><font color="black">Total Price</font></th>
</tr>


 <?php
 
         $total = 0;
   global $con;

   $ip = getip();

   $price = "select * from cart where ip_add = '$ip'";

   $run_price = mysqli_query($con,$price) ;

   while($pprice = mysqli_fetch_array($run_price)){

      $pro_id = $pprice['p_id'];
      
      $prod_price = "select * from products where prd_id = '$pro_id'";

      $run_pro_price = mysqli_query($con,$prod_price);


      while($ppprice = mysqli_fetch_array($run_pro_price)){

         $product_price = array($ppprice['prd_price']);
         $product_title = $ppprice['prd_title'];
         $product_image = $ppprice['prd_img'];
         $single_price = $ppprice['prd_price'];
         

         $price_sum = array_sum($product_price);

         $total +=$price_sum;

         //echo  $product_price;

 ?>
 
 <tr align="center">
   
   <td><input type="checkbox" name="remove[]" value="<?php echo $pro_id;  ?>"></td>
   <td><?php echo $product_title; ?>
    <br>
    <img src="admin_area/product_images/<?php echo $product_image; ?>" width="60" height="60"></td>
   <td>
   
   <input type="text" size="4" name="qty" value=1>
   </td>
   <td><font color="black">
   <?php echo $single_price." won";  ?></font>
   </td>
  
   <td></td>  
   
 
 </tr>
 
 
 <?php
 
 }
   }
 ?>
 
  <tr align="right">
   <td colspan="4"><b><font color="black">Sub total:</font></b></td>
   <td><font color="black"><?php echo $total." won&nbsp;";   ?></font></td>
   
   </tr>
   <tr><br><br><br><br></tr>
   <tr><br></tr>
   <tr><br></tr>
   
   <tr align="center">
   
   <td colspan="2"><input type="submit" name="update_cart" value="Update cart"></td>
   

   <td><button><a href="logindex.php" style="text-decoration:none;color:black">Continue Shopping</a></button>

   <td><button><a href="logorder.php" style="text-decoration:none;color:black">order</a></button>
   </td>

   

  <!-- <td><button><a href="checkout.php" style="text-decoration:none;color:black">Checkout</a></button></td> -->
     <!-- <td><button><a href="order.php" style="text-decoration:none;color:black">Checkout</a></button></td> -->

   </tr>

 </table>
 
 
 
 </form>
 
 <?php
 
 $ip = getip();
 

 
 if(isset($_POST['update_cart'])){
 
   foreach($_POST['remove'] as $remove){
   
       $delete_product = "delete from cart where p_id='$remove' AND ip_add='$ip'";
       $run_delete = mysqli_query($con, $delete_product);
       echo $ip;
       if($run_delete){
       
         echo "<script>window.open('cart.php','_self')</script>"    ;  
       
       }
   
   }
 
 }


 
 ?>
 
 
 </div>
    <!-- end of center content -->
<div class="right_content">
      <div class="shopping_cart">
        <div class="cart_title"><font color="white">Shopping cart</font></div>
        <div class="cart_details"><font color="skyblue"><?php total_items(); ?></font>&nbsp;items <br />
          <span class="border_cart"></span> Total: <span class="price"><?php total_price(); ?> </span> </div>
        <div class="cart_icon"><a href="logcart.php" title="header=[Checkout] body=[&nbsp;] fade=[on]"><img src="images/shoppingcart.png" alt="" width="48" height="48" border="0" /></a></div>
      </div>
      
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

          ?></font>&nbsp;!!<br />
          <span class="border_cart"></span> Enjoy Your Shopping </div>
        <div class="cart_icon"><a href="mypage.php" title="header=[Checkout] body=[&nbsp;] fade=[on]"><img src="images/mypage.png" alt="" width="48" height="48" border="0" /></a></div>
      </div>


</div>
 
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>       
       <br>
 
        <!-- end of right content -->
</div>
  <!-- end of main content -->
  <div class="footer">
    <div class="left_footer"> <img src="images/footer_logo.png" alt="" width="170" height="49"/> </div>
    <div class="center_footer">. All Rights Reserved 2018<br />
      
  
  </div>
</div>
<!-- end of main_container -->
</body>
</html>
