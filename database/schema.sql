CREATE TABLE IF NOT EXISTS jobs (
                                    id SERIAL PRIMARY KEY,
                                    title TEXT,
                                    company TEXT,
                                    location TEXT,
                                    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS skills (
                                      skill_id SERIAL PRIMARY KEY,
                                      skill_name TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS job_skills (
                                          job_id INT REFERENCES jobs(job_id),
    skill_id INT REFERENCES skills(skill_id)
    );