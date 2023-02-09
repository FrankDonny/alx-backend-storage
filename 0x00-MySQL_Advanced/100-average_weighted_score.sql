-- Write a SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUser that computes
-- and store the average weighted score for a student.
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (@user_id int)
AS
BEGIN
    DECLARE @averageWeightedScore float

    SELECT @averageWeightedScore = AVG(score * weight) / SUM(weight)
    FROM students
    WHERE user_id = @user_id

    INSERT INTO average_scores (user_id, average_weighted_score)
    VALUES (@user_id, @averageWeightedScore)
END
