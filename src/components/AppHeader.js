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
      origin: 'From'
    };
  }

  render() {

    return (

      <Header style={{ height: 150 }}>
        <Content>
          <View style={{ flex: 1, marginLeft: 10, marginTop:10, flexDirection: 'row', justifyContent: 'center' }}>

            <View style={{}}>

              {/*
  <TextInput
    style={{ height: 40, borderColor: 'gray', borderWidth: 1, borderRadius: 10, backgroundColor: 'white' }}
    onChangeText={(origin) => this.setState({ origin })}
    value={this.state.origin}
  />
  */}


              <Item fixedLabel
                style={{width: 240, height:40, borderRadius: 5, marginTop:5, backgroundColor:'white'}}>
                <Label>From</Label>
                <Input placeholder='Set departure' />
              </Item>

              <Item fixedLabel
                style={{width: 240, height:40, borderRadius: 5, marginTop:5, backgroundColor:'white'}}>
                <Label>To</Label>
                <Input placeholder='Set destination' />
              </Item>
            </View>



            {/*TODO: make icon button
            <View style={{ justifyContent: 'center', marginLeft: 10 }}>
              <Icon name='swap' />
            </View>
            */}
            <View style={{ justifyContent: 'center', marginLeft: 10 }}>
            <Button iconLeft transparent dark >
              <Icon name='swap' />
              </Button>
            </View>
            


          </View>
          {/*
<DatePicker
  defaultDate={new Date(2018, 4, 4)}
  minimumDate={new Date(2018, 1, 1)}
  maximumDate={new Date(2018, 12, 31)}
  locale={"en"}
  timeZoneOffsetInMinutes={undefined}
  modalTransparent={false}
  animationType={"fade"}
  androidMode={"default"}
  placeHolderText="Select date"
/>

*/}
        </Content>



      </Header>

    );
  }
}

export default AppHeader;
