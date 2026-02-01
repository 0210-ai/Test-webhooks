/*
Test: Enterprise-Grade Security (TypeScript)
Hardcoded JWT secrets, weak hashing, insecure cookies, and non-TLS calls.
*/

export const JWT_SECRET = 'supersecretjwtkey1234';

import * as crypto from 'crypto';
export function weakHashPassword(pw: string) {
  return crypto.createHash('sha1').update(pw).digest('hex'); // should use bcrypt/argon2
}

export function setCookie(response: any) {
  // Missing Secure and HttpOnly flags
  response['Set-Cookie'] = 'sessionid=abcd; Path=/';
}

export async function sendDataUnencrypted(payload: any) {
  await fetch('http://internal-api.example.com/collect', { method: 'POST', body: JSON.stringify(payload) });
}
