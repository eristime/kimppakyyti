import { AsyncStorage } from 'react-native';

const deviceStorage = {
     saveItem: async (key, value) => {
      try {
        await AsyncStorage.setItem(key, value);
      } catch (error) {
        console.log('AsyncStorage Error: ' + error.message);
      }
    },


    loadToken: async () => {
        try {
            return await AsyncStorage.getItem('token');
          //if (value !== null) {
          //  this.setState({
          //    token: value,
          //    loading: false
          //  });
          //} else {
          //  this.setState({
          //    loading: false
          //  });
          //}
        } catch (error) {
          console.log('AsyncStorage Error: ' + error.message);
        }
      },

      deleteToken: async () => {
        try {
          await AsyncStorage.removeItem('token');
          //.then(
          //  () => {
          //    this.setState({
          //      token: ''
          //    })
          //  }
          //);
        } catch (error) {
          console.log('AsyncStorage Error: ' + error.message);
        }
      }
    
  };

export default deviceStorage;