
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
      <div class="center_title_bar">회원가입</div>
  
 
 <table align="center" width="500" border="0">

<tr align="center" >


 <HTML>
        <HEAD>
            <META http-equiv="content-type" content="text/html; cahrset-utf-8">
</HEAD>

<BODY>

<form method="post" action="joinsuccess.php" enctype="multipart/form-data">


          <font color="black"><br>
          <table align="center" width="500" border="0">
          <th><h2><font color="black">join Information</th><th align="left"></th>
            <tr align="center">
              <td><font color="black"> 이름:</td>
              <td align="left"><INPUT TYPE="text" NAME="name"></td>
            </tr>

            <tr align="center">
              <td><font color="black"> 아이디:</td>
              <td align="left"><INPUT TYPE="text" NAME="id"></td>
            </tr>

             <tr align="center">
              <td><font color="black"> 비밀번호:</td>
              <td align="left"><INPUT TYPE="text" NAME="password"></td>
            </tr>

            <tr align="center">
              <td><font color="black">출생년도:</td>
              <td align="left"><INPUT TYPE="text" NAME="birthYear" placeholder="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;YYYY-MM-DD"></td>
            </tr>

            <tr align="center">
              <td><font color="black">지역:</td>
              <td align="left"><INPUT TYPE="text" NAME="city" placeholder="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ex) Seoul"></td>
            </tr>

            <tr align="center">
              <td><font color="black">수취인:</td>
              <td align="left"><INPUT TYPE="text" NAME="receiver"></td>
            </tr>

            <tr align="center">
              <td><br><br><br></td><td><br><br><br></td>
            </tr>

            <tr align="center">
              <td><H2><font color="black">Shipping Information</td><td></td>
            </tr>

            <tr align="center">
              <td><font color="black">수취인 전화번호:</td>
              <td align="left"><INPUT TYPE="text" NAME="telnum"></td>
            </tr>
            <tr align="center">
              <td><font color="black">수취인 핸드폰번호:</td>
              <td align="left"><INPUT TYPE="text" NAME="phonenum"></td>
            </tr>
            <tr align="center">
              <td><font color="black">배송지:</td>
              <td align="left"><INPUT TYPE="text" NAME="addr"placeholder="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ex) Seoul"></td>
            </tr>
            <tr align="center">
              <td><font color="black">이메일:</td>
              <td align="left"><INPUT TYPE="text" NAME="comment" placeholder="&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ID@Email.com"></td>
            </tr>
            <tr align="center">
              <td><font color="black">무통장 입금자명:</td>
              <td align="left"><INPUT TYPE="text" NAME="sender"></td>
            </tr>

        
           <BR><BR><br><tr><td><br><br></td><td><br><br></td></tr>
           <tr align="center">
            <td></td>
            <td><input type="submit" value="join" class="search_bt" name="join"/></td> 
          </tr>
        </font> <br>
        </table>
        </form>
        <form method="get" action="results.php" enctype="multipart/form-data">
  
  

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
