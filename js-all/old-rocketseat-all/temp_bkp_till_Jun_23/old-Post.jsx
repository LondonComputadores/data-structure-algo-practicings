// V3
// import styles from './Post.module.css';

// export function Post() {
//     return (
//         <article>
//             <header>
//                 <div>
//                     <img className={styles.avatar} src="https://github.com/AlexandrePaes.png" />
//                     <div className={styles.authorInfo}>
//                         <strong>Alexandre Paes</strong>
//                         <span>Software Engineer</span>
//                     </div>
//                 </div>

//                 <time title='11 de Maio às 7:30' dateTime='2022-05-11 07:30:00'>Publicado há 1 hora</time>
//             </header>

//             <div className={styles.content}>
//                 <p>Hey, guys!</p>
//                 <p>My portfolio has just been updated with a fresh project</p>
//                 <p>emoji here <a href="">any title</a></p>
//                 <p><a href="">#some #hastags #for #the #SEO</a></p>
//             </div>
//         </article>
//     )
// }



// V2
//
// export function Post(props) {
//     return (
//         <div>
//             <strong>{props.author}</strong>
//             <p>{props.content}</p>
//             <p>{props.separator}</p>
//         </div>
//     )
// }