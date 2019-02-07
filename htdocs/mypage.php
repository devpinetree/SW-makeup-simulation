
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
      <div class="center_title_bar">회원정보</div>
      <HTML>
        <HEAD>
            <META http-equiv="content-type" content="text/html; cahrset-utf-8">
</HEAD>

<BODY>

          <font color="black">
          <table align="center">
          <th align="center">
               <h3>               </th>
</td></tr>
          
        </table>
  
 

<?php
 
 
 $tempid="select * from templogin";
 $run_gettempid = mysqli_query($con,$tempid);
 $idrow = mysqli_fetch_row($run_gettempid); 
 $gettempid=$idrow[0];


 $getemail = "select comment from joininfo where id='$gettempid'";
 $run_getimg = mysqli_query($con,$getemail);
 $row = mysqli_fetch_row($run_getimg); 
 $email=$row[0]; 

 $memberinfo = "select * from joininfo where id='$gettempid'";
 $run_memberinfo = mysqli_query($con,$memberinfo);
 $memberinforow = mysqli_fetch_row($run_memberinfo); 
 $name=$memberinforow[0]; 
 $id=$memberinforow[1];
 $birthYear=$memberinforow[3];
 $city=$memberinforow[4];
 $receiver=$memberinforow[5];
 $telnum=$memberinforow[6];
 $addr=$memberinforow[8];
 $comment=$memberinforow[9];
 $sender=$memberinforow[10];
 $member_img = mysqli_query($con,$memberinfo);

echo "<br><h3>&nbsp&nbsp&nbsp&nbsp이름: $name<br></h2>";
echo "<h3>&nbsp&nbsp&nbsp&nbsp아이디: $id<br></h2>";
echo "<h3>&nbsp&nbsp&nbsp&nbsp생일: $birthYear<br></h2>";
echo "<h3>&nbsp&nbsp&nbsp&nbsp도시명: $city<br></h2>";
echo "<h3>&nbsp&nbsp&nbsp&nbsp수신자: $receiver<br></h2>";
echo "<h3>&nbsp&nbsp&nbsp&nbsp전화번호: $telnum<br></h2>";
echo "<h3>&nbsp&nbsp&nbsp&nbsp주소: $addr<br></h2>";
echo "<h3>&nbsp&nbsp&nbsp&nbsp이메일: $comment<br></h2>";
echo "<h3>&nbsp&nbsp&nbsp&nbsp송신자: $sender<br><br><br></h2>";


 $emailimg=$email."_1.jpg";


?>
  
<div class="center_title_bar"><font color="white">시뮬레이션 이미지</font><br><br>



  <?php 
$i=1;

for($i=1;$i<100;$i++)
{
$emailimg=$email."_".$i.".jpg";

$imgaddress="email/".$emailimg;

$FileExist=file_exists($imgaddress);
if($FileExist)
{
	echo "<img src = 'email/$emailimg' height=300 width=400>"; 
}
	
}
?>
</div>
      <br><br><br><br><br><br><br><br><br><br><br><br><br> <br><br><br><br><br> <br><br><br><br><br><br><br><br><br><br><br><br><br> <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br> <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br> <br><br><br><br><br><br><br><br><br><br>  <br><br><br><br><br><br><br><br><br><br><br><br><br> <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
</BODY>
</HTML>



        <!-- end of right content -->
</div>

<div class="right_content">
      <div class="shopping_cart">
        <div class="cart_title"><font color="white">Shopping cart</font></div>
        <div class="cart_details"><font color="skyblue"><?php total_items(); ?></font>&nbsp;<font color="white">item(s)</font> <br />
          <span class="border_cart"></span> <font color="white">Total: <span class="price"><font color="white"><?php total_price(); ?> </span> </div>
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

          ?></font>&nbsp;!! <br />
          <span class="border_cart"></span> <font color="white"> Enjoy Your Shopping </div>
        <div class="cart_icon"><a href="mypage.php" title="header=[Checkout] body=[&nbsp;] fade=[on]"><img src="images/mypage.png" alt="" width="48" height="48" border="0" /></a></div>
      </div>


</div>
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
