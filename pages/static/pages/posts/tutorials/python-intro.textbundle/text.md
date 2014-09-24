# Introduction to Python

你已經把 Python 裝好了，接下來讓我們來開始寫點程式吧！

## Python shell

在我們開始跟 Python 培養感情之前，我們先來打開在你電腦上面的 *command line* 吧！準備好之後，跟著下面的指示做：

首先，讓我們打開 Python 的 shell，輸入 `python3` 接著按下 Enter 鍵，你應該會看到

```console
$ python3
Python 3.4.1 (...)
Type "copyright", "credits" or "license" for more information.
>>>
```

## 你的第一個 Python 指令

在輸入了 `python3` 之後，應該會看到提示列變成了 `>>>`，這代表著現在我們只能夠使用在 Python 當中的指令。如果想要回到原本的提示列，那麼請輸入 `exit()`

現在讓我們開始來試試幾個 Python 的指令。首先，Python 是可以當作簡單的計算機的！試著隨便打些算式，像是 `2 + 3` 接著按下 Enter。

```python
>>> 2 + 3
5
```

看到答案出來了吧！你也可以試試看其他的指令像是：
- `4 * 5`
- `5 - 1`
- `40 / 2`
- `2**3`

看看會有些怎麼樣的結果呢？接下來讓我們看看還能在這邊做些什麼事情。

## 字串 (Strings)

Python 當中除了可以處理數字之外當然也可以處理文字，試著打打看你的名字：

```python
>>> "Django"
'Django'
```

你已經創建了你的第一個字串 (string) 了！在 Python 當中，文字就是以字串的形式存在電腦當中，並且以單括號 (`'`) 或是雙括號 (`"`) 包住。

兩個字串是可以用 + 連接在一起的，試著打：

```python
>>> "Hello " + "Django"
'Hello Django'
```

你也可以在一個字串後面用乘號 (*) 加上某個數字：

```python
>>> "Django" * 3
'DjangoDjangoDjango'
```

或是要把你的名字變成全部都是大寫的字母：

```python
>>> "Django".upper()
'DJANGO'
```

你剛剛用了一個叫做 `upper` 的 __函式__ (function)！函式 (像是 `upper()`) 是一些可以作用在某個東西上的 (在這邊的例子是 `"Django"`) 一段程式。

如果你想要知道你的名字當中有多少個字母，當然也有一個函式可以做到這件事情：

```python
>>> len("Django")
6
```

看到這邊有沒有覺得很奇怪，為什麼有時候你是在字串後面呼叫函式（像是 `"Django".upper()`），有時候你事先呼叫一個函式再把字串丟進去（像是 `len("Django")`）。在有些狀況下，函式是跟著你要作用的東西的，舉例來說，像是 `upper()` 就是只能作用在字串上面。這時候的函式我們會給他一個特殊的名稱，叫做 `__method__`。有時候，functions 則不被限定被作用在某種特定的東西上，就像是 `len()` 就是這樣子。這就是為什麼我們會直接把 `"Django"` 當作參數直接傳進去 `len()` 函式當中。

### 小結一下

好了，來小結一下目前我們學到的東西：

- __python shell__ - 在這邊輸入一些指令（程式碼）就可以看到在 Python 當中的結果
- __數字和字串__ - 在 Python 當中，我們可以拿來當計算機還有用字串來處理文字
- __運算__ - 像是 + 還有 * ，可以結合兩個不同的東西產生新的值
- __函式__ - 像是 `upper()` 還有 `len()`，可以對某些東西作用

這些是任何程式語言當中都會碰到的基礎部分，接下來讓我們來看看一些稍微困難一點的東西！

## 錯誤處理

現在讓我們來試試看一些其他的東西，我們能不能來看看一個數字的長度是多少呢？輸入 `len(304023)` 來看看：

```python
>>> len(304023)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'int' has no len()
```

