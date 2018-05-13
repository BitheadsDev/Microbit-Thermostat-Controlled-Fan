# Microbit Thermostat Controlled Fan

## Aims of the app

To control a fan once the Micro:bit temperature sensor is above a user selected temperature

## View Videos

* Part one – showing the fan in action: https://www.youtube.com/watch?v=0b-i0Yfr5sA
* Part two – showing how to construct the circuit: https://www.youtube.com/watch?v=7HUZakzsjN4

## View the circuit

There is a png and a Fritz file included in this repo that illutrates how the circuit was put together.

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
        increment (+=1) fanOnTemp by 1
    else if A was pressed:
        decrement (-=1) fanOnTemp by 1

    if no buttons have been pressed for 2000 seconds:
        Call: fan

fan:
    if temperature >= fanOnTemp:
        if temperature >= fanOnTemp:
            Supply on signal to pin0 x/5 max value amount of times (this is pulse width modulation as the pin is either on or off)
            Light up the LEDs 3 rows from the bottom to represent x/5 power
    if B was pressed:
        increment (+=1) fanOnTemp by 1
    else if A was pressed:
        decrement (-=1) fanOnTemp by 1
    else:
        while pin2 is touched:
            Increment FanSpeed up to 5 and then cycle to 1
            Show x/5 rows of LEDs lit up from the bottom
```

## Possible extensions

* Hooking up an external thermostat to get a more accurate temperature reading.
* Alternatively, use two or more Microbits to communicate through the radio function their temperatures and get an average temperature over an area.
