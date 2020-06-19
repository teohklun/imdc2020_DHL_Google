<div class="main-panel">
<?php include_once "template/nav.php"; ?>
	<div class="content">

			<div class="container" style="margin-bottom: 15px">
	      <div class="card-header ">
	          <p class="card-category" style="text-align-last: center";><span style="font-size: 20px">Line Chart Generator</span></p>
	      </div>
			</div>

	    <div class="container-fluid">
	    	<form class="form-horizontal" action="test.php" method="post" id="form1" name="form1">
		    	<div class="row">
		        <div class="col-md-12">
		         <div class="card ">
									<div class="col-md-12 col-sm-12 col-xs-12 align-self-center">
								    <label for="text-info"><span class="text-info">select one date range type</span></label>

										<div class="row" style="margin-left: 15px; margin-right: 15px;" >
											<div class="col-md-6 col-sm-6 col-xs-6">
					              <div class="radio icheck-peterriver">
					                  <input <?= isset($_POST["form1"]) ? $_POST["date-range-type"] == "range" ? "checked" : ""  : "checked" ?> value="range" type="radio" id="date-range-type-1" name="date-range-type">
					                  <label for="date-range-type-1">Date A - Date B</label>
					              </div>
					            </div>
											<div class="col-md-6 col-sm-6 col-xs-6">
					              <div class="radio icheck-peterriver">
					                  <input <?= isset($_POST["form1"]) ? $_POST["date-range-type"] == "multi" ? "checked" : ""  : "" ?> type="radio" value="multi" id="date-range-type-2" name="date-range-type">
					                  <label for="date-range-type-2">Multi Single Date</label>
					              </div>
					            </div>
				          	</div>
				       	</div>
							      <!-- <label for="text-info"><span class="text-warning">Select either one type date range</span></label> -->
										<div id="date-range-div" class="col-md-12 col-sm-12 col-xs-12 align-self-center" <?= isset($_POST["form1"]) ? $_POST["date-range-type"] == "multi" ? "hidden" : ""  : "" ?> >
							      	<label for="Date"><span class="text-info">Date</span></label>
											<input id="range-date" class="form-control date" type="text" name="date-range" id="timepicker1"  value="<?= isset($input['Date']) ? $input['Date'] : '' ?>">
										</div>
										<div id="multi-date-div" class="col-md-12 col-sm-12 col-xs-12 align-self-center" <?= isset($_POST["form1"]) ? $_POST["date-range-type"] == "range" ? "hidden" : ""  : "hidden" ?> >
											<label for="date-m"><span class="text-info">Multi Select Date</span></label>
											<input type="text" id="date-m" class="form-control" name="date-multi" placeholder="Pick the multiple dates">
										</div>

									<div class="row" style="margin-left: 15px; margin-right: 15px;" >
										<div class="col-md-4 col-sm-4 col-xs-4">
											<label for="session"><span class="text-info">Session</span></label>
				              <div class="radio icheck-peterriver">
				                  <input type="radio" value="" <?= isset($_POST["form1"]) ? $_POST["session"] == "" ? "checked" : ""  : "checked" ?> id="session1" name="session">
				                  <label for="session1">No select</label>
				              </div>
				              <div class="radio icheck-peterriver">
				                  <input <?= isset($_POST["form1"]) ? $_POST["session"] == "m" ? "checked" : ""  : "" ?>  type="radio" value="m" id="session2" name="session">
				                  <label for="session2">Morning</label>
				              </div>
				              <div class="radio icheck-peterriver">
				                  <input <?= isset($_POST["form1"]) ? $_POST["session"] == "a" ? "checked" : ""  : "" ?>  type="radio" value="a" id="session3" name="session">
				                  <label for="session3">Afternoon</label>
				              </div>
				            </div>
					            <div class="col-md-4 col-sm-4 col-xs-4">
												<label for="Radio"><span class="text-info">Action Base</span></label>
					              <div class="radio icheck-peterriver">
					                  <input type="radio" value="" <?= isset($_POST["form1"]) ? $_POST["action"] == "" ? "checked" : ""  : "checked" ?> id="action1" name="action">
					                  <label for="action1">No select</label>
					              </div>
					              <div class="radio icheck-peterriver">
					                  <input <?= isset($_POST["form1"]) ? $_POST["action"] == "P" ? "checked" : ""  : "" ?> type="radio" value="P" id="action2" name="action">
					                  <label for="action2">Pick Up</label>
					              </div>
					              <div class="radio icheck-peterriver">
					                  <input <?= isset($_POST["form1"]) ? $_POST["action"] == "D" ? "checked" : ""  : "" ?> type="radio" value="D" id="action3" name="action">
					                  <label for="action3">Delivery</label>
					              </div>
					            </div>
				            <div class="col-md-4 col-sm-4 col-xs-4">
											<label for="Radio"><span class="text-info">Series Style</span></label>
				              <div class="radio icheck-peterriver">
				                  <input <?= isset($_POST["form1"]) ? $_POST["mode"] == "weekday" ? "checked" : ""  : "checked" ?> type="radio" value="weekday" id="mode2" name="mode">
				                  <label for="mode2">Week Day Mode</label>
				              </div>
				              <div class="radio icheck-peterriver">
				                  <input <?= isset($_POST["form1"]) ? $_POST["mode"] == "month" ? "checked" : ""  : "" ?> type="radio" value="month" id="mode3" name="mode">
				                  <label for="mode3">Monthly mode</label>
				              </div>
				         			<div class="radio icheck-peterriver">
				                  <input <?= isset($_POST["form1"]) ? $_POST["mode"] == "day" ? "checked" : ""  : "" ?> type="radio" value="day" id="mode4" name="mode">
				                  <label for="mode4">Day mode</label>
				              </div>
				            </div>
				            </div>
										<label for="Radio" style="display: block;text-align: center;"><span class="text-info">Time filter</span></label>
			          		<div class="row" style="margin-left: 15px; margin-right: 15px;">
											<div class="col-xl-4 col-md-4 mb-4">
					              <div class="radio icheck-peterriver">
				                  <input <?= isset($_POST["form1"]) ? $_POST["t-mode"] == "before" ? "checked" : ""  : "checked" ?> type="radio" value="before" id="t-mode-1" name="t-mode">
				                  <label for="t-mode-1">Before</label>
					              </div>
					            </div>
											<div class="col-xl-4 col-md-4 mb-4">
					              <div class="radio icheck-peterriver">
				                  <input <?= isset($_POST["form1"]) ? $_POST["t-mode"] == "after" ? "checked" : ""  : "" ?> type="radio" value="after" id="t-mode-2" name="t-mode">
				                  <label for="t-mode-2">After</label>
					              </div>
					            </div>
											<div class="col-xl-4 col-md-4 mb-4">
					         			<div class="radio icheck-peterriver">
				                  <input <?= isset($_POST["form1"]) ? $_POST["t-mode"] == "between" ? "checked" : ""  : "" ?> type="radio" value="between" id="t-mode-3" name="t-mode">
				                  <label for="t-mode-3">Between</label>
					              </div>
					            </div>
				            </div>
				          	<div class="row" style="margin-left: 15px; margin-right: 15px;" >
											<div class="<?= isset($_POST["t-mode"]) ? $_POST["t-mode"] == "between" ? "col-md-5 mb-5" : "col-md-10 mb-10" : "col-xl-10 col-md-10 mb-10" ?>" id="div-time-1">
											 <label for="time"><span class="text-info" id="time-1-text">Time</span></label>
								        <input class="form-control timepicker" type="text" name="StartTime" id="timepicker1"  value="<?= isset($_POST["StartTime"])? $_POST["StartTime"] : ""?>">
								      </div>
								      <div class="col-xl-5 col-md-5 mb-5" id="div-time-2" <?= isset($_POST["t-mode"]) ? $_POST["t-mode"] == "between" ? "" : "hidden" : "hidden" ?> >
											 <label for="time"><span class="text-info">End Time</span></label>
								        <input class="form-control timepicker" type="text" name="EndTime" id="timepicker2"  value="<?= isset($_POST["EndTime"])? $_POST["EndTime"] : ""?>">
								      </div>
								      <div class="col-xl-2 col-md-2 mb-2" style="text-align: center;">
											 <label for="button clear" style="visibility:hidden;display: block;"><span class="text-info">hide</span></label>
			            			<input class="btn btn-primary" type="button" name="form1" id="clear-t" value="Reset Time" style="margin-bottom: 20px" >
								      </div>
								  </div>
				          	<div class="row" style="margin-left: 15px; margin-right: 15px;">
								      <div class="col-md-12 mb-12">
											 <label for="driver" style="display: block;"><span class="text-info">Driver Name</span></label>
											  <select class="select2 form-control" name="names[]"  multiple="multiple">
									        <?php foreach($driver as $key => $value): ?>
									          <<?= "option value = ". $value . (isset($_POST["names"]) ? in_array($value, $_POST["names"]) ? " selected" : "" : "")?>> <?= $value ?> </option>
									        <?php endforeach; ?> 
												</select>
								      </div>
								    </div>
								<div class="col-md-12 col-sm-12 col-xs-12" style="text-align: center;">
			            <input class="btn btn-primary" type="submit" name="form1" value="Submit" style="margin-bottom: 20px;margin-top: 20px" >
								</div>
						</div>
	    	</form>

          <div class="card-header " style="text-align-last: center";>
              <h4 class="card-title">Job(s) in <?= isset($input) ? $input["mode"] == "weekday" ? "Weekday" : "Days in time interval" : "Example"?> </h4>
          </div>
          <div class="card-body ">
            <div id="chart-line-1" class="ct-chart ct-golden-section"></div>
            <div class="legend">
                <i class="fa fa-circle text-info"></i> 
                <?= isset($input) ? $input["mode"] == "weekday" ? $input["mode"] == "month" ? "Month" : "Weekday" : "Days in time interval" : "Example"?>
              </br>
                <span class="text-danger"><?= isset($error) ? $message : "" ?></span>
            </div>
            <hr>
            <div class="stats">

                <!-- <i class="fa fa-clock-o"></i> Campaign sent 2 days ago -->
            </div>
	        </div>

	    </div>
	</div>
