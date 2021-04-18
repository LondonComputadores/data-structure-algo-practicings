#! /usr/bin/env bash

// let greet = "Olá, Mundo!"
// alert(greet)


 
peso = prompt("Digite seu peso: ");
altura = prompt("Digite sua altura: ");

imc = peso / (altura * altura);

alert("Seu resultado é de: " + imc);

if(imc < 17)
  alert("Muito abaixo do peso");
else {
    if(imc < 18.5)
      alert("abaixo do peso");
    else {
        if(imc < 25)
          alert("peso normal");
        else {
            if(imc < 30)
             alert("acima do peso");
            else {
                if(imc < 35)
                  alert("obesidade I");
                else {
                    if(imc < 40)
                      alert("obesidade II");
                    else {
                        alert("obesidade III")
                    }
                }
            }
        }
    }
}


// Vamos Refazer Nosso Teste do IMC
// Agora, com o uso de “AND”, podemos reescrever nosso código de cálculo de
// IMC. É questionável se o programa resultante será melhor que o apresentado
// originalmente, mas nosso objetivo aqui é didático.

    
// function imc() {  
//   var peso = prompt("entre com seu peso");
//   var altura = prompt("entre com sua altura");
//   var imc = peso / (altura * altura);
//   alert("Seu IMC ficou em: " + imc );
//   if (imc < 17) alert("muito abaixo do peso");
//   if ( (imc >= 17) && (imc < 18.5) ) alert("abaixo do peso");
//   if ( (imc >= 18.5) && (imc < 25) ) alert("peso normal");
//   if ( (imc >= 25) && (imc < 30) ) alert("acima do peso");
//   if ( (imc >= 30) && (imc < 35) ) alert("obesidade I");
//   if ( (imc >= 35) && (imc < 40) ) alert("obesidade II");
//   if (imc >= 40) alert("obesidade III");
// }
// console.log(imc);


console.time("t"); //start new timer for label name: "t"
let arr = []; //store empty array
for(let i = 0; i < 1000000; i++) { //1 million iterations
arr.push(i); //push current i value
}
console.timeEnd("t"); //stop the timer for label name: "t" and print elapsed time