恭喜！我們發現了第一個錯誤。錯誤訊息告訴我們 "int" （代表著 integer，也㺵是整數的意思）沒有長度 (length)，那麼我們該怎麼辦呢？也許我們可以把原本的數字轉成字串試試看！

```python
>>> len(str(304023))
6
```

這次可沒錯誤了！我們在 `len` 函式當中，使用了 `str` 這個函式，`str()` 可以把任何東西都轉換成字串。

- `str` 函式把東西轉成 __字串__
- `int` 函式把東西轉成 __整數__

> 小提醒：我們可以把任何數字轉成文字，不過我們沒辦法把任意文字轉成數字，想想看如果輸入 `int("hello")` 應該出現什麼呢？

## 變數 (Variables)

在程式設計當中，一個很重要的概念就是變數 (variables)，什麼是變數呢？你可以把變數想成某些東西的別名，透過使用變數，我們可以讓程式更好讀也更好理解。有點難懂嗎？讓我們來看看例子！

讓我們來創建一個叫做 `name` 的變數：

```python
>>> name = "Django"
```

這樣我們就建了一個叫做 name 的變數，內容則是一個為 `"Django"` 的字串。

不知道你有沒有注意到，這次你的程式並不會像之前一樣印出任何東西，那麼我們要怎麼知道我們真的有成功創了一個變數呢？讓我們輸入 `name` 來看看：

```python
>>> name
'Django'
```

恭喜！你真的成功了創了第一個變數了！你也可以試著來改變這個變數的內容看看：

```python
>>> name = "django"
>>> name
'django'
```

當然你也可以把這個變數傳到函式裡面：

```python
>>> len(name)
6
```

變數當中的內容不只能放字串，要放數字也可以，讓我們來試試看：

```python
>>> a = 4
>>> b = 6
>>> a * b
24
```

不過如果我們不小心打錯了變數的名稱會怎麼樣呢？試試看吧！

```python
>>> name = "Maria"
>>> names
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'names' is not defined
```

我們又看到一個錯誤了！如你所見，Python 當中有著各式各樣的不同錯誤，在這邊我們看到了一個叫做 **NameError** 的錯誤。如果你不小心用了一個你沒有定義過的變數，那麼 Python 就會吐出這個錯誤給你，因此，如果你看到了這個錯誤，記得檢查一下你有沒有拼錯字喔！

## print 函式

試試看打以下的指令：

```python
>>> name = 'Maria'
>>> name
'Maria'
>>> print(name)
Maria
```

當你只有輸入 `name` 的時候，Python 會輸出 'name' 這個變數的表示式，當中有五個字母 M-a-r-i-a，以及前後兩個單引號。當你輸入 `print(name)` 的時候，Python 會把這個變數的內容印出來，這邊可以看到前後的引號不見了！

等等我們會常常用到 `print()` 這個函式，我們寫程式的過程當中可以一直把變數印出來來幫助我們確認程式有沒有錯誤。

## 串列 (Lists)

除了字串還有整數外，Python 還有各式各樣不同形態的物件，現在我們要來介紹一個叫做 __list__ 的東西。list 是什麼呢？當我們要存一個東西的時候，我們可以用一個變數來做到，如果要存很長的一整串東西的時候，那麼我們就會用 list 來做。

讓我們來創建一個 list：

```python
>>> []
[]
```

在這邊，我們建立了一個空的 list，看起來好像沒什麼用，接著讓我們創建一個塞滿樂透號碼的 list 吧！

```python
>>> lottery = [3, 42, 12, 19, 30, 59]
```

我們建了一個 list 並且把它用 lottery 這個變數來表示，如果我們想要知道 lottery 這個 list 裡面放了多少個數字該怎麼辦呢？剛剛是不是有某個函式可以做到呢？

```python
>>> len(lottery)
6
```

沒錯！ `len()` 能夠給你 list 的長度，那麼如果我們想要來把數字由小排到大呢？

