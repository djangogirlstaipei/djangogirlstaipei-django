---
title: "HTML"
---

HTML = Hyper Text Markup Language
超文字標注語言

---

談到 HTML 的時後，不免就會要先提到 CSS 跟 JavaScript。
在網頁的架構中，HTML/CSS/JavaScript 是如影隨形，相輔相成的技術。

---

因為它們三者各別代表了三個不同的面向

---

HTML - 文件，結構

CSS  - 樣式，外觀

JavaScript - 事件，行為

---

HTML 可以引入各種媒體，如圖片，影片，CSS，JavaScript 或是建立連結到另外一個 HTML 頁面。

---

所以 HTML 是建立網際網路的重要的媒介哦!

---

基本上 HTML 就是由一系列的標籤 (tags) 所組成，
HTML 跟程式語言有著一樣的基本結構跟目的，就是要用來描敘內容。
我們先介紹最常見的這幾種:

* 文字標籤 (text tags)
* 列表標籤 (list tags)
* 超連結標籤 (hyperlinks)
* 結構性標籤 (structure)

而基本上每個標籤的屬性當中， 類別名稱 (class name) `class` 是我們最常使用到的。

> P.S. 這邊所分類的標籤可能會跟妳到市面上找到的 HTML 文件規範的分類有所出入，主要是因為方便教學，同學有興趣可以去翻閱看看。

---

## 文字標籤 Text Tags

&lt;h1&gt;—&lt;h6&gt; 標題（headings），由大（&lt;h1&gt;）到小（&lt;h6&gt;）。&lt;p&gt; 段落標籤。

```
<h1>, <h2>, <h3>, <h4>, <h5>, <h6>, <p>
```

* &lt;em&gt; 用口氣強調所選擇的文字 (emphasis)
* &lt;strong&gt; 更加強調所選擇文字

```
<em>, <strong>
```


### Example

```
<h1>旅行與我</h1>
<h2>什麼是旅行呢?</h2>
<p>我<em>最喜歡</em>旅行了!</p>
<p>旅行就像是一段人生的小旅程的縮影，妳不知道妳會碰見誰，妳不知道會往那裡走。</p>

<h2>喜歡那個國家呢?</h2>
<p><strong>西班牙!!!</strong>那裡是一個夢幻的國度，有美食，午覺，跟藝術。</p>

```

<h1>旅行與我</h1>
<h2>什麼是旅行呢?</h2>
<p>我<em>最喜歡</em>旅行了!</p>
<p>旅行就像是一段人生的小旅程的縮影，妳不知道妳會碰見誰，妳不知道會往那裡走。</p>

<h2>喜歡那個國家呢?</h2>
<p><strong>西班牙!!!</strong>那裡是一個夢幻的國度，有美食，午覺，跟藝術。</p>

---

## 列表標籤 List Tags

```
<ul>, <ol>, <li>
```

* &lt;ul&gt; 無序列表 (Unordered List)
* &lt;ol&gt; 有序列表 (Ordered List)
* &lt;li&gt; 列表項目 (List Item)

### Example

```
<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>
```

<ul>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ul>

```
<ol>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ol>
```
<ol>
    <li>Item 1</li>
    <li>Item 2</li>
    <li>Item 3</li>
</ol>
---


## Hyperlinks

建立超連結，可以把在文件建立連結到文件本身的某個區塊，或是連到另外一份文件哦。

```
<a name='like' href='like.html' rel='like'>Like</a>
```

主要的屬性有 `name, href, rel`：

* name - 用來辦識該連結的目的地
* href - 連結的網址
* rel - 該連結的關係 (Relation)

---


## 結構性 Structure

```
<div>, <span>
```

&lt;div&gt; 是指一個區塊性質的元素，他會造成段落，本身對於內容沒有賦於什麼特別的意義，例如，&lt;p&gt; 可能是代表一個段落，&lt;h1&gt;是指大標題。所以普遍我們拿來做區塊性的版面排版。

&lt;span&gt; 則類似 &lt;div&gt;，也是不會對內容賦於任何意義，也不會造成段落。

我們在使用 &lt;div&gt; 跟 &lt;span&gt; 通常會搭配 `class` 的屬性來客制化各種樣式跟排版，如果當妳不知道用什麼標籤來描敘妳的內容的時後，可以考慮用 `<div> 或是 <span>` 哦!

## 結語

HTML 是用來描敘文件的內容，所以會根據內容的差異來使用不同的標籤，就跟我們寫作的時後，會用不同的文字來表達想要傳遞的內容的意涵，而一份好的 HTML 不止是讓電腦看得懂，還要讓**人**也可以很容易的閱讀，例如:

```
<div class='sidebar'>
    <ul class='menu-list'>
        <li class='menu-list__item'>Home</li>
        <li class='menu-list__item'>Profile</li>
        <li class='menu-list__item'>Facebook</li>
    </ul>
</div>
<div class='content'>
    <h1 class='article-title'>Title</h1>
    <h2>Tagname</h2>
    <p>................</p>
</div>

```

我們可以很容易的了解，這個頁面是一個具有 `sidebar` 跟 `content` 兩個區塊的頁面，
裡面自有 `menu-list` 選單，跟 `article-title` 文章相關的內容。

現在妳們已經具備基本的 HTML 的知識，可以開始進入 Django 的世界了!
