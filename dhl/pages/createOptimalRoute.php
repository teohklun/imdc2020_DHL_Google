<?php
include_once "../utility/packed_library.php";
?>

<?php include_once "template/header.php"; ?>
<body>

<?php 
// print_r($_POST);
if(!empty($_POST)){
    if(isset($_POST["form1"])) {
        // $date = $_POST["date"];
        // split("-", string);
        $originalDate = $_POST["date"];
        $_POST["date"] = str_replace("-", "", $_POST["date"]);
        $input = $_POST;
        print_r($input);

        $post = $_POST;
        // Request URL
        $json = curl_post($url . "/generateRoute", $post);
        print_r($json);

        if($json == "job is empty, it could be the session no job at all .") {
          $error = true;
          $message = $json;
        } else {
          $error = false;
          $message = $json;
        }

        // $chartData = [];
        // // $chartData["label"] =;
        // $total = count($json);
        // $i = 0;
        // foreach ($json as $label => $value) {
        //   $chartData["series"][] = $value;
        //   // }
        //   $chartData["label"][] = $label;
        // }
        // print_r($chartData["label"]);
    }
    
}

?>

    <div class="wrapper">
        <div class="sidebar" data-image="../assets/img/sidebar-5.jpg">
<?php include_once "template/sidebar.php"; ?>
        </div>

<div class="main-panel">
<?php include_once "template/nav.php"; ?>
  <div class="content">

      <div class="container" style="margin-bottom: 15px">
        <div class="card-header ">
            <p class="card-category" style="text-align-last: center";><span style="font-size: 20px">Create Optimal Route</span></p>
        </div>
      </div>

      <div class="container-fluid">
        <form class="form-horizontal" action="createOptimalRoute.php" method="post" id="form1" name="form1">
          <div class="row">
            <div class="col-md-12">
                  <div class="container">
                    <!-- <label for="text-info"><span class="text-warning">Select either one type date range</span></label> -->
                    <div id="date-range-div" class="col-md-12 col-sm-12 col-xs-12 align-self-center">
                      <label for="Date"><span class="text-info">Date</span></label>
                      <input type="date" id="date" name="date" value=<?= isset($originalDate) ?  $originalDate : date('Y-m-d')  ?> required>
                    </div>
                  </div>
                  <div class="row" style = "margin-left: 15px">
                      <label for="session"><span class="text-info">Session</span></label>
                      <div class="radio icheck-peterriver">
                          <input <?= isset($_POST["form1"]) ? $_POST["session"] == "m" ? "checked" : ""  : "checked" ?>  type="radio" value="m" id="session2" name="session">
                          <label for="session2">Morning</label>
                      </div>
                      <div class="radio icheck-peterriver">
                          <input <?= isset($_POST["form1"]) ? $_POST["session"] == "a" ? "checked" : ""  : "" ?>  type="radio" value="a" id="session3" name="session">
                          <label for="session3">Afternoon</label>
                      </div>
                  </div>
                  <div class="container">
                    <span class=<?= isset($error) ? $error == true ? "text-danger" :  "text-success" : ""?>><?= isset($message) ? $message : ""?></span>
                  </div>
                <div class="col-md-12 col-sm-12 col-xs-12 align-self-center">
                  <input class="btn btn-primary" type="submit" name="form1" value="Submit" style="margin-bottom: 20px" >
                </div>
            </div>
        </form>

      </div>
  </div>
</div>

</div>

<?php include_once "template/footer.php"; ?>
</div>

        </body>

</html>