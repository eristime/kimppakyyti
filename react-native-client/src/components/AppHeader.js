import React, { Component } from "react";
import { View, TextInput } from "react-native";
import {
  Button,
  Content,
  Container,
  DatePicker,
  Icon,
  Input,
  Item,
  Label,
  Header,
  Text
} from "native-base";


class AppHeader extends Component {

  constructor(props) {
    super(props);
    this.state = {
      destination: '',
      departure: '',
      chosenDate: new Date()
    };
    this.setDate = this.setDate.bind(this);
  }

  setDate(newDate) {
    this.setState({ chosenDate: newDate });
  }

  render() {

    return (

      <Header style={{ height: 150 }}>
        <Content>
          <View style={{ flex: 1, marginLeft: 10, marginTop: 10, flexDirection: 'row', justifyContent: 'center' }}>

            <View >

              <Item fixedLabel
                style={{ width: 270, height: 35, borderRadius: 5, marginTop: 5, backgroundColor: 'white' }}>
                <Label>From</Label>
                <Input placeholder='Set departure' />
              </Item>

              <Item fixedLabel
                style={{ width: 270, height: 35, borderRadius: 5, marginTop: 5, backgroundColor: 'white' }}>
                <Label>To</Label>
                <Input placeholder='Set destination' />
              </Item>
            </View>


            <View style={{ justifyContent: 'center'}}>
              <Button iconLeft transparent dark >
                <Icon name='swap' />
              </Button>
            </View>

          </View>
          
          <View style={{marginLeft:10, flexDirection:'row', justifyContent:'flex-start'}}>
            <Label>When</Label>
            <DatePicker
            defaultDate={new Date(2018, 4, 4)}
            minimumDate={new Date(2018, 1, 1)}
            maximumDate={new Date(2018, 12, 31)}
            locale={"en"}
            timeZoneOffsetInMinutes={undefined}
            modalTransparent={false}
            animationType={"fade"}
            androidMode={"default"}
            placeHolderText="Date"
            textStyle={{ color: "white" }}
            placeHolderTextStyle={{ color: "#d3d3d3" }}
            onDateChange={(date) => this.setDate(date)}
          />

            <Button iconLeft transparent dark >
                <Icon name='more' />
            </Button>
          </View>
          
          
        </Content>

      </Header>

    );
  }
}

{/* TODO: contruct a stylesheet

  const styles = StyleSheet.create({
  destination: {
    flex: 1,
    backgroundColor: '#fff',
    paddingTop: 100,
    paddingHorizontal: 30
  },
  row: {
    marginBottom: 20,
  },
  columns: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'flex-start',
  },
  field: {
    marginRight: 10,
  },
  ageField: {
    width: 60,
  },
  button: {
    width: 80,
    marginTop: 15,
  },
  error: {
    marginTop: 10,
  },
  errorMsg: {
    color: 'red'
  }
})

*/}


export default AppHeader;
