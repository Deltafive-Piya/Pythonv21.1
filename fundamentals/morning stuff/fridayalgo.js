




function zipArraysIntoMap(keys, values) {
    // if the length of keys is not equal to length of values: return false. 
      if(keys.length < values.length){
        return false
      }
    //   create empty object
      let obj = {};
    // 
      for(let i = 0; i < keys.length; i++){
        if(values[i]){
            obj[keys[i]] = values[i];
        }else {
            obj[keys[i]] = undefined;
        }
    }
    return obj
  }
console.log(zipArraysIntoMap(keys1,vals1))
console.log(zipArraysIntoMap(keys2,vals2))
console.log(zipArraysIntoMap(keys3,vals3))
console.log(zipArraysIntoMap(keys4,vals4))