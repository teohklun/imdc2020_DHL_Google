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
								<div class="container">
									<div class="col-md-12 col-sm-12 col-xs-12 align-self-center">
								    <label for="text-info"><span class="text-info">select one date range type</span></label>

										<div class="row">
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
				       	</div>
		         			<div class="container">
							      <!-- <label for="text-info"><span class="text-warning">Select either one type date range</span></label> -->
										<div id="date-range-div" class="col-md-12 col-sm-12 col-xs-12 align-self-center" <?= isset($_POST["form1"]) ? $_POST["date-range-type"] == "multi" ? "hidden" : ""  : "" ?> >
							      	<label for="Date"><span class="text-info">Date</span></label>
											<input id="range-date" class="form-control date" type="text" name="date-range" id="timepicker1"  value="<?= isset($input['Date']) ? $input['Date'] : '' ?>">
										</div>
										<div id="multi-date-div" class="col-md-12 col-sm-12 col-xs-12 align-self-center" <?= isset($_POST["form1"]) ? $_POST["date-range-type"] == "range" ? "hidden" : ""  : "hidden" ?> >
											<label for="date-m"><span class="text-info">Multi Select Date</span></label>
											<input type="text" id="date-m" class="form-control" name="date-multi" placeholder="Pick the multiple dates">
										</div>
									</div>
									<div class="row" style = "margin-left: 15px">
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
<!-- 				              <div class="radio icheck-peterriver">
				                  <input type="radio" checked id="mode1" name="mode">
				                  <label for="mode1">No select</label>
				              </div> -->
				              <div class="radio icheck-peterriver">
				                  <input <?= isset($_POST["form1"]) ? $_POST["mode"] == "weekday" ? "checked" : ""  : "checked" ?> type="radio" value="weekday" id="mode2" name="mode">
				                  <label for="mode2">Week Day Mode</label>
				              </div>
				              <div class="radio icheck-peterriver">
				                  <input <?= isset($_POST["form1"]) ? $_POST["mode"] == "day" ? "checked" : ""  : "" ?> type="radio" value="day" id="mode3" name="mode">
				                  <label for="mode3">Day mode</label>
				              </div>
				            </div>
				            <div class="col-md-1 col-sm-1 col-xs-1"></div>
			          	</div>
								<div class="col-md-1 col-sm-1 col-xs-1 align-self-center">
			            <input class="btn btn-primary" type="submit" name="form1" value="Submit" style="margin-bottom: 20px" >
								</div>
						</div>
	    	</form>

          <div class="card-header ">
              <h4 class="card-title">Email Statistics</h4>
              <p class="card-category">Last Campaign Performance</p>
          </div>
          <div class="card-body ">
            <div id="chart-line-1" class="ct-chart ct-golden-section"></div>
            <div class="legend">
                <i class="fa fa-circle text-info"></i> 
                <?= isset($input) ? $input["mode"] == "weekday" ? "Weekday" : "Days" : "Example"?>
            </div>
            <hr>
            <div class="stats">

                <i class="fa fa-clock-o"></i> Campaign sent 2 days ago
            </div>
	        </div>

	    </div>
	</div>
</div>
