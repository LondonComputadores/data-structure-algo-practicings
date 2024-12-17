import { ThumbsUp, Trash } from 'phosphor-react';
import { Avatar } from './Avatar';
import styles from './Comment.module.css';
import { useState } from 'react';

export function Comment({content, deleteComment}) {
	const [likeCount, setLikeCount] = useState(0);

	function handleDeleteComment() {
		deleteComment(content);
	}

	function handleLikeComment() {
		setLikeCount((state) => {
			return state + 1
	  });
	}
	
	return (
		<div className={styles.comment}>
			<Avatar hasBorder={false} src="https://github.com/AlexandrePaes.png" />

			<div className={styles.commentBox}>
				<div className={styles.commentContent}>
					<header>
						<div className={styles.authorAndTime}>
							<strong>Alexandre Paes</strong>
							<time title='11 de Maio às 7:30' dateTime='2022-05-11 07:30:00'>
								Publicado há 1 hora
							</time>
						</div>

						<button onClick={handleDeleteComment} title='Delete comment'>
							<Trash size={24}/>
						</button>
					</header>

					<p>{content}</p>

				</div>

				<footer>
					<button onClick={handleLikeComment}>
						<ThumbsUp /> 
						Aplause <span>{likeCount}</span>
					</button>
				</footer>

			</div>

		</div>

	)
}