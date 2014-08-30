---
title: "安裝與專案設定"
---

# 安裝與專案設定

本節將引導你安裝並設定專案所需要的環境。我們會進行以下的步驟：

1. 安裝 Python 3.4。
2. 安裝 Git。

以下請根據你使用的作業系統，選擇合適的教學。

## 安裝 Python

* [Microsoft Windows](#microsoft-windows)
* [OS X](#os-x)
* [Linux](#linux)

### Microsoft Windows

首先，[下載 Python 3.4.1](http://www.python.org/ftp/python/3.4.1/python-3.4.1.msi)。雙擊下載後的安裝檔，你應該會看到這個畫面

![Python 3.4.1 安裝初始畫面](http://d.pr/i/1mKN+)

請持續按下一步，直到出現這個畫面

![Python 3.4.1 安裝元件畫面](http://d.pr/i/qXHO+)

確認**只有最後一個選項**打叉，按下一步開始安裝。安裝程式可能會要求管理員權限，請在提示視窗中確認。稍等一會兒，直到出現這個畫面

![Python 3.4.1 安裝完成畫面](http://d.pr/i/a9X9+)

就代表安裝完成了！這應該會在你的系統槽（通常是 C 槽）安裝一個 `Python34` 目錄，其中包含許多檔案，包含一個 `python.exe`。

接著請下載[這個批次檔](http://d.pr/f/vGet)並執行。把剛剛安裝的 `python.exe` 拖進出現的黑視窗，按下 Enter。執行完畢後，你的桌面應該會出現一個叫做「Django Environment」的捷徑。

雙擊打開它。你應該會看到這樣的畫面：

![Windows Command Prompt](http://d.pr/i/VeBp+)

出現的這行字叫做 *prompt*。當它出現時（結尾會是一個 `>` 符號），代表終端機已經完成所有的工作，準備好等你輸入下一個指令。

輸入 `python` 看看。你應該會看到類似下面的畫面：

![Windows Python Prompt](http://d.pr/i/6cJY+)

這就代表安裝成功了！你可以直接關掉這個視窗。未來當我們說「打開終端機」時，就代表你需要用這個「Django Environment」捷徑打開視窗來使用。

接下來請直接跳到[建立開發環境](#建立開發環境)節。

### OS X

我們推薦使用 [Homebrew](http://brew.sh) 安裝 Python。首先，按下螢幕右上角的放大鏡（它叫 Spotlight），並輸入「終端機」（英文：Terminal），像這樣：

![OS X Spotlight 搜尋終端機](http://d.pr/i/HtTA+)

點一下第一個結果，應該會出現類似這樣的視窗：

![OS X 終端機](http://d.pr/i/WgLd+)

未來當我們說「打開終端機」時，就代表你需要打開一個這樣的視窗。你可能會想要把這個程式固定到 Dock 上，方便未來開啟。

注意畫面上的最後一行字。這行字叫做 *prompt*。當它出現時（結尾會是一個 `$` 符號），代表終端機已經完成所有的工作，準備好等你輸入下一個指令。

拷貝下面的指令，貼到終端機視窗內，並按下 Return 執行它：

```bash
ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"
```

如果畫面停在這個狀態，請再按一次 Return：

![OS X Homebrew 安裝初始畫面](http://d.pr/i/zQgI+)

如果畫面顯示 `Password:`，請輸入你的管理者密碼。當你輸入時密碼並不會顯示在畫面上（也不會出現 `*****` 這樣！），請不要緊張，放心輸入後按下 Return 即可：

![OS X 詢問密碼](http://d.pr/i/9Z27+)

接著應該會跳出一個這樣的視窗（如果沒有也沒關係，請直接跳到後面「已完成安裝此軟體」畫面之後的步驟）。請按「安裝」：

![OS X 安裝命令列開發者工具](http://d.pr/i/9PFO+)

在跳出的「命令列工具許可協議」視窗選擇同意，就會開始安裝。完成之後應該會跳出這個畫面：

![OS X 命令列開發者工具安裝完成畫面](http://d.pr/i/aGfn+)

按下完成就可以關閉視窗。

回到之前的終端機視窗。如果終端機畫面停在「Press any key when the installation has completed.」這行字，就再按一次 Return：

![OS X Homebrew 等候命令列開發者工具安裝畫面](http://d.pr/i/PZEB+)

接著繼續等待，直到出現

```
==> Installation successful!
==> Next steps
Run `brew doctor` before you install anything
Run `brew help` to get started
```

便代表安裝完成。現在你的終端機視窗應該類似下面這樣，最後一行是以 `$` 結尾：

![OS X 完成 Homebrew 安裝後狀態](http://d.pr/i/DVGw+)

輸入下面的指令，安裝 Python 3.4：

```bash
brew install python3
```

等到畫面停在像下面的狀態，就代表安裝完成了！

![OS X 完成 Python 3 安裝](http://d.pr/i/XibC+)

接下來請直接跳到[建立開發環境](#建立開發環境)節。

### Linux

這裡以 Ubuntu 14.04 (Trusty Tahr) 為例。如果你用其他的版本，請洽教練～

首先按下左上角的搜尋鈕，在輸入框中搜尋「terminal」：

![Ubuntu 搜尋 terminal](http://d.pr/i/KkAg+)

選擇第一個選項，應該會出現像下面的視窗：

![Ubuntu terminal](http://d.pr/i/KCzk+)

未來當我們說「打開終端機」時，就代表你需要打開一個這樣的視窗。你可能會想要把這個程式固定到 Launcher 上，方便未來開啟。

注意畫面上的最後一行字。這行字叫做 *prompt*。當它出現時（結尾會是一個 `$` 符號），代表終端機已經完成所有的工作，準備好等你輸入下一個指令。

拷貝以下的指令，貼到終端機中（用 ctrl-shift-v 或者右鍵選擇貼上），並按下 Enter 以執行：

```bash
sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt-get install python3 python3-pip -y
```

如果出現類似下面的畫面（顯示 `[sudo] password for XXX:`，`XXX` 會是你的使用者名稱），請輸入你的管理者密碼。當你輸入時密碼並不會顯示在畫面上（也不會出現 `*****` 這樣！），請不要緊張，放心輸入後按下 Enter 即可：

![Ubuntu 詢問密碼](http://d.pr/i/evzQ+)

這應該會跑一陣子。完成之後，接著拷貝以下的指令至終端機執行：

```bash
wget -qO - //d.pr/f/mbQy+ | sudo python3
```

如果系統詢問你的密碼，同樣照著前面的方法輸入。等到出現 `All done!` 後，就完成了！

## 建立開發環境

我們來建立一個目錄，用來存放所有這個教學中會用到的檔案。首先，我們必須決定要把這個目錄建立在哪裡。你的家目錄會是一個不錯的選擇。在 Windows 上，這會是類似 `C:\Users\XXX\` 的路徑（`XXX` 是你的使用者名稱）；在 Linux 上會是 `/home/XXX/`，OS X 上則是 `/Users/XXX/`。

我們先進入這個目錄。打開終端機，輸入 `cd`，後面加一個空格，然後輸入前面的路徑，按下 Enter。

我們建立一個 `djangogirls` 目錄來存放專案檔案：

```bash
mkdir djangogirls
```

然後進入這個目錄：

```bash
cd djangogirls
```

接著我們要來建立一個**虛擬環境**（virtual environment，簡稱 *virtualenv*）。這個東西可以讓你在每一個專案中使用不同的 Python/Django 環境，所以當你升級某一個網站時，不會影響到其他的專案。聽起來很有用吧！所以我們要來用它。

在終端機中輸入以下的指令：

```bash
python3 -m venv myvenv
```

> Windows 使用者請輸入 `python -m venv myvenv`

這會建立一個叫 `myvenv` 的目錄，裡面包含前面所說的 Python/Django 虛擬環境（基本上就是一堆目錄和檔案而已）。用下面的指令啟用它：

```bash
source myenv/bin/activate
```

> Windows 使用者請輸入 `myenv\Scripts\activate`

執行完畢後，你應該會發現你的 prompt 前面多了一些東西，像這樣（以 Windows 為例）：

```batch
(myvenv) C:\Users\Name\XXX>
```

注意到前面的 `(myenv)` 嗎？這就代表你目前處於 *myenv* 這個虛擬環境中。當你在開發專案時，請留意自己有沒有在該專案的虛擬環境中。如果這個設定不正確，就可能沒辦法執行程式喔！

## 安裝 Django

確認你自己還在剛剛建立的虛擬環境中。我們現在要用 `pip` 這個工具來安裝 Django。輸入以下的指令：

```bash
pip install django==1.7.0
```

> 希望這個教材能早日成真⋯⋯ orz

注意後面 `==` 的部分！你應該會看到類似下面的輸出：

```
Downloading/unpacking django==1.7.0
Installing collected packages: django
Successfully installed django
Cleaning up...
```

這樣就（終於）完成了！你現在已經有了完整的開發環境，可以準備開始建立你的第一個 Django 專案。
