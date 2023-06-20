# Testing

## Index

 * [Error resolution and Debugging](#error-resolution-and-debugging)
 * [Manual testing](#manual-testing)
 * [Code Institue Linter testing](#code-institue-linter-testing)
 
  ## Error Resolution and Debugging 
1. Whilst not a problem that had occured from myself, it is worth noting that Gitpod had a authentication issue and meant I was unable to push saved work up to GitHub, this may result in some uncongruent and messy commit messages, see attached email for verification ![Gitpod auth error](../documentation/error_resolution_pics/Gitpod_authentication_error.png "Gitpod auth error picture")

2. It took me a couple of goes with the ascII art to realise that I have to break it down into three different print statements to show the images as I wanted them.

3. I was havin trouble with adding the username to the scorebaord as passing through two seperate variables became a problem, so thanks to the mentors at Code Institue I changed to to an array ffirst and passed that through into the update_score function. 

4. After trying to consitently debug my programe for various reasons / testing the flow of the game itself, I realsied that I was having to use print statements all the time but didn't want it to remain in my permenant code. So I figured out how to add a --debug statement into my code so I could use it when I was testing and not worry about it ruining the end game. I used this helpful article to implement it from [OpenSorce](https://opensourceoptions.com/blog/how-to-pass-arguments-to-a-python-script-from-the-command-line/#:~:text=In%20Python%2C%20arguments%20are%20passed,used%20to%20parse%20named%20arguments)

## Code Institue Linter Testing 

After building the main bulk of my code I started chekcing for errors within the CI Linter. See Below:
1. Run.py 

2. Utility.py


