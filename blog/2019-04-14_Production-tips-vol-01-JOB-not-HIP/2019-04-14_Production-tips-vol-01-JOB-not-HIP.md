Welcome to what I hope will be a fortnightly post of tips and tricks that I've 
accumulated and picked up over the years. Some of them may be simple and obvious, 
others hopefully not but if its of any use at all to someone then it's been 
worth writing!

Starting small this week, it's something that I've seen overlooked many times but is crucial to working efficiently in Houdini: $JOB.

#### Production Tips Vol.01: $JOB not $HIP

The short answer is so that you aren't relying on all your paths being created 
from where the hip file is. If it were to moved for some reason or taken from 
one project to another, it could break all your pathing. This might be fine for 
a single scene file job, but once you start to have multiple scene files you 
will need a to leverage $JOB.

With $HIP being the default it's easy to just keep using it but taking a few 
mins to set up $JOB will make your life much easier and ensure paths play nicely.

The best way to quickly set it up is to use the [project feature][1], it's nice 
and simple to use and for most solo users is ideal. The documentation on it 
is very clear and well written. Larger facilities will no doubt have their own 
automatic sourcing scripts to set $JOB.

It's a small tip and I imagine a lot of users are already doing this, but it's 
one of those features that if you haven't been using it then it has the 
potential to be a massive time and efficiency boost!

/Carlo

[1]:https://www.sidefx.com/docs/houdini/basics/project
