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

export default AppHeader;
