Gamekeeper
• gamekeeperId → username, password, email
• username → gamekeeperId, password, email
• email → gamekeeperId, username, password

Player
• playerId → username, password, email, points, bin, storeItems, memberSince
• username → playerId, password, email, points, bin, storeItems, memberSince
• email → playerId, username, password, points, bin, storeItems, memberSince

Resource
• resourceId → title, description, url
• url → resourceId, title, description

StoreItem
• itemId → name, description, cost
• name → itemId, description, cost

Trash
• trashId → name, description, value
• name → trashId, description, value

Event
• eventId → trashId, locationId, questionSet, status, startDateTime, endDateTime
• locationId, startDateTime → eventId, trashId, questionSet, status, endDateTime
• locationId, endDateTime → eventId, trashId, questionSet, status, startDateTime

Question
• questionId → question, answer, wrongAnswer1, wrongAnswer2, wrongAnswer3, wrongAnswer4
• question → questionId , answer, wrongAnswer1, wrongAnswer2, wrongAnswer3, wrongAnswer4

Location
• locationId → buildingName, qrCode
• qrCode → locationId, buildingName