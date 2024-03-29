<p>There is a special keyboard with <strong>all keys in a single row</strong>.</p>

<p>Given a string <code>keyboard</code> of length 26 indicating the layout of the keyboard (indexed from 0 to&nbsp;25), initially your finger is at index 0. To type a character, you have to move your finger to the index of the desired character. The time taken to move your finger from index <code>i</code> to index <code>j</code> is <code>|i - j|</code>.</p>

<p>You want to type a string <code>word</code>. Write a function to calculate how much time it takes to type it with one finger.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> keyboard = &quot;abcdefghijklmnopqrstuvwxyz&quot;, word = &quot;cba&quot;
<strong>Output:</strong> 4
<strong>Explanation: </strong>The index moves from 0 to 2 to write &#39;c&#39; then to 1 to write &#39;b&#39; then to 0 again to write &#39;a&#39;.
Total time = 2 + 1 + 1 = 4. 
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> keyboard = &quot;pqrstuvwxyzabcdefghijklmno&quot;, word = &quot;leetcode&quot;
<strong>Output:</strong> 73
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>keyboard.length == 26</code></li>
	<li><code><font face="monospace">keyboard</font></code> contains each&nbsp;English lowercase letter&nbsp;exactly once in some order.</li>
	<li><code>1 &lt;= word.length &lt;= 10^4</code></li>
	<li><code>word[i]</code>&nbsp;is an English lowercase letter.</li>
</ul>
<div><div>Related Topics</div><div><li>String</li></div></div>