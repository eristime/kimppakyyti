import React from 'react';
import {
  Text,
} from 'native-base';

const ImportantText = (props) => {
    return (
        <Text style={{fontSize:18, padding:2, fontWeight:'900'}}>{props.children}</Text>
    );
  };
export default ImportantText;
