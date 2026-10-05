<!DOCTYPE html>

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

```
<title>AI Spam Detector</title>

<style>
    * {
        box-sizing: border-box;
        font-family: Arial, sans-serif;
    }

    body {
        margin: 0;
        min-height: 100vh;
        display: flex;
        justify-content: center;
        align-items: center;
        background: linear-gradient(135deg, #667eea, #764ba2);
    }

    .container {
        width: 90%;
        max-width: 600px;
        background: white;
        padding: 35px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        text-align: center;
    }

    h1 {
        color: #333;
        margin-bottom: 10px;
    }

    p {
        color: #666;
        margin-bottom: 25px;
    }

    textarea {
        width: 100%;
        height: 150px;
        padding: 15px;
        border: 2px solid #ddd;
        border-radius: 10px;
        resize: none;
        font-size: 16px;
        outline: none;
    }

    textarea:focus {
        border-color: #667eea;
    }

    button {
        margin-top: 20px;
        padding: 12px 30px;
        border: none;
        border-radius: 8px;
        background: #667eea;
        color: white;
        font-size: 16px;
        cursor: pointer;
    }

    button:hover {
        background: #5568d8;
    }

    #result {
        margin-top: 25px;
        padding: 15px;
        border-radius: 10px;
        font-size: 18px;
        font-weight: bold;
        display: none;
    }

    .spam {
        background: #ffe5e5;
        color: #d60000;
    }

    .safe {
        background: #e5ffe9;
        color: #008a20;
    }

    .warning {
        background: #fff3cd;
        color: #856404;
    }

    .footer {
        margin-top: 25px;
        font-size: 13px;
        color: #999;
    }
</style>
```

</head>

<body>

<div class="container">

```
<h1>📧 AI Spam Detector</h1>

<p>Enter any message to check if it is SPAM or NOT SPAM.</p>

<textarea id="message"
    placeholder="Type your message here..."></textarea>

<br>

<button onclick="checkSpam()">Check Message</button>

<div id="result"></div>

<div class="footer">
    AI Spam Detection Project
</div>
```

</div>

<script>

    /*
       Spam keywords based on the training examples
       from the original Python project.
    */

    const spamWords = [
        "free",
        "money",
        "win",
        "won",
        "lottery",
        "cheap",
        "meds",
        "10000",
        "dollars",
        "click",
        "urgent",
        "prize",
        "claim",
        "reward",
        "congratulations"
    ];

    function checkSpam() {

        const messageBox = document.getElementById("message");
        const resultBox = document.getElementById("result");

        const message = messageBox.value.trim().toLowerCase();

        if (message === "") {

            resultBox.style.display = "block";
            resultBox.className = "warning";
            resultBox.innerHTML = "⚠️ Please type a message first.";

            return;
        }

        let score = 0;

        /*
           Check the message for spam-related words.
        */

        spamWords.forEach(function(word) {

            if (message.includes(word)) {
                score++;
            }

        });

        resultBox.style.display = "block";

        /*
           If one or more spam keywords are found,
           classify the message as SPAM.
        */

        if (score > 0) {

            resultBox.className = "spam";

            resultBox.innerHTML =
                "🚨 This is SPAM!<br><small>Spam keywords detected: "
                + score + "</small>";

        } else {

            resultBox.className = "safe";

            resultBox.innerHTML =
                "✅ This is NOT SPAM - Safe message";

        }
    }

</script>

</body>
</html>
