<h1 align="center">
 <b>P.R.I.D.E</b>
 </h1>
<h4 align="center">
 Phishing Resistant Identicons
 </h4>

<p align="center">
 <a href="https://www.python.org">
  <img src="https://img.shields.io/badge/MADE%20WITH%20-Python-blueviolet">
 </a>
 <a href="https://www.gnu.org/licenses/gpl-3.0">
  <img src="https://img.shields.io/badge/License-GPLv3-brightgreen.svg">
 </a>
</p>

<h2>Introduction</h2>
<p> Identicons are visual representation of hash values. Usually they look something like these :</p><br>

<p align="center">
  <img src="/Assets/sample_identicon_2.png">&emsp; &emsp; &emsp;
  <img src="/Assets/sample_identicon_1.png">
  </p>

<br>
<p> As a matter of fact, GitHub uses identicons as profile pictures by default based on the username of users. Since no two users have the same username, every user has a unique identicon. It is also used in many blog sites to uniquely identify each user even if the names are same.</p>
<p> <a href="https://github.com/donpark">Don Park</a> came up with the idea of using identicons to prevent phishing in 2007 in this blog <a href="https://web.archive.org/web/20080510221519/http://www.docuverse.com/blog/donpark/2007/01/22/identicon-based-anti-phishing-protection">post</a>.
  
<p> This project implementation is inspired from that idea. I would like to tout this as an alternate way to sign in to websites to safeguard against phishing attempts. Everyday, we log in to multiple websites, whether it is for e-mail, news feeds, games or social media. There is always a risk that the webpage that loads could have been compromised by an attacker as part of a MiTM attack or a general phishing scheme and hence the danger of your accounts being compromised without you even knowing it. </p>

<h2>Working</h2>
<p>A user loads up a website he/she wants to log into. The user then inputs his username/email first. This is sent to the server where it's validated for an existing record. If yes, then the server generates an identicon from the hashed password and sends it back to the users' browser. The user can see the identicon generated from the server. At the same time, the user's browser fetches the hashed password (read: password manager fetches the password it must have stored before) and generates the identicon. Both the identicons are placed side by side. If they are identical, then the opened site can be trusted. Now, the user can safely input his/her password.  
  
<h2>Pre-requisites</h2>
 <p>The major dependencies used are :
<ul type="disc">
  <li>Flask - 1.1.2</li>
  <li>Flask-SQLAlchemy - 2.4.4</li>
  <li>passlib - 1.7.2</li>
  <li>pydenticon - 0.3.1</li>
  <li>sockets - 1.0.0</li>
  <li>SQLAlchemy - 1.3.19</li>
  </ul>
  
  For the complete list check <a href="requirements.txt">this</a>.</p>

<h2>Possible Limitations</h2>
 <p>This implementation does change the user experience. Obviously, humans don't embrace change.</p>
 <p>Firstly, the user needs to store passwords in the device. Password managers provide a solution to this issue. But, people rather use the crappy password managers built into the browsers. The idea of "all eggs in one basket" seems to frighten them.
</p>
  
   
<h2>Comments</h2> 
<p> If you have any suggestions or anything about how this isn't going to work at all, let me know. Open a PR, maybe.</p>
<p> As of now, this implementation just shows how the system may work, it doesn't fetch credentials from a password manager to create identicons at the client side. It has proven to be challenging. For testing purposes, I created another database which acts as a storage unit for credentials, imitating a password manager.</p>

<h2>License</h2>

<a href="LICENSE">GPLv3</a>
