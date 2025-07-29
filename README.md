markdown
# Utelly MCP Server

## Overview

The Utelly MCP Server is a powerful platform designed to aggregate metadata feeds from various Video On Demand (VOD) services. This server provides a universal search and discovery tool for Movies, Series, and TV Shows, enabling users to find where to watch their favorite content across multiple streaming services. 

## Features

- **Universal Search and Recommendations**: Offers comprehensive search capabilities for Movies, Series, and TV Shows, pulling data from a wide range of popular streaming services such as Netflix, Amazon Prime, iTunes, Disney+, AppleTV+, YouTube Premium, CBS All Access, and more.

- **Personalized Recommendations**: Enhances user experience by providing personalized content recommendations based on user preferences and history.

- **Availability Lookup**: Users can easily find out where a specific movie or show is available for streaming in their country.

## Core Tools

### /lookup Endpoint
- **Functionality**: This tool allows users to search for a TV show or movie by name and retrieve its availability across supported services for a particular country.
- **Parameters**:
  - `term`: Name of the show or movie you want to check availability for. Supports partial strings.
  - `country`: Optional parameter to filter services available in a specific country. Supported territories include UK, US, AR, AT, BE, BR, CA, DE, ES, FR, IE, ID, IT, IS, KR, MY, MX, NO, NL, PT, SE, & SG.

### /idlookup Endpoint
- **Functionality**: This tool helps users find where to watch a movie or TV show using common IDs (e.g., IMDb, TMDb, Wiki).
- **Parameters**:
  - `source_id`: The unique identifier for the show or movie.
  - `source`: The source from which the ID is derived (e.g., IMDb, TMDb).
  - `country`: Optional parameter to filter services available in a specific country. Supported territories as listed above.

## Conclusion

The Utelly MCP Server is an essential tool for anyone looking to streamline their viewing experience by easily locating where they can watch their favorite content across various streaming platforms. With its robust capabilities and user-friendly tools, it transforms the way users discover and enjoy content.