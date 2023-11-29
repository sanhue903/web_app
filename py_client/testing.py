results = []
for chapter in range(2):
    chapter_data = {
        'chapter': {
            'id': chapter,
            'question': []
        }
    }
    for question in range(2):
        question_data = {
            'id': question,
            'score': []
        }

        for score in range(2):
            score_data = {
                'student_id': score,
                'time': score,
                'attempts': score
            }
            question_data['score'].append(score_data)
        chapter_data['chapter']['question'].append(question_data)
    results.append(chapter_data)

print(results)