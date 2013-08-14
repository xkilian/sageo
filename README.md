sageo
=====

A monitoring web interface using the Flask framework based on check_mk Multisite

The technologies used are:
- Twitter Bootstrap for CSS styles
- Python Flask web framework
- Babel for translations
- MK Livestatus

Sageo provides a solid core on which to build a complete web monitoring interface for Nagios and Nagios derived monitoring systems. It uses the standard Livestatus protocol for fast and efficient data retrieval. It is built using an MVC software architecture which separates the representation of information from the user's interaction with it. The interface is developer friendly.

Installation
------------

# Dependencies
<pre><code>sudo aptitude install python-virtualenv</code></pre>

# Installation
<pre><code>virtualenv env
. env/bin/activate
git clone https://github.com/smlacombe/sageo.git
cd sageo
pip install -r requirements.txt
python db_create.py
</code></pre>


# Configuration
Add your broker address
<pre><code>vim config.py
</code></pre>

# Compile LESS files (CSS)
You need first to install LESS compiler (LESSC command)
Debian based:
<pre><code>
apt-get install lessc
</pre></code>

Compile LESS files
<pre><code>
cd app/static/css
lessc less/main.less main.css
</code></pre>

# Run server
Launch server
<pre><code>python run.py
</code></pre>

Go to : http://127.0.0.1:5000
