import { Avatar } from './Avatar';
import { Comment } from './Comment';
import styles from './Post.module.css';

// export function Post({props}) {
export function Post({author, publishedAt}) {
	// console.log(props); It was used only to show some changes on the...
	// ...browser's console.
	const publishedDateFormatted = new Intl.DateTimeFormat('pt-br', {
		day: '2-digit',
		month: 'long',
		hour: '2-digit',
		minute: '2-digit',
	}).format(publishedAt)

	return (
		<article className={styles.article}>
			<header>
				<div className={styles.author}>
					{/* <Avatar src="https://github.com/AlexandrePaes.png" /> */}
					<Avatar src={author.avatarUrl}/>
						<div className={styles.authorInfo}>
							{/* <strong>Alexandre Paes</strong> */}
							<strong>{author.name}</strong>
							{/* <span>Software Engineer</span> */}
							<span>{author.role}</span>
						</div>
				</div>

				<div className={styles.time}>
					<time title='11 de Maio às 7:30' dateTime='2022-05-11 07:30:00'>
						{/* Publicado há 1 hora //v1 */}
						{/* {publishedAt.toString()} //v2 */}
						{publishedDateFormatted}
					</time>
				</div>
			</header>

			<div className={styles.content}>
				<p>Hey, guys!</p>
				<p>My portfolio has just been updated with a fresh project as part of the Ignite Bootcamp from Rocketseat.</p>
				<p>emoji here <a href="">Any title here</a></p>
				<br />
				<p>
					<a href="">#some</a>{" "}
					<a href="">#hastags</a>{' '}
					<a href="">#for</a>{' '}
					<a href="">#the</a>{' '}
					<a href="">#SEO</a>{' '}
				</p>
			</div>

			<form className={styles.commentForm}>
				<strong>Leave your feedback:</strong>
				<textarea placeholder='Leave your feedback' />
				<button type='submit'>Send</button>
			</form>

			<div className={styles.commentList}>
				<Comment />
				<Comment />
				<Comment />
			</div>

		</article>
	)
}