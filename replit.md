# WMS (Warehouse Management System) Application

## Overview
This is a Flask-based Warehouse Management System with SAP B1 integration. The application provides inventory management, transfer operations, barcode generation, and invoice creation functionality.

## Project Architecture
- **Framework**: Flask (Python web framework)
- **Database**: PostgreSQL (Replit managed database)
- **Frontend**: HTML templates with Bootstrap styling
- **Integration**: SAP Business One API integration
- **Authentication**: Flask-Login for user management

## Current Configuration
- **Port**: 5000 (configured for Replit webview)
- **Database**: PostgreSQL with automatic table creation
- **Environment**: Production-ready with gunicorn server
- **Logging**: File-based logging system enabled

## Key Features
- User authentication and role management
- Inventory transfer operations
- Barcode and QR code generation
- SAP B1 integration for warehouse operations
- Serial number tracking
- Invoice creation module
- Pick list management
- GRPO (Goods Receipt PO) functionality

## Setup Status
✅ PostgreSQL database configured and connected (migrated from MySQL)
✅ Default admin user created (username: admin, password: admin123)
✅ Environment variables configured (DATABASE_URL, SESSION_SECRET)
✅ Gunicorn server running on port 5000 with webview output
✅ Deployment configuration set for autoscale
✅ All database tables created with default data
✅ Flask application configured for Replit environment with ProxyFix
✅ Application successfully running in Replit environment

## Default Credentials
- **Username**: admin
- **Password**: admin123
- **Role**: System Administrator

## Modules
- Main application routes
- Inventory transfer module
- Serial item transfer module
- Invoice creation module
- SAP B1 integration utilities
- Barcode generation utilities

## Recent Changes
- Migrated from MySQL to PostgreSQL for Replit environment (September 5, 2025)
- Database configuration updated to use Replit's managed PostgreSQL
- Workflow configured with webview output on port 5000
- ProxyFix middleware properly configured for Replit iframe environment
- Deployment configuration set for autoscale production deployment
- PostgreSQL-specific constraint handling implemented
- Default branch and admin user initialized successfully