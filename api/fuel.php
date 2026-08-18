<?php
// ==============================================================================
// LEANO ENERGY - SECURE SERVER-SIDE FUEL SA API PROXY
// Hides the API Key on the server so it is never exposed to browser DevTools.
// ==============================================================================

header('Content-Type: application/json; charset=utf-8');
header('Access-Control-Allow-Origin: *');
header('Access-Control-Allow-Methods: GET');

$apiKey = '012fdea1778b4bcbb98a701bae959a5f';
$apiUrl = 'https://api.fuelsa.co.za/exapi/fuel/current';

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($ch, CURLOPT_TIMEOUT, 10);
curl_setopt($ch, CURLOPT_HTTPHEADER, array(
    'key: ' . $apiKey
));

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$curlError = curl_error($ch);
curl_close($ch);

if ($httpCode === 200 && $response) {
    echo $response;
} else {
    // Fallback using file_get_contents if cURL is restricted
    $opts = array(
        'ssl' => array(
            'verify_peer' => false,
            'verify_peer_name' => false,
        ),
        'http' => array(
            'method' => 'GET',
            'header' => "key: " . $apiKey . "\r\n"
        )
    );
    $context = stream_context_create($opts);
    $fallbackResponse = @file_get_contents($apiUrl, false, $context);
    
    if ($fallbackResponse !== false) {
        echo $fallbackResponse;
    } else {
        http_response_code(200);
        echo json_encode(array(
            'error' => 'Unable to fetch fuel prices',
            'detail' => $curlError
        ));
    }
}
?>
