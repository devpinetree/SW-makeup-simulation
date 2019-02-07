
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
      <div class="center_title_bar">Your Products</div>
  
 <form action="" enctype="multipart/form-data" method="post">
 
 <table align="center" width="500" border="0">

<tr align="center" >

<th></th>
  <th><h2><font color="black">주문상품 확인</font></th>
  <th></th>
  <th></th>
</tr>

<tr align="center" >

<td></td>
  <td><font color="black">Product(s)</font></td>
  <td><font color="black">Quantity</font></td>
  <td><font color="black">Total Price</font></td>
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
   <td></td>
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
   <td colspan="5"><b><font color="black"><h2>주문 금액:</font></b></td>
   <td><font color="black"><h3><?php echo $total." won&nbsp;";   ?></font></td>
   
   </tr>
   <tr><br><br><br><br></tr>
   <tr><br></tr>
   <tr><br></tr>
   


 </table>
 <HTML>
        <HEAD>
            <META http-equiv="content-type" content="text/html; cahrset-utf-8">
</HEAD>

<BODY>



          <font color="black"><br>
          <table align="center" width="500" border="0">
          <th><h2>Orderer Information</th><th align="left"></th>
            <tr align="center">
              <td> 주문자명:</td>
              <td align="left"><INPUT TYPE="text" NAME="name"></td>
            </tr>
            <tr align="center">
              <td>출생년도:</td>
              <td align="left"><INPUT TYPE="text" NAME="birthYear"></td>
            </tr>

            <tr align="center">
              <td>지역:</td>
              <td align="left"><INPUT TYPE="text" NAME="city"></td>
            </tr>

            <tr align="center">
              <td>수취인:</td>
              <td align="left"><INPUT TYPE="text" NAME="receiver"></td>
            </tr>

            <tr align="center">
              <td><br><br><br></td><td><br><br><br></td>
            </tr>

            <tr align="center">
              <td><H2>Shipping Information</td><td></td>
            </tr>

            <tr align="center">
              <td>수취인 전화번호:</td>
              <td align="left"><INPUT TYPE="text" NAME="telnum"></td>
            </tr>
            <tr align="center">
              <td>수취인 핸드폰번호:</td>
              <td align="left"><INPUT TYPE="text" NAME="phonenum"></td>
            </tr>
            <tr align="center">
              <td>배송지:</td>
              <td align="left"><INPUT TYPE="text" NAME="addr"></td>
            </tr>
            <tr align="center">
              <td>배송시 요청사항:</td>
              <td align="left"><INPUT TYPE="text" NAME="comment"></td>
            </tr>
            <tr align="center">
              <td>무통장 입금자명:</td>
              <td align="left"><INPUT TYPE="text" NAME="sender"></td>
            </tr>

        
           <BR><BR><br><tr><td><br><br></td><td><br><br></td></tr>
           <tr align="center">
            <td></td>
            <td> <button><a href="logordersuccess.php" style="text-decoration:none;color:black">order</a></button></td> 
          </tr>
        </font> <br>
        </table>
        </form>

        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
</BODY>
</HTML>

 
 
 <?php
 
 $ip = getip();
 




 
 ?>
 
 </div>

<!-- end of center content -->
<div class="right_content">
      <div class="shopping_cart">
        <div class="cart_title"><font color="white">Shopping cart</font></div>
        <div class="cart_details"><font color="skyblue"><?php total_items(); ?></font>&nbsp;<font color="white">items<br>
          <span class="border_cart"></span> Total:</font>  <span class="price"><?php total_price(); ?> </span> </div>
        <div class="cart_icon"><a href="logcart.php" title="header=[Checkout] body=[&nbsp;] fade=[on]"><img src="images/shoppingcart.png" alt="" width="48" height="48" border="0" /></a></div>
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

          ?></font>&nbsp;!!<br />
          <span class="border_cart"></span>  Enjoy Your Shopping</div>
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
