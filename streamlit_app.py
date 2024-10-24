<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ランダム人選択アプリ</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
        }
        #result {
            font-size: 24px;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <h1>ランダム人選択アプリ</h1>
    <textarea id="names" rows="10" cols="30" placeholder="名前を1行ずつ入力してください"></textarea><br><br>
    <button onclick="selectRandomPerson()">ランダムに選ぶ</button>
    <div id="result"></div>

    <script>
        function selectRandomPerson() {
            const namesText = document.getElementById('names').value;
            const namesArray = namesText.split('\n').filter(name => name.trim() !== '');
            
            if (namesArray.length === 0) {
                document.getElementById('result').innerText = '名前を入力してください';
                return;
            }

            const randomIndex = Math.floor(Math.random() * namesArray.length);
            const selectedPerson = namesArray[randomIndex];
            
            document.getElementById('result').innerText = `選ばれた人: ${selectedPerson}`;
        }
    </script>
</body>
</html>