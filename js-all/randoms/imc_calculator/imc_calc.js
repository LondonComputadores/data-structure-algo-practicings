#! /usr/bin/env bash

// let greet = "Olá, Mundo!"
// alert(greet)





let peso = prompt("Digite seu peso: ");
let altura = prompt("Digite sua altura: ");
let imc = peso / (altura * altura);

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