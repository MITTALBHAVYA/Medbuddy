
---

# MedBuddy MyCut Frontend

The frontend for the **MedBuddy MyCut** project is developed using React with Vite as the build tool. It provides an intuitive user interface for interacting with the MedBuddy AI chatbot and managing healthcare-related queries and appointments.

## Features

- **Responsive UI**: Built with React and Tailwind CSS for a modern and responsive design.
- **Chat Interface**: Allows users to interact with the MedBuddy AI chatbot for healthcare-related inquiries.
- **Appointment Management**: Provides functionality for booking appointments and viewing doctor information.
- **Interactive Components**: Includes components for navigation, footer, and chat interface.

## Project Structure

```
frontend/
├── node_modules/
├── public/
│   └── vite.svg
├── src/
│   ├── assets/
│   │   ├── chatbot.avif
│   │   └── react.svg
│   ├── components/
│   │   ├── Chat.jsx
│   │   ├── Footer.jsx
│   │   ├── Homepage.jsx
│   │   └── Navbar.jsx
│   ├── App.css
│   ├── App.jsx
│   ├── index.css
│   ├── main.jsx
│   ├── output.css
├── .gitignore
├── eslint.config.js
├── index.html
├── package-lock.json
├── package.json
├── postcss.config.js
├── README.md
├── tailwind.config.js
└── vite.config.js
```

### `src/`

Contains the source code for the frontend application.

- **`assets/`**: Includes static assets like images and icons.
- **`components/`**: Contains React components used in the application.
  - **`Chat.jsx`**: Component for the chat interface with the MedBuddy AI.
  - **`Footer.jsx`**: Component for the footer section of the application.
  - **`Homepage.jsx`**: Main page component with introductory and interactive elements.
  - **`Navbar.jsx`**: Component for the navigation bar.
- **`App.jsx`**: The root component that integrates all other components.
- **`main.jsx`**: Entry point for the React application.
- **`index.css` & `App.css`**: CSS files for styling.
- **`output.css`**: Compiled Tailwind CSS file.

### `public/`

Contains the static files served by the application, including the main `index.html` file.

## Setup and Installation

1. **Install Dependencies**

    Navigate to the `frontend` directory and run:

    ```bash
    npm install
    ```

2. **Run the Development Server**

    Start the development server with:

    ```bash
    npm run dev
    ```

    The application will be available at `http://localhost:5173` by default.

3. **Build for Production**

    To build the application for production, run:

    ```bash
    npm run build
    ```

    The production files will be output to the `dist/` directory.

## Development

- **Code Style**: Ensure that your code follows the [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript) and the project's ESLint configuration.
- **Testing**: Add or modify tests as needed to ensure the application functions correctly.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License. See the [LICENSE](../../LICENSE) file for more details.

---
