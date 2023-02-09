-- Write a SQL script that creates a stored procedure
-- ComputeAverageWeightedScoreForUsers that computes
-- and store the average weighted score for all students.
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers
AS
BEGIN
    DECLARE @averageWeightedScore float

    SELECT @averageWeightedScore = AVG(score * weight) / SUM(weight)
    FROM students

    INSERT INTO average_scores (average_weighted_score)
    VALUES (@averageWeightedScore)
END
