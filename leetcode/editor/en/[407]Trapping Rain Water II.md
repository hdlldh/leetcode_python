<p>Given an <code>m x n</code> matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.</p>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<p>Both <i>m</i> and <i>n</i> are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.</p>

<p>&nbsp;</p>

<p><b>Example:</b></p>

<pre>
Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.
</pre>

<p><img src="https://assets.leetcode.com/uploads/2018/10/13/rainwater_empty.png" style="width: 100%; max-width: 500px;" /></p>

<p>The above image represents the elevation map <code>[[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]</code> before the rain.</p>

<p>&nbsp;</p>

<p><img src="https://assets.leetcode.com/uploads/2018/10/13/rainwater_fill.png" style="width: 100%; max-width: 500px;" /></p>

<p>After the rain, water is trapped between the blocks. The total volume of water trapped is 4.</p>
<div><div>Related Topics</div><div><li>Heap</li><li>Breadth-first Search</li></div></div>