```python
>>> lottery.sort()
>>> print(lottery)
[3, 12, 19, 30, 42, 59]
```

你可以看到當我們呼叫了 `sort()` 這個函式之後，lottery 當中的數字就由小排到大了！

如果你想要把這個 list 的次序倒轉該怎麼做呢？

```python
>>> lottery.reverse()
>>> print(lottery)
[59, 42, 30, 19, 12, 3]
```

很容易吧！如果你想要在 list 當中加些數字，你可以試試看以下的指令：

```python
>>> lottery.append(199)
>>> print(lottery)
[59, 42, 30, 19, 12, 3, 199]
```

如果你只希望看到 list 當中的第一個數字，你可以使用 __indexs__ 來達成，通常在資訊科學的領域當中，我們會用 index 0 來代表第一個東西，index 1 來代表第二個，以此類推。我們來試試看：

```python
>>> print(lottery[0])
59
>>> print(lottery[1])
42
```

在此，可以看到我們是透過方括號 [] 來存取不同的數字，讓我們來玩看看 6, 7, 1000, -1, 等等的 index 來看看會有什麼樣的結果吧！如果想要對 list 更加了解，可以參考[官方文件](https://docs.python.org/3/tutorial/datastructures.html)。


## 字典 (Dictionaries)

字典 (dictionary) 基本上跟 list 很像，不過在 list 當中，你是透過索引 (index) 來存取個別的成員，但是在 dictionary 當中則是透過鍵值 (key) 來存取，key 可以是一個數字或是任何字串，我們可以透過這樣來創建一個空的 dictionary：

```python
>>> {}
{}
```

接著讓我們來試著輸入以下的命令：

```python
>>> participant = {'name' : 'Django', 'country' : 'Taiwan', 'favorite_numbers' : [7, 29, 33,]}
```

在此我們創了一個叫做 `participant` 的變數，而且有三個可以用 key 存取的成員：

- `name` 這個 key 對應到的是 `'Django'` (一個字串),
- `country` 對應到 `'Taiwan'` (另一個字串),
- `favorite_numbers` 對應到了 `[7, 29, 33]` (一個 `list`).

你可以透過下面的指令來看看個別的 key 所對應的內容：

```python
>>> print(participant['name'])
Django
```

我們可以看到基本上跟 list 還蠻像的，不過你不用特別記得索引的數字，你只要記 key 的名字就好。

那麼當我們用了一個不存在的 key 的時候會發生怎麼樣的事情呢？讓我們試試看！

```python
>>> participant['age']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'age'
```

現在看到這個你應該已經不會感到驚訝了吧，我們又看到了另外一個錯誤！這次是 **KeyError**，這邊告訴了我們 `'age'` 這個 key 不存在這個 dictionary 當中。

那麼什麼時候我們要用 dictionary，什麼時候要用 list 呢？

- 如果你需要一連串有順序的東西，那麼用 list
- 如果你希望透過 key 來存取相對應的內容，那麼用 dictionary

在 dictionary 創建之後，你可以為它增加新的 key 以及其對應的內容

```python
>>> participant['favorite_language'] = 'Python'
```

就跟 list 一樣，用 `len()` 可以回傳這個 dictionary 有多少個 key 以及其對應的內容

```python
>>> len(participant)
4
```

到目前為止還能跟得上嗎？接下來我們來做點稍微困難一點的事情！

你可以用 `del` 這個指令來刪掉 dictionary 當中的某個東西，舉例來說，如果你想要把 `'favorite_numbers'` 所對應的內容刪掉，你只要用以下的指令：

```python
>>> del participant['favorite_numbers']
>>> participant
{'country': 'Taiwan', 'favorite_language': 'Python', 'name': 'Django'}
```

看吧！我們把 'favorite_numbers' 所對應的內容刪掉了！

除此之外，你也可以修改原本已經存在的 key 所對應到的內容：

```python
>>> participant['country'] = 'USA'
>>> participant
{'country': 'USA', 'favorite_language': 'Python', 'name': 'Django'}
```

很好！你成功的修改了 `'country'` 對應到的內容了！

### 小結

很好！你現在已經對程式設計有不少的了解了，讓我們來複習一下你學到了些什麼：

- __錯誤__ - 你現在已經知道要如何處理 Python 的程式語法錯誤了！
- __變數__ - 透過使用變數能讓你的程式更好讀
- __串列__ - 如果你想要讓一連串的東西依照一定順序儲存，就用串列吧
- __字典__ - 如果你想要透過 key 來存取你的內容，就用字典

## 比較

在程式設計當中，我們常常會要做兩個東西之間的比較。通常想到比較，我們最容易想到數字之間的比較，讓我們來看看簡單的例子：

```python
>>> 5 > 2
True
>>> 3 < 1
False
>>> 5 > 2 * 2
True
>>> 1 == 1
True
```

在這邊你可能會覺得奇怪，為什麼我們用 `==` 來判斷兩個數字是否相等呢？還記得之前我們講 variables 的時候，我們是用 `=` 來指派某個變數的值，所以記得如果你要確認兩個東西是否相等，千萬記得要用 `==` 來做判斷！

讓我們再來玩玩：

```python
>>> 6 >= 12 / 2
True
>>> 3 <= 2
False
```

這邊我們可以看到除了 `>` 還有 `<` 之外， `>=` 還有 `<=` 也可以拿來用！

讓我們試試看以下的指令：

```python
>>> 6 > 2 and 2 < 3
True
>>> 3 > 2 and 2 < 1
False
>>> 3 > 2 or 2 < 1
True
```

在這邊你看到了兩個沒看過的指令 `and` 跟 `or`，這兩個分別是什麼呢？

- __and__ - 如果你用了 `and`，那麼在 `and` 兩側的比較是都要成立才會回傳成立
- __or__ - 如果你用了 `or`，那麼在 `or` 兩側的比較只要其中一個成立就會回傳成立

我們看完了數字之間的比較，那麼如果我們要試著比較數字跟字串會怎麼樣？

```python
>>> 1 > 'django'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unorderable types: int() > str()
```

想必到這個時候你應該已經很熟悉錯誤的出現了，在這邊我們可以看到 Python 並不允許我們比較字串跟數字，如果出現這樣的狀況，那麼會跳出一個 **TypeError** 來告訴我們字串跟數字不能夠互相做比較。

## 布林 (Boolean)

就在剛剛你又學會了 Python 當中的一個叫做 __Boolean__ 的型別，在這種型別當中存放的只有兩種東西：

- True - 代表真
- False - 代表假

記得，在 Python 當中我們一定要寫成 True/False，也就是第一個字母大寫，其他都小寫，這樣 Python 才會認得。

Boolean 當然也可以存在變數當中：

```python
>>> a = True
>>> a
True
```

你也可以試試看以下的指令：

```python
>>> a = 2 > 5
>>> a
False
```

來練習一下下面的指令，玩看看會有什麼樣的結果呢？

- `True and True`
- `False and True`
- `True or 1 == 1`
- `1 != 2`

恭喜，接下來我們會來教些更有用的東西！

## If...elif...else

在程式當中，我們常常做的一件事情是當某些狀況成立的時候，才會執行特定的程式碼。這就是為什麼 Python 有一個叫做 __if__ 的指令存在。

試試看以下的程式：

```python
>>> if 3 > 2:
...
```

看起來好像什麼都沒有發生，不過我們這邊看到了前面的符號變成了 `...` 而不是 `>>>`，這代表著 Python 希望我們告訴它說當 `3 > 2` 成立的時候要做些什麼事情，讓我們試試看如果成立的時候印出 "It works!"。

```python
>>> if 3 > 2:
... print('It works!')
  File "<stdin>", line 2
    print('It works')
        ^
IndentationError: expected an indented block
```

很好，我們又看到錯誤了！這次我們看到的錯誤比較奇怪，是個 **IndentationError**。 Indentation 的中文翻譯通常會叫做縮排，在 Python 當中縮排是個很重要的觀念，我們必須透過縮排才可以形成一個又一個的程式區塊，以這個例子來說，這樣 Python 才會知道 if 如果成立的話要執行哪些程式碼。

那麼要怎麼做縮排呢？很簡單，只要在前面加個空格就好！不過通常我們為了一致性，絕大多數的 Python 程式設計師都會用四個空格當作縮排。

```python
>>> if 3 > 2:
...     print('It works!')
...
It works!
```

所以在 `if` 之後有縮排的程式碼都會在條件成立的時候被執行：

```python
>>> if 3 > 2:
...     print('It works!')
...     print('Another command')
...
It works!
Another command
```

### 如果 if 當中的條件不成立呢？

在之前的例子，程式只有在條件成立的時候才會執行，在 Python 當中，還提供了 `elif` 還有 `else` 這兩個指令可以用：

```python
>>> name = 'Django'
>>> if name == 'Django':
...     print('Hey Django!')
... elif name == 'John':
...     print('Hey John!')
... else:
...     print('Hey anonymous!')
...
Django!
```

試著打打看上面的程式，改變 name 的內容看看會有什麼不同的結果吧。

### 小結

在剛剛我們學到了這些東西：

- __比較__ - 在 Python 當中你可以用 `>`, `>=`, `==`, `<=`, `<` 還有 `and`, `or` 來作比較
- __布林__ - 是一種只有 `True` 或是 `False` 這兩種值得型別
- __if...elif...else__ - 讓我們能夠在某種特定狀況成立的時候才執行某段程式

## 來寫你自己的函式

記得之前我們有用過 `len()` 這個函式嗎？除了 Python 內建的函式之外，你當然也可以寫你自己需要的函式。

在一個函式當中，會有一大段能夠讓 Python 執行的程式碼。在 Python 當中，我們會以 `def` 為開頭開始定義一個函式，後面接著這個函式的名字還有一些可以傳進來的參數，讓我們從最簡單的函式開始！

```python
>>> def hi():
...
```

這邊我們又看到了 `...` 的出現，相信你在前面已經看過了，應該知道要做些什麼吧。沒錯，你需要做縮排！所以按四下空白鍵吧！

```python
>>> def hi():
...     print('Hi there!')
...     print('How are you?')
...
```

很好，我們已經完成了我們的第一個函式了。接著，讓我們來執行看看。

```python
>>> hi()
Hi there!
How are you?
```

很簡單吧，接下來讓我們來建立一個有傳入參數的函式。

```python
>>> def hi(name):
...
```

在這邊，我們創了一個叫做 hi 的函式，傳入值的變數名稱叫做 `name`

```python
>>> def hi(name):
...     if name == 'Django':
...         print("Django")
...     else:
...         print("Hi "+name)
...
```

這邊我們寫了一個簡單的函式，如果傳入的 name 是 Django，那麼就印出來 Django，否則就在前面加上 Hi。這邊我們結合了之前提到的 `if` 還有 `else`，注意到了嗎？這邊我們在 `if` 之後有縮排，這樣子是不是更能夠讓你了解到縮排的好處呢？

接著讓我們來試試看呼叫這個函式

```python
>>> hi()
    Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: hi() missing 1 required positional argument: 'name'
```

又看到一個錯誤了，還好 Python 有很清楚的跟你說錯誤在哪裡。錯誤訊息告訴我們說呼叫 `hi()` 這個函式需要傳入一個參數，但是我們呼叫的時候沒有傳入參數。所以我們應該要這樣做：

```python
>>> hi("Django")
Django
>>> hi("Steve")
Hi Steve
>>> hi("Jobs")
Hi Jobs
```

很不錯吧，我們只要傳進去不同的名字就可以有不同的結果。函式的好處就是當我們有發現有某些程式碼重複出現的時候，就可以把這些重複的地方抽出來。程式設計師都很懶惰的，如果可以的話會儘量能夠少打點字，這就是為什麼會出現函式。

## 迴圈 (Loops)

正如同我們之前提過，程式設計師都很懶惰的，都希望能夠少打點字。

還記得我們教過的 list 嗎？讓我們來創一個叫做 girls 的 list：

```python
>>> girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
```

我們希望跟 girls 這個 list 當中的名字都說 `Hi`，我們剛剛已經有建了一個 `hi` 的函式可以做到這件事情，讓我們利用回圈來做這件事情，我們可以用 `for` 這個指令來達成

```python
>>> for name in girls:
...
```

又看到了 `...`，大家應該都知道該做什麼了吧。沒錯！加上空格

```python
>>> for name in girls:
...     hi(name)
...     print('Next girl')
...
Hi Rachel
Next girl
Hi Monica
Next girl
Hi Phoebe
Next girl
Hi Ola
Next girl
Hi You
Next girl
```

正如你所見，在 `for` 這個指令的區塊當中的程式會被重複執行，每次的 `name` 都會是 `girls` 當中的一個元素，再傳入到 `hi()` 這個函式當中。

## 物件 (Objects)

在程式設計當中，有個概念叫做`物件導向程式設計 (Object-oriented programming, OOP)`，在物件導向程式設計當中，我們會試著讓程式是由一個個彼此之間能夠互動的單元組成。

那麼什麼叫做物件呢？一個物件通常會由一些屬性 (properties) 還有動作所組成。乍看之下很難懂對吧，接下來我們會來給個例子。

如果我們想要來在程式當中要模擬一隻貓，那麼我們會創建一個叫做 `Cat` 的物件。一隻貓會有那些屬性呢？可能會有名字 (name)、顏色 (color) 等等。那麼貓有會有哪些動作呢？貓當然是會喵喵叫 (meow)。所以我們會這樣定義貓這個類別的物件：

    Cat
    --------
    name
    color
    meow()

看到這裡應該可以理解了吧！這邊我們就是希望把真實的東西用屬性還有動作來描述它，通常，在物件導向程式設計當中我們這邊的動作會有個專有名稱，叫做 `method`。

在 Python 當中，我們可以透過 `class` 這個指令來定義物件，輸入下面的程式碼來定義 `Cat`：

```python
>>> class Cat:
...     def __init__(self, name, color):
...         self.name = name
...         self.color = color
...     def meow(self):
...         print(self.name + " Meow~~~")
...
```

這邊我們在 Cat 當中定義了兩個 method，分別是

```python
def __init__(self, name, color):
def meow(self):
```

這邊可以看到這兩個函式的第一個參數都是 `self`，這個參數讓我們可以知道誰呼叫這個 method。接著讓我們來看看第一個 method。

```python
def __init__(self, name, color):
    self.name = name
    self.color = color
```

通常來說，Python 的類別都會有 `__init__` 這個 method，當我們創建這個物件的時候，`__init__` 就會自動被 Python 呼叫！這邊我們傳入了兩個參數，再分別把貓的名字跟顏色給設定好。

要創建一個 Cat 物件，我們可以這樣做：

```python
>>> django = Cat("Django", "black")
```

我們可以用 `.` 來取得某個物件的屬性

```python
>>> django.name
'Django'
>>> django.color
'black'
```

要呼叫物件的 method 也同樣用 `.` 可以達成

```python
>>> django.meow()
Django Meow~~~
```

恭喜，到這邊為止你已經會了基本的物件導向程式設計了！

## 小結

基本的 Python 差不多結束了！現在你已經能夠自稱是個 Python 程式設計師 :) 休息一下吧，讓我們可以繼續迎接下面的課程。
