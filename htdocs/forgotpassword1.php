<?php



if(!isset($_POST["answer"]))
{
	header("location:index.php");
}

else
{

$con = mysqli_connect("localhost","root","1234","cosmetic");
 if(mysqli_connect_errno()){
  
  echo"Failed to connect : " . mysqli_connect_error(); 
  
}

$answ = $_POST["answer"];

$get_answer = "select id from joininfo where id='$answ'";
$get_pass = "select password from joininfo where id='$answ'";

$run = mysqli_query($con,$get_answer);
$runp = mysqli_query($con,$get_pass);

$e = mysqli_fetch_row($run);
$p= mysqli_fetch_row($runp);
$ans = $e[0];
$pass = $p[0];

if($answ==$ans)
{
	echo"<script>alert('비밀번호는 $pass 입니다.')</script>";
	echo"<script>window.open('index.php','_self')</script>";


}

else 
{
	echo"<script>alert('Invalid Answer.Please Try Again')</script>";
	echo"<script>window.open('forgotpassword.php','_self')</script>";
}

}
?>