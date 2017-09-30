// Allows access to invoke AWS Lambda function only.
AWS.config.region = "eu-west-2";
AWS.config.credentials = new AWS.CognitoIdentityCredentials({
  IdentityPoolId: 'eu-west-2:e8010ca1-700c-4d9b-8497-44c1d963f30e'
});
