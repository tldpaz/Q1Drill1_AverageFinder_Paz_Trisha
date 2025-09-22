from js import document

# This class handles the average computation for two scores.
class AverageFinder:
    def __init__(self):
        # Initialize input and output element IDs
        self.input1_id = "score1"  # str: ID for first input
        self.input2_id = "score2"  # str: ID for second input
        self.result_id = "result"  # str: ID for result display

    # This function retrieves input values, computes the average, and displays the result.
    def compute_average(self):
        s1 = document.getElementById(self.input1_id).value  # str: value from input field 1
        s2 = document.getElementById(self.input2_id).value  # str: value from input field 2

        # Convert input values to floats and validate
        try:
            num1 = float(s1)  # float: first quiz score
            num2 = float(s2)  # float: second quiz score
            if not (0 <= num1 <= 100 and 0 <= num2 <= 100):  # check if scores are in range
                document.getElementById(self.result_id).innerHTML = "Please enter scores between 0 and 100."  # display error
                return
        except ValueError:  # handles invalid input conversion
            document.getElementById(self.result_id).innerHTML = "Please enter valid numbers."  # display error
            return

        avg = (num1 + num2) / 2  # float: average of the two scores
        if avg >= 75:  # check if average is passing
            message = f"Average: {avg:.2f} <br>✅ Passed"  # str: passing message
        else:
            message = f"Average: {avg:.2f} <br>❌ Failed"  # str: failing message
        document.getElementById(self.result_id).innerHTML = message  # display result

# Create an instance to be used by PyScript
average_finder = AverageFinder()

def compute_average(*args, **kwargs):
    s1 = document.getElementById("score1").value
    s2 = document.getElementById("score2").value

    try:
        num1 = float(s1)
        num2 = float(s2)
        if not (0 <= num1 <= 100 and 0 <= num2 <= 100):
            document.getElementById("result").innerHTML = "Please enter scores between 0 and 100."
            return
    except ValueError:
        document.getElementById("result").innerHTML = "Please enter valid numbers."
        return

    avg = (num1 + num2) / 2
    if avg >= 75:
        message = f"Average: {avg:.2f} <br>✅ Passed"
    else:
        message = f"Average: {avg:.2f} <br>❌ Failed"
    document.getElementById("result").innerHTML = message

import js
js.window.compute_average = compute_average