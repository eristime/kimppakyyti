# Client

Application is developed to using Expo and so expo cli and mobile-client are needed to run the app.

## Instructions to run:

1. Install dependencies: 
```
npm install
```
2. Install expo-cli: 
```
npm install -g expo-cli
```
3. Install [expo mobile client](https://play.google.com/store/apps/details?id=host.exp.exponent&hl=en) for Android from Play Store.
4. Specify the BACKEND_DOMAIN in config.js in this folder to respond the domain where [backend](https://github.com/eristime/kimppakyyti/tree/master/backend) is running.
5. Ensure that the backend is running and connected to same private LAN as the smartphone.
 - Note: If there are multiple interfaces expo may use a wrong one by default. By setting ```REACT_NATIVE_PACKAGER_HOSTNAME``` environment variable to a correct IP will fix the problem.
6. ```expo start```
7. Scan the displayed QR-code using the expo mobile client.