</div>
<script src="<?= ASSET_JS_PLUGIN ?>/bootstrap-switch.js"></script>
<script src="<?= ASSET_JS ?>/demo.js"></script>

<script type="text/javascript">
    $(document).ready(function() {
        // Javascript method's body can be found in assets/js/demos.js
        demo.initDashboardPageCharts();
        // demo.showNotification();
    });
</script>
<script type="text/javascript" src="<?= ASSET_JS_PLUGIN ?>/select2.js"></script>
<link href="<?= ASSET_CSS ?>/select2.css" rel="stylesheet">
<script type="text/javascript" src="<?= ASSET_JS_PLUGIN ?>/daterangepicker.js"></script>
<script type="text/javascript" src="<?= ASSET_JS_CUSTOM ?>/daterange.js"></script>
<script type="text/javascript" src="<?= ASSET_JS_PLUGIN ?>/multidate.picker.js"></script>
<script type="text/javascript" src="<?= ASSET_JS_CUSTOM ?>/multi-date.js"></script>
<script src="<?= ASSET_JS_PLUGIN ?>/chartist.min.js"></script>
<script src="<?= ASSET_JS_PLUGIN ?>/chartist-plugin-1.js"></script>
<script type="text/javascript" src="<?= ASSET_JS_CUSTOM ?>/seriesGraph.js"></script>
<link href="<?= ASSET_CSS ?>/mdtimepicker.css" rel="stylesheet">
<script src="<?= ASSET_JS_PLUGIN ?>/mdtimepicker.js"></script>
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

