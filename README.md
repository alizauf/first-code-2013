This is the first coding project I ever did, back in 2013. 

It was in support of a problem I needed to solve as Product Director at Flocabulary. 

Here's the gist of the problem:

Flocabulary has hundred of educational rap videos. Along with the videos, we include interactive lyrics. When students click on the lyrics, boxes with relevant further reading and images pop out. At the time, we had several thousand images within these further reading boxes. And we had diligently maintained appropriate Creative Commons attribution, per the recommended formatting: https://wiki.creativecommons.org/wiki/Best_practices_for_attribution

BUT! We had included all of the credits on a single page labeled credits, which you can see here thanks to the Wayback Machine: https://web.archive.org/web/20130816035548/http://www.flocabulary.com/credits/

It was becoming an unreadable mess, a big unruly blob of HTML that kept breaking when our noble, attributing interns would miss a ">", and above all, someone looking for a credit for an image wouldn't reasonably be able to find it on that page. 

We decided to move image credits to each video page, so that they were on the same page as the images themselves. 

Because it seemed like a terrible, manual task to divide up the thousands of credits we had, I decided to try my hand at writing a python script to parse the big blob of HTML and append the video page ID to the relevant credit, so we could store each video's credits along with the video. 

We had included the video name in the HTML CC credit. So I looked for a name in the credit string and then looked that name up in a separate file that had video names and video IDs. In doing so, I was able to sort the credits into their relevant video. Then, because it would be silly to have the name of the video on the credit when it appeared on the video page, I removed that. 

It worked! You can see an example of where the credits live now: You can see an example on the bottom right here: https://www.flocabulary.com/10-the-date/

If I were to do this now, rather than just create a new sorted blob of HTML, I would have extracted the data from the HTML to create a more structured credits table. 



