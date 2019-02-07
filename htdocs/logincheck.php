
<?php

include("functions/functions.php");


if(!isset($_POST["text1"]))
{
	header("location:logindex.php");
}

else
{

 $con = mysqli_connect("localhost","root","1234","cosmetic");

 if(mysqli_connect_errno()){
  
  echo"Failed to connect : " . mysqli_connect_error(); 
  
}

$uid=$_POST["text1"];
$pwd=$_POST["password1"];

global $con;
$sql="INSERT INTO templogin VALUES('".$uid."')"; 
$run_loginid=mysqli_query($con,$sql);
if($run_loginid){
}else{
    echo "데이터 입력 실패".mysqli_error($con);
}


echo $uid;
echo $pwd;

$qry="select * from joininfo where id='$uid' and password='$pwd'";

$result=mysqli_query($con,$qry);

$n=mysqli_num_rows($result);


if($n>0)
{
    header("location:logindex.php?tn=$uid");
    
}

else
{
	echo "<script>alert('ID or Password is incorrect!')</script>";
	 echo "<script>window.open('loginerror.php','_self')</script>";
}

}
?>