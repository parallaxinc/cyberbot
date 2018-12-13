
/**
 * Use this file to define custom functions and blocks.
 * Read more at https://makecode.microbit.org/blocks/custom
 */

// Initialize routine - may need to move into a block that the user calls "on startup"
while (pins.digitalReadPin(DigitalPin.P8) == 0);
basic.pause(1)
pins.i2cWriteNumber(83, 0, NumberFormat.UInt8LE, true)
pins.i2cWriteNumber(83, 99, NumberFormat.UInt8LE, false)
basic.pause(10)
pins.digitalWritePin(DigitalPin.P8, 1)
basic.pause(10)



enum MyEnum {
    //% block="one"
    One,
    //% block="two"
    Two
}

enum pinReadType {
    //% block="qti sensors"
    qti,
    //% block="digital states"
    states,
    //% block="digital directions"
    directions
}

enum pinSetType {
    //% block="states"
    states,
    //% block="directions"
    directions
}

enum botPin {
    //% block="P0"
    P0,
    //% block="P1"
    P1,
    //% block="P2"
    P2,
    //% block="P3"
    P3,
    //% block="P4"
    P4,
    //% block="P5"
    P5,
    //% block="P6"
    P6,
    //% block="P7"
    P7,
    //% block="P8"
    P8,
    //% block="P9"
    P9,
    //% block="P10"
    P10,
    //% block="P11"
    P11,
    //% block="P12"
    P12,
    //% block="P13"
    P13,
    //% block="P14"
    P14,
    //% block="P15"
    P15,
    //% block="P16"
    P16,
    //% block="P17"
    P17,
    //% block="P18"
    P18,
    //% block="P19"
    P19,
    //% block="P20"
    P20,
    //% block="P21"
    P21,
    //% block="P22"
    P22
}

/**
 * Cyberbot blocks
 */
//% weight=100 color=#1a26ce icon="\uf085"
namespace cyberbot {
    export function sendCommand(pin1: number, cmd: number, pin2: number, states: number, arg1: number, arg2: number) {
        let outStop0 = true
        let outStop1 = true
        if (!arg1 && !arg2) { outStop0 = false }
        if (arg1 && !arg2) { outStop1 = false }
        pins.i2cWriteNumber(83, 1, NumberFormat.UInt8LE, true)
        pins.i2cWriteNumber(83, pin1, NumberFormat.UInt8LE, true)
        pins.i2cWriteNumber(83, pin2 || 0, NumberFormat.UInt8LE, true)
        pins.i2cWriteNumber(83, states || 0, NumberFormat.UInt8LE, outStop0)
        if (arg1) {
            pins.i2cWriteNumber(83, arg1, NumberFormat.UInt32LE, outStop1)
        }
        if (arg2) {
            pins.i2cWriteNumber(83, arg2, NumberFormat.UInt32LE, false)
        }
        pins.i2cWriteNumber(83, 0, NumberFormat.UInt8LE, true)
        pins.i2cWriteNumber(83, cmd, NumberFormat.UInt8LE, false)
        cmd = 1
        while (cmd != 0) {
            pins.i2cWriteNumber(83, 0, NumberFormat.UInt8LE, true)
            cmd = pins.i2cReadNumber(83, NumberFormat.UInt8LE, false)
        }
    }

    /**
     * Set a pin to output 0 (low), 1 (high), or 2 (toggle)
     * @param p pin
     * @param s what state to set the pin to
     */
    //% block
    //% s.min=0 s.max=2
    export function digitalWrite(p: botPin, s: number): void {
        if (s < 0 || s > 1) { s = 4 }
        if (s == 0) { s = 2 }
        sendCommand(p, s, 0, 0, null, null)
    }

    /**
     * Set a pin to output an analog voltage (using PWM)
     * @param p pin
     * @param value to set PWM duty cycle to (from 0 - 0% to 1023 - 100%)
     */
    //% block
    export function analogWrite(p: botPin, value: number): void {
        if (value < 0) value = 0;
        if (value > 1023) value = 1023;
        sendCommand(p, 32, 0, 0, value, null)
    }

    /**
     * Read the digital state of a pin
     * @param p pin
     * @returns 0 (low) or 1 (high)
     */
    //% block
    export function digitalRead(p: botPin): number {
        sendCommand(p, 3, 0, 0, null, null)
        pins.i2cWriteNumber(83, 24, NumberFormat.UInt8LE, true)
        return pins.i2cReadNumber(83, NumberFormat.Int32LE, false)
    }

    /**
     * Read the digital states of a group of pins
     * @param startPin starting pin
     * @param numberOfPins [2-8] number of pins, eg: 4
     */
    //% block="read $action from $p2 pins starting at $startPin"
    //% numberOfPins.min=2 numberOfPins.max=8
    export function readDigitalStates(action: pinReadType, startPin: botPin, numberOfPins: number = 4): number {
        let a = 33;  // qti
        switch (action) {
            case pinReadType.states: a = 8;  // states
            case pinReadType.directions: a = 6;  // directions
        }
        sendCommand(numberOfPins + startPin - 1, a, startPin, 0, null, null)
        pins.i2cWriteNumber(83, 24, NumberFormat.UInt8LE, true)
        return pins.i2cReadNumber(83, NumberFormat.Int32LE, false)
    }

    /**
     * Set the digital states of a group of pins
     * @param action 
     * @param startPin starting pin
     * @param numberOfPins [2-8] number of pins, eg: 4
     * @param states binary value to set pins to
     */
    //% block="write digital $action to $numberOfPins pins|starting at $startPin|using $sts"
    //% inlineInputMode=inline
    //% numberOfPins.min=2 numberOfPins.max=8
    export function writeDigitalStates(action: pinSetType, startPin: botPin, numberOfPins: number = 4, sts: number): void {
        sendCommand(numberOfPins + startPin - 1, (action == pinSetType.states ? 7 : 5), startPin, sts, null, null)
    }

}
