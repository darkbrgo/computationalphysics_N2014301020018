摘要
-------
problem5.3   求解电容器周围的电势场。本题研究两块有限导体平板，其边界条件为左侧平板上电势为+1，右侧平板上电势为-1，周围x=±1和y=±1的地方电势为0

背景
-------
在不存在电荷的空间中，电势的分布遵循拉普拉斯方程:   ▽²V=0
理论上，只要在一定的边界条件下求解就可以得到静电势的空间分布，但是除了一些特殊的边界条件以外，对于这类问题我们难以得到解析解。所以使用数值计算的方法，得到电势的数值解。

本题采用Gauss-Seidel方法求解。

正文
-------

 - 画出等高线电势图和对应的3D图像[代码1](https://github.com/darkbrgo/computationalphysics_N2014301020018/blob/master/exercise12/exercise_12.py)![enter image description here](https://github.com/darkbrgo/computationalphysics_N2014301020018/blob/master/exercise12/12.1.png)![enter image description here](https://github.com/darkbrgo/computationalphysics_N2014301020018/blob/master/exercise12/12.2.png)
 - 画出电场线矢量图[代码2](https://github.com/darkbrgo/computationalphysics_N2014301020018/blob/master/exercise12/exercise_12.1.py)
 - ![enter image description here](https://github.com/darkbrgo/computationalphysics_N2014301020018/blob/master/exercise12/12.3.png)
 - 结论：    平板处电势最强，且平板间的电场均匀，整体分布符合实际情况

致谢
-------
致谢13级华杨同学，借鉴了代码

