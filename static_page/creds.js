AWS.config.update({region: "eu-west-2"});
AWS.config.credentials = new AWS.CognitoIdentityCredentials({
  // Read only access to DynamoDB.
  IdentityPoolId: "eu-west-2:bffba4da-4094-46a1-8906-b01d325a03a3",
  RoleArn: "arn:aws:iam::740583530883:role/Cognito_DynamoPoolUnauth"
});
