
<?php

include("functions/functions.php");
include("includes/db.php");

cart();
?>

<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<?php

include("header.php");

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
      <div class="center_title_bar">Orderer Information</div>
      <HTML>
        <HEAD>
            <META http-equiv="content-type" content="text/html; cahrset-utf-8">
</HEAD>

<BODY>

          <font color="black"><br><br><br><br><br>
          <table align="center">
          <th align="center">
               <h3>                 주문 정보가 모두 일치합니까?<br><br><br></th>
               <tr><td align="center"><button><a href="ordersuccess.php" style="text-decoration:none;color:black">네</a></button><td align="center"><button><a href="order.php" style="text-decoration:none;color:black">아니오</a></button>
</td></tr>
          
        </table>
        <div class="center_content">
      <div class="center_thin_bar"><font color="white"></div>
  
 <form action="" enctype="multipart/form-data" method="post">
 
 <table align="center" width="500" border="0">

<tr align="center" >

<th> </th>
  <th><h2><font color="black">주문상품 확인</font></th>
  <th></th>
</tr>

<tr align="center" >

<td> </td>
  <td><font color="black">Product(s)</font></td>
  <td><font color="black">Quantity</font></td>
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
   <td> </td>
   <td><?php echo $product_title; ?>
    <br>
    <img src="admin_area/product_images/<?php echo $product_image; ?>" width="60" height="60"></td>
   <td>
   
   <input type="text" size="4" name="qty" value=1>
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
 
        <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
</BODY>
</HTML>


      </div>
<!-- end of center content -->

       
       <br>    <br> <br>   <br>     <br><br><br><br><br><br><br><br><br><br><br><br><br>

            
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
