# Microbit Thermostat Controlled Fan

## Aims of the app

To control a fan once the Micro:bit temperature sensor is above a user selected temperature

## Details and controls

* The user can select the temperature that the fan will be active above by using the Micro:bit buttons
* The user will be able to control the fan speed by tilting the device

## Things you need

* A Micro:bit
* A USB lead
* A computer to copy and write the code
* Kittronik Inventor's Kit for BBC Microbit, specifically:
  * 1 x breakboard
  * 1 x breakout board
  * 1 x transistor
  * 1 x 2.2Ω resistor
  * 1 x Terminal connector
  * 1 x motor
  * 3 x male to female jumper wire
  * 1 x fan blade

## Things you should learn

* How to create a multi-stage application that passes data from one stage to another
* Using buttons and gestures to control an external device
* How to use the output pins to power an external device
* Creating a circuit that uses a transitor to amplify current
* Build understanding of pulse width modulation

## Initial pseudocode runthrough

```
setTemp:
    if B was pressed:
        increment (+=1) fanOnTemp by 1 up to 30
    else if A was pressed:
        decrement (-=1) fanOnTemp by 1 down to 5 degrees

    if no buttons have been pressed for 3000 seconds:
        Call: fan

fan:
    if temperature >= fanOnTemp:
        if start:
            Supply power 50% of the time to a pin (this is pulse width modulation as the pin is either on or off rather than supplying 50% power)

            Light up half the LEDs left to right top to bottom (rounding down) to represent half power
        else if B was pressed:
            increment (+=1) fanOnTemp by 1 up to 30
        else if A was pressed:
            decrement (-=1) fanOnTemp by 1 down to 5 degrees
        else if tilt right:
            Increment supplied power to pin to increase fan speed up to power 100% of the time
            show more lights

            Increase amount of lit LEDs up until all 25 LEDs represents 100% powered
        elseif tilt left:
            decrement supplied power to pin to decrease fan speed down to 0

            Decrease amount of lit LEDs until 0 LEDs represents 0% powered
```
