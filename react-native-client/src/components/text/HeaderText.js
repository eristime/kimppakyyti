import React from 'react';
import {
  Text,
} from 'native-base';

const DefaultText = (props) => {
    return (
        <Text style={{fontSize:25, padding:2}}>{props.children}</Text>
    );
  };
export default DefaultText;
