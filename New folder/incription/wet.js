const { createHash } = require('crypto');

//create string hash with sha256
//func to hash

function hash(string){
    return createHash('sha256').update(string).digest('hex');
}
//comp 2 hash password
// password in database
let password = 'password123';
const hash1 = hash(password);
console.log(hash1)
//pass given by user
password='password123';
const hash2 = hash(password);
const match = hash1 === hash2;
console.log(hash2)
console.log(match ? 'good password': 'wrong password');

const {scyptSync, randomBytes} = require('crypto');

function signup(email, password) {
    //create unique salt per user
    const salt = randomBytes(16).toString('hex');
    // create a unique hash
    const hashedPassword = scryptSync(password, salt, 64).toString('hex');
    //database stores
    const user ={email,password:`${salt}:${hashedPassword}`}
    users.push(user);
    return user 
}
function login(email,password){
const user = users.find(v=> v.email === email);
if (!user) return 'user not found';
// decode the pass
const [salt,key] = user.password.split(':')
const hashBuffer=scryptSync(password,salt,64);
const keyBuffer=Buffer.from(key,'hex');
//compare the pssword
const match1 = hashedBuffer.toString('hex') == keyBuffer.toString('hex');
if(match1){
    return 'login successful';
}
else{
    return 'login failed'
}
}
//login or signup user
const users=[];
const users= signup('lpan@icstars.org','leo123')
console.log(user)
const lgin = login('lphan@icstars.org','leo123')

