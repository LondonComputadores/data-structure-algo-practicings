import { format, formatDistanceToNow } from 'date-fns';
import ptBR from 'date-fns/esm/locale/pt-BR';
import { useState } from 'react';
import { Avatar } from './Avatar';
import { Comment } from './Comment';
import styles from './Post.module.css';

export function Post({author, publishedAt, content}) {

	const [comments, setComments] = useState([
		
		'Posting here is so cool'
	])

	const [newCommentText, setNewCommentText] = useState('')

	const publishedDateFormatted = format(publishedAt, "d 'de' LLLL 'às' HH:mm'h'", {
		locale: ptBR,
	})

	const publishedDateRelativeToNow = formatDistanceToNow(publishedAt, {
		locale: ptBR,
		addSuffix: true,
	})

	function handleCreateNewComment() {
		event.preventDefault()
		//const newCommentText = event.target.comment//.value
		setComments([...comments, newCommentText]);
		setNewCommentText('')  // This line replaced the line below
		//event.target.comment.value = '';
	}

	function handleNewCommentChange() {
		event.target.setCustomValidity('');
		setNewCommentText(event.target.value);
	}

	function handleNewCommentInvalid() {
  	event.target.setCustomValidity('This field cannot be empty!');
  }

	function deleteComment(commentToDelete) {
		const commentsWithoutDeletedOne = comments.filter(comment => {
			return comment !== commentToDelete;
		})
	 	
		setComments(commentsWithoutDeletedOne);
	}

	const isNewCommentEmpty = newCommentText.length === 0;

	return (
		<article className={styles.article}>
			<header>
				<div className={styles.author}>
					<Avatar src={author.avatarUrl}/>
						<div className={styles.authorInfo}>
							<strong>{author.name}</strong>
							<span>{author.role}</span>
						</div>
				</div>

				<div className={styles.time}>
					{/* <time title='11 de Maio às 7:30' dateTime='2022-05-11 07:30:00'>
						{publishedDateFormatted}
					</time> */}
					{/* <time title={publishedDateFormatted} dateTime='2022-05-11 07:30:00'> */}
					
					<time title={publishedDateFormatted} dateTime={publishedAt.toISOString()}>
						{publishedDateRelativeToNow}
					</time>
				</div>
			</header>

			<div className={styles.content}>
				{content.map(line => {
					if (line.type === 'paragraph') {
						return <p>{line.content}</p>
					} else if (line.type === 'link') {
						return <p><a href="#">{line.content}</a></p>;
					}
				})}
			</div>

			<form onSubmit={handleCreateNewComment} className={styles.commentForm}>
				<strong>Leave your message here:</strong>

				<textarea //placeholder='Leave your feedback'
					name="comment"
					placeholder="Your Message Goes Here"
					value={newCommentText}
					onChange={handleNewCommentChange}
					onInvalid={handleNewCommentInvalid}
					required
				/>
				
				<footer>
					<button type='submit' disabled={isNewCommentEmpty}>Publish</button>
				</footer>	
			</form>

			<div className={styles.commentList}>
				{/* It was like this b4 map below
				<Comment />
				<Comment />
				<Comment />
				*/}

				{comments.map(comment => {
					return <Comment content={comment} deleteComment={deleteComment}/>
				})}
			</div>

		</article>
	)
}