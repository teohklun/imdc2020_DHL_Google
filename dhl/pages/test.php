<?php
include_once "../utility/packed_library.php";
?>

<?php include_once "template/header.php"; ?>
<body>

<?php 
// print_r($_POST);
if(!empty($_POST)){
    if(isset($_POST["form1"])) {
        $input = $_POST;
        // print_r($input["date-range"]);

        $dates = explode(" - ", $input["date-range"]);
        $startDate = $dates[0];
        $endDate = $dates[1];

        $post = $_POST;
        // Request URL

        $json = curl_post($url . "/job", $post);

        $chartData = [];
        // $chartData["label"] =;
        $total = count($json);
        $i = 0;
        foreach ($json as $label => $value) {
          $chartData["series"][] = $value;
          // }
          $chartData["label"][] = $label;
        }
        print_r($chartData["label"]);
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

<script src="<?= ASSET_JS_CORE ?>/popper.min.js" type="text/javascript"></script>

<script src="<?= ASSET_JS_PLUGIN ?>/bootstrap-switch.js"></script>
<script src="<?= ASSET_JS ?>/demo.js"></script>

<script type="text/javascript">
    $(document).ready(function() {
        // Javascript method's body can be found in assets/js/demos.js
        demo.initDashboardPageCharts();
        // demo.showNotification();
    });
</script>
<script type="text/javascript" src="<?= ASSET_JS_PLUGIN ?>/daterangepicker.js"></script>
<script type="text/javascript" src="<?= ASSET_JS_CUSTOM ?>/daterange.js"></script>
<script type="text/javascript" src="<?= ASSET_JS_PLUGIN ?>/multidate.picker.js"></script>
<script type="text/javascript" src="<?= ASSET_JS_CUSTOM ?>/multi-date.js"></script>
<script src="<?= ASSET_JS_PLUGIN ?>/chartist.min.js"></script>
<script src="<?= ASSET_JS_PLUGIN ?>/chartist-plugin-1.js"></script>
<script type="text/javascript" src="<?= ASSET_JS_CUSTOM ?>/seriesGraph.js"></script>

<script>

  var startDate =  '<?= isset($input['date-range']) ? $startDate : date('Y-m-d') ?>';
  var endDate = '<?= isset($input['date-range']) ? $endDate : date('Y-m-d') ?>';
  createDateRangePickeR("#range-date", startDate, endDate);

  var chartLabel = <?= isset($chartData) ? isset($chartData["label"]) ? json_encode($chartData["label"]) : json_encode(["b", "c", "d"]) : json_encode(["a", "b", "c"]) ?>;
  var chartSeries = <?= isset($chartData) ? isset($chartData["series"]) ? json_encode($chartData["series"]) : json_encode([1, 5, 8]) : json_encode([1, 5, 7]) ?> ;
  drawSeriesGraph("#chart-line-1", chartLabel, chartSeries);

  var multi = "<?= !empty($_POST) ? isset($input['date-multi']) ? "0" : "1" : "1" ?>" == false;
  var str = "<?= isset($input['date-multi']) ? $input['date-multi'] : "1" ?>" ;
  createMultiDateSelection("#date-m", multi, str);

  $("#date-range-type-1").click(function() {
      $("#multi-date-div").attr("hidden", true);
      $("#date-range-div").removeAttr("hidden");

    });
  $("#date-range-type-2").click(function() {
      $("#multi-date-div").removeAttr("hidden");
      $("#date-range-div").attr("hidden", true);

    });

</script>
</html>