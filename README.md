# HO ゲージの前面展望を Node-Red で構築

ファイルは json ファイルになります。
Node-Red でファイルを読み込んでください。

尚、カメラ画像とカメラ映像は排他処理となります。
カメラ映像を始めると途中で止めることができないので、再起動処理をしてください。
また、カメラの画像、映像ともに URL をご自身の使用する環境に変更してください。

## python file

camera の画像及び動画の処理の python プログラムはホームディレクトリへ置く。

## index file

templete ディレクトリを作成してその中へ index ファイルを置く。

## Raspberry-pi-zero-w

os: rasbian(desktop)

## Camera

ras pi camera v2
