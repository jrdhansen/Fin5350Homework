Jared Hansen <br>
A01439768 <br>
Finance 5350, Dr. Brough <br>
Fall 2017 <br>

## What Should Computational Economists Do?


Before diving headfirst into the argument of the role of a computational economist,
we must address the foundation upon which this discussion will be based: namely, a definition
of what economics is. Then we may proceed into discussing what the role of an economist is,
and what part computation plays in that role.


As a necessary (but inherently cowardly) caveat, I must admit that I am very unlearned
when it comes to formal economic and financial theory. As such, I will be approaching the topic
with a fair amount of naïveté, and with the biased eyes and training of a computational
statistician. Prior to this course, the full extent of my formal education in economics consisted
of a basic macroeconomics course. One of the few things I remember from the class was a definition
the professor gave of what economics is. To paraphrase him: “Economics is the study of how people
allocate scarce resources and respond to incentives.” In reading Buchanan’s "What Should Economists
Do?", though, I came across a passage that completely contradicts this definition: “Economists
should concentrate their attention on a particular form of human activity, and upon the various
institutional arrangements that arise as a result of this form of activity. Man’s behavior in the
market relationship, reflecting the propensity to truck and to barter, and the manifold variations
in structure that this relationship can take; these are the proper subjects for the economist’s
study.” (Buchanan, 214)  Buchanan goes on to refute that economics should be a study of allocation
of scarce resources and decision-making, but should focus on the study of markets.


For the remainder of this discussion we’ll rely on this determination of what economics is.
From this we can say that an economist is one whose role is to study markets: their creation,
behavior, regulation, and all other aspects. However, what role should computation play in this study?
To paraphrase Buchanan, economists that use mathematical modeling as their primary tool essentially
throw to the side the most crucial component of economics; the decision-making process of entities
within a market (Buchanan, 217). While there is no doubt that the decision-making process is truly the
driver of economics, I don’t believe that it is what economists should be studying. If that is the
case, then neuroscientists are the true economists since they examine the physical processes that
occur in our brains when we make choices. No, I think that economics ought to remain similar to how it
is now, studying markets using the tools of modeling. The modeling itself, though, is where I think that
economists have a significant amount of room for improvement. 


It is fairly safe to say that most people with any amount of exposure to economics would consider
it a science since it is studied using the scientific method. Systematic observation, measurement,
experiments, and the formulation, testing, and modification of hypotheses are all inherent to economic
studies. The thing that I believe that Buchanan takes issue with is that the assumptions that discard the
human part of economics result in hypotheses that aren’t completely accurate since they’re not taking into
account all available information. While I can agree on the fact that assumptions made by some economic
models are inane and unreasonable, I don’t think that discarding modeling entirely should be the answer.
If we are operating under the premise that modeling doesn’t belong in economics because it results in less
than 100% accurate analysis, then almost all of “science as we know it” would be rendered irrelevant.
Except for certain areas of mathematics, there is no such thing as a completely precise science, and even
mathematics relies on the assumptions of the truthfulness of certain basic axioms. Physics, one of the
best-understood and most exacting branches of science, is not completely precise; there are entire courses
devoted to the study of error analysis in physics. Rather than throw away modeling from the economist’s
toolbox, what needs to happen is a more rigorous, through approach to modeling. Computational power is one
of the most valuable things economists have at their disposal. Although imperfect, holistic modeling is by
far the best way we have to study markets and their qualities, as studying the neurochemical processes in
the brains of each individual involved in some market would be ideal but impossible. Due to the fact that
we could arguably tie the decisions of any human on the earth to the market being studied, this would
require both information we can’t procure, as well as computational power not yet available to us. The
problem lies not in modeling itself, but in the assumptions that are made in order to utilize a certain kind
of model.


My suggestion on how to progress in the right direction is to move toward machine learning algorithms.
A simple maxim on which to base this migration would be a quote from the great John Tukey: “Far better an
approximate answer to the right question, which is often vague, than an exact answer to the wrong question,
which can always be made precise. Data analysis must progress by approximate answers, at best, since its
knowledge of what the problem really is will at best be approximate.” (Tukey, 13)  By trying to answer the
wrong questions precisely, economics has become a science that often doesn’t produce viable results.
Statisticians are as much to blame for the ridiculous assumptions of some models as economists are. If the
mathematical validity of a model can be “proven” then it is automatically given more credibility. This
fallacious thinking has been perpetuated by statisticians, and adopted by economists, for decades. I’m of the
belief that predictive accuracy should trump mathematical provability when it comes to modeling. After all,
is the point to obtain more correct predictions, or to be able to justify one’s model on the basis of
mathematical construction? Although many machine learning algorithms are more or a less a “black box” into
which it can be difficult to see, this should not matter. If the chief goal of a model is to achieve the
highest possible predictive accuracy, then the means by which we arrive there don’t matter so long as they’re
reproducible.


Another one of the most beautiful things that machine learning does in this case is that it allows us
to throw asinine assumptions out the window. Leo Breiman, the father of the random forests algorithm, made a
telling comment on this topic. “With data gathered from uncontrolled observations on complex systems involving
unknown physical, chemical, or biological mechanisms, the a priori assumption that nature would generate the
data through a parametric model selected by the statistician can result in questionable conclusions that cannot
be substantiated by appeal to goodness-of-fit tests and residual analysis.” (Breiman, 204)  If economists are
to rely upon statistical and mathematical modeling in their work, they ought to rely on machine learning
algorithms. They don’t necessitate any unreasonable assumptions, and they provide more accurate results in
almost any circumstance.


A personal insight I can provide on this topic has to do with survival analysis. (Although, my research
is specifically on survival analysis in biomedical studies, the same principle can be applied to duration
analysis in economic studies.) In my research, I’ve been examining whether an algorithm known as random survival
forests (RSF) outperforms the tried-and-true Cox Proportional Hazards (CPH) model when it comes to predicting
the survival times of patients. Here, the obvious flaw is that the CPH model is only valid to use when the
proportional hazards assumption is satisfied (survival curves must be quantifiably similar in shape for men
versus women, or for other categorical variables within the data). On the other hand, RSF relies upon no such
assumption. It probably comes as no surprise that the RSF algorithm beats the CPH model when examining data that
do not meet the proportional hazards assumption. However, even when the data comfortably satisfy the proportional
hazards assumption, RSF continues to beat CPH handily! This is one example among many as to why machine learning
algorithms are the way of the future when it comes to data analysis.


Computation is not just necessary in the role of an economist, it is essential. In approaching the study
of enormous quantities of market data scientifically, mathematical and statistical modeling is by far the best
resource available for an economist. What needs to change are the models being used and their underlying
assumptions. Economists must first stomach that the predictive accuracy and reproducible results of machine
learning are more important and valuable than the mathematical justification of older models. Once they do so,
economics will experience significant growth as an academic discipline, companies will make better decisions and
higher profits, and the vast amounts of data available to the world will no longer be relegated to analysis by
ill-suited, antiquated methods, leading to an age of predictive power that will forever advance the human race.







### Works Cited


- Breiman, Leo. "Statistical modeling: The two cultures (with comments and a rejoinder by the author)."
	Statistical science16.3 (2001): 199-231.

- Buchanan, James M. "What should economists do?." Southern Economic Journal (1964): 213-222.

- Tukey, John W. "The future of data analysis." The annals of mathematical statistics 33.1 (1962): 1-67.
