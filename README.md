# Alarm++


## Inspiration
Mornings are always a struggle. Traditional alarms might wake you up for a moment, but it's too easy to shut them off and go back to bed. We wanted a solution that forces the user to fully wake up before the alarm turns off.

## What it does
Like any other alarm, Alarm++ allows users to set alarms at any date and time. However, what sets Alarm++ apart from the competition is its defining feature: jumping jack detection. Users choose anywhere from 5-25 jumping jacks as Alarm++'s "off button." When the time comes, an alarm repeats and doesn't turn off until the user performs the required amount of jumping jacks in front of their camera.

## How we built it
Alarm++ uses a trained, deep-learning neural network and OpenCV to detect people in the camera. The neural network then estimates the pose of the person and calculates a skeletal system of joint to represent the positions and orientations of the person's limbs. Using this data, Alarm++ is able to determine if the person on the camera is performing jumping jacks and keeps track of how many jumping jacks the user has completed. 

## Challenges we ran into
The main challenge for Alarm++ was the weakness of our computers and the complicated nature of our neural network usage. It took us many hours to finish our pose estimation system, and once we did we found that the rate at which poses could be estimated was suboptimal because our laptops are not powerful enough to process the videos quickly. In addition, the sun and the low quality webcams made our images come out poorly.

## Accomplishments that we're proud of
Our system involves neural networks and and multithreading to achieve our body-tracking alarm. This system was certainly the hardest to implement and our greatest achievement today.

## What we learned
Today, we learned a lot about the relationships between training, neural networks, and OpenCV. We also learned about universal GUI programming. 

## What's next for Alarm++
An Android or iOS app that syncs with the computer to play the alarms and detect jumping jacks, along with the optimization of our pose estimation system. With a better pose estimation system, we could include new exercises, such as pushups and burpees.
