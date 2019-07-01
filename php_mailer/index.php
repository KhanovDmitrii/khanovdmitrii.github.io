<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

//Load Composer's autoloader
require 'vendor/autoload.php';

if(!$_POST)
	die();

$mail = new PHPMailer(true);                              // `true` разрешает исключения
try {
    // настройки сервера
    $mail->SMTPDebug = 2;                                 // подробный отчёт о действиях
    $mail->isSMTP();                                      // использование SMTP
    $mail->Host = 'smtp.yandex.ru';
    $mail->SMTPAuth = true;                                
    $mail->Username = 'useruser@yandex.ru';               // SMTP логин
    $mail->Password = 'jkdhg23565sfgsa';                  // пароль  
    $mail->SMTPSecure = 'tls';                            // шифрование TLS encryption, вариант – `ssl`  
    $mail->Port = 587;                                    // порт TCP   

    // setFrom и replyTo для Яндекса должны совпадать с Username
    $mail->setFrom('useruser@yandex.ru', 'Mailer');
    $mail->addAddress($_POST['to'], 'Khanov D');     // кому направляете письмо

    $mail->addReplyTo($_POST['from'], 'Mailer');

    $mail->CharSet = 'UTF-8';

    // Содержимое
    $mail->isHTML(true);                                  // формат письма – HTML
    $mail->Subject = $_POST['subj'];
    $mail->Body    = $_POST['text'];
    $mail->AltBody = strip_tags($_POST['text']);

    $mail->send();
    echo 'Отправлено!';
} catch (Exception $e) {
    echo 'Не удалось отправить. Mailer Error: ', $mail->ErrorInfo;
}