$('.timepicker').mdtimepicker({
  // format of the time value (data-time attribute)
  timeFormat: 'hh:mm:ss.000',
  // format of the input value
  format: 'hh:mm:ss',     
  // theme of the timepicker
  // 'red', 'purple', 'indigo', 'teal', 'green'
  theme: 'purple',       
  // determines if input is readonly
  readOnly: false,
  // determines if display value has zero padding for hour value less than 10 (i.e. 05:30 PM); 24-hour format has padding by default
  hourPadding: false,
    clearBtn:true
  
});

</script>
<script>
	$(document).ready(function() {
    $('.select2').select2();
});
	$("#clear-t").click(function(){
		$("#timepicker1").val("");
		$("#timepicker2").val("");
	});

	$("#t-mode-3").change(function(){
		$("#time-1-text").text("StartTime");
		$("#div-time-1").attr('class', 'col-md-5 mb-5');
		$("#div-time-2").attr('class', 'col-md-5 mb-5');
		$('#div-time-2').removeAttr('hidden');
	});

	$("#t-mode-2").change(function(){
		$("#time-1-text").text("Time");
		$("#div-time-2").attr("hidden", true);
		$("#div-time-1").attr('class', 'col-md-10 mb-10');
	});

	$("#t-mode-1").change(function(){
		$("#time-1-text").text("Time");
		$("#div-time-2").attr("hidden", true);
		$("#div-time-1").attr('class', 'col-md-10 mb-10');
	});

</script>