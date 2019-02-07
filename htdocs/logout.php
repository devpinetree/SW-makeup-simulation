


<?php 
include("includes/db.php");
        
            global $con;
            $a=0;
            $qry="select id from templogin";

            $resultid=mysqli_query($con,$qry);
            $row = mysqli_fetch_array($resultid);
            $id = $row['id'];

            $deleteqry="delete from templogin where id='$id'";
            mysqli_query($con,$deleteqry);

            if($a==0)
            {
            header("Location:index.php"); 
            }
            exit();

?>