<?php

function curl_post($url_link, $data = null){
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $url_link);
    curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
    curl_setopt($ch, CURLOPT_POST, 1);
    curl_setopt( $ch, CURLOPT_HTTPHEADER, array('Content-Type:application/json'));
    curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 0); 
    curl_setopt($ch, CURLOPT_TIMEOUT, 400); //timeout in seconds
    // server response
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    $server_response = curl_exec ($ch);
    curl_close ($ch);
    $json = json_decode($server_response, true);


    return $json;
}