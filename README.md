<h1>AirBnB_clone</h1>

<p>
<a href="https://www.airbnb.com/">Airbnb</a>. is an online marketplace for arranging or offering lodging, primarily homestays, or tourism experiences. The company does not own any of the real estate listings, nor does it host events; it acts as a broker, receiving commissions from each booking.
</p>

<p>The goal of the project is to deploy on our own server a simple copy of the <b>AirBnB website</b>.</p>

<h2>Description of the project</h2>
We don’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track at <a href="https://www.alxafrica.com
">ALX</a>.

This project will be a complete a full web application composed by:
<ul>
<li>A command interpreter to manipulate data without a visual interface, like in a Shell (<i>perfect for development and debugging</i>).</li>
<li>A website (<i>the front-end</i>) that shows the final product to everybody: <b>static and dynamic</b>.</li>
<li>A database or files that store data (<b>data = objects</b>).</li>
<li>An API that provides a communication interface between the front-end and your data (<i>retrieve, create, delete, update them</i>).</li>
</ul>
<br>
The first part of the whole project is: <b>AirBnB clone - The console</b>

<h2>AirBnB clone - The console</h2>
The console This is the first part of this project, it represents the data model.

The purpose of this model is to:
<ul>
<li>Build the data model.</li>
<li>Perform operations like (<i>create, update, destroy, etc</i>) in the objects via a console.</li>
<li>Build a powerfull storage system, that will be capable of storing and loading objects to and from a file (<a href="https://www.json.org/json-en.html">JSON file</a>).</li>
</ul>
<br>
<h2>How to start using it</h2>
First of all, to use our application you have to clone our repository using the command on your terminal:


<pre class="notranslate"><code>git clone <a>https://github.com/1cloudio/AirBnB_clone.git</a></code>


Once this is done, a folder named AirBnB_clone-master is created, you have to go inside it, using de command cd on your terminal.

<code>cd AirBnB_clone-master</code>


Once you're inside of the AirBnB_clone-master folder, you have to execute the console with the command:

<code>./console.py</code>



Done this, it will show the console of our application, from here, we can interact with the application data.

<h2>Examples</h2>
Now we are going to show some of the application features.

<h3>help command</h3>
This command shows us the help for the most common actions on the console.

On the console type: <code>help</code>

<h3>create</h3>
Creates an instances of a class, usage: <code>create <ClassName></code>


It can also be used as follows: <code><ClassName>.create</code>

<h3>all</h3>
Shows all created instances, usage: <code>all (OPTIONAL)<ClassName></code>



It can also be used like this: <code><ClassName>.all</code>

<h3>show</h3>
Shows info about a created instance of a class using id as parameter, usage: <code>show <ClassName> id</code>


It can also be used al follows: <code><ClassName>.show("id")</code> <i>id must be in parenthesis and quoted</i>

<h3>destroy</h3>
Destroys a created instance of a class using id as parameter, usage: <code>destroy <ClassName> id</code>


It can also be used as follows: <code><ClassName>.destroy("id")</code> <i>id must be in parenthesis and quoted</i>

<h3>update</h3>
Updates a created instance of a class using id as parameter as well as the attribute name and the value, usage: <code>update <ClassName> <attribute name> '<attribute value>'</code>


It can also be used as follows: <code><ClassName>.update("id", "attribute name", "attribute value")</code>

<h3>count</h3>
Counts the number of instances of a class: usage: <code>count <ClassName></code>


It can also be used like this: <code><ClassName>.count</code>

<h2>⛏️ Built Using</h2>
<a href="https://www.Python.org">Python</a> - Programming language

<h2>✍️ Authors</h2>
<ul><li>@1cloudio - Nnachi Michael</li>
<li>@TRUHUB1 - Oladosu Rukayat-Isiaq</li></ul>
