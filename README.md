# #Terminal-System-Monitor



***What even is this?***

> This is a terminal system monitor like btop or htop, but a much simpler version. It shows custom ASCII art, CPU usage, RAM usage, and a stopwatch to track time (like how long you have been coding). You can use this in your terminal to display your own ASCII art, check your system stats, and use the timer. You can also use this code as a skeleton to build your own custom terminal system monitor.



***Built with :-***

1. Python and tcss (language)

2. Textual (Framework for UI/CSS in terminal)

3. Psutil (Library to get hardware info)

   

***Images :-***

![Image1](/home/dixit/system-monitor/images/ss1.png)

![Image2](/home/dixit/system-monitor/images/ss2.png)



***How you can contribute(if you want to of-course) :-***

You can contribute in this by adding your own widgets that you feel are useful and cool like ascii art/animation etc. Feel free to do anything that you would like (free will if you believe in it).



***Deployment :-***

Just Clone It (you know the deal)

Once cloned, run these quick commands to get it going: 

```bash
python -m venv venv
source venv/bin/activate
pip install textual psutil
python dashboard.py
