export const convertDateForAPI = (dateObject) => {
    /*
    param:date, JS date object
    */
    // getMonth() returns month from 0 to 11
    let month = (dateObject.getMonth() + 1).toString();
    let date = (dateObject.getDate()).toString();
    if (month.length < 2) {
      month = '0' + month;
    }
    if (date.length < 2) {
      date = '0' + date;
    }
    return `${dateObject.getFullYear()}-${month}-${date}`;
  };

  export const convertToHoursMinutes = (dateObject) => {
    /*
    param:date, JS date object
    */
   //returns formatted time

    return `${dateObject.getHours()}:${dateObject.getMinutes()}`;
  };
