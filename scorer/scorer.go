package main

import "C"
import (
	"unsafe"
	"strconv"
	"time"
)

//export SleepEfficiency
func SleepEfficiency(cstrs **C.char) int {
	
	// [PSQI4, PSQI1, PSQI3]
	var responses []string
	slice := unsafe.Slice(cstrs, 1<<30)

	for i := 0; slice[i] != nil; i++ {
		responses = append(responses, C.GoString(slice[i]))
	}

	hoursSlept, _ := strconv.Atoi(responses[0])
	bedTime, _ := strconv.Atoi(responses[1])
	wakeTime, _ := strconv.Atoi(responses[2])

	PSQI3 := responses[2] + "h"
	PSQI1 := responses[1] + "h"
	
	var sleepDay int = 1
	var wakeUpDay int = 2

	if bedTime <= wakeTime {
		sleepDay = 2
	}

	wakeUp, err := time.ParseDuration(PSQI3)

	if err != nil {
		return 0
	}

	lieDown, err := time.ParseDuration(PSQI1)

	if err != nil {
		return 0
	}

	start := time.Date(2024, time.January, sleepDay, int(lieDown.Hours()), 0, 0, 0, time.UTC)

	end := time.Date(2024, time.January, wakeUpDay, int(wakeUp.Hours()), 0, 0, 0, time.UTC)

	hoursInBed := end.Sub(start)

	var efficiency float64 = float64(hoursSlept) / hoursInBed.Hours() * float64(100)

	var score int

	if efficiency >= 85.0 {
		score = 0
	} else if efficiency >= 75.0 {
		score = 1
	} else if efficiency >= 65.0 {
		score = 2
	} else {
		score = 3
	}

	return score
}

func main() {}