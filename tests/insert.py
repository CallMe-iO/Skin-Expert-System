DELETE FROM users;

INSERT INTO users (username, password, role) VALUES
('admin', '$2b$12$Nw7GxT6hXoF7UwIWIo8k7OoQgF8EJpjG4yZvwhW4X9eybTt/ZG1Jm', 'admin'),
('user1', '$2b$12$JypAV7EwTqLOeBdBWkqEYOd/kn9xVz9g/U.xZuJ9B/vsErU/hQq3G', 'user');
