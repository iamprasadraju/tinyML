# Gradient Descent

Reference -> https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent

video on gradient descent-> https://www.youtube.com/watch?v=QoK1nNAURw4

Gradient descent is a mathematical technique (optimizatiion algorithm) that iteratively finds the weights and bias that produce the model with the lowest loss. Gradient descent finds the best weight and bias by repeating the following process for a number of user-defined iterations.




The model begins training with randomized weights and biases near zero, and then repeats the following steps:



1. Calculate the loss with the current weight and bias.

2. Determine the direction to move the weights and bias that reduce loss.

3. Move the weight and bias values a small amount in the direction that reduces loss.

4. Return to step one and repeat the process until the model can't reduce the loss any further.


![alt text](https://developers.google.com/static/machine-learning/crash-course/linear-regression/images/gradient-descent.png)

<hr></hr>

**Math behind gradient descent**

Example:


| Pounds in 1000s (Feature) | Miles per Gallon (Label) |
|---------------------------|---------------------------|
| 3.50                      | 18                        |
| 3.69                      | 15                        |
| 3.44                      | 18                        |
| 3.43                      | 16                        |
| 4.34                      | 15                        |
| 4.42                      | 14                        |
| 2.37                      | 24                        |



1. The model starts training by setting the weights and bias to zero.

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mstyle mathsize="0.85em">
    <mrow class="MJX-TeXAtom-ORD">
      <mi>W</mi>
      <mi>e</mi>
      <mi>i</mi>
      <mi>g</mi>
      <mi>h</mi>
      <mi>t</mi>
      <mo>:</mo>
      <mtext>&#xA0;</mtext>
      <mn>0</mn>
    </mrow>
  </mstyle>
</math>
&nbsp;

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mstyle mathsize="0.85em">
    <mrow class="MJX-TeXAtom-ORD">
      <mi>B</mi>
      <mi>i</mi>
      <mi>a</mi>
      <mi>s</mi>
      <mo>:</mo>
      <mtext>&#xA0;</mtext>
      <mn>0</mn>
    </mrow>
  </mstyle>
</math>
&nbsp;

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mstyle mathsize="0.85em">
    <mrow class="MJX-TeXAtom-ORD">
      <mi>y</mi>
      <mo>=</mo>
      <mn>0</mn>
      <mo>+</mo>
      <mn>0</mn>
      <mo stretchy="false">(</mo>
      <msub>
        <mi>x</mi>
        <mn>1</mn>
      </msub>
      <mo stretchy="false">)</mo>
    </mrow>
  </mstyle>
</math>
&nbsp;


2. Calculate MSE loss with the current model parameters:


    We'll Calculate MSE Using : <math xmlns="http://www.w3.org/1998/Math/MathML">
  <mfrac>
    <mn>1</mn>
    <mi>M</mi>
  </mfrac>
  <munderover>
    <mo>&#x2211;<!-- ∑ --></mo>
    <mrow class="MJX-TeXAtom-ORD">
      <mi>i</mi>
      <mo>=</mo>
      <mn>1</mn>
    </mrow>
    <mrow class="MJX-TeXAtom-ORD">
      <mi>M</mi>
    </mrow>
  </munderover>
  <mo stretchy="false">(</mo>
  <msub>
    <mi>f</mi>
    <mrow class="MJX-TeXAtom-ORD">
      <mi>w</mi>
      <mo>,</mo>
      <mi>b</mi>
    </mrow>
  </msub>
  <mo stretchy="false">(</mo>
  <msub>
    <mi>x</mi>
    <mrow class="MJX-TeXAtom-ORD">
      <mo stretchy="false">(</mo>
      <mi>i</mi>
      <mo stretchy="false">)</mo>
    </mrow>
  </msub>
  <mo stretchy="false">)</mo>
  <mo>&#x2212;<!-- − --></mo>
  <msub>
    <mi>y</mi>
    <mrow class="MJX-TeXAtom-ORD">
      <mo stretchy="false">(</mo>
      <mi>i</mi>
      <mo stretchy="false">)</mo>
    </mrow>
  </msub>
  <msup>
    <mo stretchy="false">)</mo>
    <mn>2</mn>
  </msup>
</math>

    where *i* represents the *ith* training example and *M* represents the number of examples.

&nbsp;


<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mstyle mathsize="0.85em">
    <mrow class="MJX-TeXAtom-ORD">
      <mi>L</mi>
      <mi>o</mi>
      <mi>s</mi>
      <mi>s</mi>
      <mo>=</mo>
      <mfrac>
        <mrow>
          <mo stretchy="false">(</mo>
          <mn>18</mn>
          <mo>&#x2212;<!-- − --></mo>
          <mn>0</mn>
          <msup>
            <mo stretchy="false">)</mo>
            <mn>2</mn>
          </msup>
          <mo>+</mo>
          <mo stretchy="false">(</mo>
          <mn>15</mn>
          <mo>&#x2212;<!-- − --></mo>
          <mn>0</mn>
          <msup>
            <mo stretchy="false">)</mo>
            <mn>2</mn>
          </msup>
          <mo>+</mo>
          <mo stretchy="false">(</mo>
          <mn>18</mn>
          <mo>&#x2212;<!-- − --></mo>
          <mn>0</mn>
          <msup>
            <mo stretchy="false">)</mo>
            <mn>2</mn>
          </msup>
          <mo>+</mo>
          <mo stretchy="false">(</mo>
          <mn>16</mn>
          <mo>&#x2212;<!-- − --></mo>
          <mn>0</mn>
          <msup>
            <mo stretchy="false">)</mo>
            <mn>2</mn>
          </msup>
          <mo>+</mo>
          <mo stretchy="false">(</mo>
          <mn>15</mn>
          <mo>&#x2212;<!-- − --></mo>
          <mn>0</mn>
          <msup>
            <mo stretchy="false">)</mo>
            <mn>2</mn>
          </msup>
          <mo>+</mo>
          <mo stretchy="false">(</mo>
          <mn>14</mn>
          <mo>&#x2212;<!-- − --></mo>
          <mn>0</mn>
          <msup>
            <mo stretchy="false">)</mo>
            <mn>2</mn>
          </msup>
          <mo>+</mo>
          <mo stretchy="false">(</mo>
          <mn>24</mn>
          <mo>&#x2212;<!-- − --></mo>
          <mn>0</mn>
          <msup>
            <mo stretchy="false">)</mo>
            <mn>2</mn>
          </msup>
        </mrow>
        <mn>7</mn>
      </mfrac>
    </mrow>
  </mstyle>
</math>

&nbsp;

3. Calculate the slope of tangent to the loss function at each weight and the bias:

&nbsp;
<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mstyle mathsize="0.85em">
    <mrow class="MJX-TeXAtom-ORD">
      <mi>W</mi>
      <mi>e</mi>
      <mi>i</mi>
      <mi>g</mi>
      <mi>h</mi>
      <mi>t</mi>
      <mtext>&#xA0;</mtext>
      <mi>s</mi>
      <mi>l</mi>
      <mi>o</mi>
      <mi>p</mi>
      <mi>e</mi>
      <mo>:</mo>
      <mo>&#x2212;<!-- − --></mo>
      <mn>119.7</mn>
    </mrow>
  </mstyle>
</math>
&nbsp;


<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mstyle mathsize="0.85em">
    <mrow class="MJX-TeXAtom-ORD">
      <mi>B</mi>
      <mi>i</mi>
      <mi>a</mi>
      <mi>s</mi>
      <mtext>&#xA0;</mtext>
      <mi>s</mi>
      <mi>l</mi>
      <mi>o</mi>
      <mi>p</mi>
      <mi>e</mi>
      <mo>:</mo>
      <mo>&#x2212;<!-- − --></mo>
      <mn>34.3</mn>
    </mrow>
  </mstyle>
&nbsp;


**How to calculate slope**

### 1. Weight Derivative

The derivative of the loss function with respect to the weight is written as:

<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mfrac>
    <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
    <mrow>
      <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
      <mi>w</mi>
    </mrow>
  </mfrac>
  <mfrac>
    <mn>1</mn>
    <mi>M</mi>
  </mfrac>
  <munderover>
    <mo>&#x2211;<!-- ∑ --></mo>
    <mrow class="MJX-TeXAtom-ORD">
      <mi>i</mi>
      <mo>=</mo>
      <mn>1</mn>
    </mrow>
    <mrow class="MJX-TeXAtom-ORD">
      <mi>M</mi>
    </mrow>
  </munderover>
  <mo stretchy="false">(</mo>
  <msub>
    <mi>f</mi>
    <mrow class="MJX-TeXAtom-ORD">
      <mi>w</mi>
      <mo>,</mo>
      <mi>b</mi>
    </mrow>
  </msub>
  <mo stretchy="false">(</mo>
  <msub>
    <mi>x</mi>
    <mrow class="MJX-TeXAtom-ORD">
      <mo stretchy="false">(</mo>
      <mi>i</mi>
      <mo stretchy="false">)</mo>
    </mrow>
  </msub>
  <mo stretchy="false">)</mo>
  <mo>&#x2212;<!-- − --></mo>
  <msub>
    <mi>y</mi>
    <mrow class="MJX-TeXAtom-ORD">
      <mo stretchy="false">(</mo>
      <mi>i</mi>
      <mo stretchy="false">)</mo>
    </mrow>
  </msub>
  <msup>
    <mo stretchy="false">)</mo>
    <mn>2</mn>
  </msup>
</math>

&nbsp;

and evaluates to:


<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mfrac>
    <mn>1</mn>
    <mi>M</mi>
  </mfrac>
  <munderover>
    <mo>&#x2211;<!-- ∑ --></mo>
    <mrow class="MJX-TeXAtom-ORD">
      <mi>i</mi>
      <mo>=</mo>
      <mn>1</mn>
    </mrow>
    <mrow class="MJX-TeXAtom-ORD">
      <mi>M</mi>
    </mrow>
  </munderover>
  <mo stretchy="false">(</mo>
  <msub>
    <mi>f</mi>
    <mrow class="MJX-TeXAtom-ORD">
      <mi>w</mi>
      <mo>,</mo>
      <mi>b</mi>
    </mrow>
  </msub>
  <mo stretchy="false">(</mo>
  <msub>
    <mi>x</mi>
    <mrow class="MJX-TeXAtom-ORD">
      <mo stretchy="false">(</mo>
      <mi>i</mi>
      <mo stretchy="false">)</mo>
    </mrow>
  </msub>
  <mo stretchy="false">)</mo>
  <mo>&#x2212;<!-- − --></mo>
  <msub>
    <mi>y</mi>
    <mrow class="MJX-TeXAtom-ORD">
      <mo stretchy="false">(</mo>
      <mi>i</mi>
      <mo stretchy="false">)</mo>
    </mrow>
  </msub>
  <mo stretchy="false">)</mo>
  <mo>&#x2217;<!-- ∗ --></mo>
  <mn>2</mn>
  <msub>
    <mi>x</mi>
    <mrow class="MJX-TeXAtom-ORD">
      <mo stretchy="false">(</mo>
      <mi>i</mi>
      <mo stretchy="false">)</mo>
    </mrow>
  </msub>
</math>


### 2. Bias derivative


The derivative of the loss function with respect to the bias is written as:
&nbsp;



<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mfrac>
    <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
    <mrow>
      <mi mathvariant="normal">&#x2202;<!-- ∂ --></mi>
      <mi>b</mi>
    </mrow>
  </mfrac>
  <mfrac>
    <mn>1</mn>
    <mi>M</mi>
  </mfrac>
  <munderover>
    <mo>&#x2211;<!-- ∑ --></mo>
    <mrow class="MJX-TeXAtom-ORD">
      <mi>i</mi>
      <mo>=</mo>
      <mn>1</mn>
    </mrow>
    <mrow class="MJX-TeXAtom-ORD">
      <mi>M</mi>
    </mrow>
  </munderover>
  <mo stretchy="false">(</mo>
  <msub>
    <mi>f</mi>
    <mrow class="MJX-TeXAtom-ORD">
      <mi>w</mi>
      <mo>,</mo>
      <mi>b</mi>
    </mrow>
  </msub>
  <mo stretchy="false">(</mo>
  <msub>
    <mi>x</mi>
    <mrow class="MJX-TeXAtom-ORD">
      <mo stretchy="false">(</mo>
      <mi>i</mi>
      <mo stretchy="false">)</mo>
    </mrow>
  </msub>
  <mo stretchy="false">)</mo>
  <mo>&#x2212;<!-- − --></mo>
  <msub>
    <mi>y</mi>
    <mrow class="MJX-TeXAtom-ORD">
      <mo stretchy="false">(</mo>
      <mi>i</mi>
      <mo stretchy="false">)</mo>
    </mrow>
  </msub>
  <msup>
    <mo stretchy="false">)</mo>
    <mn>2</mn>
  </msup>
</math>

and evaluates to:


<math xmlns="http://www.w3.org/1998/Math/MathML">
  <mfrac>
    <mn>1</mn>
    <mi>M</mi>
  </mfrac>
  <munderover>
    <mo>&#x2211;<!-- ∑ --></mo>
    <mrow class="MJX-TeXAtom-ORD">
      <mi>i</mi>
      <mo>=</mo>
      <mn>1</mn>
    </mrow>
    <mrow class="MJX-TeXAtom-ORD">
      <mi>M</mi>
    </mrow>
  </munderover>
  <mo stretchy="false">(</mo>
  <msub>
    <mi>f</mi>
    <mrow class="MJX-TeXAtom-ORD">
      <mi>w</mi>
      <mo>,</mo>
      <mi>b</mi>
    </mrow>
  </msub>
  <mo stretchy="false">(</mo>
  <msub>
    <mi>x</mi>
    <mrow class="MJX-TeXAtom-ORD">
      <mo stretchy="false">(</mo>
      <mi>i</mi>
      <mo stretchy="false">)</mo>
    </mrow>
  </msub>
  <mo stretchy="false">)</mo>
  <mo>&#x2212;<!-- − --></mo>
  <msub>
    <mi>y</mi>
    <mrow class="MJX-TeXAtom-ORD">
      <mo stretchy="false">(</mo>
      <mi>i</mi>
      <mo stretchy="false">)</mo>
    </mrow>
  </msub>
  <mo stretchy="false">)</mo>
  <mo>&#x2217;<!-- ∗ --></mo>
  <mn>2</mn>
</math>


&nbsp;


Move a small amount in the direction of the negative slope to get the next weight and bias. For now, we'll arbitrarily define the "small amount" as 0.01 (learniing rate):


<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mstyle mathsize="0.85em">
    <mrow class="MJX-TeXAtom-ORD">
      <mi>N</mi>
      <mi>e</mi>
      <mi>w</mi>
      <mtext>&#xA0;</mtext>
      <mi>w</mi>
      <mi>e</mi>
      <mi>i</mi>
      <mi>g</mi>
      <mi>h</mi>
      <mi>t</mi>
      <mo>=</mo>
      <mi>o</mi>
      <mi>l</mi>
      <mi>d</mi>
      <mtext>&#xA0;</mtext>
      <mi>w</mi>
      <mi>e</mi>
      <mi>i</mi>
      <mi>g</mi>
      <mi>h</mi>
      <mi>t</mi>
      <mo>&#x2212;<!-- − --></mo>
      <mo stretchy="false">(</mo>
      <mi>s</mi>
      <mi>m</mi>
      <mi>a</mi>
      <mi>l</mi>
      <mi>l</mi>
      <mtext>&#xA0;</mtext>
      <mi>a</mi>
      <mi>m</mi>
      <mi>o</mi>
      <mi>u</mi>
      <mi>n</mi>
      <mi>t</mi>
      <mo>&#x2217;<!-- ∗ --></mo>
      <mi>w</mi>
      <mi>e</mi>
      <mi>i</mi>
      <mi>g</mi>
      <mi>h</mi>
      <mi>t</mi>
      <mtext>&#xA0;</mtext>
      <mi>s</mi>
      <mi>l</mi>
      <mi>o</mi>
      <mi>p</mi>
      <mi>e</mi>
      <mo stretchy="false">)</mo>
    </mrow>
  </mstyle>
</math>

&nbsp;

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mstyle mathsize="0.85em">
    <mrow class="MJX-TeXAtom-ORD">
      <mi>N</mi>
      <mi>e</mi>
      <mi>w</mi>
      <mtext>&#xA0;</mtext>
      <mi>b</mi>
      <mi>i</mi>
      <mi>a</mi>
      <mi>s</mi>
      <mo>=</mo>
      <mi>o</mi>
      <mi>l</mi>
      <mi>d</mi>
      <mtext>&#xA0;</mtext>
      <mi>b</mi>
      <mi>i</mi>
      <mi>a</mi>
      <mi>s</mi>
      <mo>&#x2212;<!-- − --></mo>
      <mo stretchy="false">(</mo>
      <mi>s</mi>
      <mi>m</mi>
      <mi>a</mi>
      <mi>l</mi>
      <mi>l</mi>
      <mtext>&#xA0;</mtext>
      <mi>a</mi>
      <mi>m</mi>
      <mi>o</mi>
      <mi>u</mi>
      <mi>n</mi>
      <mi>t</mi>
      <mo>&#x2217;<!-- ∗ --></mo>
      <mi>b</mi>
      <mi>i</mi>
      <mi>a</mi>
      <mi>s</mi>
      <mtext>&#xA0;</mtext>
      <mi>s</mi>
      <mi>l</mi>
      <mi>o</mi>
      <mi>p</mi>
      <mi>e</mi>
      <mo stretchy="false">)</mo>
    </mrow>
  </mstyle>
</math>

&nbsp;

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mstyle mathsize="0.85em">
    <mrow class="MJX-TeXAtom-ORD">
      <mi>N</mi>
      <mi>e</mi>
      <mi>w</mi>
      <mtext>&#xA0;</mtext>
      <mi>w</mi>
      <mi>e</mi>
      <mi>i</mi>
      <mi>g</mi>
      <mi>h</mi>
      <mi>t</mi>
      <mo>=</mo>
      <mn>0</mn>
      <mo>&#x2212;<!-- − --></mo>
      <mo stretchy="false">(</mo>
      <mn>0.01</mn>
      <mo stretchy="false">)</mo>
      <mo>&#x2217;<!-- ∗ --></mo>
      <mo stretchy="false">(</mo>
      <mo>&#x2212;<!-- − --></mo>
      <mn>119.7</mn>
      <mo stretchy="false">)</mo>
    </mrow>
  </mstyle>
</math>

&nbsp;

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mstyle mathsize="0.85em">
    <mrow class="MJX-TeXAtom-ORD">
      <mi>N</mi>
      <mi>e</mi>
      <mi>w</mi>
      <mtext>&#xA0;</mtext>
      <mi>b</mi>
      <mi>i</mi>
      <mi>a</mi>
      <mi>s</mi>
      <mo>=</mo>
      <mn>0</mn>
      <mo>&#x2212;<!-- − --></mo>
      <mo stretchy="false">(</mo>
      <mn>0.01</mn>
      <mo stretchy="false">)</mo><math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mstyle mathsize="0.85em">
    <mrow class="MJX-TeXAtom-ORD">
      <mi>N</mi>
      <mi>e</mi>
      <mi>w</mi>
      <mtext>&#xA0;</mtext>
      <mi>b</mi>
      <mi>i</mi>
      <mi>a</mi>
      <mi>s</mi>
      <mo>=</mo>
      <mn>0.34</mn>
    </mrow>
  </mstyle>
</math>
      <mo>&#x2217;<!-- ∗ --></mo>
      <mo stretchy="false">(</mo>
      <mo>&#x2212;<!-- − --></mo>
      <mn>34.3</mn>
      <mo stretchy="false">)</mo>
    </mrow>
  </mstyle>
</math>

&nbsp;

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mstyle mathsize="0.85em">
    <mrow class="MJX-TeXAtom-ORD">
      <mi>N</mi>
      <mi>e</mi>
      <mi>w</mi>
      <mtext>&#xA0;</mtext>
      <mi>w</mi>
      <mi>e</mi>
      <mi>i</mi>
      <mi>g</mi>
      <mi>h</mi>
      <mi>t</mi>
      <mo>=</mo>
      <mn>1.2</mn>
    </mrow>
  </mstyle>
</math>

&nbsp;

<math xmlns="http://www.w3.org/1998/Math/MathML" display="block">
  <mstyle mathsize="0.85em">
    <mrow class="MJX-TeXAtom-ORD">
      <mi>N</mi>
      <mi>e</mi>
      <mi>w</mi>
      <mtext>&#xA0;</mtext>
      <mi>b</mi>
      <mi>i</mi>
      <mi>a</mi>
      <mi>s</mi>
      <mo>=</mo>
      <mn>0.34</mn>
    </mrow>
  </mstyle>
</math>

&nbsp;

Use the new weight and bias to calculate the loss and repeat. Completing the process for six iterations, we'd get the following weights, biases, and losses:


| Iteration | Weight | Bias | Loss (MSE) |
|-----------|--------|------|-------------|
| 1         | 0      | 0    | 303.71      |
| 2         | 1.2    | 0.34 | 170.67      |
| 3         | 2.75   | 0.59 | 67.3        |
| 4         | 3.17   | 0.72 | 50.63       |
| 5         | 3.47   | 0.82 | 42.1        |
| 6         | 3.68   | 0.9  | 37.74       |


You can see that the loss gets lower with each updated weight and bias. In this example, we stopped after six iterations. In practice, a model trains until it converges. When a model converges, additional iterations don't reduce loss more because gradient descent has found the weights and bias that nearly minimize the loss.

![alt text](https://developers.google.com/static/machine-learning/crash-course/linear-regression/images/convergence.png)
