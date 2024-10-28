// Define your projects here
const projects = [
    {
        name: "Treasure Island Game",
        links: [
            { label: "Version 1.0", url: "https://suraj8300.github.io/Treasure-Island-Game-1.0/" },
            { label: "Version 2.0", url: "https://suraj8300.github.io/Treasure-Island-Game-2.0/" }
        ]
    },
    {
        name: "Tic Tac Toe Game",
        links: [
            { label: "Version 1.0", url: "https://suraj8300.github.io/Tic-Tac-Toe-Game/" }
        ]
    },
    {
        name: "Cypher Encoder Decoder",
        links: [
            { label: "Version 1.0", url: "https://cypher-game.onrender.com/Project1" }
        ]
    },
    {
        name: "Project Under Progress",
        links: [
            { label: "Not released yet!", url: "https://suraj8300.github.io/My-Portfolio/" },
            { label: "Not released yet!", url: "https://suraj8300.github.io/My-Portfolio/" }
        ]
    },
    // Add more projects as needed
];

// Function to create project items
function displayProjects() {
    const projectList = document.getElementById('project-list');

    projects.forEach(project => {
        // Create project item container
        const projectItem = document.createElement('div');
        projectItem.classList.add('project-item');

        // Create project name element
        const projectName = document.createElement('h3');
        projectName.classList.add('project-name');
        projectName.textContent = project.name;

        // Optional: Make project name clickable to first link
        projectName.addEventListener('click', () => {
            window.open(project.links[0].url, '_blank');
        });

        // Create links container
        const linksContainer = document.createElement('div');
        linksContainer.classList.add('project-links');

        project.links.forEach(link => {
            const a = document.createElement('a');
            a.href = link.url;
            a.textContent = link.label;
            a.target = '_blank';
            linksContainer.appendChild(a);
        });

        // Append name and links to project item
        projectItem.appendChild(projectName);
        projectItem.appendChild(linksContainer);

        // Append project item to the list
        projectList.appendChild(projectItem);
    });
}

// Initialize the projects on page load
document.addEventListener('DOMContentLoaded', displayProjects);