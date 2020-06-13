
<?php 
print_r($_POST);
if(!empty($_POST)){
    if(isset($_POST["form1"])) {
        print("posted !!!!");
        $ch = curl_init();

        // params example
        $post = [
            'date' => 20121105,
            'password' => 'pass1'
        ];

        $post = $_POST;

        // Request URL
        curl_setopt($ch, CURLOPT_URL, "http://127.0.0.1:8007/test");
        curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($post));
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt( $ch, CURLOPT_HTTPHEADER, array('Content-Type:application/json'));

        // server response
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

        $server_response = curl_exec ($ch);

        curl_close ($ch);

        print($server_response);
        print("Here");
    }
    
} else {
    print("asddasdsdas");
}

?>
       
<form class="form-horizontal" id="login-form"
action="debug.php" method="post" id="form1"
>
            <div class="control-group input-append">
                <label for="text" class="control-label">Email</label>
                <div class="controls">
                    <input name="email" id="email" type="email" value="" placeholder="Enter your email"/> 
                </div>
            </div>
            <br>
            <div class="control-group input-append">
                <label for="passwd" class="control-label">Passworassd</label>
                <div class="controls">
                    <input name="passwd" id="passwd" type="password" value="" placeholder="Enter your password"/> 
                </div>
            </div>
            <br>
            <div class="control-group">
                <div class="controls">
                    <div class="left1">
                        <input type="submit" id="login" value="Submit" class="btn btn-success" name="formtest"/>
                    </div>
                </div>
            </div>
        </form>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>


<!-- <script>

$('#login').click(function(){
    alert("clicked");
    $.ajax({
        url: "debug.php",
        type:'POST',
        dataType:"json",
        data: $("#login-form").serialize()
    }).done(function(data){
        // var json_text = JSON.stringify(data, null, 2);
        // obj = JSON.parse(json_text);
        // if(obj.status == 'done') 
        //     alert('you are logged in'); 
    });
});
</script> -->


<?php 
// $ch = curl_init();

// // params example
// $post = [
//     'date' => 20121105,
//     'password' => 'pass1'
// ];

// // Request URL
// curl_setopt($ch, CURLOPT_URL, "http://127.0.0.1:8007/test");
// curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($post));
// curl_setopt($ch, CURLOPT_POST, 1);
// curl_setopt( $ch, CURLOPT_HTTPHEADER, array('Content-Type:application/json'));

// // server response
// curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// $server_response = curl_exec ($ch);

// curl_close ($ch);
?>