# Adversarial Attacks against Fake News Detection Models  

This project was done during my semester-long visit at the [University of Wisconsin-Madison](https://www.wisc.edu/).  

Cooperated with [Justin Hsu](https://justinh.su/), Huankang Guan and [Meghana Moorthy Bhat](https://meghu2791.github.io/).  

Our initial work will show up in [ICAART 2019](http://www.icaart.org/?y=2019)!  

Citation:  

`Zhixuan Zhou, Huankang Guan, Meghana Moorthy Bhat, and Justin Hsu, "Fake News Detection via NLP is Vulnerable to Adversarial Attacks," in 11th International Conference on Agents and Artificial Intelligence (ICAART), 2019.`  

or:  

`Zhixuan Zhou, Huankang Guan, Meghana Moorthy Bhat, and Justin Hsu, "Fake News Detection via NLP is Vulnerable to Adversarial Attacks," arXiv, 2019.`

## Abstract of the paper  

News plays a significant role in shaping people’s beliefs and opinions. Fake news has always been a problem,
which wasn’t exposed to the mass public until the past election cycle for the 45th President of the United
States. While quite a few detection methods have been proposed to combat fake news since 2015, they focus
mainly on linguistic aspects of an article without any fact-checking. In this position paper, we argue that these
models have the potential to misclassify fact-tampering fake news as well as under-written real news. Through
experiments on Fakebox, a state-of-the-art fake news detector, we show that fact tampering attacks can be
effective. To address these weaknesses, we argue that fact checking should be adopted in conjunction with
linguistic characteristics analysis, so as to truly separate fake news from real news.  

Full paper [here](https://arxiv.org/abs/1901.09657)  

## AutoWeb  

Automatically feed articles to Fakebox and store labels back to csv. file.  

Require Python3 to run urllib.  

Run Main.py directly and output.csv will be written. If it doesn't work on Windows, perhaps it's because you don't have authority for writing files. Re-install Python or turn to Linux.
