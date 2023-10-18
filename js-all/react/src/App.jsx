
//import './style.css';

// Declaration of the component MyButton

function MyButton() {
  return (
    <div>
	  <button>
	    I'm a button
	  </button>
	</div>
  );
}

// Nesting MyButton into another component

export default function MyApp() {
	return (
		<div>
			<h1>Welcome to my app</h1>
			<MyButton />
		</div>
	);
}