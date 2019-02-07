
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
      
<?php 
$name=$_POST['name'];
$id=$_POST['id'];
$password=$_POST['password'];

$birthYear=$_POST['birthYear'];
$city=$_POST['city'];
$receiver=$_POST['receiver'];
$telnum=$_POST['telnum'];
$phonenum=$_POST['phonenum'];
$addr=$_POST['addr'];
$comment=$_POST['comment'];
$sender=$_POST['sender'];

global $con;
$sql="INSERT INTO joininfo VALUES('".$name."','".$id."','".$password."','".$birthYear."','".$city."','".$receiver."','".$telnum."','".$phonenum."','".$addr."','".$comment."','".$sender."')"; 
$run_join=mysqli_query($con,$sql);
if($run_join){
}else{
    echo "데이터 입력 실패".mysqli_error($con);
}



 ?>
      <HTML>
        <HEAD>
            <META http-equiv="content-type" content="text/html; cahrset-utf-8">
</HEAD>

<BODY>

    <FORM METHOD="post" ACTION="update_result.php">
          <font color="black"><br><br><br><br><br>
          <table align="center">
          <th align="center">
               <h2> <?PHP echo $name; ?>님의 회원가입이 성공적으로 마무리되었습니다. :)</th>

        </table>
<BODY>
<HTML>
      </div>
<!-- end of center content -->
<div class="right_content">
      <div class="shopping_cart">
        <div class="cart_title"><font color="white">Shopping cart</font></div>
        <div class="cart_details"><font color="skyblue"><?php total_items(); ?></font><font color="white">&nbsp;items </fomt><br>
          <span class="border_cart"></span> Total: <span class="price"><?php total_price(); ?> </span> </div>
        <div class="cart_icon"><a href="cart.php" title="header=[Checkout] body=[&nbsp;] fade=[on]"><img src="images/shoppingcart.png" alt="" width="48" height="48" border="0" /></a></div>
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
