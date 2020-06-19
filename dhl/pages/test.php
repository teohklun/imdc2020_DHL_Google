<?php
include_once "../utility/packed_library.php";
?>

<?php include_once "template/header.php"; ?>
<body>

<?php 

$driver = curl_post($url . "/getDriverList");

// print_r($_POST);
if(!empty($_POST)){
    if(isset($_POST["form1"])) {
        $input = $_POST;
        print_r($_POST);

        $dates = explode(" - ", $input["date-range"]);
        $startDate = $dates[0];
        $endDate = $dates[1];

        $post = $_POST;
        // Request URL

        $json = curl_post($url . "/job", $post);

        $chartData = [];
        // $chartData["label"] =;
        if($json) {
          $total = count($json);
          $i = 0;
          if(is_array($json) && !empty($json) ) {
            print("DASdasadsdas");

            foreach ($json as $label => $value) {
              $chartData["series"][] = $value;
              // }
              $chartData["label"][] = $label;
            }

            if(!isset($chartData["series"][0])){
              unset($chartData);
            }

            // print_r($chartData["label"]);
            print_r($json);
            print_r("here");

          } else {
              $error = true;
              $message = "data not receive";
          }
        }
    }
    
}

?>

    <div class="wrapper">
        <div class="sidebar" data-image="../assets/img/sidebar-5.jpg">
<?php include_once "template/sidebar.php"; ?>
        </div>


<?php include_once "_sub_test.php"; ?>

</div>

<?php include_once "template/footer.php"; ?>
</div>

        </body>

<!--   Core JS Files   -->


</html>