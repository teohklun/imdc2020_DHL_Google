<?php
include_once "../utility/packed_library.php";
?>
<?php include_once "template/header.php"; ?>
<body>
	    <div class="wrapper">
        <div class="sidebar" data-image="../assets/img/sidebar-5.jpg">
<?php include_once "template/sidebar.php"; ?>
        </div>

<div class="main-panel">
<?php include_once "template/nav.php"; ?>
	<div class="content">
		<div class="container" style="margin-bottom: 15px">
	      <div class="card-header ">
	      	<a href="createOptimalRoute.php">
	          <p class="card-category" style="text-align-last: center";><span style="font-size: 20px">Create Optimal Routes</span></p>
	      </a>
	      </div>
		</div>

		<div class="container" style="margin-bottom: 15px">
	      <div class="card-header ">
	      	<a href="multiR.php">
	          <p class="card-category" style="text-align-last: center";><span style="font-size: 20px">View Single Date routes</span></p>
	      </a>
	      </div>
		</div>

		<div class="container" style="margin-top: 15px">
	      <div class="card-header ">
	      	<a href="singleR.php">
	          <p class="card-category" style="text-align-last: center";><span style="font-size: 20px">View Single Route (driver)</span></p>
	      </a>
	      </div>
		</div>
	</div>
</div>


</div>

</div>

        </body>

        </html>