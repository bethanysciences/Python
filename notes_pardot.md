https://www.npmjs.com/package/pardot-streaming-client/v/0.0.2
https://www.npmjs.com/package/pardot

Executive	https://pi.pardot.com/emailTemplate/readReport/id/17296
Fac/Ops	https://pi.pardot.com/emailTemplate/readReport/id/17342
IT	https://pi.pardot.com/emailTemplate/readReport/id/17354
HR	https://pi.pardot.com/emailTemplate/readReport/id/17346

https://github.com/mneedham91/PyPardot4/
Pip3 install pypardot4

POST: https://pi.pardot.com/api/login/version/3
message body: email=bob.smith@fourwindsinteractive.com&password=xxxxxxxxxxxx&user_key=f095c88c502a8d1b606e2f45827eee64

Pardot API keys expire after 60 minutes.
If PyPardot detects an 'Invalid API key' error during any API call, it will automatically attempt to re-authenticate and obtain a new valid API key. If re-authentication is successful, the API call will be re-issued. If re-authentication fails, a PardotAPIError is thrown.
