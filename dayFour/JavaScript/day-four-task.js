function sumOfTwoNumbers(array, number){
    let newArray = [];
    let count = 0;

    for(let index = 0; index < array.length; index++){
        for(count = 0; count < array.length; count++){
            if(array[index] + array[count] == number){
                newArray[0] = array[index];
                newArray[1] = array[count];
                break;
            }
        }
        if(newArray[0] == array[index] && newArray[1] == array[count]){
            break;
        }
    }

    return newArray;

}

function rangeBetweenLargestAndSmallestNumbers(array){
    let largest = array[0];

    for(let index = 1; index < array.length; index++){
        if(array[index] > largest){
            largest = array[index];
        }
    }
    let smallest = array[0];

    for(let index = 1; index < array.length; index++){
        if(array[index] < smallest){
            smallest = array[index];
        }
    }

    let range = [];

    for(let index = 0; index < (largest-smallest) + 1; index++){
        range[index] = index;
    }



    for(let index = 0; index < range.length; index++){
        range[index] = smallest;
        smallest++;
    }

    return range;
}

//console.log(sumOfTwoNumbers([8, 6, 12, 4, -2], 6))
//console.log(rangeBetweenLargestAndSmallestNumbers([14, 9, 6, 5, 8, 10]))

module.exports = { sumOfTwoNumbers, rangeBetweenLargestAndSmallestNumbers }
