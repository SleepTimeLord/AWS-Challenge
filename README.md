# Badge Cloning Detection

A repeatable pandas-based method for detecting potential badge cloning by
finding users who appear at two different locations too close together in
time to be physically possible ("impossible traveler" detection).

Built for the [AWS Security Career Pathway Activity](https://github.com/amzn/AWSSecurityCareerPathwayActivityRust).

## Plan of Action

1. **Get each user's locations and times.** Group the access logs by user
   and sort each user's events chronologically.
2. **Determine the time between 2 unique locations.** For each user, compare
   consecutive events at *different* locations and calculate the time gap.
3. **Flag impossible travel.** If the time between locations is less than
   **4 [UNIT]**, log the user as having a potentially cloned badge.

## Why This Works

A real person can't badge into two different places within seconds of each
other. If the same badge shows up in two places faster than anyone could
travel between them, it's a strong sign that someone has a copy.
