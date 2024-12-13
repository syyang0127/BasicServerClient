# 1. Base image
FROM node:16-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy package.json and package-lock.json (if available)
COPY package*.json ./

# 4. Install dependencies
RUN npm install

# 5. Copy the client source code
COPY . .

# 6. Build the client application
RUN npm run build

# 7. Expose the port the client will run on
EXPOSE 3000

# 8. Command to run the client application
CMD ["npm", "start"]
